# Paper 1 reproducibility and data guide

Checked: 2026-10-09. All commands below are run from the project root. The CLI flags
were checked against the actual scripts; `--help` was executed for the primary
download, extraction, feature, validation, diagnostic and figure entry points.
This guide distinguishes rebuilding submitted artifacts, verifying saved evidence,
and independently reproducing signal-level computations.

## Environment

On the author's current workstation, use:

```sh
PYTHON=/Users/lkc/miniforge3/envs/motortrust/bin/python
"$PYTHON" -m pip check
```

After extracting the code bundle on another machine, install the project into a
Python 3.12 environment and set `PYTHON` to that environment's interpreter:

```sh
python -m venv .venv
.venv/bin/python -m pip install -e ".[dev,publication]"
PYTHON=.venv/bin/python
```

On Windows, use `.venv\Scripts\python.exe` directly. The current tested package
versions are in `Current_Environment.txt`. The historical external model metadata
records scikit-learn 1.9.0; the current audit environment has 1.9.1. No complete
original training-environment lock was located. Saved predictions and reveal hashes
are the immutable reference; a new numerical training run must be reconciled and
must not overwrite or silently replace them.

## One command for the complete private delivery on the author workstation

```sh
"$PYTHON" scripts/package_jom_delivery.py
```

This invokes the core `build_jom_submission.py` builder, then produces `Figures_and_Sources.zip` and the private `JOM_Author_Review_Package.zip`, each with a CRC/hash manifest. The archive excludes third-party reference full texts. It uses the curated JOM sources and saved Paper 1 evidence. Rendering requires
the publication runtime described in the builder/QA report. Building artifacts
does not repeat an external fault reveal, fit a new detector or add evidence.

The compact code ZIP intentionally omits private author administration and final visual-review records. From that extraction, use `"$PYTHON" scripts/build_jom_submission.py` to rebuild the editable submission artifacts and render them using an available publication runtime. The private-delivery wrapper additionally requires the author-reviewed QA report, delivery index and completed local administrative files; it is not a promised standalone command from the compact ZIP. Rebuilding any changed pages requires new visual inspection.

## Evidence checks without raw data or retraining

```sh
"$PYTHON" scripts/validate_manuscript_evidence.py --output tmp/reproduction/historical_evidence.json
"$PYTHON" scripts/audit_jom_evidence.py --output tmp/reproduction/jom_evidence.json
"$PYTHON" -m ruff check src scripts tests
"$PYTHON" -m pytest -ra tests/test_fault_baseline.py tests/test_external_seed_sensitivity.py tests/test_external_feature_drift.py tests/test_manuscript_evidence_validation.py
```

The historical validator also checks the preserved historical manuscript wording;
the second audit works from saved system-block and transient-window predictions.
It verifies all eleven external methods, calibration p-values, system maxima,
complete five-seed outputs, primary-seed reconciliation, transient record splits,
window-level endpoints and immutable reveal-artifact hashes. It only writes its
JSON report. The numerical/scope checks for the current JOM presentation are part
of the JOM builder and final QA.

## Data access and attribution

Raw data are excluded from the code bundle. Each dataset uses CC BY 4.0 and must
be attributed to the original creators and dataset DOI in reuse.

| Dataset | Access | Scope |
|---|---|---|
| KAIST current/vibration stator-fault dataset, version 5 | https://doi.org/10.17632/rgn5brrgrn.5 | Exploratory source-family benchmark: 3 physical PMSMs, duplicate healthy aliases removed |
| Dual-three-phase PMSM short-circuit emulation | https://doi.org/10.5281/zenodo.13889418 | Primary internally frozen cross-dataset test: 8 healthy + 48 fault operating records from 1 physical motor |
| 200 W / 20 kW transient interturn short circuit | https://doi.org/10.5281/zenodo.15631383 | Secondary frozen parser failure plus separately labeled post-reveal single-motor sensitivity |

`docs/data_sources.yaml`, download manifests and reveal logs provide checksums,
file identifiers, licensing, time intervals and historical execution status.
The source ZIP files total approximately 7 GB; the primary external MAT files
total approximately 1.32 GB; the transient ZIP is approximately 91.5 MB.
Historical protocol status lines and script descriptions remain preserved even
when they describe the earlier sealed stage; all fault datasets are now revealed.

## Optional signal-level reproduction into separate outputs

Run these only in a fresh extraction or with the explicit output paths below.
They are reproduction runs on already revealed public data, not new confirmations.
Do not change features, windows, roles, thresholds, model set, exclusions or seeds
to improve agreement or performance. Keep saved `results/` intact.

### KAIST

```sh
"$PYTHON" scripts/download_kaist_faults.py
"$PYTHON" scripts/extract_kaist_current.py
"$PYTHON" scripts/build_current_features.py --output tmp/reproduction/kaist_current_features.csv.gz
"$PYTHON" scripts/run_healthy_covariance_baseline.py --features tmp/reproduction/kaist_current_features.csv.gz --results-dir tmp/reproduction/healthy_covariance_v0
"$PYTHON" scripts/compare_covariance_methods.py --results-dir tmp/reproduction/healthy_covariance_v0
"$PYTHON" scripts/run_oneclass_baselines.py --features tmp/reproduction/kaist_current_features.csv.gz --results-dir tmp/reproduction/oneclass_baselines
"$PYTHON" scripts/compare_oneclass_to_proposed.py --oneclass-dir tmp/reproduction/oneclass_baselines --proposed-dir tmp/reproduction/healthy_covariance_v0
```

Defaults retain 0.2 s non-overlapping windows, first 120 s, 3 s/max blocks,
4/1/20/1/14 target-health split, alpha=0.05 and the frozen feature-arm/ridge rules.
The exploratory results must retain that identity after reproduction.

### Primary external test

```sh
"$PYTHON" scripts/download_external_pmsm_validation.py --datasets dual_three_phase_health dual_three_phase_fault_reveal
"$PYTHON" scripts/build_external_pmsm_health_features.py --output tmp/reproduction/external_features.csv.gz
"$PYTHON" scripts/run_external_pmsm_validation.py --source-features tmp/reproduction/kaist_current_features.csv.gz --external-features tmp/reproduction/external_features.csv.gz --require-faults --results-dir tmp/reproduction/external_validation
```

The feature-builder name contains "health" for historical reasons but the frozen
filename grammar reads the complete now-revealed 56-record directory. The analysis
interval remains [12,36) s, with two measured three-phase current subsystems and
one system-level max/calibration. Results from a new interpreter are reproduction
outputs and are compared with the preserved primary run.

Saved-output diagnostics can be recomputed without fitting or changing thresholds:

```sh
"$PYTHON" scripts/analyze_external_pmsm_results.py --validation-dir results/external_pmsm_validation --output-dir tmp/reproduction/external_analysis
"$PYTHON" scripts/analyze_external_failure_diagnostics.py --validation-dir results/external_pmsm_validation --health-block-inventory results/external_health_audit/block_inventory.csv --output-dir tmp/reproduction/failure_diagnostics
"$PYTHON" scripts/analyze_external_feature_drift.py --frozen-results-dir results/external_pmsm_validation --source-features data/processed/kaist_current_features.csv.gz --external-features data/processed/external_dual_three_phase_health_features.csv.gz --results-dir tmp/reproduction/feature_drift
```

The feature-geometry diagnostic requires the exact hash-locked processed feature
files. The path resolver supports relocation but will reject a hash mismatch.
All these diagnostics remain post-reveal. Five-seed reproduction refits only the
preimplemented stochastic models on frozen healthy inputs:

```sh
"$PYTHON" scripts/run_external_seed_sensitivity.py --frozen-results-dir results/external_pmsm_validation --source-features data/processed/kaist_current_features.csv.gz --external-features data/processed/external_dual_three_phase_health_features.csv.gz --results-dir tmp/reproduction/seed_sensitivity
```

If exact primary-seed reconciliation fails in a different library version, retain
both runs and report the difference; do not choose a replacement seed.

### Secondary transient compatibility

```sh
"$PYTHON" scripts/download_transient_pmsm_archive.py
"$PYTHON" scripts/audit_transient_pmsm_archive.py --output-dir tmp/reproduction/transient_archive_audit
"$PYTHON" -m zipfile -e data/raw/transient_cross_capacity/OpenData.zip data/raw/transient_cross_capacity/extracted
"$PYTHON" scripts/build_transient_pmsm_features.py --features tmp/reproduction/transient_primary_features.csv.gz --results-dir tmp/reproduction/transient_primary_compatibility
"$PYTHON" scripts/build_transient_pmsm_features_post_reveal.py --features tmp/reproduction/transient_post_reveal_features.csv.gz --results-dir tmp/reproduction/transient_post_reveal_compatibility
```

The primary parser's expected outcome is 0/21 compatible and no detector scoring.
The opt-in repair is post-reveal. Only 4/9 records from the 20 kW motor meet the
frozen endpoint, so the two-motor scoring gate remains failed. The saved 200 W-only
window predictions may be independently audited with `audit_jom_evidence.py`;
they cannot reinstate confirmation. Producing a new 200 W-only scoring run requires
an explicitly separated compatibility table for the 12 200 W records, preserving
the original 21-row table and failure. The submitted package does not run this as
a default submission requirement.

## Minimum saved files for standalone evidence verification

The code bundle should include `pyproject.toml`, Paper 1 `src` and scripts/tests,
the preserved historical manuscript, original protocols/reveal logs, the JOM sources,
references, `docs/data_sources.yaml`, and these saved evidence inputs:

- `results/healthy_covariance_v0/target_1kW/scale_free/log_euclidean_entity_covariance/block_predictions.csv`
- `results/healthy_covariance_v0/target_1.5kW/scale_free/log_euclidean_entity_covariance/block_predictions.csv`
- `results/healthy_covariance_v0/target_3kW/scale_free/log_euclidean_entity_covariance/block_predictions.csv`
- `results/oneclass_baselines/record_summary.csv` and `comparison_to_proposed.csv`
- `results/external_pmsm_validation/` (all eleven system-block files and summary/metadata files)
- `results/external_seed_sensitivity/block_predictions_by_seed.csv.gz` and `aggregate_seed_ranges.csv`
- `results/sampling_rate_sensitivity/external_method_comparison.csv`
- `results/transient_feature_build/record_compatibility.csv` and `onset_diagnostics.csv`
- `results/transient_feature_build_post_reveal_implicit_time/record_compatibility.csv` and `onset_diagnostics.csv`
- `results/transient_pmsm_validation_post_reveal_200w/aggregate_summary.csv`, `per_record_summary.csv`, `window_predictions.csv.gz` and `record_splits.csv`

To rebuild all main/supplement figures from saved summaries also include Paper 1
covariance/one-class summaries/comparisons, external health audit/block inventory,
external analysis/failure-diagnostic/feature-drift tables and all cited sampling-rate
diagnostic tables. The exact packaged file manifest is authoritative. The four
processed Paper 1 feature tables together total about 20 MB compressed and enable
optional refitting/geometry reconstruction without redistributing raw signals.
They must be included if the bundle promises those operations without re-download.

Export sanitation may replace obsolete workstation paths in metadata, while the
original project files and their historical hashes remain preserved. Such exported
copies must be labeled as sanitized metadata. CSV/gzip prediction files used in
the reveal-hash audit must retain original bytes and line endings. The ZIP excludes
raw datasets, `.git`, caches, credentials, author private contact drafts and Papers
2–4 experiments; a compact hash manifest and ZIP CRC test document integrity.
