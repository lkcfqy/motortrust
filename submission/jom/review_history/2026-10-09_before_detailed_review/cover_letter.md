---
title: >-
  Cover Letter to Journal of Magnetics
---

[SUBMISSION DATE]

Dear Editor,

I submit the research article entitled *Frozen Cross-Dataset Reliability of
Healthy-Only PMSM Stator-Fault Detection* for consideration in the *Journal of Magnetics*.

The article examines a practical limitation of electromagnetic condition monitoring:
whether a stator-fault alarm adapted with target healthy currents retains reliability
across datasets. Interturn faults can disturb current symmetry and harmonic structure,
while speed, load, winding topology and measurement conditions also change these
signals. The study evaluates these competing influences through a fixed healthy-only
pipeline and target-only controls, rather than claiming a new universally superior
algorithm.

The exploratory KAIST result was 95.71% fault-block detection with 0/42 healthy
alarms. After a pre-reveal internal Git freeze, the primary Log-Euclidean detector
detected 96/384 external fault blocks (25.00%), produced 1/32 healthy alarms and
attained AUROC 0.6354. Its descriptive Wilson upper bound of 15.74% exceeded the
prespecified 12% health gate. The preimplemented target-only MinCovDet comparator
reached 70.05% detection with 0/32 healthy alarms at the primary seed, but its gate
passed for only three of five seeds. The failed primary result is retained.

All 48 external fault records came from one physical dual-three-phase PMSM. The
article reports the fault-turn and phase confounding, unmatched pooled AUROC load
support, time dependence, and absence of real-time deployment evidence. The internal
Git freeze was not an externally registered preregistration. A secondary frozen
parser failure is also reported, with repaired analysis identified as post-reveal
and non-confirmatory. These boundaries are central to the engineering message:
high detection in a motor family and a late alarm on every record do not demonstrate
reliable transfer to another motor.

The topic connects current-based stator diagnostics, permanent-magnet machines and
electromagnetic monitoring with reproducible alarm evaluation. The supplementary
material provides the complete comparison, seed sensitivity and failure diagnostics;
the accompanying code package provides frozen protocols, lower-grain results and
data acquisition instructions. Their upload category is subject to the active
submission system's supplementary-file options.

I am the sole author. [AUTHOR TO CONFIRM BEFORE SUBMISSION: originality; no concurrent
submission or prior publication of this article; approval of the manuscript and
declarations; data permissions; and any required institutional permission. Replace
this paragraph with the verified statements.]

This research received no funding. [AUTHOR TO COMPLETE: competing interests, acknowledgments and final AI
assistance disclosure. OpenAI Codex assisted code review, evidence checks, English
revision and document preparation; the author must review the resulting content and
confirm responsibility before submission.]

Sincerely,

LI KAICHEN

Department of Artificial Intelligence Convergence Engineering, Changwon National University

20 Changwondaehak-ro, Uichang-gu, Changwon-si, Gyeongsangnam-do 51140, Republic of Korea

lkcfqy@gmail.com; [AUTHOR TO SUPPLY TELEPHONE]
