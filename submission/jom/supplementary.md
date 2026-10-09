---
title: Supplementary Material for Frozen Cross-Dataset Reliability of Healthy-Only PMSM Stator-Fault Detection
bibliography: ../../references/key_papers.bib
link-citations: true
---

**Author:** LI KAICHEN, Department of Artificial Intelligence Convergence Engineering, Changwon National University

## S0. Status, analysis purposes, and provenance

This supplement separates the original pre-reveal decisions from later diagnostics.
The historical Chinese protocols retain their original titles and hypotheses; the
English reporting does not reinterpret their internal Git freeze as an external
preregistration. The frozen primary Log-Euclidean score, external interval, health
roles, thresholds, record inclusion, and primary seed are unchanged.

| Evidence component | Status | Permitted inference |
|---|---|---|
| KAIST three-motor comparison and sensitivities | Exploratory; target faults inspected during development | Conditional same-family comparison; no untouched confirmation |
| External primary scoring and ten preimplemented comparators | Frozen before external fault-value access | Complete pre-reveal comparison on one external motor |
| External paired contrasts, horizon cuts, block-position AUROC, and first alarms | Post-reveal diagnostics of saved scores | Conditional explanation of ranking and trajectory coverage |
| Five-seed stochastic refits | Post-reveal audit using previously fixed seeds and healthy-only fits | Stability range; no best-seed selection or revised primary |
| Feature geometry reconstruction | Post-reveal, analysis-only | Exact reconstruction and descriptive contribution allocation |
| KAIST 100-to-10 kHz sampling control | Post-reveal sensitivity | Result under one changed source sampling arm; no primary replacement |
| Secondary transient parser | Prospectively frozen compatibility audit; accepted 0/21 | Parser failure; no detector comparison at primary reveal |
| Repaired 200 W transient analysis | Post-reveal, one physical motor, non-confirmatory | Descriptive cross-record sensitivity only |

The secondary transient dataset has no independent healthy-only records. Its frozen
parser failure and repaired single-motor analysis supply no usable confirmatory
cross-motor replication. The two subsystems of the primary external motor are also
not independent motors. All results are offline; latency, memory, and embedded stability were
not measured. No analysis here establishes a safety guarantee.

The current submission-package audit verifies saved numerical outputs in the
specified Conda environment, which contains scikit-learn 1.9.1. The original
external output metadata records scikit-learn 1.9.0; a complete historical
environment lock was not located. Dependency specifications and recorded tool
versions support provenance, but do not establish a byte-identical historical
runtime. Saved-result evidence verification is therefore distinguished from any
current-environment stochastic refit. The original scores and primary seed remain
unchanged; the reproducibility guide records this version boundary.

The following purposes explain why the already completed post-reveal diagnostics
are retained. They are reporting rationales, not newly claimed pre-reveal hypotheses.
No additional diagnostic in this reporting revision uses external labels to alter fitting,
features, inclusion, time support, seed choice, or alarm thresholds.

| Diagnostic purpose | Diagnostic and data boundary | Interpretation rule |
|---|---|---|
| Does 100% record-any detection hide late alarms? | Fixed-prefix counts and first alarms from saved external prediction rows | Report all prefix denominators and preserve full-interval primary; early trajectory is not fault-onset latency |
| Does source health help relative to target health? | Estimator-family paired record differences using saved outputs; fit-derived masks disclosed | Attribute the observed contrast to this source-augmentation protocol; covariance-estimator contrasts are qualified |
| Is the best comparator's seed stable? | Five fixed healthy-only stochastic fits, same calibration rule, all seed results | Report range and gate pass count; never select a seed after fault inspection |
| Is operating position associated with score? | Saved block scores with healthy speed proxies; no score refit | Association only; block/time/speed and unmeasured factors co-vary |
| Does the frozen geometry emphasize useful fault directions? | Hash-locked covariance reconstruction plus common-support pooled feature summaries and matched differences | Contribution decomposition is descriptive and non-unique, not a causal feature-selection rule |
| Can sampling mismatch alone rescue transfer? | Antialiased 10 kHz source arm with otherwise unchanged settings | Preserve original result; a null rescue narrows one explanation under this pipeline |
| Can a repaired transient parser count as confirmation? | Separate opt-in repair directory; unchanged signal/onset contract | Retain primary 0/21 failure and motor-level incompatibility; label repaired analysis post-reveal |

Original sources are Mendeley Data 10.17632/rgn5brrgrn.5, Zenodo
10.5281/zenodo.13889418, and Zenodo 10.5281/zenodo.15631383; all carry CC BY 4.0
[@jung2022pmsmfaultdataset; @kozovsky2024dualthreephasepmsm;
@zezula2024transientpmsm]. The associated external machine description is
[@kozovsky2022dualthreephasemodel]. Raw data are obtained from those repositories;
this supplement and the code bundle provide derived outputs and reconstruction
instructions rather than redistributing raw archives.

## Technical summary

The complete frozen external comparison favors Target MinCovDet, not Proposed:
Target MinCovDet detected 70.05% of 384 fault blocks with 0/32 held-out healthy false
alarms, whereas Proposed detected 25.00% with 1/32 false alarms. Conditional
complete-record comparisons show reduced detection under the frozen source-augmentation
pipelines, including MinCovDet configurations with different fit-derived masks, except that target-only and source+target OC-SVM tied in mean
detection. The apparent performance increase late in each record is coupled to the
shared acceleration ramp. Five-seed, feature-geometry, and 100 kHz-to-10 kHz
sensitivity analyses did not change the frozen primary result. All external
intervals and post-reveal comparisons remain conditional on a single physical motor.
The secondary 21-record transient audit did not supply confirmatory evidence: the
frozen parser accepted 0/21 records, the repaired 20 kW arm failed its compatibility
gate, and all methods had zero first-second detection in the repaired 200 W sensitivity.

## S1. Data, experimental units, and locked splits

The **physical motor** is the generalization unit, the **MAT/TDMS record** is the
condition-level resampling unit, the 3 s **block** is the alarm unit, and the 0.2 s
window is the feature-extraction unit. Repeated windows and ordered blocks from one
record are not independent replications. The external dataset contains only one
physical motor; its 48 fault records are operating-condition records, not 48 motors.

| Dataset | Physical motors | Physical records | Record-subsystem streams | Sampling | Frozen analysis grain |
| --- | --- | --- | --- | --- | --- |
| KAIST source | 3 (1, 1.5, and 3 kW) | 45 (3 healthy; 42 fault) | not applicable | 100 kHz; leading 120 s | 600 non-overlapping 0.2 s windows and 40 3 s blocks per record |
| External dual-three-phase PMSM | 1 (custom 30.16 kW) | 56 (8 healthy; 48 fault) | 112 (2 subsystems per record) | 10 kHz; [12, 36) s | 120 windows and 8 blocks per record-subsystem; one system block after maxima |

The external MAT records contain two three-phase current subsystems (`SubSys1` and
`SubSys2`). Each subsystem is scored separately. A block score is the maximum over
15 windows within a subsystem followed by the maximum over the two subsystems. Thus,
each physical record contributes exactly eight system block scores.

### S1.1. Ordered split definitions

| Stage | KAIST leave-one-motor-out | External validation |
| --- | --- | --- |
| Source reference | healthy blocks 0–23 for each of the two source motors; balanced subset 0, 8, 15, 23 | three KAIST source motors; covariance blocks 0–23 and balanced blocks 0, 8, 15, 23 |
| Target adaptation | blocks 0–3 (4 blocks; 60 windows) from the held-out motor's healthy record | 0 N·m healthy record, blocks 0–3 (60 windows per subsystem) |
| Guard / unused | blocks 4 and 25 | 0 N·m blocks 4–7 are unused for validation |
| Calibration | healthy blocks 5–24 (20 blocks) | healthy loads 10, 20, and 30 N·m; all 8 blocks (3 records; 24 system blocks) |
| Held-out health test | healthy blocks 26–39 (14 blocks) | healthy loads 5, 15, 25, and 35 N·m; all 8 blocks (4 records; 32 system blocks) |
| Fault test | 14 records × 40 blocks = 560 blocks per target motor | 6 turn-fault states × 8 loads = 48 records; 8 blocks each = 384 system blocks |

The external 6-by-8 grid is not crossed by fault phase. Fault-turn levels 1, 3, 5,
and 6 use phase U, whereas levels 2 and 4 use phase V. Consequently, fault-turn count
and phase effects are not separately identifiable; the turn-stratified record bootstrap
conditions on this fixed assignment rather than resolving it.

All primary two-dataset models use the named 27-feature scale-free arm. Electrical fundamental frequency remains in this arm, so it is neither wholly dimensionless nor guaranteed speed invariant. The unchanged feature order is: `fundamental_hz`, `sequence_unbalance`, `fundamental_amplitude_cv`, `phase_rms_cv`, `clarke_radius_cv`, `zero_sequence_ratio`, `spectral_entropy`, `sideband_lower_ratio`, `sideband_upper_ratio`, `harmonic_2_ratio_mean`, `harmonic_2_ratio_max`, `harmonic_3_ratio_mean`, `harmonic_3_ratio_max`, `harmonic_4_ratio_mean`, `harmonic_4_ratio_max`, `harmonic_5_ratio_mean`, `harmonic_5_ratio_max`, `thd_2_to_5_mean`, `rms_ratio_a`, `crest_a`, `kurtosis_a`, `rms_ratio_b`, `crest_b`, `kurtosis_b`, `rms_ratio_c`, `crest_c`, `kurtosis_c`. Source features are
robustly centered and scaled within source motor; external target features are
robustly centered and scaled within subsystem from the frozen adaptation subset.
The split-conformal alarm level is `alpha = 0.05`. Arithmetic covariance methods use
ridge fraction 0.001 and the Proposed Log-Euclidean method uses the source-selected
ridge fraction 0.01. No external fault row enters fitting, scaling, calibration, or
threshold construction.


### S1.2. Frozen feature and fitting definitions

Each phase is demeaned and Hann-windowed before a real FFT, with amplitude
normalization 2/sum(Hann) and no zero padding. The 0.2 s windows give 5 Hz bins.
`fundamental_hz` is the bin maximizing three-phase mean spectral magnitude in
20–500 Hz, not a directly measured speed. Harmonic orders 2–5 use the nearest bin
to each multiple of that frequency, divided by the same-phase fundamental magnitude
plus machine epsilon; each order reports the phase mean and maximum. THD is the
phase mean of the root sum of squared order-2–5 ratios. The lower/upper sideband
ratios use nearest bins at 0.75/1.25 times the fundamental, normalized by mean
fundamental magnitude. These are fixed spectral heuristics, not order tracking.

At the fundamental bin, `sequence_unbalance` is min(|I1|, |I2|)/max(|I1|, |I2|)
for the two rotating sequence components (zero if both vanish), making it invariant
to phase-sequence orientation; it is not always a fixed negative/positive ratio.
The amplitude-invariant Clarke transform supplies radius coefficient of variation
(CV) and zero-sequence RMS divided by mean phase RMS. Per-phase RMS ratios use the
three-phase mean RMS; crest factors use absolute peak/RMS; kurtosis is Pearson
kurtosis (`fisher=False`, default biased estimator). CVs use population standard
deviation divided by the corresponding mean plus machine epsilon. Spectral entropy
uses phase-averaged power from 20–2000 Hz, probability normalization and division by
the log bin count.

Healthy normalization uses the coordinate median and 1.4826 times median absolute
deviation. A scale no greater than 1e-8 times max(|median|, 1) falls back to population
standard deviation, then to 1.0 if still too small. Only permitted healthy fitting
rows enter these statistics. Source-label ridge development maximized mean source
fault-block detection minus twice mean source healthy false-alarm rate over
0.0001/0.001/0.01/0.1, excluding each outer KAIST target; all selected 0.01.
The selection table and JSON are retained in `results/log_ridge_selection/`.

MinCovDet centers healthy fitting rows for pivoted QR and retains the estimated
independent columns, with rank tolerance sqrt(machine epsilon) times the first
absolute diagonal of R. Both external target-only fits retain 26/27 columns,
excluding `rms_ratio_c` (60 rows); both source-plus-target fits retain 27/27
(240 rows). The full augmentation pipeline changes both sample count and effective
mask. At alpha 0.05 with 20 or 24 calibration blocks, alarm requires a score strictly
above the calibration maximum; ties are not alarmed. H1 uses the upper endpoint of
the descriptive two-sided 95% Wilson score interval, not a one-sided 95% limit.

## S2. Complete frozen external comparison across 11 methods

At the prespecified external seed, Target MinCovDet had the highest detection: 70.05% fault-block detection,
zero false alarms among 32 held-out healthy blocks, and AUROC 0.9268. It was also the
only method satisfying the prespecified empirical H1 rule. Proposed achieved 25.00%
detection, one false alarm (3.12%), and AUROC 0.6354. These external results are
reported in full below; method-specific score thresholds are not comparable in
magnitude across estimators.

The external pooled AUROC compares 384 fault blocks spanning all eight loads with 32
held-out health blocks from only 5, 15, 25, and 35 N·m. It is therefore a descriptive
ranking statistic under unequal load support, not a load-matched population estimand.
Fault prevalence is 384/416 (92.31%), the no-skill average-precision baseline.
AUPRC is prevalence dependent and does not estimate deployed alarm precision.
Training/reference labels describe covariance shape or one-class fitting; all
methods still use target-health normalization and calibration.

The following two column groups share the first-column identifiers and preserve every original row, value, and row order. Read corresponding rows together; splitting is a layout change only.

Table S2a. Complete frozen external comparison across 11 methods (column group 1 of 2).

| Method | Healthy training/reference | Threshold | Health FA | H1 | Fault block detection |
| --- | --- | --- | --- | --- | --- |
| Target Ledoit–Wolf | target adaptation | 183.887 | 1/32 (3.12%) | fail | 141/384 (36.72%) |
| Target sample covariance | target adaptation | 738.703 | 1/32 (3.12%) | fail | 215/384 (55.99%) |
| Source covariance | source healthy | 109212 | 1/32 (3.12%) | fail | 49/384 (12.76%) |
| Entity-balanced covariance | source entities + target | 1250.37 | 1/32 (3.12%) | fail | 105/384 (27.34%) |
| Proposed: Log-Euclidean entity covariance | source entities + target | 4983.29 | 1/32 (3.12%) | fail | 96/384 (25.00%) |
| Target OC-SVM (RBF) | target adaptation | 0.401736 | 1/32 (3.12%) | fail | 49/384 (12.76%) |
| Source+target OC-SVM (RBF) | source-balanced + target | 0.827663 | 1/32 (3.12%) | fail | 49/384 (12.76%) |
| Target Isolation Forest | target adaptation | 0.569218 | 3/32 (9.38%) | fail | 230/384 (59.90%) |
| Source+target Isolation Forest | source-balanced + target | 0.581677 | 2/32 (6.25%) | fail | 194/384 (50.52%) |
| Target MinCovDet | target adaptation | 1238.1 | 0/32 (0.00%) | pass | 269/384 (70.05%) |
| Source+target MinCovDet | source-balanced + target | 9802.52 | 1/32 (3.12%) | fail | 116/384 (30.21%) |

Table S2b. Complete frozen external comparison across 11 methods (column group 2 of 2; continued).

| Method | Record-macro detection | Descriptive bootstrap interval (%) | Record any-alarm | AUROC | AUPRC |
| --- | --- | --- | --- | --- | --- |
| Target Ledoit–Wolf | 36.72% | [32.55, 41.41] | 100.00% | 0.7675 | 0.9747 |
| Target sample covariance | 55.99% | [51.04, 61.46] | 100.00% | 0.8757 | 0.9883 |
| Source covariance | 12.76% | [12.50, 13.28] | 100.00% | 0.5747 | 0.9435 |
| Entity-balanced covariance | 27.34% | [23.18, 32.03] | 100.00% | 0.6972 | 0.9648 |
| Proposed: Log-Euclidean entity covariance | 25.00% | [21.09, 29.43] | 100.00% | 0.6354 | 0.9583 |
| Target OC-SVM (RBF) | 12.76% | [10.68, 15.36] | 87.50% | 0.7209 | 0.9622 |
| Source+target OC-SVM (RBF) | 12.76% | [11.20, 14.58] | 91.67% | 0.6876 | 0.9558 |
| Target Isolation Forest | 59.90% | [57.29, 62.76] | 100.00% | 0.8670 | 0.9876 |
| Source+target Isolation Forest | 50.52% | [47.92, 53.12] | 100.00% | 0.8245 | 0.9833 |
| Target MinCovDet | 70.05% | [65.36, 75.26] | 100.00% | 0.9268 | 0.9934 |
| Source+target MinCovDet | 30.21% | [26.04, 34.90] | 100.00% | 0.7013 | 0.9666 |

H1 requires both a descriptive Wilson upper bound no greater than 0.12 and a maximum
held-out-load false-alarm rate no greater than 0.15. The record-bootstrap interval
resamples complete fault records within the six fault-turn strata (10,000 draws,
seed 711). Because every fault record has eight blocks, block-weighted and
record-macro detection coincide here. The 2.5th–97.5th bootstrap percentiles are descriptive record-weighting sensitivities
conditional on the observed single motor; population coverage has not been established.

## S3. Conditional paired comparisons and source-transfer contrasts

### S3.1. Every frozen candidate versus Proposed

The following two column groups share the first-column identifiers and preserve every original row, value, and row order. Read corresponding rows together; splitting is a layout change only.

Table S3.1a. Every frozen candidate versus Proposed (column group 1 of 2).

| Candidate | Candidate detection | Proposed detection | Candidate − Proposed | Descriptive paired interval (pp) | Bootstrap p |
| --- | --- | --- | --- | --- | --- |
| Target MinCovDet | 70.05% | 25.00% | +45.05 pp | [+40.62, +49.48] | 0.0001 |
| Target Isolation Forest | 59.90% | 25.00% | +34.90 pp | [+31.77, +38.02] | 0.0001 |
| Target sample covariance | 55.99% | 25.00% | +30.99 pp | [+28.12, +34.38] | 0.0001 |
| Source+target Isolation Forest | 50.52% | 25.00% | +25.52 pp | [+21.88, +28.91] | 0.0001 |
| Target Ledoit–Wolf | 36.72% | 25.00% | +11.72 pp | [+9.90, +13.54] | 0.0001 |
| Source+target MinCovDet | 30.21% | 25.00% | +5.21 pp | [+3.91, +6.51] | 0.0001 |
| Entity-balanced covariance | 27.34% | 25.00% | +2.34 pp | [+1.04, +3.65] | 0.0001 |
| Source+target OC-SVM (RBF) | 12.76% | 25.00% | -12.24 pp | [-16.15, -8.59] | 0.0001 |
| Source covariance | 12.76% | 25.00% | -12.24 pp | [-16.41, -8.33] | 0.0001 |
| Target OC-SVM (RBF) | 12.76% | 25.00% | -12.24 pp | [-16.41, -8.59] | 0.0001 |

Table S3.1b. Every frozen candidate versus Proposed (column group 2 of 2; continued).

| Candidate | Holm p | Candidate / tie / Proposed records | Candidate / Proposed health FA |
| --- | --- | --- | --- |
| Target MinCovDet | 0.0010 | 43 / 5 / 0 | 0 / 1 |
| Target Isolation Forest | 0.0010 | 47 / 1 / 0 | 3 / 1 |
| Target sample covariance | 0.0010 | 48 / 0 / 0 | 1 / 1 |
| Source+target Isolation Forest | 0.0010 | 41 / 7 / 0 | 2 / 1 |
| Target Ledoit–Wolf | 0.0010 | 33 / 15 / 0 | 1 / 1 |
| Source+target MinCovDet | 0.0010 | 21 / 26 / 1 | 1 / 1 |
| Entity-balanced covariance | 0.0010 | 10 / 36 / 2 | 1 / 1 |
| Source+target OC-SVM (RBF) | 0.0010 | 0 / 23 / 25 | 1 / 1 |
| Source covariance | 0.0010 | 0 / 23 / 25 | 1 / 1 |
| Target OC-SVM (RBF) | 0.0010 | 0 / 22 / 26 | 1 / 1 |

### S3.2. Target-only versus source-balanced training/reference

The following two column groups share the first-column identifiers and preserve every original row, value, and row order. Read corresponding rows together; splitting is a layout change only.

Table S3.2a. Target-only versus source-balanced training/reference (column group 1 of 2).

| Contrast family | Target-only | Source-balanced counterpart | Target detection | Balanced detection | Target − balanced |
| --- | --- | --- | --- | --- | --- |
| min cov det | Target MinCovDet | Source+target MinCovDet | 70.05% | 30.21% | +39.84 pp |
| sample vs log euclidean entity covariance | Target sample covariance | Proposed: Log-Euclidean entity covariance | 55.99% | 25.00% | +30.99 pp |
| sample vs arithmetic entity covariance | Target sample covariance | Entity-balanced covariance | 55.99% | 27.34% | +28.65 pp |
| isolation forest | Target Isolation Forest | Source+target Isolation Forest | 59.90% | 50.52% | +9.38 pp |
| ocsvm | Target OC-SVM (RBF) | Source+target OC-SVM (RBF) | 12.76% | 12.76% | +0.00 pp |

Table S3.2b. Target-only versus source-balanced training/reference (column group 2 of 2; continued).

| Contrast family | Descriptive paired interval (pp) | Holm p | Target / tie / balanced records |
| --- | --- | --- | --- |
| min cov det | [+35.42, +44.27] | 0.0005 | 42 / 6 / 0 |
| sample vs log euclidean entity covariance | [+28.12, +34.38] | 0.0005 | 48 / 0 / 0 |
| sample vs arithmetic entity covariance | [+25.78, +32.03] | 0.0005 | 47 / 1 / 0 |
| isolation forest | [+7.29, +11.46] | 0.0005 | 32 / 15 / 1 |
| ocsvm | [-1.04, +1.04] | 1.0000 | 2 / 44 / 2 |

The MinCovDet contrast preserves the 60-row/26-feature versus 240-row/27-feature
fitting difference described in S1.2; it does not isolate source information in a
fixed feature space.

Both tables use complete-record paired differences across the same 48 fault records,
stratified by fault turns. Two-sided centered bootstrap p-values use 10,000 draws
(seed 711); Holm adjustment is applied separately to the 10 candidate-vs-Proposed
comparisons and the five transfer contrasts. The smallest attainable nonzero
bootstrap estimate is 0.0001. These post-reveal comparisons quantify conditional
differences on one motor; their nominal p-values and adjusted values are diagnostics of the resampling scheme,
without established inferential validity under the dependent record grid. Holm
adjustment does not remove dependence or establish cross-motor generalization. The two covariance contrasts against target sample covariance are
the closest covariance transfer comparisons but do not hold the matrix estimator
fixed. Isolation Forest's `max_samples="auto"` and OC-SVM's `gamma="scale"` are
data adaptive; fixed implementations do not imply identical numerical fitting
parameters after source augmentation. The Holm summaries also do not account for
all post-reveal analysis choices.

## S4. Horizon, first-alarm, and acceleration-position diagnostics

All records follow the same [12, 36) s acceleration segment, divided into block IDs
0–7. Block position therefore co-moves with speed. The all-eight-block detection rate weights each position equally. Record-any
detection accumulates alarm opportunities over the full horizon and can be driven
by late high-score positions. The following fixed-prefix diagnostics retain the
frozen scores and thresholds and describe early-trajectory coverage.

### S4.1. First four, first seven, and all eight blocks

| Method | Blocks 0–3: detection / any / health FA (%) | Blocks 0–6: detection / any / health FA (%) | Blocks 0–7: detection / any / health FA (%) |
| --- | --- | --- | --- |
| Target Ledoit–Wolf | 6.77 / 16.67 / 0.00 | 27.68 / 87.50 / 0.00 | 36.72 / 100.00 / 3.12 |
| Target sample covariance | 25.00 / 35.42 / 0.00 | 49.70 / 100.00 / 0.00 | 55.99 / 100.00 / 3.12 |
| Source covariance | 0.00 / 0.00 / 0.00 | 0.30 / 2.08 / 0.00 | 12.76 / 100.00 / 3.12 |
| Entity-balanced covariance | 3.12 / 10.42 / 0.00 | 16.96 / 62.50 / 0.00 | 27.34 / 100.00 / 3.12 |
| Proposed: Log-Euclidean entity covariance | 2.60 / 10.42 / 0.00 | 14.29 / 52.08 / 0.00 | 25.00 / 100.00 / 3.12 |
| Target OC-SVM (RBF) | 0.00 / 0.00 / 0.00 | 2.08 / 6.25 / 0.00 | 12.76 / 87.50 / 3.12 |
| Source+target OC-SVM (RBF) | 0.00 / 0.00 / 0.00 | 1.49 / 6.25 / 0.00 | 12.76 / 91.67 / 3.12 |
| Target Isolation Forest | 29.17 / 85.42 / 18.75 | 54.46 / 100.00 / 10.71 | 59.90 / 100.00 / 9.38 |
| Source+target Isolation Forest | 19.79 / 75.00 / 12.50 | 44.35 / 97.92 / 7.14 | 50.52 / 100.00 / 6.25 |
| Target MinCovDet | 54.69 / 64.58 / 0.00 | 65.77 / 89.58 / 0.00 | 70.05 / 100.00 / 0.00 |
| Source+target MinCovDet | 5.21 / 14.58 / 0.00 | 20.24 / 62.50 / 0.00 | 30.21 / 100.00 / 3.12 |

Each cell reports fault-block detection, fault-record any-alarm, and held-out healthy
block false-alarm rate. Denominators are respectively 192/48/16 for blocks 0–3,
336/48/28 for blocks 0–6, and 384/48/32 for blocks 0–7.

### S4.2. First alarm by physical fault record

| Method | Records ever alarmed | Never alarmed | First block Q1 / median / Q3 | Healthy-RPM proxy Q1 / median / Q3 |
| --- | --- | --- | --- | --- |
| Target Ledoit–Wolf | 48/48 | 0 | 4 / 5 / 6 | 889 / 1216 / 1643 |
| Target sample covariance | 48/48 | 0 | 2 / 4 / 5 | 463 / 889 / 1216 |
| Source covariance | 48/48 | 0 | 7 / 7 / 7 | 2214 / 2214 / 2214 |
| Entity-balanced covariance | 48/48 | 0 | 5 / 6 / 7 | 1216 / 1643 / 2214 |
| Proposed: Log-Euclidean entity covariance | 48/48 | 0 | 6 / 6 / 7 | 1642 / 1643 / 2214 |
| Target OC-SVM (RBF) | 42/48 | 6 | 7 / 7 / 7 | 2214 / 2214 / 2214 |
| Source+target OC-SVM (RBF) | 44/48 | 4 | 7 / 7 / 7 | 2214 / 2214 / 2214 |
| Target Isolation Forest | 48/48 | 0 | 0 / 2 / 3 | 218 / 463 / 644 |
| Source+target Isolation Forest | 48/48 | 0 | 0 / 1 / 3.2 | 218 / 340 / 706 |
| Target MinCovDet | 48/48 | 0 | 0 / 1 / 5 | 218 / 318 / 1216 |
| Source+target MinCovDet | 48/48 | 0 | 5 / 6 / 7 | 1216 / 1643 / 2214 |

First-alarm quantiles are calculated only among records that ever alarm. The RPM
quantity is the median RPM from the matching-load healthy record and block; it is a
proxy, not a measured fault-record RPM and not a stationary time-to-detection
estimate. Proposed first alarm occurred at median block 6, while Target MinCovDet
first alarm occurred at median block 1.

### S4.3. AUROC matched by acceleration block

The following two column groups share the first-column identifiers and preserve every original row, value, and row order. Read corresponding rows together; splitting is a layout change only.

Table S4.3a. AUROC matched by acceleration block (column group 1 of 2).

| Method | B0 | B1 | B2 | B3 | B4 |
| --- | --- | --- | --- | --- | --- |
| Target Ledoit–Wolf | 0.385 | 0.922 | 1.000 | 1.000 | 1.000 |
| Target sample covariance | 0.844 | 0.906 | 0.958 | 0.990 | 1.000 |
| Source covariance | 0.703 | 0.896 | 0.948 | 0.995 | 1.000 |
| Entity-balanced covariance | 0.589 | 0.917 | 1.000 | 1.000 | 1.000 |
| Proposed: Log-Euclidean entity covariance | 0.526 | 0.453 | 0.734 | 0.854 | 0.911 |
| Target OC-SVM (RBF) | 0.464 | 0.823 | 0.953 | 0.990 | 1.000 |
| Source+target OC-SVM (RBF) | 0.464 | 0.802 | 0.948 | 0.990 | 0.995 |
| Target Isolation Forest | 0.453 | 0.724 | 0.979 | 0.964 | 0.974 |
| Source+target Isolation Forest | 0.505 | 0.807 | 0.885 | 0.990 | 0.990 |
| Target MinCovDet | 0.755 | 0.880 | 0.969 | 1.000 | 1.000 |
| Source+target MinCovDet | 0.698 | 0.917 | 1.000 | 0.969 | 0.932 |

Table S4.3b. AUROC matched by acceleration block (column group 2 of 2; continued).

| Method | B5 | B6 | B7 | Equal-weight mean | Pooled |
| --- | --- | --- | --- | --- | --- |
| Target Ledoit–Wolf | 1.000 | 1.000 | 1.000 | 0.913 | 0.767 |
| Target sample covariance | 1.000 | 1.000 | 1.000 | 0.962 | 0.876 |
| Source covariance | 1.000 | 1.000 | 1.000 | 0.943 | 0.575 |
| Entity-balanced covariance | 1.000 | 1.000 | 1.000 | 0.938 | 0.697 |
| Proposed: Log-Euclidean entity covariance | 0.958 | 1.000 | 1.000 | 0.805 | 0.635 |
| Target OC-SVM (RBF) | 1.000 | 1.000 | 0.891 | 0.890 | 0.721 |
| Source+target OC-SVM (RBF) | 1.000 | 1.000 | 0.917 | 0.889 | 0.688 |
| Target Isolation Forest | 0.984 | 1.000 | 1.000 | 0.885 | 0.867 |
| Source+target Isolation Forest | 1.000 | 1.000 | 1.000 | 0.897 | 0.825 |
| Target MinCovDet | 1.000 | 1.000 | 1.000 | 0.951 | 0.927 |
| Source+target MinCovDet | 0.979 | 1.000 | 1.000 | 0.937 | 0.701 |

Blocks B0–B7 correspond to [12,15), [15,18), [18,21), [21,24), [24,27), [27,30),
[30,33), and [33,36) s. Each position-specific AUROC compares four held-out healthy
blocks with 48 fault blocks at the same position. The equal-weight mean describes
matched-position discrimination; the pooled AUROC remains the frozen primary
ranking metric. Neither treats the eight ordered blocks as independent motors.

## S5. Five-seed stochastic sensitivity

The following two column groups share the first-column identifiers and preserve every original row, value, and row order. Read corresponding rows together; splitting is a layout change only.

Table S5a. Five-seed stochastic sensitivity (column group 1 of 2).

| Stochastic method | Primary detection | Five-seed detection | Range | Max \|change\| from primary | Health FA range |
| --- | --- | --- | --- | --- | --- |
| Target Isolation Forest | 59.90% | 51.30–59.90% | 8.59 pp | 8.59 pp | 1–3/32 (3.12–9.38%) |
| Source+target Isolation Forest | 50.52% | 47.92–53.65% | 5.73 pp | 3.12 pp | 0–3/32 (0.00–9.38%) |
| Target MinCovDet | 70.05% | 65.36–77.08% | 11.72 pp | 7.03 pp | 0–2/32 (0.00–6.25%) |
| Source+target MinCovDet | 30.21% | 30.21–33.85% | 3.65 pp | 3.65 pp | 1–1/32 (3.12–3.12%) |

Table S5b. Five-seed stochastic sensitivity (column group 2 of 2; continued).

| Stochastic method | H1 passes | Threshold range | AUROC range |
| --- | --- | --- | --- |
| Target Isolation Forest | 0/5 | 0.562858–0.569218 | 0.8371–0.8906 |
| Source+target Isolation Forest | 2/5 | 0.578661–0.593532 | 0.8062–0.8530 |
| Target MinCovDet | 3/5 | 934.173–1396.26 | 0.9219–0.9352 |
| Source+target MinCovDet | 0/5 | 8857.36–9802.52 | 0.6795–0.7320 |

The five-seed list 20260820, 1201, 2402, 3603, 4804 was fixed for exploratory KAIST
baselines before external reveal; the external five-seed audit itself was post-reveal.
Only 20260820 is the prespecified external seed. For each seed, the
estimator is refitted only on the same frozen healthy training subset, and its
threshold is mechanically recalibrated from the same 24 healthy calibration blocks
at alpha 0.05. No fault score affects a threshold. Primary-seed reconciliation gave
zero alarm mismatches for all four methods (maximum score discrepancy
1.46 × 10^-11). No formal seed-stability gate was specified before reveal, so the full ranges
are descriptive and were not used to change the reported model or protocol.

## S6. Post-reveal feature drift and frozen-geometry reconstruction

The feature diagnostic is post-reveal and descriptive. Single-feature AUROC pools
64 healthy and 384 fault record–subsystem–block means over the four held-out healthy
loads; each mean contains 15 windows. This is common-support pooled AUROC, not
pair-conditional AUROC. Direction-free values equal max(AUROC, 1−AUROC), choosing
orientation after reveal. The displayed top-eight ranking uses robust-z direction-free AUROC on these
revealed labels; it is not independently validated feature performance. Matched differences and their dz separately match load,
subsystem, and block position; one healthy condition is reused across six fault
conditions. Here dz is the mean paired robust-z difference divided by its sample
standard deviation (ddof=1). The matched units are not independent motor replications.

Frozen-score allocation instead uses the winning subsystem/window of each physical
system block: 32 held-out health blocks and 384 fault blocks at all eight loads.
For target-standardized coordinates z, c_j = z_j(Pz)_j sums to z^T Pz. Individual
terms can be negative. Each winning window's absolute share is |c_j|/sum_k |c_k|,
then averaged over blocks. Thus these allocation shares and single-feature AUROCs
have different units and load support; they are not an ablation comparison.

The following two column groups share the first-column identifiers and preserve every original row, value, and row order. Read corresponding rows together; splitting is a layout change only.

Table S6a. Post-reveal feature drift and frozen-geometry reconstruction (column group 1 of 2).

| Feature | Family | Raw direction-free AUROC | Robust-z direction-free AUROC | Matched robust-z dz | Fault \|contribution\| share |
| --- | --- | --- | --- | --- | --- |
| harmonic_3_ratio_max | harmonic sideband | 0.927 | 0.933 | +1.032 | 0.35% |
| harmonic_3_ratio_mean | harmonic sideband | 0.925 | 0.925 | +0.992 | 0.24% |
| rms_ratio_a | current shape | 0.815 | 0.862 | +0.679 | 21.62% |
| phase_rms_cv | sequence imbalance | 0.769 | 0.825 | +0.662 | 9.42% |
| fundamental_amplitude_cv | current shape | 0.769 | 0.797 | +0.661 | 3.34% |
| thd_2_to_5_mean | harmonic sideband | 0.788 | 0.795 | +0.840 | 1.21% |
| rms_ratio_c | current shape | 0.664 | 0.741 | -0.179 | 2.30% |
| zero_sequence_ratio | sequence imbalance | 0.695 | 0.701 | -0.998 | 8.50% |

Table S6b. Post-reveal feature drift and frozen-geometry reconstruction (column group 2 of 2; continued).

| Feature | Health \|contribution\| share | Max \|speed rho\| |
| --- | --- | --- |
| harmonic_3_ratio_max | 0.71% | 0.509 |
| harmonic_3_ratio_mean | 0.52% | 0.501 |
| rms_ratio_a | 3.86% | 0.469 |
| phase_rms_cv | 8.08% | 0.513 |
| fundamental_amplitude_cv | 1.26% | 0.598 |
| thd_2_to_5_mean | 0.96% | 0.588 |
| rms_ratio_c | 0.45% | 0.080 |
| zero_sequence_ratio | 8.79% | 0.067 |

Harmonic-3 ratios discriminate fault from health individually but receive less than
1% of the frozen score's absolute contribution, whereas `rms_ratio_a` receives
21.62%. These distinct summaries motivate a locked-reference misalignment hypothesis.
Low absolute allocation does not establish feature irrelevance, and this coordinate-
dependent, non-unique decomposition did not select or reweight features. Block and fundamental frequency co-move,
and the reported speed associations do not identify causal fault features.

### S6.1. Exact reconstruction checks

| Subsystem | Adaptation windows | Rank / 27 | Condition number | Max contribution-sum error | Center match | Scale match |
| --- | --- | --- | --- | --- | --- | --- |
| SubSys1 | 60 | 27 | 309.53 | 2.910e-11 | yes | yes |
| SubSys2 | 60 | 27 | 300.11 | 7.276e-11 | yes | yes |

Across all 448 physical-record block scores, the maximum absolute reconstructed-
versus-frozen score error was 3.638e-12; the maximum feature-contribution
sum error was 7.276e-11. The reconstructed center, scale,
Log-Euclidean covariance, winning subsystem/window, system maximum, p-value, and
alarm were checked without fitting a new model or recomputing a threshold. Fault
labels did not enter covariance reconstruction.

## S7. Post-reveal 100 kHz to 10 kHz sampling-rate sensitivity

The KAIST three-phase current was mechanically anti-aliased and decimated from
100 kHz to 10 kHz with `scipy.signal.resample_poly` (`up=1`, `down=10`, Kaiser
beta 5.0, line padding) over each complete leading 120 s record before the frozen
0.2 s windows were cut. The feature definitions, 3 s maximum block aggregation,
splits, ridge values, methods, seeds, calibration rule, and external feature table
were unchanged. This analysis was specified after fault reveal and was not used for
model or protocol selection.

| Source feature arm | Rows | Records | Windows / record | Blocks / record | Duplicate keys | Nonfinite values |
| --- | --- | --- | --- | --- | --- | --- |
| native_100khz | 27000 | 45 | 600–600 | 40–40 | 0 | 0 |
| polyphase_10khz | 27000 | 45 | 600–600 | 40–40 | 0 | 0 |

The following two column groups share the first-column identifiers and preserve every original row, value, and row order. Read corresponding rows together; splitting is a layout change only.

Table S7a. Post-reveal 100 kHz to 10 kHz sampling-rate sensitivity (column group 1 of 2).

| Method | Sampling dependency | Detection, 100 kHz source | Detection, 10 kHz source | Change | Health FAR, 100 kHz |
| --- | --- | --- | --- | --- | --- |
| Target Ledoit–Wolf | target-only control | 36.72% | 36.72% | +0.00 pp | 3.12% |
| Target sample covariance | target-only control | 55.99% | 55.99% | +0.00 pp | 3.12% |
| Source covariance | source-sensitive | 12.76% | 12.50% | -0.26 pp | 3.12% |
| Entity-balanced covariance | source-sensitive | 27.34% | 25.26% | -2.08 pp | 3.12% |
| Proposed: Log-Euclidean entity covariance | source-sensitive | 25.00% | 24.74% | -0.26 pp | 3.12% |
| Target OC-SVM (RBF) | target-only control | 12.76% | 12.76% | +0.00 pp | 3.12% |
| Source+target OC-SVM (RBF) | source-sensitive | 12.76% | 12.50% | -0.26 pp | 3.12% |
| Target Isolation Forest | target-only control | 59.90% | 59.90% | +0.00 pp | 9.38% |
| Source+target Isolation Forest | source-sensitive | 50.52% | 52.08% | +1.56 pp | 6.25% |
| Target MinCovDet | target-only control | 70.05% | 70.05% | +0.00 pp | 0.00% |
| Source+target MinCovDet | source-sensitive | 30.21% | 27.60% | -2.60 pp | 3.12% |

Table S7b. Post-reveal 100 kHz to 10 kHz sampling-rate sensitivity (column group 2 of 2; continued).

| Method | Health FAR, 10 kHz | AUROC, 100 kHz | AUROC, 10 kHz |
| --- | --- | --- | --- |
| Target Ledoit–Wolf | 3.12% | 0.7675 | 0.7675 |
| Target sample covariance | 3.12% | 0.8757 | 0.8757 |
| Source covariance | 3.12% | 0.5747 | 0.5496 |
| Entity-balanced covariance | 6.25% | 0.6972 | 0.6849 |
| Proposed: Log-Euclidean entity covariance | 3.12% | 0.6354 | 0.6331 |
| Target OC-SVM (RBF) | 3.12% | 0.7209 | 0.7209 |
| Source+target OC-SVM (RBF) | 3.12% | 0.6876 | 0.6977 |
| Target Isolation Forest | 9.38% | 0.8670 | 0.8670 |
| Source+target Isolation Forest | 3.12% | 0.8245 | 0.8643 |
| Target MinCovDet | 0.00% | 0.9268 | 0.9268 |
| Source+target MinCovDet | 3.12% | 0.7013 | 0.6966 |

Proposed detection changed from 25.00% to 24.74% (-0.26 percentage points), and
AUROC changed from 0.6354 to 0.6331. Across the 48 physical fault records, alarm
rate improved for 0, tied for 47, and worsened for 1. Its KAIST
leave-one-motor-out source detection remained 91.96%
(100 kHz: 95.71%) and AUROC remained
0.9947 (100 kHz: 0.9993),
so the 10 kHz arm was not globally unusable. All five target-only controls reproduced
448/448 block scores, p-values, and alarms with zero mismatches. Matching the nominal source sampling rate by this procedure did not recover
performance. It narrows that explanation under the fixed extractor, while leaving
sensor, analog-filter, controller, noise, and other acquisition-chain differences
unresolved.

## S8. Hash registry, interpretation limits, and next validation step

| Role | Artifact | SHA-256 |
| --- | --- | --- |
| processed input | `data/processed/kaist_current_features.csv.gz` | 6276bfae67169f0e70a3b1bd3c4fdbf42c08631a4d4dcfd097ef8246ef970d20 |
| processed input | `data/processed/external_dual_three_phase_health_features.csv.gz` | cef907bd7c7fef66170a87672df937827bd9a0e8c3f2083599ab277a19de9f0e |
| sampling input | `data/processed/kaist_current_features_10khz.csv.gz` | 4d196d756b01ab43bd6431a2334a5922787eaf83df7836927c4f1d4d436b13ad |
| raw-file hash registry | `data/processed/external_dual_three_phase_health_features.csv.metadata.json` | f5a2925970af69db85eaa3699841600b4f9457396ba7250078147a8beb9448ad |
| primary result | `results/external_pmsm_validation/aggregate_summary.csv` | d21ae9068e39ecfb0c3d4b597fdf150f490079ccd0739bfc4b14a79cdad38cfa |
| paired diagnostic | `results/external_failure_diagnostics/paired_vs_proposed.csv` | 7a5794bb4470c1bd97a17776b40ed469eac8322270dea79d1e5f84410cb1122b |
| horizon diagnostic | `results/external_failure_diagnostics/horizon_detection_record_any.csv` | 658e1136d0d3cbac95b7a261139fbf4730e93dc41332e505321bf5fb78db25c4 |
| position diagnostic | `results/external_failure_diagnostics/block_auroc.csv` | 225cc74409c08cedeb292eadd3c664381062aab180c36cd93c402d8c61e969a5 |
| seed diagnostic | `results/external_seed_sensitivity/aggregate_seed_ranges.csv` | f8634fc426c6bed9091a2cdd246b08bd014c74f07992658b2f47da95c182a8bb |
| feature diagnostic | `results/external_feature_drift/feature_diagnostic_summary.csv` | 6eda1b2d27f262d23782774d58c9887ae1161e58e84499c94eca9e1349fc1720 |
| geometry check | `results/external_feature_drift/score_reconstruction_checks.csv` | 1607861e42f0dbd0ad10422c64dc42a0551e7bf159a2e7af2d0ab138b10eac18 |
| sampling diagnostic | `results/sampling_rate_sensitivity/external_method_comparison.csv` | 77697abc45ab32648118e23f468b499e5b52c8383ac73b94aa4ccb8ed2931373 |

The external processed-feature metadata JSON contains the individual SHA-256 hash,
sampling rate, length, health/fault metadata, and subsystem/window counts for all 56
MAT records. The hash registry above fixes the inputs and derived result tables from
which this supplement was mechanically generated.

### S8.1. Limits on inference

- **One external motor.** The eight loads, six fault-turn configurations, two
  subsystems, and eight ordered blocks are repeated conditions on one physical
  dual-three-phase motor. Neither record bootstrap nor Holm correction creates
  independent motor replication.

- **Dependent calibration and test blocks.** The 24 calibration blocks come from
  three healthy load records and the 32 held-out health blocks from four records.
  Conformal p-values and Wilson intervals are therefore empirical/descriptive, not
  guarantees under arbitrary within-record dependence.

- **Post-reveal diagnostics.** Sections S3–S7 were specified after external fault
  reveal. They retain the frozen predictions or mechanically rerun an explicitly
  defined sampling arm; they introduce no new selected model, feature, ridge,
  threshold, aggregation, or primary claim.

- **Speed-position coupling.** The analyzed record segment is an acceleration ramp.
  Block ID, time, electrical-frequency proxy, and speed co-move, so first-alarm and
  feature associations cannot isolate causal effects or stationary detection delay.

- **Current-only scope.** The pipeline reads only the two three-phase current sets.
  Voltage, dq variables, and other modalities were not used. The test therefore does
  not cover faults whose detectable signature requires those channels.

- **Dataset-specific target adaptation.** Target-only methods use 60 healthy
  adaptation windows per subsystem, while source-balanced variants combine these
  with source healthy references. Performance gaps describe this locked protocol,
  not every possible transfer strategy.

The decisive next validation is a prospectively frozen replication on additional
independent external motors, preferably with stationary speed/load segments as well
as ramps. Until that experiment, external uncertainty is conditional on the single
observed motor and the failure of source balancing should not be generalized as a
population-level effect.

## S9. Prospectively logged secondary transient-set audit

This audit used Zenodo 10.5281/zenodo.15631383: 12 records from one 200 W
PMSM and nine records from one 20 kW PMSM, all sampled at 10 kHz and all
containing a transition from prefault operation to an interturn short circuit. It has
no separate healthy-only records. Signal values remained sealed until the parser,
onset rule, whole-record split, 80% motor-compatibility gate, detector family, and
outputs had been frozen.


The predefined detector input is measured `ialbt_meas` alpha–beta current,
mechanically mapped to pseudo three-phase currents: ia = alpha,
ib = (−alpha + sqrt(3) beta)/2, and ic = (−alpha − sqrt(3) beta)/2.
True zero sequence is unobservable, not demonstrated to be zero. Both source and
target therefore use the predeclared 26-feature arm excluding `zero_sequence_ratio`;
KAIST 10 kHz features are the fixed source. The independent `if_meas` onset rule uses
10 ms causal RMS and threshold max(b + 10 sigma, 0.02 max(RMS)), where b is the
median of the initial min(0.5 s, 20% of record duration) baseline and sigma is
1.4826 times its median absolute deviation. Onset is the start of the first 20 ms
interval continuously at or above the threshold, with a 0.2 s prefault guard. Detector scores do not set onset.
Unlike the primary external 3 s system-block analysis, this protocol calibrates and
alarms 0.2 s windows at alpha 0.05.

### S9.1. Compatibility gate and preserved primary failure

| Stage | Motor | Compatible records | Fraction (%) | Use |
| --- | --- | --- | --- | --- |
| Frozen primary parser | 200W | 0/12 | 0.00 | no features or scores |
| Frozen primary parser | 20kW | 0/9 | 0.00 | no features or scores |
| Post-reveal implicit-time repair | 200W | 12/12 | 100.00 | descriptive sensitivity only |
| Post-reveal implicit-time repair | 20kW | 4/9 | 44.44 | 44.44%; failed the frozen 80% gate |

The frozen primary parser required an explicit monotonic 10 kHz time candidate.
All 21 MATLAB `timeseries` objects instead stored uniform timing in `TimeInfo` while
their explicit `Time_` arrays were empty. The run therefore stopped before feature
extraction and produced no detector scores. After that failure was committed, a
separate opt-in parser reconstructed time from the stored start, increment, and length.
Five 20 kW records then remained incompatible because detected onset overlapped the
frozen 0.5 s baseline. No alternative baseline or record subset was selected, so the
20 kW motor has no quantitative endpoint.

### S9.2. Post-reveal 200 W single-motor sensitivity

The secondary protocol specified twelve configurations, adding a target-only
log-ridge covariance control to the primary evaluation's eleven configurations.
Each of 12 200 W records was held out in turn. Depending on the hash split,
6 other records supplied prefault fit windows and
5 records supplied 67-88
calibration windows. Across all twelve held-out records there were 176 prefault test windows, 60 primary first-second windows, and 120 windows over the full 2 s post-onset horizon. Each record contributed five first-second and ten 2 s post-onset windows; the 176 prefault windows are a pooled total rather than a per-record count.

| Method | Held-out prefault alarms | First 1 s fault alarms | Record-any alarms | Full 2 s fault alarms | Mean record AUROC |
| --- | --- | --- | --- | --- | --- |
| Target Ledoit–Wolf | 7/176 | 0/60 | 0/12 | 0/120 | 0.280 |
| Target sample covariance | 11/176 | 0/60 | 0/12 | 0/120 | 0.562 |
| Target Log-Euclidean covariance | 11/176 | 0/60 | 0/12 | 0/120 | 0.546 |
| Source covariance | 9/176 | 0/60 | 0/12 | 0/120 | 0.532 |
| Entity-balanced covariance | 13/176 | 0/60 | 0/12 | 0/120 | 0.559 |
| Proposed: Log-Euclidean entity covariance | 8/176 | 0/60 | 0/12 | 0/120 | 0.541 |
| Target OC-SVM (RBF) | 9/176 | 0/60 | 0/12 | 0/120 | 0.389 |
| Source+target OC-SVM (RBF) | 8/176 | 0/60 | 0/12 | 0/120 | 0.161 |
| Target Isolation Forest | 11/176 | 0/60 | 0/12 | 0/120 | 0.447 |
| Source+target Isolation Forest | 12/176 | 0/60 | 0/12 | 0/120 | 0.524 |
| Target MinCovDet | 9/176 | 0/60 | 0/12 | 0/120 | 0.564 |
| Source+target MinCovDet | 9/176 | 0/60 | 0/12 | 0/120 | 0.539 |

Mean record AUROC averages twelve within-record AUROCs comparing each held-out
record's eligible prefault windows with its five first-second fault windows; it is
not the full-2-second AUROC.

Every method produced zero thresholded alarms in both post-onset horizons. Held-out
prefault alarms ranged from 7/176 to 13/176. Proposed produced
8/176 prefault alarms and mean record AUROC
0.541; Target MinCovDet produced
9/176 and AUROC
0.564. Because all 12 methods tie at zero detection,
paired thresholded transfer comparisons are uninformative; score-ranking differences
do not rescue the missed early alarms. This analysis is post-reveal, contains one
physical motor, and reuses prefault and fault segments from the same transition
records. It cannot confirm cross-capacity transfer or support population inference.

### S9.3. Audit hashes

| Role | Artifact | SHA-256 |
| --- | --- | --- |
| prospectively frozen pre-reveal protocol | `docs/secondary_transient_validation_protocol.md` | d5f072dd6b494e6b09c1ec6c8956c5d0e60310fc724711d4a66792a78b1b8a08 |
| chronological reveal log | `docs/secondary_transient_reveal_log.md` | 2620b53b6a6ef16d093d74f9b7522fd937dff8c3d61f6bef2ecbb515ad374801 |
| frozen parser compatibility | `results/transient_feature_build/record_compatibility.csv` | b2f737ca6d2dfbd20f211b1e083dd7a045954658f21f7a7553bcf8fb93aa219e |
| post-reveal compatibility | `results/transient_feature_build_post_reveal_implicit_time/record_compatibility.csv` | 315d0887fc8db78d87f6ac8db3c120bc91977b4ee4b4e42a8b65748a5c7172a0 |
| post-reveal features | `data/processed/transient_pmsm_features_post_reveal_implicit_time.csv.gz` | 92fea2691ea737319dd43469130b0275bce596bab1e98f0bc4c391f109899ad1 |
| 200 W method summary | `results/transient_pmsm_validation_post_reveal_200w/aggregate_summary.csv` | aa4904f52069c94e3d5ddf885b63fffa54cd35b71671fc5ab85cc9ee1bede41b |
| 200 W record summary | `results/transient_pmsm_validation_post_reveal_200w/per_record_summary.csv` | b73c1260342d09d1d52546d6fbded7106e352127e80e6dacc67538d556447ad8 |
| 200 W predictions | `results/transient_pmsm_validation_post_reveal_200w/window_predictions.csv.gz` | 4c474ac9da88f2b34daff2bb2151939ccc2b77b004ea3e4dfb959fe5da19e3d6 |

The immutable frozen parser failure and the opt-in repaired analysis are stored in
separate result directories. The repaired feature-table hash is checked against both
the extractor and validation metadata before this section is generated.

## S10. Exploratory KAIST comparisons, sensitivities, and failed hypotheses

These results were used in method development and are exploratory. Their retention
allows the same-family finding to be evaluated without crowding the main external
reliability question. None selects a new external feature, threshold, seed, record,
or aggregation. Three KAIST motors provide the physical holdout units, but each has
only one unique healthy record; the fourteen later-time health blocks per motor
remain dependent parts of that record.

### S10.1. Covariance references and paired record differences

| Covariance method | Health alarms | Wilson upper (%) | Mean detection (%) | Worst motor (%) | Mean fold AUROC |
|---|---:|---:|---:|---:|---:|
| Target Ledoit--Wolf | 1/42 | 12.32 | 90.30 | 82.14 | 0.9969 |
| Target sample covariance | 0/42 | 8.38 | 93.87 | 86.79 | 0.9983 |
| Source-only covariance | 0/42 | 8.38 | 89.11 | 70.18 | 0.9968 |
| Arithmetic entity covariance | 0/42 | 8.38 | 95.48 | 87.86 | 0.9989 |
| Primary Log-Euclidean | 0/42 | 8.38 | 95.71 | 90.00 | 0.9993 |

The primary detected 1608 of 1680 fault blocks across 42 complete fault records.
Per-target detection was 100.00%, 90.00%, and 97.14% for 1.0, 1.5, and 3.0 kW.
The mean is 95.71% and the worst motor is 90.00%; zero observed health alarms is
not evidence of zero population risk.

| Contrast: primary minus comparator | Mean difference (pp) | Paired 95% interval (pp) |
|---|---:|---:|
| Target Ledoit--Wolf | +5.42 | [0.59, 11.19] |
| Target sample covariance | +1.85 | [-2.14, 6.01] |
| Source-only covariance | +6.61 | [1.79, 12.32] |
| Arithmetic entity covariance | +0.24 | [-1.37, 2.32] |

Ten thousand bootstrap replicates resample complete records within target motor,
then average the three motor means. The comparisons do not establish uniform
superiority of Log-Euclidean geometry. Figure S1 displays these paired results.

![Figure S1. Exploratory paired covariance differences.](../../paper/figures/paired_detection_differences.pdf)

Figure S1. Record-level paired primary-minus-covariance detection differences.
Points are equal-motor means and intervals are motor-stratified complete-record
percentile bootstrap intervals over the 42 KAIST fault records. Positive values
favor the primary. The KAIST comparison is exploratory.

### S10.2. Established one-class controls

| One-class method | Health alarms | Mean detection (%) | Worst motor (%) |
|---|---:|---:|---:|
| Target OC-SVM | 0/42 | 89.70 | 82.68 |
| Source+target OC-SVM | 0/42 | 91.25 | 82.86 |
| Target Isolation Forest | 1/42 | 97.56 | 95.36 |
| Source+target Isolation Forest | 0/42 | 96.07 | 90.71 |
| Target MinCovDet | 1/42 | 89.82 | 84.11 |
| Source+target MinCovDet | 1/42 | 92.32 | 87.32 |
| Primary Log-Euclidean | 0/42 | 95.71 | 90.00 |

Primary minus source+target Isolation Forest was -0.36 percentage points
([-3.93, 3.45]), leaving their difference unresolved. Primary minus target OC-SVM
was +6.01 points ([1.07, 11.90]); primary minus target MinCovDet +5.89
([0.95, 11.67]); and primary minus source+target MinCovDet +3.39 ([0.30, 6.85]).
The primary-versus-source+target OC-SVM interval included zero. Target Isolation
Forest's higher detection was accompanied by 1/42 health alarms and a 12.32%
descriptive Wilson upper bound, just above H1. Across five seeds, source+target
Isolation Forest varied from 96.01% to 96.85% detection and zero to two health
alarms. These findings constrain a superiority claim; they do not provide new
independent-motor confirmation.

![Figure S2. Exploratory paired one-class differences.](../../paper/figures/oneclass_detection_differences.pdf)

Figure S2. Primary-minus-one-class record-level detection differences. Points and
intervals use the same complete-record, motor-stratified exploratory bootstrap as
Figure S1. Parenthetical false-alarm counts refer to 42 later-time health blocks.

### S10.3. Adaptation budget and calibration feasibility

The fixed-horizon sensitivity keeps calibration and test time common while varying
the adaptation prefix. Its health denominator is 30 blocks rather than the 42 of
the primary split. The different denominators must not be pooled as independent
health evidence.

| Adaptation (s) | Adaptation blocks | Fixed-horizon detection (%) | Health alarms | Minimum p if adaptation alone calibrated |
|---|---:|---:|---:|---:|
| 3 | 1 | 94.64 | 0/30 | 0.500 |
| 6 | 2 | 96.90 | 0/30 | 0.333 |
| 12 | 4 | 96.25 | 0/30 | 0.200 |
| 24 | 8 | 94.94 | 0/30 | 0.111 |

In a separate sequential sensitivity, calibration follows the adaptation prefix;
the pattern was also nonmonotone. The apparent maximum at 6 s cannot select a
primary setting after fault inspection. The original 12 s adaptation remains
unchanged. Four adaptation blocks fit a reference but cannot resolve a p-value
of 0.05; at least nineteen calibration units are required. Both sensitivities
retain an independent calibration role rather than conflating adaptation with
alarm calibration.

![Figure S3. Exploratory adaptation sensitivity.](../../paper/figures/adaptation_budget.pdf)

Figure S3. Exploratory adaptation-budget sensitivity and arithmetic calibration
feasibility. Fixed-horizon and sequential designs change different time roles and
do not replace the primary chronological split. Minimum attainable p-values use
1/(n+1); none of these adaptation prefixes alone resolves 0.05.

### S10.4. Block length and aggregation

| Alarm block rule | Detection (%) | Health alarms | Calibration units | Disposition |
|---|---:|---:|---:|---|
| 1 s maximum | 93.61 | 2/138 | 60 | Exploratory |
| 2 s maximum | 93.73 | 0/66 | 30 | Exploratory |
| 3 s maximum | 95.71 | 0/42 | 20 | Exact primary reconstruction |
| 3 s 90th percentile | 97.32 | 1/42 | 20 | H1 failed; not selected |
| 5 s maximum | Not scored | Not scored | 12 | 0.05 alarm unresolved |
| 6 s maximum | Not scored | Not scored | 10 | 0.05 alarm unresolved |

The 3 s maximum reproduces the primary output. The 90th percentile increases
detection but its 12.32% Wilson upper health bound misses the predeclared 12%
gate. Five- and six-second blocks do not supply enough calibration units within
60 s. The 3 s maximum was motivated by healthy autocorrelation and remains the
primary; fault outcomes cannot change it.

![Figure S4. Exploratory block-rule sensitivity.](../../paper/figures/block_sensitivity.pdf)

Figure S4. Exploratory block length and aggregation. The figure includes the
health-count and calibration-resolution evidence for each tested setting. Changes
in block duration also change the temporal analysis denominator; blocks are not
independent motor replications.

### S10.5. Preserved failed hypotheses

The original protocol hypothesized improved detection at the lowest two nominal
severities. All covariance methods reached 100% there, making the proposed
difference uninformative rather than proven. The original positive severity-score
ordering hypothesis also failed: three of six motor-by-fault-family Spearman
associations were negative, including both families for the 1.0 kW motor.
Severity labels therefore cannot support severity regression or a monotone
physical-response claim from this representation.

The hypothesis that window calibration underestimates deployment risk also lacks
a strong causal test here. Later-time KAIST health comes from the same acquisition,
so split or resampling differences cannot establish independent-session behavior.
The protocol avoids adjacent-window mixing, but it does not quantify a specific
amount of leakage-induced inflation on this dataset.

![Figure S5. Exploratory nominal-severity patterns.](../../paper/figures/severity_detection.pdf)

Figure S5. Exploratory detection across labeled nominal severity. Nonmonotone
patterns and the low-severity ceiling are retained. The plot does not establish
severity estimation or a monotone causal relationship.

## S11. Reporting and reproducibility boundary

The main manuscript retains the frozen failed primary result and six core figures;
this supplement retains complete comparator, diagnostic, compatibility, and
exploratory sensitivity details. The code package provides commands to reconstruct
the reported tables and figures, plus the immutable reveal outputs used for
evidence checking. Full raw recomputation requires the original licensed archives.

This reporting revision preserves the original protocols and first external/secondary
reveal evidence as distinct historical artifacts. Diagnostic explanations and
repaired compatibility analyses do not replace the frozen outcomes. The original
scores and result files remain unchanged; current-environment checks and stochastic
refits are distinguished from byte-identical historical execution.
