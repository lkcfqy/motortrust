# Paper 1 reference and claim-support audit

Checked **2026-10-09 (Asia/Seoul)**. Scope: the existing Paper 1 bibliography, the JOM manuscript/supplement, and a small, targeted recent same-journal check. This is not a systematic review or proof of priority. The archived JEET reference audit is retained unchanged.

**Read this together with the later [paragraph-level support review](Detailed_Review_References.md) and [revision recheck](Detailed_Review_References_Recheck.md).** Metadata resolution does not establish claim support or full-text access. The later review identifies specific overbroad wording, the distinction between current-vector and phase-current harmonic indicators, and the Wilson interval definition; its source-by-source access levels supersede any broader impression from this earlier summary. In particular, Jeong 2017 and Li 2023 were not independently read in full in the later check, and algorithm-origin citations were not all reread in full. Their retained claims are deliberately narrow.

## Metadata verification

Command actually executed using the existing Conda environment:

```sh
/Users/lkc/miniforge3/envs/motortrust/bin/python scripts/audit_reference_metadata.py --as-of 2026-10-09 --json submission/jom/reference_evidence/all_existing_paper1_metadata_checked.json --markdown submission/jom/reference_evidence/all_existing_paper1_metadata_checked.md --workers 2
```

Result: **34/34 existing Paper 1 identifiers resolved; 34/34 passed the script's title, first-author, and available-year checks.** This script does not validate every author's name, pages, scientific quality or every claim. Additional Crossref JSON snapshots retain registered author lists, titles, volumes, issues and pages; Zenodo-native JSON retains dataset creator/date records. `paper1_metadata_audit_2026-10-09.json` records the first metadata retrieval (including temporary 429s); the successful later `all_existing_paper1_metadata_checked.json` is the final identifier audit. Rate-limit failures are not bibliographic defects.

The JOM main draft and supplement were then combined in a temporary audit input, using the shared bibliography plus `jom_references.bib` without changing either source. The actual JOM selection contains **30 unique citations; 30/30 resolved and 30/30 passed** the same metadata checks. This includes the newly added Park/Harmony/Baek JOM paper. The successful final JOM-specific snapshot is `reference_evidence/final_jom_metadata_checked.json` (with a matching Markdown report). The temporary inputs are `tmp/jom/audit_main_and_supp.md` and `tmp/jom/audit_combined.bib`; neither is an upload document.

An extended comparison also checked every available registered author position/count and available volume/issue/page field for the JOM selection against archived Crossref JSON. All author counts agree; the name-parsing differences below were retained with original-display explanations. The IEICE article number `20240550` is represented by Crossref as `20240550–20240550`, an article-number representation rather than conflicting pagination. Missing registry fields were left unavailable rather than declared matches. Results are archived in `reference_evidence/final_jom_extended_metadata_checked.json`.

```sh
/Users/lkc/miniforge3/envs/motortrust/bin/python scripts/audit_reference_metadata.py --manuscript tmp/jom/audit_main_and_supp.md --bibliography tmp/jom/audit_combined.bib --as-of 2026-10-09 --json submission/jom/reference_evidence/final_jom_metadata_checked.json --markdown submission/jom/reference_evidence/final_jom_metadata_checked.md --workers 2
```

Manual metadata findings:

- Yoon/Yu's article is in *Applied Sciences* **14(1), 221 (2024)**, with online publication in December 2023. The 2024 issue-year citation is valid; no correction is warranted.
- Zenodo record 15631383 explicitly gives publication date **2024-02-01**. Its larger numeric record ID is not evidence for changing the citation to 2025. Record 13889418 gives **2024-10-04**. Mendeley version 5 gives **2022-11-17**. Preserve these dataset dates.
- Wang et al. has a real proceedings-pagination difference: the DOI/Crossref IEEE record gives **11285–11294**, whereas the [official CVF accepted-paper page](https://openaccess.thecvf.com/content_CVPR_2019/html/Wang_Characterizing_and_Avoiding_Negative_Transfer_CVPR_2019_paper.html) and its original PDF give **11293–11302**. The existing shared BibTeX entry follows the final IEEE DOI registry and is unchanged. The final JOM display omits this conference paper's page range while retaining authors, title, conference, year and DOI, so it does not silently select a conflicting version. This package discloses the discrepancy; it is not evidence of a calculation error. If citing the CVF accepted version explicitly in future, use its pages and identify that version.
- The Park/Harmony/Baek JOM original PDF displays **Peter Nkwocha Harmony**; its Crossref entry parses this person differently (`given: Peter Harmony`, `family: Nkwocha`). The JOM-specific entry follows the original author's displayed name and produces `P. N. Harmony`; author-list parsing in the registry is not silently treated as ground truth.
- Particles/hyphens in author surnames (e.g. Van Driessen, von Mohrenschildt and Yong-Hwa Park) follow article display/bibliography conventions; capitalization differences in the registry are not scientific discrepancies.

No existing shared bibliography entry or frozen result was rewritten automatically. The JOM-specific addition is `jom_references.bib`. The extra JOM paper's author/title/volume/issue/pages/DOI were checked against the official original PDF and Crossref. The main Word bibliography is generated from the actual citation order, not copied from an old numbered list.

## Claim-to-source map for retained claims

The current JOM draft uses the following sources for narrow background, mathematical or data-description claims. Experimental numbers and failure boundaries come from this project's frozen outputs, not from these references. Publisher abstracts, original full texts or original author/institution records were used where accessible; the pre-existing `docs/literature_gap.md` remains the fuller Paper 1 audit. Some IEEE full-text pages returned an anti-bot/access page in this check; no paywall was bypassed and no unread detailed numerical claim was introduced.

| Citation key(s) | Claim supported in current draft | Primary basis and boundary |
|---|---|---|
| `zafarani2018itscreview` | PMSM ITSC signatures depend on operating condition, short-circuit path and controller action. | [Original authors' institutional record](https://open.metu.edu.tr/handle/11511/41067) describes the paper's own FEM, drive-model and testbench analysis; original article DOI 10.1109/JESTPE.2018.2811538. The review portion maps the field; its original analysis supports contextual dependence. No universal harmonic increase is asserted. |
| `jeong2017negativesequence` | Early ITSC diagnosis uses negative-sequence components. | Original article title and DOI-registered IEEE record, 10.1109/TIE.2017.2677355; its original abstract/author-uploaded paper describes a speed-robust indicator. Used only for signal rationale, not a borrowed detection rate or transfer guarantee. |
| `li2024negativesequence` | Negative-sequence current-vector harmonics indicate winding asymmetry; the indicator response is condition sensitive. | [Official IEICE original PDF](https://globals.ieice.org/en_publications/elex/10.1587/elex.21.20240550/_pdf), §§2–5: models, second harmonic and prototype test; §3 explicitly discusses speed/load influence on NSC amplitude. Does not establish health-only transfer. |
| `urresty2013nonstationary` | PMSM order tracking follows fault-related harmonics under changing speed and loads. | Original article/author-uploaded paper, DOI 10.1109/TPEL.2012.2198077, reports current third-harmonic and zero-sequence-voltage order tracking across speed/load. Current draft does not claim those indicators were implemented here. |
| `li2024physicaldatapmsm` | Physical-data models address sparse PMSM diagnosis at rapidly varying speed. | [Original publisher article](https://www.sciencedirect.com/science/article/abs/pii/S0952197624000964) describes high-temperature, varying-speed oil-drilling diagnosis and a speed-sensitive extraction scheme. This supervised method does not validate Paper 1's false-alarm gate. |
| `wang2019negativetransfer` | Transfer can worsen the target-only reference. | [Official CVF original paper](https://openaccess.thecvf.com/content_CVPR_2019/papers/Wang_Characterizing_and_Avoiding_Negative_Transfer_CVPR_2019_paper.pdf), §3 formally compares against target-only learning. General transfer principle; no motor empirical evidence is attributed to it. The later check read the corresponding original-author arXiv v4 full text and verified the same-algorithm comparison in §3, equations (3)–(4). |
| `kumar2024negativetransfer` | Machinery research already treats negative-transfer mitigation. | [Original authors' institutional article record](https://scholar.nycu.edu.tw/en/publications/mitigating-negative-transfer-learning-in-source-free-unsupervised/) and original IEEE DOI 10.1109/TIM.2024.3476610. Source-free UDA with pseudo-labels is distinct from healthy-only frozen calibration. No cited accuracy gain appears in the current draft. |
| `li2020domaingeneralization` | Rotating-machinery domain generalization predates this study. | Original article DOI 10.1016/j.neucom.2020.05.014 and registered title; `docs/literature_gap.md` reports its original domain-augmentation/adversarial/metric-learning study. Current claim is existence, not comparative superiority. |
| `li2023causalconsistency` | Collaborative multimachine bearing generalization is established. | Original IEEE article DOI 10.1109/TII.2022.3174711, registered title/metadata and inherited primary audit. Its supervised fault knowledge is distinct from the present alarm protocol. The current main draft does not depend on reproducing the exact six-machine/43-bearing counts. |
| `zhao2024dgbenchmark` | Multi-dataset fault-diagnosis benchmarks already exist. | [Original publisher article](https://www.sciencedirect.com/science/article/abs/pii/S0951832024000395) describes its own eight-public/two-self-collected benchmark. The empirical component is primary; its survey component is used only as context. |
| `liu2025frequencyguided` | Source-domain emphasis and negative transfer are recognized by machinery DG work. | [Original publisher article](https://www.sciencedirect.com/science/article/pii/S0263224125003483) explicitly motivates frequency-guided generation by source-heavy regularizers. No SOTA result is borrowed into Paper 1. |
| `wheat2024dataleakage` | Signal/acquisition/physical-part holdouts can yield different diagnosis performance. | Original IEEE Access article DOI 10.1109/ACCESS.2024.3497716 and [authors' McMaster repository](https://macsphere.mcmaster.ca/handle/11375/31458); inherited primary audit checks run/day/part comparisons. Current main text deliberately omits the exact >40% number because no exact percentage-point interpretation is needed. |
| `roberts2017structuredcv` | Dependence requires structured validation. | [Original Ecography article](https://nsojournals.onlinelibrary.wiley.com/doi/abs/10.1111/ecog.02881), 40, 913–929. Used as general methodological reasoning, not motor-performance evidence. |
| `hurlbert1984pseudoreplication` | Derived samples do not create independent experimental units. | Original *Ecological Monographs* article DOI 10.2307/1942661. General experimental-unit principle; motor-specific unit counts are audited from project data. |
| `scholkopf2001support` | OC-SVM is an established unlabeled support-estimation method. | [Original MIT Press article](https://direct.mit.edu/neco/article/13/7/1443/6529/Estimating-the-Support-of-a-High-Dimensional), 13, 1443–1471. No alarm-risk transfer guarantee is inferred. |
| `liu2008isolationforest` | Isolation Forest is an established anomaly detector. | [Original IEEE conference article](https://ieeexplore.ieee.org/abstract/document/4781136/metrics), DOI 10.1109/ICDM.2008.17. Algorithm origin, not evidence of PMSM performance. |
| `rousseeuw1999mcd` | MCD is established robust location/scatter estimation. | [Original Technometrics article](https://www.tandfonline.com/doi/abs/10.1080/00401706.1999.10485670), 41, 212–223. MinCovDet is an existing comparator, not a new main method or a Gaussian guarantee. |
| `arsigny2006logeuclidean` | Matrix-logarithm averaging supplies Log-Euclidean SPD geometry. | [Original Wiley article](https://onlinelibrary.wiley.com/doi/pdf/10.1002/mrm.20965) and [authors' INRIA original preprint](https://www-sop.inria.fr/asclepios/Publications/Arsigny/arsigny_mrm_2006.pdf). Geometry origin; DTI results do not imply fault-detection reliability. |
| `angelopoulos2023conformal` | Conventional finite-sample conformal calibration relies on exchangeability. | [Publisher's original tutorial](https://www.nowpublishers.com/article/Details/MAL-101), 16, 494–591. Tutorial explains theory, not a new PMSM result. |
| `chernozhukov2018dependentconformal` | Dependence needs modified procedures/assumptions. | [Original PMLR paper](https://proceedings.mlr.press/v75/chernozhukov18a.html): block permutation and approximate validity under conditions. The present simple rank calibration does not inherit that theorem automatically. |
| `barber2026timeseriesconformal` | Time-series conformal behavior depends on temporal assumptions. | [Original 2026 PMLR paper](https://proceedings.mlr.press/v313/barber26a.html): coverage loss bounds under stationary beta-mixing assumptions. This study did not verify those conditions. |
| `farouq2021mondrianfleet`, `farouq2022conformalfleet` | Conformal fleet anomaly alarms predate this study. | [Original 2021 publisher paper](https://www.sciencedirect.com/science/article/abs/pii/S0925231221012005), [original 2022 publisher paper](https://www.sciencedirect.com/science/article/abs/pii/S095741742200313X). District-heating/heterogeneous-fleet work is a precedent, not validation of motor alarms. |
| `diallo2025falsealarms` | Limited training data can prevent nominal false-alarm control. | [Original publisher article](https://www.sciencedirect.com/science/article/abs/pii/S0959152425001234) directly describes its TEP experiments and marginal/conditional threshold comparison. No general guarantee from its adjusted procedures is transferred to this study. |
| `jung2023pmsmfaultdata`, `jung2022pmsmfaultdataset` | KAIST data provenance, motor ratings, fixed-condition acquisition and current sampling. | [Original dataset article](https://pmc.ncbi.nlm.nih.gov/articles/PMC9957734/), [original version-5 deposit](https://data.mendeley.com/datasets/rgn5brrgrn/5). Duplicate aliases and exact usable file/block counts are project audits, not claims that these papers certify the pipeline. |
| `kozovsky2024dualthreephasepmsm`, `kozovsky2022dualthreephasemodel` | External dual-three-phase motor data and machine design provenance. | [Original Zenodo deposit](https://zenodo.org/records/13889418), original associated IEEE modelling article DOI 10.1109/IECON49645.2022.9968364. Design parameters are not claimed measured load/speed summaries of every analysis block. |
| `zezula2024transientpmsm` | Secondary-transient dataset provenance. | [Original Zenodo deposit](https://zenodo.org/records/15631383) and native metadata JSON; 200 W/20 kW file identities and parser acceptance/failure are project audits. No online capability is inherited from the source title. |
| `park2025electromagnetic` | Same-journal electromagnetic signal monitoring and the dependence of diagnostic usefulness on signal/machine context. | [Official JOM original PDF](https://www.magnetics.or.kr/upload/jom/upfile_260106095352151.pdf). Restrictions are detailed below. |

## Recent JOM relevance check

1. **Park, Junki; Peter Nkwocha Harmony; Jeihoon Baek (2025).** *Electromagnetic Signal Analysis for Electrical and Mechanical Fault Diagnosis in Synchronous Motor*. *Journal of Magnetics* **30(4), 596–605**. DOI [10.4283/JMAG.2025.30.4.596](https://doi.org/10.4283/JMAG.2025.30.4.596). The official original ten-page PDF was read and archived locally in `reference_evidence/park2025_official_fulltext.pdf`. Its analysis is FEM simulation of a 6400 kVA synchronous motor with rotor winding/damper-bar faults, not a PMSM cross-dataset field validation. Section 4.3 reports reduced stator-current amplitude and no significant current-harmonic change for its stator turn-to-turn case, then uses stray flux. It supports electromagnetic-monitoring relevance and signal/machine dependence. It does **not** show frozen cross-machine alarm reliability, independently replicated motors, population false-alarm control or this manuscript's real-time readiness. Do not repeat its broad real-time assertions as evidence for Paper 1.
2. **Miao, Luting; Meimei Xu; Qian Zhang (2024).** *Modular Winding Arrangement Design to Suppress Short-Circuit Current and Magnetic Coupling in PM Machines for Flywheel Battery*. *Journal of Magnetics* **29(4), 397–404**. DOI [10.4283/JMAG.2024.29.4.397](https://doi.org/10.4283/JMAG.2024.29.4.397). [Official original PDF](https://www.magnetics.or.kr/upload/jom/upfile_250106093526242.pdf) checked and archived. This is a relevant PM-machine fault-current/magnetic-coupling engineering context, but it studies winding design rather than cross-dataset alarms. It is recorded as recent same-journal context and is not added merely to increase same-journal citations.

No located JOM paper establishes the present protocol's safety or removes its single-external-motor limit. The review does not assert that no other relevant paper exists.

## Final citation QA boundary

Retained background citations match their actual subject and are used with the limitations above. The JOM draft removes unneeded exact literature-performance figures, confines reviews/tutorials to context/theory, and makes the project's empirical failure the central result. Do not reuse a generic citation to imply proof of causation, a safe fleet-level alarm probability, embedded deployment, or a universal algorithm ranking. After any final author edits, check that citations remain attached to those same narrow claims and that no uncited bibliography key remains.

## Consistent journal abbreviations for the JOM bibliography

The current [official author instructions](https://jom.magnetics.or.kr/submission/journal/pages/instructions_authors.vm) give an abbreviated-journal example and a consecutive numbered list. They do not publish a journal-by-journal abbreviation dictionary or prohibit article titles/DOIs. The following are editorial normalization suggestions, not an additional official JOM rule. Conference-proceedings and data-repository names should remain identifiable rather than being forced into journal abbreviations. Retaining full article titles and DOI/URL identifiers assists this submission's evidence traceability.

| Source journal | Suggested consistent display |
|---|---|
| Journal of Magnetics | J. Magn. |
| IEEE Journal of Emerging and Selected Topics in Power Electronics | IEEE J. Emerg. Sel. Topics Power Electron. |
| IEEE Transactions on Industrial Electronics | IEEE Trans. Ind. Electron. |
| IEEE Transactions on Industrial Informatics | IEEE Trans. Ind. Inform. |
| IEEE Transactions on Instrumentation and Measurement | IEEE Trans. Instrum. Meas. |
| IEEE Transactions on Power Electronics | IEEE Trans. Power Electron. |
| IEEE Access | IEEE Access |
| IEICE Electronics Express | IEICE Electron. Express |
| Engineering Applications of Artificial Intelligence | Eng. Appl. Artif. Intell. |
| Reliability Engineering & System Safety | Reliab. Eng. Syst. Saf. |
| Expert Systems with Applications | Expert Syst. Appl. |
| Journal of Process Control | J. Process Control |
| Foundations and Trends in Machine Learning | Found. Trends Mach. Learn. |
| Neural Computation | Neural Comput. |
| Magnetic Resonance in Medicine | Magn. Reson. Med. |
| Ecological Monographs | Ecol. Monogr. |
| Data in Brief | Data Brief |
| Neurocomputing | Neurocomputing |
| Measurement | Measurement |
| Ecography | Ecography |
| Technometrics | Technometrics |

Only display formatting is affected. Preserve author names, year, identifiers and documented version-specific pages. Do not automatically replace the shared bibliography with abbreviations or infer metadata corrections from stylistic variation.

Final JOM display choice: the Wang 2019 conference reference omits the disputed proceedings pagination and retains the verified title, proceedings, year and DOI. The shared historical bibliography remains unchanged.
