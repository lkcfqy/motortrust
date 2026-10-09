from pathlib import Path

import pytest

from pmsm_sci.faults.artifact_paths import frozen_feature_path


def test_relocation_keeps_an_existing_recorded_input_preferred(tmp_path: Path) -> None:
    recorded = tmp_path / "original.csv.gz"
    canonical = tmp_path / "canonical.csv.gz"
    recorded.write_bytes(b"original")
    canonical.write_bytes(b"relocated")
    assert frozen_feature_path(str(recorded), canonical) == recorded


def test_obsolete_workstation_path_uses_the_local_copy(tmp_path: Path) -> None:
    canonical = tmp_path / "canonical.csv.gz"
    canonical.write_bytes(b"frozen values")
    assert frozen_feature_path("missing-workstation/features.csv.gz", canonical) == canonical


def test_missing_explicit_override_never_silently_uses_another_input(tmp_path: Path) -> None:
    canonical = tmp_path / "canonical.csv.gz"
    canonical.write_bytes(b"frozen values")
    with pytest.raises(FileNotFoundError):
        frozen_feature_path(
            "missing-workstation/features.csv.gz", canonical, override=tmp_path / "missing.csv.gz"
        )
