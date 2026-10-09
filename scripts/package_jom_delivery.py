"""Rebuild and archive the private JOM author-review delivery.

Visual approval is carried forward only when every rendered page matches the
individually inspected PNG hashes. Changed pages require a new human/agent review.
Copyrighted reference full texts and temporary render images are not distributed.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "submission/jom"
FIXED_DATE = (2026, 10, 9, 0, 0, 0)


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def write_archive(target: Path, paths: list[Path]) -> dict:
    manifest = []
    with zipfile.ZipFile(target, "w") as archive:
        for path in sorted(set(paths)):
            data = path.read_bytes()
            if len(data) > 25_000_000:
                raise ValueError(f"Unexpected large delivery file: {path.relative_to(ROOT)}")
            name = path.relative_to(ROOT).as_posix()
            archive.writestr(
                zipfile.ZipInfo(name, FIXED_DATE), data, compress_type=zipfile.ZIP_DEFLATED
            )
            manifest.append({"path": name, "bytes": len(data), "sha256": sha(data)})
        archive.writestr(
            zipfile.ZipInfo("DELIVERY_MANIFEST.json", FIXED_DATE),
            json.dumps(manifest, indent=2) + "\n",
            compress_type=zipfile.ZIP_DEFLATED,
        )
    with zipfile.ZipFile(target) as archive:
        bad = archive.testzip()
        if bad:
            raise ValueError(f"Archive CRC failure: {bad}")
        for item in manifest:
            if sha(archive.read(item["path"])) != item["sha256"]:
                raise ValueError(f"Archive manifest mismatch: {item['path']}")
    return {
        "file": target.name,
        "bytes": target.stat().st_size,
        "files": len(manifest),
        "sha256": sha(target.read_bytes()),
        "crc_and_manifest": "pass",
    }


def review_status() -> dict:
    records = (
        ("final_main_visual_review.json", "Main_Manuscript_AUTHOR_INPUT_REQUIRED"),
        ("final_supplementary_visual_review.json", "Supplementary_Material"),
        ("final_cover_visual_review.json", "Cover_Letter_AUTHOR_INPUT_REQUIRED"),
    )
    status = {}
    for name, stem in records:
        record_path = OUT / "reference_evidence" / name
        if not record_path.is_file():
            status[stem] = {"current": False, "reason": "No page inspection record"}
            continue
        record = json.loads(record_path.read_text())
        expected = record.get("page_png_sha256") or {
            str(p["page"]): p["sha256"] for p in record.get("page_images", [])
        }
        page_dir = ROOT / "tmp/jom/render" / stem
        current_pages = list(page_dir.glob("page-*.png"))
        changed = []
        for number, digest in expected.items():
            path = page_dir / f"page-{number}.png"
            if not path.is_file() or sha(path.read_bytes()) != digest:
                changed.append(int(number))
        passed = bool(expected) and not changed and len(current_pages) == len(expected)
        status[stem] = {
            "current": passed,
            "reviewed_pages": len(expected),
            "changed_pages": sorted(changed),
            "current_pdf_sha256": sha((OUT / f"{stem}.pdf").read_bytes()),
            "method": "Every current PNG hash compared with individually inspected page hashes",
        }
    return status


def package() -> dict:
    required = (
        "QA_Report.md",
        "DELIVERY_INDEX.md",
        "Main_Manuscript_AUTHOR_INPUT_REQUIRED.docx",
        "Main_Manuscript_AUTHOR_INPUT_REQUIRED.pdf",
        "Main_Manuscript_AUTHOR_INPUT_REQUIRED.doc",
        "Supplementary_Material.docx",
        "Supplementary_Material.pdf",
        "Cover_Letter_AUTHOR_INPUT_REQUIRED.docx",
        "Cover_Letter_AUTHOR_INPUT_REQUIRED.pdf",
        "Paper1_Reproducibility_Code.zip",
        "build_metadata.json",
    )
    for name in required:
        if not (OUT / name).is_file():
            raise FileNotFoundError(f"Author-review package is incomplete: {name}")
    figure_paths = [
        p
        for directory in ("figures", "figure_sources")
        for p in (OUT / directory).rglob("*")
        if p.is_file()
    ]
    figures = write_archive(OUT / "Figures_and_Sources.zip", figure_paths)
    status = {
        "date": "2026-10-09",
        "purpose": "Private author review; author contact details included; not a public release",
        "upload_ready": False,
        "pending": "Author declarations/approval, actual official forms, portal rules and total fees",
        "visual_review": review_status(),
        "figures_archive": figures,
        "code_archive": json.loads((OUT / "build_metadata.json").read_text())["zip"],
        "excluded": ["Copyrighted reference full texts", "Raw data", "Temporary page images"],
    }
    (OUT / "delivery_status.json").write_text(json.dumps(status, indent=2) + "\n")
    files = []
    for path in OUT.rglob("*"):
        if not path.is_file() or path.name in {
            "JOM_Author_Review_Package.zip",
            "delivery_archive_metadata.json",
        }:
            continue
        if "__pycache__" in path.parts or path.name.startswith("."):
            continue
        if "reference_evidence" in path.parts and (
            path.suffix != ".json"
            or (
                not path.name.startswith("final_")
                and path.name
                not in {"legacy_doc_visual_review.json", "admin_material_consistency_check.json"}
            )
        ):
            continue
        files.append(path)
    files.append(ROOT / "docs/jom_submission_requirements_2026-10-09.md")
    complete = write_archive(OUT / "JOM_Author_Review_Package.zip", files)
    # Keep the archive's own digest outside the archive to avoid a circular hash.
    (OUT / "delivery_archive_metadata.json").write_text(json.dumps(complete, indent=2) + "\n")
    return {"delivery": complete, "review": status}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--package-only", action="store_true", help="Archive existing rendered/checked artifacts"
    )
    args = parser.parse_args()
    if not args.package_only:
        subprocess.run(
            [sys.executable, str(ROOT / "scripts/build_jom_submission.py")],
            cwd=ROOT,
            check=True,
        )
    print(json.dumps(package(), indent=2))


if __name__ == "__main__":
    main()
