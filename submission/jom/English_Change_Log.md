> Updated 2026-10-09: detailed substantive review and response are in `Detailed_Review_CN.md`; final QA supersedes pre-review page counts and author-field status below.

# JOM English revision and scientific boundary log

Prepared: 2026-10-09 (Asia/Seoul)

This log covers `submission/jom/manuscript.md` and `submission/jom/supplementary.md`.
It does not modify `paper/manuscript.md`, `paper/outline.md`, the original protocols,
reveal logs, frozen scores, or the JEET package. Its checks are source-text checks;
the separate final QA report records rendering and package verification.

## Manuscript focus and editorial changes

- The title is **Frozen Cross-Dataset Reliability of Healthy-Only PMSM Stator-Fault
  Detection**. It names the reliability question without claiming general deployment
  success or a new superior algorithm.
- The English main draft contains approximately 5,151 whitespace-delimited words,
  including tables, captions, placeholders, and front matter. The abstract contains
  124 words and six keywords, satisfying the checked 100--150-word/3--6-keyword
  JOM rules. Counts can change slightly when author information is inserted.
- The narrative follows one question: whether healthy-only source assistance retains
  alarm reliability across a frozen dataset transfer. Physical current asymmetry,
  harmonics, operating conditions, and healthy-reference geometry introduce the
  question before machine-learning comparisons.
- Six core figures are retained: protocol, KAIST covariance comparison, complete
  external comparison, ordered drift, turn--phase/load grid, and frozen feature
  geometry. Five exploratory sensitivity/comparison figures move to the supplement.
  Tables are numbered I--III, with captions prepared for separate table sheets.
- Repeated contribution lists, detailed audit chronology, full paired comparison
  families, adaptation/block sensitivities, seed ranges, and transient hash tables
  are moved to or retained in the supplement. The main text still reports all central
  failures and the decisive limitations.
- The main draft has five separately displayed equations for robust alignment, relative
  ridge, Log-Euclidean covariance, anomaly score, and rank p-value. Actual numbering
  and Word equation presentation are the document builder's responsibility.

## Preserved numerical and methodological identity

The abstract, results, and conclusion retain the exploratory 95.71% KAIST result
and the frozen external 25.00% result. Main and supplementary reporting preserve:

| Evidence anchor | Reporting |
|---|---|
| KAIST primary | 1608/1680 fault blocks; 95.71%; 0/42 health alarms |
| External primary | 96/384; 25.00%; 1/32 health alarms; AUROC 0.6354 |
| Failed health gate | Wilson upper 15.74% > preset 12%; maximum-load FAR 12.5% |
| Target-only MinCovDet | 269/384; 70.05%; 0/32; AUROC 0.9268 |
| Comparator uncertainty | Five seeds: 65.36--77.08%; 0--2/32 health alarms; H1 passes 3/5 |
| Paired target-MinCovDet advantage | 45.05 percentage points [40.62, 49.48] |
| Same-estimator source contrast | Target-only minus source+target MinCovDet 39.84 points [35.42, 44.27] |
| Frozen secondary parser | 0/21 accepted; no primary detector score |

No feature, time interval, model, healthy fit, threshold, exclusion, seed, metric,
or primary designation changes in this revision. Log-Euclidean remains primary.
Target MinCovDet remains a preimplemented comparator. The five-seed audit and
paired external diagnostics are explicitly post-reveal. The independent evidence
audit verifies calculations from lower-grain records separately.

## Clarifications and repaired presentation errors

1. The internal Git freeze is explicitly distinguished from externally registered
   preregistration. Historical protocol titles and original hypotheses remain intact.
2. One external physical motor is stated throughout. Its 48 records, windows, blocks,
   and two current subsystems are not independent motor replications.
3. Turn count is inseparable from fault phase: U for turns 1/3/5/6, V for 2/4.
   Pooled AUROC contrasts eight fault loads with four held-out health loads.
4. First-alarm position in the external sweep measures early-trajectory coverage,
   not fault-onset latency: faults already exist in the analyzed acceleration records.
   Healthy-record speed is identified as a proxy where applicable.
5. The named scale-free arm retains `fundamental_hz`. The text therefore states that
   it is not wholly dimensionless or guaranteed speed invariant. This is a reporting
   clarification, not post-reveal feature removal.
6. Contribution percentages are defined under a symmetric cross-term decomposition.
   They are non-unique descriptive allocations, not causal importance weights.
7. The original supplementary sentence could be read as saying each held-out 200 W
   record had 176 prefault test windows. The new supplement clarifies that **176 is
   the pooled total across twelve records**, with 60 pooled first-second fault
   windows and 120 pooled 2 s windows. This repairs prose only; frozen outputs and
   calculations are unchanged.
8. The secondary frozen parser's 0/21 failure remains visible in the main manuscript.
   Its repaired 200 W analysis is post-reveal, single-motor, and non-confirmatory;
   the repaired 20 kW 4/9 incompatibility is not selectively rescued.
9. Real-time, embedded, severity, causal, population-risk, and unrestricted
   generalization claims are withheld because the available evidence does not
   establish them. Later-paper detector improvements do not replace Paper 1 evidence.

## Supplement structure

- S0 supplies a provenance/status matrix and maps each retained diagnostic to a
  specific review question, data-use boundary, and interpretation rule. These are
  current reporting rationales rather than retroactive pre-reveal hypotheses.
- S1--S9 preserve the saved generated external comparison, paired contrasts, horizon
  analysis, seed audit, feature geometry, sampling-rate control, hash registry,
  and transient compatibility/sensitivity evidence.
- S10 holds exploratory KAIST covariance and one-class comparisons, adaptation
  budget, block-rule sensitivity, and failed hypotheses, with Figures S1--S5.
- S11 states the reproducibility and publication boundary. No public release,
  author approval, funding, competing-interest fact, or copyright signature is
  invented.

## JOM-specific literature and author information

The publication artwork is prepared in grayscale to avoid assuming that color fees
are covered; original vector figure sources are retained separately. Figure captions
identify methods through labels and hatching rather than color names.

The recent same-journal paper by Park, Harmony, and Baek, DOI
10.4283/JMAG.2025.30.4.596, is cited for its finite-element current/stray-flux
synchronous-motor diagnostic context. It is not cited as PMSM cross-machine transfer
evidence or as proof of a universal harmonic increase. Its metadata are in the
separate JOM bibliography checked against the original article.

The author line, official affiliation, address, email, ORCID, telephone/fax,
funding, contributions, competing interests, institutional requirements, approval,
and hosting route remain explicit author-input fields. A nonanonymous JOM draft
is prepared; the old JEET anonymous/title-page structure is not carried forward.

The AI-assistance statement accurately identifies coding, consistency, document,
and English drafting support and requires human review. It does not claim that
author approval has already occurred.

## Completed text checks and remaining document checks

Completed text checks: all 30 main cited keys exist in the combined bibliography;
all six main figure paths exist; five display equations are separated; the abstract
is 133 whitespace-counted words after detailed review; main and supplementary lower-grain denominators are described with
their correct units; no new analysis is required by this revision.

## Final source refinements after independent audit

The main freeze description now names dependency specifications and recorded tool
versions, rather than asserting a complete historical environment lock. Original
metadata records scikit-learn 1.9.0 while the current saved-result audit uses 1.9.1.
The supplement explains why verifying immutable saved evidence is distinct from
claiming an identical historical stochastic runtime. The discussion uses “frozen
external result” instead of “confirmation result.”

Seven supplementary tables with eight to eleven columns were mechanically split
into two column groups, each with at most six columns and a shared first column.
These are Sections S2, S3.1, S3.2, S4.3, S5, S6, and S7. Continuation captions
and reading instructions identify matching rows. A cell-by-cell reconstruction
assertion verified that every original heading, row, value, and order was preserved;
this is a layout change and does not alter computations or frozen evidence.

Remaining checks belong to package QA: numbered/abbreviated reference rendering,
Word pagination, separate table/caption sheets, PDF page inspection, placeholder
inventory, code-bundle validation, and author completion. This preparation draft
must not be described as directly uploadable while those author fields remain.
