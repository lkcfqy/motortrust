"""Read-only Paper 1 audit of saved predictions, splits and reveal-artifact hashes.

This is evidence verification, not a new detector run. It never writes into results/.
The original validator retains its historical manuscript wording checks; this audit
also verifies the seed and transient claims from the lowest saved prediction grain.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.metrics import roc_auc_score

from pmsm_sci.faults.statistics import wilson_interval

if __package__:
    from scripts import validate_manuscript_evidence as historical
else:
    import validate_manuscript_evidence as historical

ROOT = Path(__file__).resolve().parents[1]
PRIMARY_SEED = 20260820
EXPECTED_SEEDS = {PRIMARY_SEED, 1201, 2402, 3603, 4804}


def read_frame(path: Path) -> pd.DataFrame:
    frame = pd.read_csv(path)
    for name in ("alarm", "is_healthy", "primary_post_window", "main_endpoint_compatible"):
        if name in frame:
            frame[name] = historical._bool(frame[name])
    return frame


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def check_p_values(frame: pd.DataFrame) -> None:
    calibration = frame.loc[frame["role"].eq("calibration"), "score"].to_numpy()
    if len(calibration) != 24:
        raise AssertionError("External calibration must contain 24 frozen healthy blocks")
    expected = (1 + (calibration[:, None] >= frame["score"].to_numpy()).sum(axis=0)) / 25
    np.testing.assert_allclose(frame["p_value"], expected, rtol=0, atol=1e-15)
    np.testing.assert_array_equal(frame["alarm"], expected <= 0.05)
    np.testing.assert_allclose(
        frame["score"],
        frame[["subsystem_score_SubSys1", "subsystem_score_SubSys2"]].max(axis=1),
        rtol=0,
        atol=1e-12,
    )
    if frame.duplicated(["record_id", "block_id"]).any():
        raise AssertionError("Duplicate system record/block prediction")
    role_loads = {
        role: set(frame.loc[frame["role"].eq(role), "load_nm"])
        for role in ("adaptation", "calibration", "health_test")
    }
    if role_loads != {
        "adaptation": {0.0}, "calibration": {10.0, 20.0, 30.0},
        "health_test": {5.0, 15.0, 25.0, 35.0},
    }:
        raise AssertionError(f"External frozen role/load partition changed: {role_loads}")


def summarize_external(frame: pd.DataFrame) -> dict[str, object]:
    check_p_values(frame)
    return historical._summarize_external(frame)


def audit_external(root: Path) -> dict[str, object]:
    summaries = {}
    aggregate = read_frame(root / "results/external_pmsm_validation/aggregate_summary.csv")
    for method in aggregate["method"]:
        frame = read_frame(
            root / "results/external_pmsm_validation" / method / "system_block_predictions.csv"
        )
        summary = summarize_external(frame)
        stored = aggregate.loc[aggregate["method"].eq(method)].iloc[0]
        for key, stored_key in (
            ("false_alarms", "false_alarms"),
            ("fault_alarms", None),
            ("block_auroc", "block_auroc"),
            ("record_macro_detection_rate", "fault_record_macro_detection_rate"),
        ):
            if stored_key:
                np.testing.assert_allclose(summary[key], stored[stored_key], rtol=0, atol=1e-12)
        summaries[method] = summary
    if len(summaries) != 11:
        raise AssertionError("Frozen external comparison must retain all eleven methods")
    return summaries


def audit_seeds(root: Path) -> list[dict[str, object]]:
    frame = read_frame(root / "results/external_seed_sensitivity/block_predictions_by_seed.csv.gz")
    rows = []
    for (method, seed), group in frame.groupby(["method", "seed"], sort=True):
        summary = summarize_external(group)
        rows.append({"method": method, "seed": int(seed), **summary})
        if int(seed) == PRIMARY_SEED:
            primary = read_frame(
                root / "results/external_pmsm_validation" / method / "system_block_predictions.csv"
            )
            keys = ["record_id", "block_id"]
            seed_values = group.set_index(keys).sort_index()
            primary_values = primary.set_index(keys).sort_index()
            pd.testing.assert_index_equal(seed_values.index, primary_values.index)
            np.testing.assert_array_equal(seed_values["alarm"], primary_values["alarm"])
            np.testing.assert_allclose(
                seed_values["score"], primary_values["score"], rtol=0, atol=1e-8
            )
    for method, group in frame.groupby("method"):
        if set(group["seed"]) != EXPECTED_SEEDS:
            raise AssertionError(f"Seed inventory differs for {method}")
    if len(rows) != 20:
        raise AssertionError("Seed audit must retain four comparators and five seeds")
    return rows


def audit_transient(root: Path) -> list[dict[str, object]]:
    base = root / "results/transient_pmsm_validation_post_reveal_200w"
    frame = read_frame(base / "window_predictions.csv.gz")
    splits = pd.read_csv(base / "record_splits.csv")
    for row in splits.itertuples():
        fit = set(row.fit_records.split("|"))
        calibration = set(row.calibration_records.split("|"))
        if fit & calibration or row.heldout_record_id in fit | calibration:
            raise AssertionError("Transient heldout/fit/calibration records overlap")
        if row.calibration_windows < 19:
            raise AssertionError("Transient calibration is arithmetically infeasible")
    np.testing.assert_array_equal(frame["alarm"], frame["p_value"] <= 0.05)
    if frame.duplicated(["record_id", "method", "seed", "segment", "window_id"]).any():
        raise AssertionError("Duplicate transient prediction")
    rows = []
    for (method, seed), group in frame.groupby(["method", "seed"], sort=True):
        healthy = group.loc[group["segment"].eq("pre_fault")]
        primary_fault = group.loc[group["segment"].eq("post_fault") & group["primary_post_window"]]
        all_fault = group.loc[group["segment"].eq("post_fault")]
        if (len(healthy), len(primary_fault), len(all_fault)) != (176, 60, 120):
            raise AssertionError("Transient pre/primary/all-window denominators changed")
        aucs = []
        for record, values in group.groupby("record_id", sort=True):
            selected = values.loc[values["segment"].eq("pre_fault") | values["primary_post_window"]]
            aucs.append(roc_auc_score(selected["segment"].eq("post_fault"), selected["score"]))
            example = values.iloc[0]
            if record in set(example["fit_records"].split("|")) | set(
                example["calibration_records"].split("|")):
                raise AssertionError("Heldout transient record appears in prediction fit metadata")
        rows.append({
            "method": method, "seed": int(seed), "records": int(group["record_id"].nunique()),
            "healthy_windows": len(healthy), "false_alarms": int(healthy["alarm"].sum()),
            "first_second_windows": len(primary_fault),
            "first_second_detections": int(primary_fault["alarm"].sum()),
            "two_second_windows": len(all_fault),
            "two_second_detections": int(all_fault["alarm"].sum()),
            "mean_record_auroc": float(np.mean(aucs)),
        })
    return rows


def audit_reveal_hashes(root: Path) -> list[dict[str, object]]:
    # Only immutable value/compatibility artifacts are required. Original metadata
    # contains historical workstation paths; exported metadata may be sanitized.
    expected = {
        "results/transient_feature_build/record_compatibility.csv":
            "b2f737ca6d2dfbd20f211b1e083dd7a045954658f21f7a7553bcf8fb93aa219e",
        "results/transient_feature_build/onset_diagnostics.csv":
            "7eb70257593da06f682a3ddda54a9d260d4fc514f645237f5ca74b08f8da61a6",
        "results/transient_feature_build_post_reveal_implicit_time/record_compatibility.csv":
            "315d0887fc8db78d87f6ac8db3c120bc91977b4ee4b4e42a8b65748a5c7172a0",
        "results/transient_feature_build_post_reveal_implicit_time/onset_diagnostics.csv":
            "a495a24658fc9769ac3346a8c9a7979d988b0f1a63c280196073922acc1f23ac",
        "results/transient_pmsm_validation_post_reveal_200w/aggregate_summary.csv":
            "aa4904f52069c94e3d5ddf885b63fffa54cd35b71671fc5ab85cc9ee1bede41b",
        "results/transient_pmsm_validation_post_reveal_200w/per_record_summary.csv":
            "b73c1260342d09d1d52546d6fbded7106e352127e80e6dacc67538d556447ad8",
        "results/transient_pmsm_validation_post_reveal_200w/window_predictions.csv.gz":
            "4c474ac9da88f2b34daff2bb2151939ccc2b77b004ea3e4dfb959fe5da19e3d6",
    }
    rows = []
    for relative, expected_hash in expected.items():
        actual = sha256(root / relative)
        if actual != expected_hash:
            raise AssertionError(f"Reveal artifact hash mismatch: {relative}")
        rows.append({"path": relative, "sha256": actual, "matches_reveal_log": True})
    return rows


def audit(root: Path) -> dict[str, object]:
    return {
        "status": "pass", "analysis_role": "read-only evidence verification; no refit",
        "kaist": historical.recompute_kaist(root),
        "external_headlines": historical.recompute_external(root),
        "external_all_methods_from_system_blocks": audit_external(root),
        "external_seed_results_from_system_blocks": audit_seeds(root),
        "transient_compatibility": historical.recompute_transient(root),
        "transient_results_from_windows": audit_transient(root),
        "reveal_artifact_hashes": audit_reveal_hashes(root),
        "wilson_boundary_check": {
            "zero_of_42": wilson_interval(0, 42), "one_of_32": wilson_interval(1, 32),
            "all_of_42": wilson_interval(42, 42),
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--output", type=Path, default=ROOT / "submission/jom/evidence_audit.json")
    args = parser.parse_args()
    result = audit(args.root)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"status": result["status"], "output": str(args.output)}))


if __name__ == "__main__":
    main()
