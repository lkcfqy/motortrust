---
title: Frozen Cross-Dataset Reliability of Healthy-Only PMSM Stator-Fault Detection
bibliography: [../../references/key_papers.bib, jom_references.bib]
link-citations: true
---

**Author:** LI KAICHEN

**Affiliation:** Department of Artificial Intelligence Convergence Engineering, Changwon National University, 20 Changwondaehak-ro, Uichang-gu, Changwon-si, Gyeongsangnam-do 51140, Republic of Korea

**Corresponding author:** LI KAICHEN; lkcfqy@gmail.com; postal address as above

**Telephone:** +82-10-3915-7350; **Fax:** Not available

**ORCID:** https://orcid.org/0009-0008-8743-3162

## Abstract

Current-based healthy-only alarms may fail across permanent-magnet synchronous motors
(PMSMs), operating conditions, and measurement domains. We evaluate eleven detectors
with separated healthy fitting and calibration under a frozen external protocol.
The primary Log-Euclidean detector achieved 95.71% exploratory fault-block detection
with 0/42 healthy alarms on three same-family PMSMs. On one external dual-three-phase
PMSM, it detected 96/384 blocks (25.00%), produced 1/32 healthy alarms, and attained
AUROC 0.6354. Its descriptive two-sided 95% Wilson upper endpoint of 15.74% exceeded
the preset 12% gate. Preimplemented target-only MinCovDet achieved 70.05% detection
and 0/32 alarms, but passed the gate in only three of five seeds. Ordered alarms and
paired estimator-family configurations show trajectory-associated drift and reduced
detection under the frozen source-augmentation pipeline. These offline findings
identify protocol-specific failure boundaries on one external motor, without
population safety or real-time deployment guarantees.

**Keywords:** permanent-magnet synchronous motor; stator short circuit;
cross-dataset reliability; healthy-only detection; negative transfer; alarm calibration

## 1. Introduction

Stator interturn short circuits disturb winding symmetry and can damage a
permanent-magnet synchronous motor (PMSM). Current-based indicators include negative-sequence components,
current-vector measures, and fault-sensitive harmonics
[@zafarani2018itscreview; @jeong2017negativesequence; @li2024negativesequence;
@urresty2013nonstationary].
Monitoring currents is attractive because the drive already measures them. However,
a signature that separates healthy and faulty signals on one laboratory motor need
not produce a reliable alarm after transfer to another motor. Healthy current distributions can differ across machines and operating conditions.
The source and external datasets differ in power rating, winding topology, acquisition
chain, and speed/load trajectory; this comparison does not isolate each difference.
Normal operating variation can enter the same score directions as a short-circuit signature.

This distinction matters for deployment. Target fault examples may be unavailable,
whereas a healthy commissioning trace is obtainable. A practical transfer detector
must fit and set its threshold without target faults, and it must be
compared with a detector fitted from target health alone. Adding source-machine data
is useful only if it improves that non-transfer reference under the same alarm
protocol. Here, healthy-only describes reference fitting, normalization, and target
alarm calibration; source-domain development can use labeled source faults.
Negative transfer is possible
[@wang2019negativetransfer; @kumar2024negativetransfer].

Rotating-machinery research already includes cross-machine domain generalization
and large multi-dataset benchmarks [@li2020domaingeneralization;
@li2023causalconsistency; @zhao2024dgbenchmark]. Those advances do not remove the
need to distinguish fault classification from healthy-only alarm reliability. A high
area under the receiver-operating-characteristic curve (AUROC) can coexist with a
poor fixed threshold. Likewise, counting a record as detected after any alarm can
hide failure throughout most of its operating trajectory.

The evaluation split is equally consequential. Adjacent windows from one acquisition
share a motor, sensors, and operating history. Randomly assigning them to training
and testing does not test a new motor or session. Machinery studies have documented
large performance changes when holdout is moved from signals to acquisitions and
physical parts [@wheat2024dataleakage]. Structured validation and explicit
experimental units are needed when observations are dependent
[@roberts2017structuredcv; @hurlbert1984pseudoreplication].

We address a focused question: does healthy-only source assistance retain reliable
stator-fault alarms under a frozen cross-dataset transfer? An exploratory study on
three same-manufacturer PMSMs motivated a motor-balanced Log-Euclidean covariance
detector. For public data acquired by an independent laboratory, we froze feature extraction,
healthy fitting, thresholds, comparators, and the analysis interval before accessing
external fault values. The detector that performed well internally failed externally
and remains the primary method in this report. The contribution is an auditable
reliability evaluation: it exposes a ranking reversal, quantifies source augmentation
against target-only controls, and preserves operating-condition and replication
limits. It does not claim a new universally superior algorithm.

## 2. Background and evaluation rationale

### 2.1. Fault signatures under changing operating conditions

An interturn fault changes current symmetry and the relation between phase currents.
Sequence and current-vector indicators have been used to detect winding asymmetry
[@jeong2017negativesequence; @li2024negativesequence]. Fault-sensitive current
harmonics have also been evaluated using order tracking under changing speed and
load [@urresty2013nonstationary]. These are distinct indicators, whose response
depends on machine configuration and closed-loop operation
[@zafarani2018itscreview]; they do not validate the present feature set. Under nonstationary speed, spectral components move in
frequency; their measured magnitude and resolution depend on the window and sampling
chain. Load changes alter healthy current relationships and drive response.
Physical-data models have also addressed PMSM diagnosis at rapidly varying speed
[@li2024physicaldatapmsm].

A recent *Journal of Magnetics* study compares current and stray-flux signatures
using finite-element simulations of electrical and mechanical faults in a synchronous
motor with wound-field excitation [@park2025electromagnetic]. It illustrates the relevance of electromagnetic
signals to machine diagnosis; it does not establish healthy-only PMSM transfer or
validate the present cross-dataset alarm.

These physical considerations motivate normalized current features and within-target
healthy alignment, but neither step guarantees operating invariance. A covariance
detector can assign large precision to a direction with small variance during
commissioning; a subsequent healthy speed or load change may then raise its anomaly
score. This study examines that failure empirically. It does not infer the causal
contribution of any single operating variable, localize fault phase, or estimate
shorted-turn severity.

### 2.2. Transfer, one-class references, and alarm calibration

Cross-machine generalization predates this work. Prior studies address collaborative
multimachine generalization and multi-dataset fault-diagnosis benchmarking
[@li2023causalconsistency; @zhao2024dgbenchmark]. Frequency-guided
machinery methods also address adverse source-domain emphasis
[@liu2025frequencyguided]. Our narrower contribution concerns a fault-blind external
reveal with a target-only reference, rather than priority in transfer learning.

One-class support vector machines (OC-SVM), Isolation Forest, and Minimum Covariance
Determinant (MinCovDet) are established methods
[@scholkopf2001support; @liu2008isolationforest; @rousseeuw1999mcd].
Log-Euclidean covariance averaging likewise uses an established geometry for
symmetric positive-definite matrices [@arsigny2006logeuclidean]. They provide
different healthy descriptions; each still requires a threshold on an untouched
healthy calibration set. Within an estimator-family pair, common input definitions, calibration, and
target-health allowance aid interpretation of source augmentation. Fit-derived
feature masks must also be reported separately.

Rank-based conformal calibration supplies an interpretable threshold construction,
but conventional coverage results rely on exchangeability
[@angelopoulos2023conformal]. Dependence requires additional assumptions or methods
[@chernozhukov2018dependentconformal; @barber2026timeseriesconformal].
Conformal industrial-fleet alarms and false-alarm studies also precede this work
[@farouq2021mondrianfleet; @farouq2022conformalfleet;
@diallo2025falsealarms]. Here, a block p-value is an empirical rank summary from
ordered motor records. It is not a proof of 5% population risk. We report alarm
counts, temporal coverage, and a predeclared descriptive health gate together.

## 3. Data and frozen analysis boundary

### 3.1. Exploratory KAIST data

The KAIST/Mendeley release contains 1.0, 1.5, and 3.0 kW PMSMs from one
manufacturer, measured at fixed 3000 rpm and one load setting
[@jung2023pmsmfaultdata; @jung2022pmsmfaultdataset]. Three-phase current was
sampled at 100 kHz. Each motor has interturn and intercoil faults at seven nominal
nonzero severity levels. Healthy records stored under the two fault families are
duplicate aliases: corresponding archive members have identical uncompressed size
and cyclic redundancy check, and an extracted pair also matched by SHA-256.
Deduplication therefore leaves three healthy and 42 fault records.

Some fault files exceed the nominal 120 s duration. Every record is restricted to
its first 120 s so that long acquisitions receive no extra weight. Each contributes
600 non-overlapping 0.2 s windows and forty 3 s blocks, each containing fifteen
windows. Three leave-one-motor-out folds use two source motors and one target motor.
Target healthy blocks 0--3 provide 12 s adaptation, block 4 is a guard, blocks
5--24 provide 60 s calibration, block 25 is a guard, and blocks 26--39 provide
42 s later-time health testing. Source healthy blocks 0--23 supply the reference;
later source blocks support nested validation without using target faults.

The approximately 3 s healthy feature cycle motivated the primary block duration.
All normalization and fitting use only the permitted healthy regions. Nevertheless,
KAIST target faults were inspected during method development. Its results are
exploratory even though each reported fit is target-fault blind. A leakage-resistant
split cannot retrospectively restore an untouched confirmation set.

### 3.2. Independent-laboratory external data

The external release contains interturn short-circuit emulation on one custom
dual-three-phase PMSM [@kozovsky2024dualthreephasepmsm]. The associated machine
paper reports 30.16 kW nominal power, a 200 V DC link, 107 A maximum continuous
current, ten pole pairs, and 8000 rpm nominal speed
[@kozovsky2022dualthreephasemodel]. These are design parameters; the released
10 kHz records are acceleration sweeps rather than steady 5000 rpm tests.

An audit using only the eight healthy records fixed the common interval [12, 36) s
before external fault access. It contains eight 3 s blocks per record. Across
healthy files, measured speed spans approximately 174--2650 rpm in that interval,
within the frozen electrical fundamental-frequency search band of 20--500 Hz.
Local block IDs 0--7 correspond exactly to original-record blocks 4--11; absolute
sample and time coordinates remain in the output.

Healthy roles use disjoint load files. The 0 N m file supplies four adaptation
blocks from [12, 24) s. Files at 10, 20, and 30 N m supply 24 calibration blocks;
files at 5, 15, 25, and 35 N m supply 32 health-test blocks. The remaining 0 N m
blocks and data outside the common interval are unused. Record separation prevents
shared-file fitting and testing, but does not establish independent sessions.

All 48 fault records were included: six shorted-turn conditions at eight loads
from 0 to 35 N m. The grid is not crossed by phase. Turns 1, 3, 5, and 6 use
phase U; turns 2 and 4 use phase V. Turn and phase effects are therefore
inseparable. The records and their two three-phase subsystems belong to one physical
motor; neither records nor subsystem streams increase the number of independent
motor replications.

Table I summarizes the different healthy partitions. Figure 1 shows the motor and
time separation used to develop the protocol. Supplementary Section S1 specifies
the external system-level split and the complete feature list.

Table I. Data and healthy roles in the primary two-dataset evaluation. Blocks and
subsystems are derived observations, not independent physical motors.

| Item | Exploratory KAIST | Frozen external evaluation |
|---|---|---|
| Physical motors | Three: 1.0, 1.5, 3.0 kW | One: 30.16 kW dual-three-phase |
| Unique records | 3 healthy; 42 fault | 8 healthy; 48 fault |
| Current sampling | 100 kHz | 10 kHz |
| Analyzed interval | First 120 s | [12, 36) s |
| Target adaptation | 4 blocks; 12 s per target | 0 N m; 4 blocks; 12 s |
| Calibration | 20 blocks per target | 10/20/30 N m; 24 system blocks |
| Health test | 14 blocks per target; 42 total | 5/15/25/35 N m; 32 system blocks |
| Fault endpoint | 42 records; 1680 blocks | 48 records; 384 system blocks |

### 3.3. Pre-reveal freeze and empirical failure rule

The external protocol, eleven detector implementations, feature parser, dependency
specifications and recorded tool versions,
healthy references, 24 calibration scores, thresholds, and complete reveal manifest
were stored in hash-addressed Git commits before fault values were opened. Two
output/statistical audit corrections made during download preceded signal access
and did not change features, scoring, fitting, thresholds, or method designation.
All planned files were checked against official filenames, byte counts, and MD5
digests and evaluated on the unchanged interval. None was excluded or substituted.
This was an internal prospective repository freeze, not an externally registered
preregistration. The historical protocol and subsequent execution log are retained
separately.

The predeclared H1 health gate requires the pooled upper endpoint of a descriptive
two-sided 95% Wilson score interval to be no greater than 12%, and a maximum
per-motor or per-test-load empirical
false-alarm rate no greater than 15%. This is an engineering evidence gate, not a
motor-population safety theorem. A gate failure cannot justify threshold changes or
removal of fault results. Log-Euclidean covariance remains the frozen primary method
regardless of comparator performance after reveal.

## 4. Healthy-only models and evaluation

### 4.1. Fixed current representation and covariance score

Each 0.2 s window yields current-shape statistics, phase RMS ratios, Clarke-vector
dispersion, sequence ratios, normalized harmonics, sideband ratios, total harmonic
distortion, and spectral entropy. Supplementary Section S1.2 gives the exact spectral,
sequence, and scaling definitions. The frozen 27-feature arm, historically named
*scale-free*, excludes
absolute RMS, zero-sequence RMS, fundamental amplitude, and mean Clarke radius.
It retains electrical fundamental frequency, so the representation is not wholly
dimensionless or speed invariant. Its inclusion is preserved in the frozen analysis;
post-reveal diagnostics cannot be used to remove it from the primary score.

For healthy reference samples from entity $m$, coordinate-wise median $c_m$ and
robust scale $r_m$ define

\[
\widetilde{x}_{m,i}=(x_{m,i}-c_m)\oslash r_m.
\]

Only source reference or target adaptation samples enter these statistics. Let
$S_m$ denote their sample covariance. The primary relative ridge is

\[
S_m^{(\lambda)}=S_m+\lambda\frac{\operatorname{tr}(S_m)}{d}I.
\]

Development was not fully unsupervised. The ridge fraction $\lambda=0.01$ was
selected from $10^{-4},10^{-3},10^{-2},10^{-1}$ by nested pseudo-target validation
on source motors, using their labeled faults and held-out healthy blocks. The
objective was mean source fault-block detection minus twice the mean source healthy
false-alarm rate; the outer target motor was excluded from each selection. All three
KAIST outer folds selected 0.01, which was frozen before external fault access.
This source-label use does not alter the exploratory status of KAIST. Equal-entity
Log-Euclidean averaging gives

\[
\Sigma_{\mathrm{LE}}=
\exp\left(\frac{1}{M}\sum_{m=1}^{M}\log S_m^{(\lambda)}\right).
\]

The target-standardized anomaly score is

\[
s(x)=\widetilde{x}^{\top}\Sigma_{\mathrm{LE}}^{\dagger}\widetilde{x}.
\]

Two KAIST sources and the target each contribute one covariance internally.
Externally, all three KAIST healthy sources and one target subsystem contribute
equally. Each external subsystem receives its own target median, scale, and
covariance. The system window score is the maximum of the two subsystem scores;
the system block score is the maximum over its fifteen windows. One calibration is
applied to this combined score. The subsystems are not separately alarmed at 5%.

### 4.2. Comparators and fair source assistance

The other covariance references are target Ledoit--Wolf, regularized target sample,
source-only, and arithmetic entity-balanced covariance. One-class comparators pair
target-only and source-plus-target versions of OC-SVM, Isolation Forest, and
MinCovDet. Every method starts from the same 27 input features and shares the block
maximum, target calibration set, and alarm level. Target-only one-class fitting uses four adaptation
blocks. Source-assisted one-class fitting uses four complete healthy blocks from each
source and target, with source blocks selected at fixed evenly spaced positions
within the allowed reference. Thus a long source record cannot dominate merely by
supplying more windows.

OC-SVM uses an RBF kernel, gamma="scale", and nu=0.05. Isolation Forest uses
500 trees; its built-in contamination cutoff is not the operating alarm threshold.
The preset `max_samples="auto"` uses 60 versus 240 rows for the paired Isolation
Forests; OC-SVM's `gamma="scale"` also depends on its healthy fitting data.
MinCovDet removes invariant or algebraically redundant coordinates by rank-revealing
QR using healthy fitting rows only. In each external subsystem, target-only MinCovDet
retained 26 features from 60 fitting rows, excluding `rms_ratio_c`; source-plus-target
fitting retained all 27 from 240 rows. These masks were not equalized after reveal.
Hyperparameters and the primary stochastic seed 20260820 were fixed before external
reveal. The five-seed list fixed for exploratory KAIST baselines was reused in a
post-reveal external stability audit, with no best-seed selection. MinCovDet is a
preimplemented comparator rather than a replacement primary method. The label
“Proposed” in retained artwork and archived tables denotes the frozen Log-Euclidean method.

### 4.3. Calibration, outcomes, and conditional uncertainty

For block score $A_b$ and $n$ healthy calibration scores,

\[
p_b=\frac{1+\sum_{j=1}^{n}\mathbf{1}(A_j\ge A_b)}{n+1}.
\]

An alarm occurs when $p_b\le0.05$. There are 20 calibration blocks internally and 24 externally. At least 19 units
are required to attain a p-value of 0.05, so four adaptation blocks cannot also be
called a 5% calibration set. Both implemented thresholds are calibration maxima at
this alarm level: a score must strictly exceed the calibration maximum. A tie with
that maximum is not alarmed. Blocks share acquisition history and, externally, an ordered
acceleration trajectory. Neither exchangeability nor a sufficient mixing condition
has been established. P-values and Wilson intervals are therefore descriptive under
the observed dependence.

Fault detection is the mean alarm fraction per complete record, averaged equally
within motors for KAIST and across external records. Equal external record length
also makes it equal to 96/384 for the primary method. We report raw healthy counts,
worst-motor performance, AUROC, and the H1 decision. KAIST AUROC is a mean across
folds. External pooled AUROC compares fault blocks at eight loads with health
blocks at four held-out loads; it is not load matched.

Paired differences resample complete records in 10,000 bootstrap draws: within
motor internally and within the six fixed turn--phase strata externally. External
2.5th--97.5th percentile intervals are descriptive record-weighting sensitivities,
not calibrated population confidence intervals. They do not estimate between-motor
variation. Post-reveal paired comparisons additionally apply Holm correction within
their stated comparison families; percentile intervals remain unadjusted. Neither
coverage nor inferential p-value validity has been established under this dependence. No window or block is treated as an independent physical repetition.

## 5. Results

### 5.1. Exploratory same-family performance

The primary detector produced 0/42 later-time healthy alarms, with a descriptive
Wilson upper bound of 8.38%. It detected 1608/1680 fault blocks: 100.00%,
90.00%, and 97.14% for the 1.0, 1.5, and 3.0 kW targets, respectively, averaging
95.71%. Table II and Fig. 2 show that this is competitive within the source family,
but does not establish broad algorithmic superiority.

Table II. Exploratory KAIST comparison at the common block alarm level. Mean
detection weights the three target motors equally; health counts pool 14 blocks per
motor. Paired comparisons and sensitivity details are in Supplementary Section S10.

| Method | Healthy alarms | Mean detection | Worst-motor detection |
|---|---:|---:|---:|
| Target Ledoit--Wolf | 1/42 | 90.30% | 82.14% |
| Target sample covariance | 0/42 | 93.87% | 86.79% |
| Source-only covariance | 0/42 | 89.11% | 70.18% |
| Arithmetic entity covariance | 0/42 | 95.48% | 87.86% |
| **Primary Log-Euclidean** | **0/42** | **95.71%** | **90.00%** |
| Target OC-SVM | 0/42 | 89.70% | 82.68% |
| Source+target OC-SVM | 0/42 | 91.25% | 82.86% |
| Target Isolation Forest | 1/42 | 97.56% | 95.36% |
| Source+target Isolation Forest | 0/42 | 96.07% | 90.71% |
| Target MinCovDet | 1/42 | 89.82% | 84.11% |
| Source+target MinCovDet | 1/42 | 92.32% | 87.32% |

Target-only MinCovDet detected 89.82% internally. The primary was not the highest-
detection method overall: source+target Isolation Forest achieved 96.07% with 0/42
healthy alarms, and target-only Isolation Forest achieved 97.56% with 1/42. The
latter's Wilson upper endpoint of 12.32% narrowly exceeded H1. Complete paired
intervals and covariance contrasts are retained in Supplementary Section S10.

The exploratory development hypotheses also had failures. Low nominal severities
had a ceiling effect rather than a demonstrated improvement; anomaly scores were
not monotone in severity. Shorter adaptation or alternative aggregation sometimes
increased detection, but fault outcomes cannot select those settings. Supplementary
Section S10 retains these results and the original 12 s/3 s maximum setting.

### 5.2. Frozen external failure and ranking reversal

All 48 planned external fault records passed the fixed parser and interval checks,
with no exclusions. The primary detector retained its locked health outcome:
1/32 alarms (3.125%). The maximum held-out-load false-alarm rate was 1/8
(12.5%), but the pooled descriptive Wilson upper bound was 15.74%, above the
12% H1 limit. The gate therefore failed; this health failure was recorded before fault reveal.
The reveal subsequently assessed fault detection. The available health evidence
did not satisfy the preset criterion; it does not prove that a population false-alarm
rate exceeds 5%.

The detector alarmed on 96/384 fault blocks, giving 25.00% detection (descriptive
turn-stratified record-bootstrap interval [21.09, 29.43]%) and pooled AUROC
0.6354. Target-only MinCovDet, an existing frozen comparator, alarmed on 269/384
blocks: 70.05% ([65.36, 75.26]%), with 0/32 healthy alarms and AUROC 0.9268.
Its paired advantage over the primary was 45.05 percentage points
([40.62, 49.48]). MinCovDet was the sole method to pass H1 at the prespecified seed. Table III
and Fig. 3 display the complete comparison, including unsuccessful controls.

Table III. Frozen external comparison on one physical motor. Fault detection is
the equal-record mean across 48 records; AUROC is pooled under unequal load support.
H1 uses descriptive health bounds and load-specific rates, not independent motor
replication. Interval and threshold details are in Supplementary Section S2.

| Method | Healthy alarms | Fault detection | AUROC | H1 |
|---|---:|---:|---:|---|
| Target Ledoit--Wolf | 1/32 | 36.72% | 0.7675 | Fail |
| Target sample covariance | 1/32 | 55.99% | 0.8757 | Fail |
| Source-only covariance | 1/32 | 12.76% | 0.5747 | Fail |
| Arithmetic entity covariance | 1/32 | 27.34% | 0.6972 | Fail |
| **Primary Log-Euclidean** | **1/32** | **25.00%** | **0.6354** | **Fail** |
| Target OC-SVM | 1/32 | 12.76% | 0.7209 | Fail |
| Source+target OC-SVM | 1/32 | 12.76% | 0.6876 | Fail |
| Target Isolation Forest | 3/32 | 59.90% | 0.8670 | Fail |
| Source+target Isolation Forest | 2/32 | 50.52% | 0.8245 | Fail |
| Target MinCovDet | 0/32 | 70.05% | 0.9268 | Pass |
| Source+target MinCovDet | 1/32 | 30.21% | 0.7013 | Fail |

The Log-Euclidean and target-only MinCovDet ordering reversed from exploratory
KAIST (95.71% versus 89.82%) to external data (25.00% versus 70.05%). This is a
protocol-specific pairwise reversal, not an overall-best claim.

Across the five previously fixed KAIST seeds, target-only MinCovDet remained above the
other audited stochastic variants, but detection varied from 65.36% to 77.08%,
healthy alarms from 0 to 2/32, and only three seeds passed H1. That mechanical
post-reveal sensitivity does not authorize replacing the primary or choosing a
better seed. The point result is conditional on its seed as well as its motor.

### 5.3. Operating trajectory and source augmentation

Post-reveal diagnostics retained frozen predictions and thresholds. The primary
detector raised no alarm on any fault record in blocks 0--2 and alarmed on all
48 records in block 7. Its only health alarm was also in block 7. Median healthy
speed rose from approximately 218 to 2214 rpm across the local block sequence.
Consequently, the 48/48 record-any result masks weak coverage through earlier
operating points (Fig. 4). The faults were already present during these acceleration
records, so this is early-trajectory coverage rather than fault-onset latency.

In the first four blocks, detection was 2.60% and 10.42% of records had any alarm;
in the first seven, these were 14.29% and 52.08%. The median first alarm was
block 6, approximately 1643 rpm using the matching healthy record as a speed
proxy. Target MinCovDet detected 54.69% of the first four blocks and first alarmed
at median block 1. The proxy does not substitute for measured fault-record speed.

Block position and the primary score had Spearman associations of 0.8361 in
held-out health and 0.8212 in faults. The equal-weight mean of block-position-specific
AUROCs was 0.8047, compared with pooled AUROC 0.6354. Matching position does not
fix the unequal load support or make a new independent evaluation, but it indicates
that some fault-ranking information survives beneath the trajectory-associated
score change. These associations cannot establish speed as the sole cause.

Load-resolved detection declined from 56.25% at 0 N m to 12.50% at 35 N m
(Fig. 5). Detection across the fixed turn--phase conditions ranged from 15.63%
to 32.81% without a monotone trend. Phase and turns cannot be separated, so this
is not a severity-effect estimate.

The paired MinCovDet configurations belong to the same estimator family. Target-only
MinCovDet exceeded source+target MinCovDet by 39.84 percentage points
([35.42, 44.27]); their detection was 70.05% versus 30.21%. Target-only
Isolation Forest also exceeded its source-assisted counterpart, whereas OC-SVM
tied in mean detection. The MinCovDet pair differs in fitting rows and the resulting
26/27-feature masks, so its gap describes the frozen augmentation pipeline as a
whole, not an isolated causal effect of source information. The observed reductions
are conditional negative transfer under these complete configurations. The primary Log-Euclidean configuration
still exceeded the source-covariance reference by 12.24 points ([8.33, 16.41]), but that
contrast also changes matrix aggregation and regularization and cannot isolate the
effect of source inclusion. Complete paired contrasts are in Supplementary Section S3.

### 5.4. Bounded diagnostics and secondary compatibility failure

A post-reveal geometry audit reconstructed all 448 frozen primary block scores
with maximum absolute discrepancy $3.64\times10^{-12}$. For target-standardized
coordinates $z=\widetilde{x}$ and precision matrix $P$, the allocation $c_j=z_j(Pz)_j$
sums to $z^\top Pz$ and shares cross-terms symmetrically. Electrical fundamental
frequency had pooled single-feature AUROC 0.5038 on common load support, yet
accounted for 18.07% of absolute fault-score allocation and 38.54% of health
allocation. Third-harmonic mean and maximum ratios each had direction-free AUROC
above 0.925 but together less than 0.6% fault allocation (Fig. 6). The AUROCs pool
subsystem-block means over four common loads; allocation shares average winning
windows over system blocks and all eight fault loads. Direction is selected
post-reveal as max(AUROC, 1−AUROC). These distinct summaries motivate a hypothesis
of locked-reference misalignment; they are not a feature ablation or causal
importance measure. Low allocation does not prove irrelevance to the decision.

A separate post-reveal sampling-rate control antialias-filtered and resampled
KAIST sources to 10 kHz while retaining other settings. External primary detection
changed from 25.00% to 24.74%, AUROC from 0.6354 to 0.6331, and health alarms
remained 1/32. It did not rescue transfer under this pipeline. These diagnostics
characterize existing failure evidence; they do not redesign the primary detector.

A prospectively frozen secondary transient audit attempted 21 public records from
200 W and 20 kW motors [@zezula2024transientpmsm]. The frozen parser accepted
0/21 because it required explicit time arrays whereas the MATLAB objects stored
uniform time implicitly. No detector score was produced. This compatibility
failure remains the primary outcome. An opt-in post-reveal repair made 12/12
200 W and 4/9 20 kW records compatible; the latter failed the preset 80%
motor gate. A single-200-W-motor sensitivity then yielded 0/60 first-second
fault-window alarms for every detector and 0/120 through 2 s. Primary health
alarms were 8/176 and target-MinCovDet health alarms 9/176. This post-reveal,
non-confirmatory result provides descriptive evidence only. Its predefined
alpha--beta-derived representation and window-level calibration differ from the
primary evaluation; it does not establish a general detector failure. Full details are in Supplementary Section S9.

## 6. Discussion

The external experiment changes the engineering interpretation of the internal
result. Healthy covariance transfer appeared effective among three related motors,
yet its frozen alarm failed when winding topology, acquisition chain, load, and
speed trajectory changed together. The observed target-only advantage shows why a
source-assisted detector needs a non-transfer reference under the same target-health
budget and threshold rule. High same-family detection is insufficient evidence for
cross-motor deployment.

Reporting failure adds information beyond a lower average score. Ordered alarms
show that record-any detection can be inflated by late trajectory alarms. Load
stratification shows where coverage is weakest. The frozen-geometry allocation
is consistent with operating-reference misalignment, although individual feature
discrimination and absolute allocation use different units and supports. Matching
nominal source sampling rate did not recover performance under this extractor; other
acquisition-chain differences remain unresolved. These observations motivate
diagnostic checks for future evaluations: inspect held-out health as well as faults,
evaluate early operating segments, compare same-estimator target-only fitting, and
report every unsupported condition.

These checks do not establish a remedy. Conditioning a healthy reference on speed
and load is physically motivated, but any feature removal, revised covariance,
threshold, or condition-aware model selected using the revealed faults would be
exploratory here. Confirming a remedy requires a new untouched motor or laboratory test. Any
subsequent adaptation is a separate exploratory development and cannot rewrite the
frozen external result. Additional algorithms, repeated seed searches, and repeated analysis of the
same machine cannot supply missing independent motor replication.

Calibration also has two distinct resource requirements. Twelve seconds of target
health can fit a reference, whereas a resolvable nominal 5% rank alarm requires
at least 19 calibration units. Twenty or twenty-four ordered blocks meet that
arithmetic condition but do not establish statistical independence. Independent
healthy sessions and operating-envelope coverage are needed before a motor- or
session-level false-alarm claim can be assessed. Zero observed alarms, including
the favorable MinCovDet seed, cannot be interpreted as zero deployment risk.

The main scientific limitations are the small number of physical motors and the
compound external shift. KAIST has one unique healthy acquisition per motor and
was reused during development. The external dataset has one motor, similar
acceleration records, and no demonstrated independent sessions. Its turn count is
confounded with phase, and its pooled AUROC has unequal health/fault load support.
Time, speed, temperature, controller, topology, and sensor effects are not
independently manipulated. Bootstrap and Wilson quantities therefore summarize
recorded conditions rather than a PMSM population. The faults are laboratory
emulations rather than natural field degradation. The secondary transient parser
failed before scoring and the repaired sensitivity concerns only one motor.

All analyses were offline. Feature-extraction latency, memory use, and embedded
numerical stability were not benchmarked. A 0.2 s window and a 3 s block specify
analysis resolution, not demonstrated real-time feasibility. The available evidence
also supports neither severity estimation, prognosis, nor a safety guarantee.

## 7. Conclusion

A frozen healthy-only PMSM detector declined from 95.71% exploratory same-family
detection to 25.00% on an external motor and failed its preset health-evidence
gate. A preimplemented target-only MinCovDet comparator reached 70.05%, while its
five-seed gate instability limits the favorable operating point. Trajectory-associated
alarm drift and estimator-family source controls expose a protocol-specific failure
boundary; the MinCovDet pair also differs in fit-derived feature masks. The useful result is this reproducible ranking reversal on one external
motor, with the original primary failure preserved. Broader reliability requires new
independent motor and healthy-session evidence, not retuning on the revealed faults.

## Acknowledgments and funding

This research received no funding.

[AUTHOR INPUT REQUIRED: confirm acknowledgments, if any.]

## Statements and declarations

**Competing interests:** The author declares no competing interests.

**Author contributions:** LI KAICHEN performed all research and manuscript work. [AUTHOR INPUT REQUIRED: review any additional journal or institutional authorship requirements.]

**Ethics:** This analysis uses public experimental machine-current data and involves
no human participants, animals, or personal data. [AUTHOR INPUT REQUIRED: verify any
applicable institutional requirements before finalizing the ethics statement.]

**Generative AI assistance:** A language-model-based assistant was used under the
author's direction for code maintenance, consistency checks, document preparation,
and English drafting and editing. Numerical results were computed from the cited
datasets and checked against saved outputs. [AUTHOR INPUT REQUIRED: review the
scope of this disclosure, verify all text and references, and approve the final
manuscript. Author approval has not been asserted in this preparation draft.]

## Data and code availability

The KAIST/Mendeley dataset, external dual-three-phase dataset, and secondary
transient dataset are public under CC BY 4.0
[@jung2022pmsmfaultdataset; @kozovsky2024dualthreephasepmsm;
@zezula2024transientpmsm]. The accompanying reproducibility package contains
checksummed data-access instructions, feature extraction, detector evaluation,
complete-record statistics, selected derived evidence, protocols, and automated
checks. Raw archives are obtained from their original repositories and are not
redistributed in the code package. Supplementary material preserves complete
comparisons, failed hypotheses, post-reveal diagnostics, compatibility outcomes,
and the hash registry. [AUTHOR INPUT REQUIRED: confirm the journal-approved route
for hosting or uploading code and supplementary files; no public release is claimed.]

## Figure captions

Figure 1. Exploratory motor holdout, chronological target-health roles, and
Log-Euclidean scoring flow. The same 0.2 s windows and 3 s block maximum are retained
externally, where target-health roles instead use separate load records (Table I).
Blocks and windows remain dependent within records.

![Figure 1. Protocol overview.](../../paper/figures/protocol_overview.pdf)

Figure 2. Exploratory KAIST covariance comparison: per-motor fault detection and
healthy false-alarm intervals. Three physical motors are held out in turn, with
14 later-time health blocks per motor. Wilson intervals are descriptive; the
target faults were inspected during development.

![Figure 2. Exploratory covariance comparison.](../../paper/figures/method_performance.pdf)

Figure 3. Complete frozen external comparison on one dual-three-phase motor.
Detection intervals resample 48 complete fault records within fixed turn--phase
strata (384 ordered blocks). Health intervals summarize four held-out load records
(32 blocks). H1 limits are 12% for the pooled Wilson upper bound and 15% for
the maximum-load empirical false-alarm rate. The solid highlighted bar identifies the observed comparator
leader; the hatched bar identifies the unchanged frozen primary. Neither interval
represents independent motor replication.

![Figure 3. Frozen external method comparison.](../../paper/figures/external_method_performance.pdf)

Figure 4. Post-reveal primary-score and alarm trajectories over eight ordered 3 s
external blocks, using unchanged scores and thresholds. Score medians and
interquartile ranges summarize 48 fault and four held-out healthy records per
position. Approximate healthy speed rises with position; both axes are associated
operating descriptions rather than evidence of an isolated causal speed effect.

![Figure 4. Operating-trajectory drift.](../../paper/figures/external_condition_drift.pdf)

Figure 5. Frozen primary alarm fractions across six fixed turn--phase conditions
and eight loads. Each cell describes one physical record containing eight ordered
blocks; 12.5% means one alarmed block. Turns 1/3/5/6 use phase U and turns 2/4
phase V, preventing separate turn and phase inference. The grid belongs to one motor.

![Figure 5. Turn--phase-by-load coverage.](../../paper/figures/external_proposed_heatmap.pdf)

Figure 6. Post-reveal feature discrimination and score allocation. Direction-free
AUROC, max(AUROC, 1−AUROC), pools 64 healthy and 384 fault subsystem-block means
at four common loads. Matched dz separately pairs load, subsystem, and block,
reusing health six times. Absolute allocations average winning-window fractions
from 32 healthy and 384 fault system blocks, with all eight fault loads. Different
units and supports preclude an ablation interpretation; no feature or threshold
changed. Allocation is coordinate dependent and non-causal.

![Figure 6. Feature discrimination and contribution.](../../paper/figures/external_feature_geometry.pdf)
