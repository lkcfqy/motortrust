#!/usr/bin/env python3
"""Verify and restore a MotorTrust split tar.gz release using only Python 3.

Downloads are intentionally separate: put release-manifest.json and every part
in --parts-dir. --destination is the parent of the restored motortrust directory.
"""

import argparse
import hashlib
import json
import os
import re
import shutil
import sys
import tarfile
import tempfile
import unicodedata
import uuid
from pathlib import Path

CHUNK_SIZE = 1024 * 1024
MANIFEST_NAME = "release-manifest.json"
ROOT_DIRECTORY = "motortrust"
SAFE_BASENAME = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]*\Z")
SHA256 = re.compile(r"[0-9a-fA-F]{64}\Z")
WINDOWS_RESERVED = {"CON", "PRN", "AUX", "NUL"}
WINDOWS_RESERVED.update("COM" + digit for digit in "123456789¹²³")
WINDOWS_RESERVED.update("LPT" + digit for digit in "123456789¹²³")


class RestoreError(Exception):
    """An invalid or unsafe release that must not be installed."""


def require(condition, message):
    if not condition:
        raise RestoreError(message)


def positive_size(value, label):
    require(type(value) is int and value >= 0,
            f"{label} must be a non-negative integer")
    return value


def validate_basename(value, label):
    require(isinstance(value, str) and SAFE_BASENAME.fullmatch(value),
            f"{label} must be a simple ASCII filename")
    return value


def validate_digest(value, label):
    require(isinstance(value, str) and SHA256.fullmatch(value),
            f"{label} must be a SHA-256 hex digest")
    return value.lower()


def reject_duplicate_keys(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, f"Duplicate JSON key: {key}")
        result[key] = value
    return result


def load_manifest(path):
    require(path.is_file() and not path.is_symlink(),
            f"Manifest must be a regular, non-symlink file: {path}")
    require(path.stat().st_size <= 16 * 1024 * 1024, "Manifest is too large")
    with path.open("r", encoding="utf-8-sig") as stream:
        manifest = json.load(stream, object_pairs_hook=reject_duplicate_keys)
    require(isinstance(manifest, dict), "Manifest must be a JSON object")
    require(type(manifest.get("schema_version")) is int and
            manifest["schema_version"] == 1, "Unsupported schema_version")
    require(manifest.get("project") == "MotorTrust", "Unexpected project")
    require(manifest.get("root_directory") == ROOT_DIRECTORY,
            "root_directory must be motortrust")
    archive = manifest.get("archive")
    require(isinstance(archive, dict), "archive must be an object")
    validate_basename(archive.get("filename"), "archive.filename")
    require(archive.get("format") == "tar.gz", "Only tar.gz is supported")
    positive_size(archive.get("size_bytes"), "archive.size_bytes")
    positive_size(archive.get("unpacked_size_bytes"), "archive.unpacked_size_bytes")
    archive["sha256"] = validate_digest(archive.get("sha256"), "archive.sha256")
    parts = manifest.get("parts")
    require(isinstance(parts, list) and parts, "parts must be a non-empty ordered array")
    names = set()
    total = 0
    for index, part in enumerate(parts, 1):
        label = f"parts[{index}]"
        require(isinstance(part, dict), f"{label} must be an object")
        name = validate_basename(part.get("filename"), label + ".filename")
        require(name.casefold() not in names, "Duplicate part filename: " + name)
        require(name.casefold() != MANIFEST_NAME.casefold(),
                "Part filename must differ from the manifest filename")
        names.add(name.casefold())
        total += positive_size(part.get("size_bytes"), label + ".size_bytes")
        part["sha256"] = validate_digest(part.get("sha256"), label + ".sha256")
    require(total == archive["size_bytes"],
            "Sum of part sizes differs from archive.size_bytes")
    return manifest


def merge_verified_parts(parts_dir, manifest, archive_path):
    """Hash each part and the concatenation without loading parts into memory."""
    combined_hash = hashlib.sha256()
    combined_size = 0
    with archive_path.open("xb") as output:
        for index, part in enumerate(manifest["parts"], 1):
            source = parts_dir / part["filename"]
            require(source.is_file() and not source.is_symlink(),
                    f"Missing or unsafe part: {source}")
            require(source.stat().st_size == part["size_bytes"],
                    "Part size mismatch: " + part["filename"])
            part_hash = hashlib.sha256()
            part_size = 0
            print("Verifying part {}/{}: {}".format(
                index, len(manifest["parts"]), part["filename"]), flush=True)
            with source.open("rb") as incoming:
                while True:
                    chunk = incoming.read(CHUNK_SIZE)
                    if not chunk:
                        break
                    part_size += len(chunk)
                    require(part_size <= part["size_bytes"],
                            "Part grew during verification: " + part["filename"])
                    part_hash.update(chunk)
                    combined_hash.update(chunk)
                    output.write(chunk)
            require(part_size == part["size_bytes"] and
                    part_hash.hexdigest() == part["sha256"],
                    "Part checksum mismatch: " + part["filename"])
            combined_size += part_size
    require(combined_size == manifest["archive"]["size_bytes"] and
            combined_hash.hexdigest() == manifest["archive"]["sha256"],
            "Combined archive checksum mismatch")


def member_components(name):
    """Use a portable path policy, including Windows path/device restrictions."""
    require(isinstance(name, str) and name and not name.startswith("/") and
            "\\" not in name, f"Unsafe archive path: {name!r}")
    components = [part for part in name.split("/") if part not in ("", ".")]
    require(components and components[0] == ROOT_DIRECTORY,
            f"Every member must be inside motortrust/: {name!r}")
    for component in components:
        require(component != ".." and
                not any(ord(char) < 32 or ord(char) == 127 for char in component) and
                not any(char in '<>:"|?*' for char in component) and
                not component.endswith((" ", ".")),
                f"Unsafe/nonportable path component: {component!r}")
        require(component.split(".", 1)[0].upper() not in WINDOWS_RESERVED,
                f"Windows reserved path component: {component!r}")
    return components


def inside(path, base):
    try:
        path.resolve().relative_to(base.resolve())
        return True
    except ValueError:
        return False


def extract_safely(archive_path, staging, expected_size):
    """Never use tarfile.extract/extractall; create only directories and files.

    Symlinks, hardlinks, devices, FIFOs, sparse files, duplicate paths and
    case/Unicode aliases are refused on every platform.
    """
    seen = set()
    aliases = {}
    unpacked_size = 0
    file_count = 0
    with tarfile.open(str(archive_path), mode="r|gz") as archive:
        for member in archive:
            require(member.isdir() or member.isreg(),
                    "Unsupported member type (links/devices are forbidden): " + member.name)
            require(not member.issparse(), "Sparse files are not supported: " + member.name)
            components = member_components(member.name)
            normalized = "/".join(components)
            require(normalized not in seen, "Duplicate archive member: " + normalized)
            seen.add(normalized)
            # Check every prefix so case-different directory names cannot alias.
            for length in range(1, len(components) + 1):
                prefix = "/".join(components[:length])
                key = unicodedata.normalize("NFC", prefix).casefold()
                require(key not in aliases or aliases[key] == prefix,
                        "Case/Unicode path collision: " + prefix)
                aliases[key] = prefix
            target = staging.joinpath(*components)
            require(inside(target, staging), "Member escapes staging: " + member.name)
            if member.isdir():
                require(not target.exists() or target.is_dir(),
                        "Directory conflicts with file: " + normalized)
                target.mkdir(parents=True, exist_ok=True)
                continue
            require(len(components) > 1, "motortrust must be a directory")
            positive_size(member.size, "tar member size")
            unpacked_size += member.size
            require(unpacked_size <= expected_size,
                    "Archive exceeds manifest.unpacked_size_bytes")
            target.parent.mkdir(parents=True, exist_ok=True)
            require(inside(target.parent, staging), "Parent escapes staging")
            incoming = archive.extractfile(member)
            require(incoming is not None, "Cannot read member: " + normalized)
            copied = 0
            with incoming, target.open("xb") as output:
                while True:
                    chunk = incoming.read(CHUNK_SIZE)
                    if not chunk:
                        break
                    copied += len(chunk)
                    require(copied <= member.size, "Member exceeds declared size")
                    output.write(chunk)
            require(copied == member.size, "Truncated member: " + normalized)
            # Preserve basic executable bits; discard ownership, setuid and sticky bits.
            if os.name != "nt":
                target.chmod(0o755 if member.mode & 0o111 else 0o644)
            file_count += 1
    require(unpacked_size == expected_size,
            "Extracted bytes differ from manifest.unpacked_size_bytes")
    root = staging / ROOT_DIRECTORY
    require(root.is_dir(), "Archive contains no motortrust directory")
    return file_count, unpacked_size


def install(staged_root, target, overwrite):
    """Keep an existing project as a backup when overwrite is explicit."""
    require(not target.is_symlink(), "Existing motortrust target is a symlink")
    backup = None
    if target.exists():
        require(overwrite, "Destination motortrust already exists; use --overwrite explicitly")
        require(target.is_dir(), "Existing motortrust target is not a directory")
        backup = target.with_name(ROOT_DIRECTORY + ".backup-" + uuid.uuid4().hex[:12])
        target.rename(backup)
    try:
        # Recheck in case a target appeared while the archive was being verified.
        require(not target.exists() and not target.is_symlink(),
                "Destination appeared during restoration; aborting")
        staged_root.rename(target)
    except BaseException:
        if backup is not None and not target.exists() and not target.is_symlink():
            backup.rename(target)
        raise
    return backup


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--parts-dir", required=True, type=Path,
                        help="Directory containing manifest and every split part")
    parser.add_argument("--destination", required=True, type=Path,
                        help="Parent directory in which motortrust will be created")
    parser.add_argument("--manifest", type=Path,
                        help="Optional manifest path (default: parts-dir/release-manifest.json)")
    parser.add_argument("--overwrite", action="store_true",
                        help="Replace an existing motortrust directory, keeping it as a backup")
    args = parser.parse_args(argv)
    temporary = None
    try:
        parts_dir = args.parts_dir.expanduser().resolve()
        require(parts_dir.is_dir(), "parts-dir is not a directory")
        manifest_path = (args.manifest.expanduser() if args.manifest else
                         parts_dir / MANIFEST_NAME)
        manifest = load_manifest(manifest_path)
        destination = args.destination.expanduser().resolve()
        require(not destination.exists() or destination.is_dir(),
                "destination is not a directory")
        target = destination / ROOT_DIRECTORY
        require(not target.is_symlink(), "Destination motortrust is a symlink")
        require(args.overwrite or not target.exists(),
                "Destination motortrust already exists; use --overwrite explicitly")
        destination.mkdir(parents=True, exist_ok=True)
        temporary = Path(tempfile.mkdtemp(prefix=".motortrust-restore-", dir=str(destination)))
        # Fixed local archive name: the manifest filename is descriptive metadata only.
        archive_path = temporary / "verified.tar.gz"
        merge_verified_parts(parts_dir, manifest, archive_path)
        staging = temporary / "staging"
        staging.mkdir()
        file_count, unpacked_size = extract_safely(
            archive_path, staging, manifest["archive"]["unpacked_size_bytes"])
        backup = install(staging / ROOT_DIRECTORY, target, args.overwrite)
        print(f"Restored {file_count} files / {unpacked_size} bytes to {target}")
        if backup is not None:
            print(f"Previous project retained at: {backup}")
        print("This restores files only. Rebuild the Python environment separately.")
        print("Known limitations are recorded in RESTORE_CN.txt and the manifest notes.")
        return 0
    except (RestoreError, OSError, ValueError, tarfile.TarError) as error:
        print(f"RESTORE FAILED: {error}", file=sys.stderr)
        return 1
    except KeyboardInterrupt:
        print("RESTORE CANCELLED", file=sys.stderr)
        return 130
    finally:
        if temporary is not None:
            shutil.rmtree(str(temporary), ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main())
