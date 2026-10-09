# Independent Paper 1 review of the JOM preparation

Checked: 2026-10-09. This review is independent of the manuscript authoring/building
pass. It does not add an experiment, refit a detector, or alter saved results.

## Scientific claims and text

The main manuscript, supplementary source and cover letter preserve the critical
numbers: exploratory KAIST 1608/1680 (95.71%) with 0/42 health alarms; external
primary 96/384 (25.00%) with 1/32 and AUROC 0.6354; descriptive Wilson upper
15.74%, above 12%; comparator MinCovDet 269/384 (70.05%) with 0/32 at the fixed
primary seed and only 3/5 seeds passing H1. No detector is reassigned as primary.
The scientific boundaries are explicit: one physical external motor, turn/phase
confounding, unmatched pooled AUROC load support, dependent observations, internal
Git freeze rather than externally registered preregistration, association rather
than causation, and offline analyses without embedded-performance evidence.

The 0/21 transient primary parser failure is retained. Supplementary Section S9
correctly states 176 pooled prefault test windows across 12 held-out records, rather
than 176 per record. Each record supplies five primary and ten full-horizon fault
windows. The actual 200 W splits contain six fit records and five calibration
records per held-out record, and 67-88 calibration windows. This is a presentation
clarification, not a change to signals or predictions.

The historical metadata records scikit-learn 1.9.0 and the current required Conda
environment contains 1.9.1. The revised supplementary source explicitly says that
a complete original lock was not located and that original predictions are retained
instead of being replaced by current stochastic refits. The main freeze wording
now refers to dependency specifications and recorded tool versions.

## First rendering pass: not a final pass

The first supplementary rendering had twenty pages. Pages 1-12 were actually
viewed as PNGs. No clipped page contents, absent glyphs or overlapping elements
were seen. However, the 11-column external comparison at pages 4-5 and the wide
paired/seed/feature/sampling tables at pages 5-11 used narrow columns; words were
broken inside names and at least one threshold was broken across numeric digits
(183.887 became separate lines 183.88 and 7). This is a readability defect.

The authoring agent was notified and is splitting tables with more than seven
columns into repeated-key parts. Remaining first-pass pages were not reviewed
because the table revision changes pagination. No complete visual approval is
claimed for that superseded rendering. The final pass will be reported separately.

## Independent first code ZIP check

The first independent ZIP check inspected a 7,545,486-byte archive with 568 unique
entries, 567 manifest-covered files, and a maximum uncompressed file size of
1,002,385 bytes. ZIP CRC and every manifest SHA-256 passed; no raw datasets or
Paper 2-4 paths were included. The export had no processed feature inputs, so saved
evidence verification did not require re-downloading large raw archives.

The archive was extracted to `tmp/jom/bundle-audit`; all checks used the prescribed
Conda interpreter with `PYTHONPATH` pointing to that extracted `src`, ensuring the
parent project's installed editable package did not supply missing code. Both the
historical validator and the new fine-grained JOM audit passed, as did Ruff. The
first included test run had 131 passes and three failures in the legacy
`test_supplementary_material.py`, whose JEET supplementary regeneration requires
processed feature tables that were absent from the compact bundle.

One obsolete absolute workstation path remained in
`results/external_pmsm_analysis/input_manifest.csv`. The parent was notified to
exclude this nonessential execution manifest from distribution while preserving
the original project file. Neither this path nor the three test failures invalidates
the frozen numerical results. They are packaging checks that must be repaired or
explicitly excluded with a recorded scope before final handoff. Final ZIP checks
must be rerun on the replacement archive; these first-pass counts are not the final
acceptance result.

Evidence logs: `tmp/jom/bundle_integrity_independent.json`,
`bundle_historical_evidence_check.log`, `bundle_jom_evidence_check.log`,
`bundle_ruff_check.log`, and `bundle_pytest_check.log`.

## Final supplementary visual pass

The replacement supplementary PDF has 22 pages. Every final page image, 1-22,
was actually viewed. Its SHA-256 is
`72eb425640dff5a8460cb35d873a069b47c15d56756531eb16ce7ea04aedc739`.
The split external/paired/seed/feature/sampling tables now retain readable numeric
values. No clipped content, overlapping elements, missing glyphs or broken numeric
digits were found. Repeated table keys and headers, captions, figures S1-S5 and
continuous page numbers were checked. The legacy 176-per-record statement is absent;
page 15 explicitly distinguishes 176 pooled prefault windows from each record's
five first-second and ten full-horizon post-onset windows.

The main and cover-letter title now agree. The cover letter retains external
25.00%, 1/32, AUROC 0.6354 and failed 12% gate alongside the exploratory 95.71%
result. The author confirmation/declaration placeholders remain explicitly marked;
this review does not certify author approval or readiness for direct upload.
The render used LibreOffice rather than native Word, so the author still needs
the stated final Word field/page check. The machine record is
`tmp/jom/supplementary_visual_qa_final.json`. After the final reference-formatting
revision, all 22 replacement page images were viewed again; the machine record
now includes SHA-256 for every page PNG. Earlier page PNG hashes were not retained,
so this approval relies on actual re-inspection, not assumed pixel identity.

An intermediate packaging rerender changed the PDF binary hash from the individually
inspected `de2f847...` version to the `d4972ca...` version; all 22 rendered page PNG
hashes matched the retained individually inspected pages exactly. The final
`72eb425...` PDF then corrected page 1's method count to the primary plus ten
comparators, consistent with eleven total external detectors. Only page 1's PNG
changed. That page was actually re-inspected and passed; pages 2-22 retain exactly
the individually inspected PNG hashes. The current visual approval therefore has
pixel-level continuity or an actual changed-page re-inspection for every page; it
does not assume that any changed source is harmless.
The durable record is
`submission/jom/reference_evidence/final_supplementary_visual_review.json`.

## Final standalone code ZIP pass

The replacement archive was independently extracted into
`tmp/jom/bundle-audit-final4`. Its exact size is 7,539,054 bytes and SHA-256 is
`247a2075054077b6119277ac98f591fad154ecf64729bcae0fd44022c32c3894`.
It contains 568 unique files, including 567 covered by the hash manifest.
ZIP CRC and every manifest hash pass. The largest unpacked file is 1,002,385 bytes.
The obsolete absolute input manifest and legacy JEET supplementary regeneration
tests are excluded from this compact Paper 1 export; original project files remain
preserved. No raw datasets, processed feature inputs, Papers 2-4 paths, Windows
workstation paths or current local absolute paths were detected in the distribution.
CSV/gzip evidence files retain their original reveal-hash identities. Exported
metadata sanitation is documented and is not presented as an original-byte metadata
copy.

All commands below were run from the extracted directory with the prescribed
Conda interpreter and `PYTHONPATH` explicitly set to the extracted `src`:

```sh
PYTHON=/Users/lkc/miniforge3/envs/motortrust/bin/python
export PYTHONPATH="$PWD/src"
"$PYTHON" -c 'import pmsm_sci; print(pmsm_sci.__file__)'
"$PYTHON" scripts/validate_manuscript_evidence.py --output ../bundle_final_historical_evidence.json
"$PYTHON" scripts/audit_jom_evidence.py --output ../bundle_final_jom_evidence.json
"$PYTHON" -m ruff check src scripts tests
"$PYTHON" -m pytest -ra
```

The import origin was the extracted package, not the editable parent checkout.
Both saved-evidence validators and Ruff pass. Every included test passes:
**134 passed in 2.74 s**. These are compact-bundle checks; they do not replace the
recorded full-project baseline and its four Paper 2-4 failures. The archive supports
standalone saved-evidence checking and submitted-artifact rebuilding. Signal-level
reproduction and optional refits still require downloading the licensed archives
and rebuilding the exact processed features, as the reproducibility guide states.

Final machine logs: `tmp/jom/bundle_integrity_independent_final.json`,
`bundle_final_import_origin_check.log`, `bundle_final_historical_evidence_check.log`,
`bundle_final_jom_evidence_check.log`, `bundle_final_ruff_check.log` and
`bundle_final_pytest_check.log`.

The final replacement builder obtains author redaction values from the author's
metadata file rather than embedding private email/ORCID literals in source code.
An independent scan of the entire final export, including decompressed gzip text,
found no actual author-contact literals or absolute execution metadata paths.
Remaining Windows-path strings are inspection/sanitation rule constants in builder
source, not a run's input paths. Every packaged result CSV/gzip file was also
compared byte-for-byte with its corresponding original project file: zero
mismatches. The three changed files relative to the prior `52e9f11...` archive
were the new private-delivery wrapper, reproducibility guide and supplementary
method-count wording. The wrapper's complete private author-review operation is
distinguished from the compact bundle's core artifact rebuild and evidence checks.
Its default one-command execution was separately verified by the parent in the
full project (`tmp/jom/delivery_rebuild.log`). The replacement
archive was freshly extracted, and both validators, Ruff and all 134 included
tests were rerun after that change.
