# Paper 1 Journal of Magnetics author review package

Prepared against official pages checked on 2026-10-09. This package is for the
author's final review. It is **not ready for immediate upload** while author fields,
declarations, official portal forms, membership eligibility and charges remain pending.
Nothing has been submitted, sent to an editor, paid for, signed or publicly released.

Author-provided name LI KAICHEN, official Changwon National University department
and postal address, email, ORCID 0009-0008-8743-3162, no-funding statement and sole-author
work are already saved. The author also confirmed telephone +82-10-3915-7350, no
fax, no competing interests, no previous publication/concurrent review, and data-license
compliance. Remaining author inputs are acknowledgments, applicable institutional
requirements, and final-version approval/responsibility for the AI-assisted work. Official portal forms,
non-member eligibility and all applicable charges still require verification.

The original `paper/` development manuscript, frozen protocols and `submission/jeet/`
are retained. Paper 2–4 are independent and are not used to improve Paper 1's frozen
results. The current JOM editorial sources are `manuscript.md` and `supplementary.md`.

Start with `Detailed_Review_CN.md` for the substantive review and corrections, then
`DELIVERY_INDEX.md` and `JOM_Author_Review_Package.zip`. The latter is a private review archive containing author contact details; it is not a public-release or portal-upload instruction. `delivery_status.json` reports whether current page pixels match the individually inspected pages.

## Deliverables and their intended use

- `Main_Manuscript_AUTHOR_INPUT_REQUIRED.docx`: editable, identified manuscript with
  visibly pending author fields, double-spaced body, numbered references, separate
  captions, Roman table sheets and six figure plates.
- `Main_Manuscript_AUTHOR_INPUT_REQUIRED.pdf`: PDF rendered from that DOCX for review.
- `Main_Manuscript_AUTHOR_INPUT_REQUIRED.doc`: legacy-format counterpart for the
  official online page's DOC instruction; inspect in native Word before uploading.
- `Supplementary_Material.docx` and `.pdf`: complete English supplementary evidence.
- `Cover_Letter_AUTHOR_INPUT_REQUIRED.docx`, `.pdf`, and `cover_letter.md`: JOM letter
  with explicit author confirmation fields, not a signed representation.
- `figures/`: individual grayscale PDF, PNG and TIFF exports plus caption text; original colour vector artwork is in `figures/color_sources/` and `figure_sources/`.
- `figure_sources/`: original vector artwork and generating Python scripts.
- `Paper1_Reproducibility_Code.zip`: Paper 1 code, tests, frozen protocols, selected
  derived outputs and SHA-256 manifest; no raw multi-GB archives.
- `Reproducibility_Guide.md`: environment, acquisition and reproduction commands.
- `Checklist_Preparation.md`, `Copyright_Preparation.md`, `official_forms/`: unsigned
  preparation notes and available official source material. Login-only official forms
  must be obtained and completed by the author in the active submission system.
- `Author_Input_Form_CN.md` and `author_metadata_REQUIRED.yaml`: author-owned inputs.
- `Costs_and_Upload_Guide_CN.md`: fees, unresolved charges and upload guidance.
- `Evidence_Audit.md`, `evidence_audit.json`, `Reference_Audit.md`,
  `English_Change_Log.md`, `QA_Report.md`, `build_metadata.json`: internal audit records.

## Rebuild on this workstation

From the repository root, use the existing Conda interpreter:

```bash
/Users/lkc/miniforge3/envs/motortrust/bin/python scripts/package_jom_delivery.py
```

This command verifies evidence, builds and renders the Word/PDF artifacts, and archives the figures and full private author-review delivery. `scripts/build_jom_submission.py` is the underlying document/code builder.

Scientific verification and authoring use that interpreter. Rendering uses the
Codex bundled Python and headless LibreOffice, not the system Python or a desktop
LibreOffice installation. Override `--render-python` and `--render-script` on another
host; `--no-render` only authors the sources and does **not** satisfy visual QA.
Rendered PNGs are internal intermediates under `tmp/jom/render/`.

Every rebuild must be followed by visual inspection if author information, wording,
fonts, layout, figures or fields change. The saved QA report applies only to the
reviewed output hashes. Native Microsoft Word pagination and legacy DOC conversion
remain author review steps; the journal's final typeset pages determine charges.

Final upload, editor contact, payment, public release and signing require separate
explicit author authorization.

Author fields are saved in the Markdown sources and author metadata YAML. Direct Word edits do not update those sources. The builder protects Word files edited since the last recorded build; save those edits before explicitly using `--overwrite-docx`.
