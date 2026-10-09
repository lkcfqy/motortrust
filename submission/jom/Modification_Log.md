# JOM preparation modification log — 2026-10-09

## Scope and history

Work on `codex/paper1-jom` began with a clean `main`. No applicable AGENTS.md was found. The original `paper/`, `submission/jeet/`, frozen protocols, reveal logs, stored result files and shared bibliography remain unchanged. Papers 2–4 remain independent.

## Scientific presentation

The separate JOM manuscript focuses on healthy-only cross-dataset reliability, ranking reversal, trajectory drift and alarm failure. The abstract contains both the exploratory 95.71% and external 25.00% results. The original Log-Euclidean primary and preimplemented MinCovDet comparator retain their identities. All single-motor, confounding, support, dependency, causal and offline restrictions are explicit. Existing saved diagnostics were sufficient; no new model, seed search or experiment was added. Supplementary details include all saved comparisons and the original 0/21 parser failure. The 176 transient healthy windows are correctly described as pooled across 12 records, without changing predictions.

## Development

- `src/pmsm_sci/faults/statistics.py`: explicitly return zero/one Wilson boundary endpoints for k=0/n; unchanged nonboundary calculation and conclusions.
- `src/pmsm_sci/faults/artifact_paths.py` and two existing diagnostic loaders: relocate stale recorded input paths with explicit override and retained hash validation. Three regression tests cover priorities and errors.
- `scripts/audit_jom_evidence.py`: read-only fine-grained audit for blocks/calibration, seed reconciliation, transient windows/splits and reveal hashes.
- `scripts/build_jom_submission.py`: separate JOM identified Word files, editable equations, numbered references, Roman tables, captions, grayscale exports, real rendering, legacy DOC, protected direct Word edits, compact portable code ZIP with sanitized exported metadata and immutable prediction bytes.
- `scripts/package_jom_delivery.py`: one-command rebuild and private delivery archive with CRC/hash manifest and current-versus-inspected page-image comparison.
- `tests/test_jom_source_contract.py`: two checks for abstract failure visibility, keywords, citations, figures and title agreement.

## Editorial and formatting

Six main figures and three main tables remain; detailed comparisons, sensitivity results and audit details move to the supplement. Seven wide supplementary tables are split mechanically into repeated-key pairs with unchanged values/order. The S0 method-count wording is corrected to one primary plus ten comparators (eleven detectors total), with no changed results. Thirty references are checked using primary sources; the new JOM Park 2025 paper is used within its wound-field/FEM scope. Existing citation page discrepancies are recorded rather than silently choosing convenient metadata. Author-provided facts are filled, all remaining assertions stay visibly pending. No approval, signature, no-conflict declaration or institutional permission is invented.

## Verification and remaining work

See `QA_Report.md`, `Independent_Review.md`, `Reference_Audit.md`, page-image review JSON and `delivery_status.json`. Remaining four full-project test failures belong to Papers 2–4. The current environment is not claimed to be the original training lock. Final author declarations, native Word checks, actual portal forms/format, total charges and school recognition remain to be completed by the author. No submission, communication, payment or public release was performed.
