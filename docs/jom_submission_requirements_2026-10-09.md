# JOM official submission-rule check

Checked: **2026-10-09 (Asia/Seoul)**. Target: **Journal of Magnetics**, Korean Magnetics Society, ISSN 1226-1750 / 2233-6656. This check concerns the English journal, not Journal of the Korean Magnetics Society or Springer/TMS's similarly abbreviated JOM. Public-source snapshots and their hashes are in `submission/jom/official_forms/`.

## Verified requirements

| Item | Official requirement / consequence |
|---|---|
| Main file | English MS Word manuscript, with figures, sequential page numbers, A4 or letter, double spacing. Include author/institution/address and corresponding-author name, address, telephone, fax and email. Prepare the identified-author version. |
| Abstract / keywords | 100–150 words; 3–6 keywords. |
| Figures / tables | Separate figure files; fine-resolution TIFF/GIF/JPEG preferred, Arabic figure numbers, English labels/captions; collect captions on a separate page. Tables on separate sheets with Roman numerals and captions; mark insertion points. |
| Equations / references | Number displayed equations; italic variables, upright units, SI preferred. Consecutive bracket citations and a numbered list using journal/volume/page/year style. Numbered centered bold headings. |
| Forms | Copyright-transfer form and author checklist accompany submission. The public submission page directs authors to the actual forms in the online system. |
| Declarations | Acknowledge financial support and potential conflicts. Author must confirm originality, exclusive submission, final approval and accountability. Do not predeclare unknown facts. |
| After acceptance | Submit the final electronic manuscript. Author proofs are due back within two days of receipt, with typographical corrections only. Plan author availability for this short proof stage. |

Source: [Instructions to Authors](https://jom.magnetics.or.kr/submission/journal/pages/instructions_authors.vm), [Authors Responsibilities](https://jom.magnetics.or.kr/submission/journal/pages/authors_responsibilities.vm), [Research and Publication Ethics](https://jom.magnetics.or.kr/submission/journal/pages/policy_ethics.vm).

## Important public-page conflicts and unresolved items

The [Online Submission page](https://jom.magnetics.or.kr/submission/journal/pages/online_submission.vm) explicitly says Society membership is required and rejects `.docx` made with MS Word 2007/2008. It supplies a legacy [official DOC template](https://jom.magnetics.or.kr/download/JoM_Template.doc), downloaded unchanged to `submission/jom/official_forms/JoM_Template_official_2026-10-09.doc`. The [login page](https://jom.magnetics.or.kr/submission/journal/pages/login.vm?ViewFlag=author) separately offers international-author account creation. No public text resolves whether an international author at a Korean institution requires paid membership. The package therefore includes an editable DOCX plus a legacy DOC conversion where feasible; actual portal acceptance and membership applicability require author verification. This is a source conflict, not evidence for a waiver.

No downloadable official author-checklist or copyright-transfer blank was exposed by the checked public pages; their availability inside the authenticated submission workflow remains unverified. `Checklist_Preparation.md` and `Copyright_Preparation.md` are unsigned working aids, not official forms and not upload-ready replacements. This task did not log in, create an account, contact the journal, upload, sign or pay.

No explicit public rule was found for supplementary-file hosting/format/size, code archives, a required AI-disclosure format, numerical image DPI, or a mandatory ORCID. Their absence from the checked pages is **not** a prohibition or exemption. The author should check the portal's current prompts. A truthful AI-assistance statement is prepared for author approval; AI cannot be an author under the journal's human responsibility criteria. Supplemental files are prepared for review, with hosting/upload acceptance left pending. The package's TIFF export setting is a production choice, not a claimed JOM rule; inspect effective size and label legibility before upload.

## Charges and budget boundary

The [Publication Charges page](https://jom.magnetics.or.kr/submission/journal/pages/publication_charges.vm) states in English USD 300 for foreign authors for the first five **published journal pages**, then USD 10 per additional page. Its Korean paragraph instead states KRW 250,000 for five pages, whereas the English domestic-member amount is KRW 300,000. Do not substitute the lower Korean amount or infer a membership discount. The user's nationality and Korean affiliation do not resolve the applicable category in the public text. The [author instructions](https://jom.magnetics.or.kr/submission/journal/pages/instructions_authors.vm) state that color printing incurs additional costs but give no tariff or online-only-color exemption.

An 8–12 published-page editorial target gives USD 330–370 before unresolved costs, leaving USD 170–130 below the USD 500 cap. Review-PDF length is not the billing page count. Membership, color, supplementary files, any other compulsory charge, taxes and payment/remittance costs remain unconfirmed; no waiver or zero charge is assumed. Use grayscale main figures and decline optional paid services. The final invoice must fit the cap before payment.

## Scope and institutional recognition

The [Aims and Scope](https://jom.magnetics.or.kr/submission/journal/pages/aims_scope.vm) covers magnetic measurements/applications and permanent-magnet applications. The [Society's English journal page](https://www.magnetics.or.kr/eng/html/en_journal.vm) lists JOM as English and SCIE/Scopus. This supports the journal choice; it does not certify Changwon National University's specific recognition of a future article. Author must verify the university's current policy for the relevant programme and publication year.

The 8–12 published-page / 5–6 main-figure target is an editorial objective for this package. No corresponding public hard page or figure limit was found. The downloaded template has old internal Word metadata (2013); it is still linked by the current official submission page. Template age does not erase the current public instructions or authorize silently assuming a newer portal rule.

## Native template inspection

The unchanged official DOC was converted for read-only inspection using the bundled headless LibreOffice, with its own temporary profile. The user's desktop LibreOffice was not used. The inspection DOCX and structure extract are temporary QA artifacts in `tmp/jom/template/`, not a replacement official template.

The linked legacy template uses an approximately A4 page, 30 mm left/right and bottom margins and 35 mm top margin. Its English runs use Times New Roman 12 pt, a centered 16 pt bold title and 14 pt bold principal headings; its underlying Normal style contains Malgun Gothic and is overridden for English text. Body, abstract, reference and caption spacing uses 480 twips with automatic line spacing, equivalent to double spacing. Therefore, no observed double-spacing conflict exists between this template and the current author instructions. These font/margin settings are examples in the template; the public instructions do not state a mandatory font family or exact margin dimension.

One legacy sample table caption says `Table 1`, while both the current public instructions and the template's instructional paragraph specify Roman numerals. This package follows the explicit current Roman-number requirement. A sample reference displays journal, bold volume, page and year; the current public page calls its sample preferred and does not mandate exact cloning of the 2013 document's run formatting. The package preserves identified author information, double spacing, separate table/figure sheets, separate captions and numbered references while checking rendered readability.
