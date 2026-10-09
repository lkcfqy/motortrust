"""Resolve relocated frozen artifacts without modifying their historical metadata."""

from pathlib import Path


def frozen_feature_path(
    recorded_path: str, canonical_path: Path, *, override: Path | None = None
) -> Path:
    """Locate an input; callers must still verify its frozen SHA-256 before reading.

    Historical metadata may contain a Windows absolute path. The canonical local
    copy is used only when that exact historical path no longer exists. An explicit
    override never silently falls back if it is missing.
    """
    if override is not None:
        candidate = override
    else:
        recorded = Path(recorded_path)
        candidate = recorded if recorded.is_file() else canonical_path
    if not candidate.is_file():
        raise FileNotFoundError(f"Frozen feature input not found: {candidate}")
    return candidate
