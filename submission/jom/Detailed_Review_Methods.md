# Paper 1 详细模拟审稿：方法、统计与证据边界

审阅日期：2026-10-09。评审对象为本次 JOM 改稿的 `submission/jom/manuscript.md`（全文）和 `submission/jom/supplementary.md`（全文），并阅读相应原始协议、揭盲日志、算法实现、逐块预测、逐记录汇总、拟合诊断和 Git 历史。下列原句与行号指评审开始时的改稿；编辑者可能随后按本报告修订，不能因此删掉原评审发现。读取版本的 SHA-256 在 `tmp/jom/detailed_review_methods_checks.json` 中。

这是一次论文论证审查，区别于“文件能构建、数字能核对”的工程验收。本报告没有重拟合、调整参数、筛除记录或增加实验，也没有把事后诊断重新命名为冻结确认。本轮只对现有证据进行只读重算。

**模拟审稿意见：论文的集中问题和负结果有工程价值，但需要修改若干方法披露和统计措辞后再交作者最终确认。** 主要结果未发现实质算术错误。需要优先修订的是：`healthy-only` 的模型选择边界；MinCovDet 对照的不同 QR 维度；特征 AUROC 的实际 estimand；图 6 两种统计量的不同单位/支持；次级瞬态分析的独立协议。不能据本报告宣称期刊会接收，也不需要为了修复这些写作问题继续增加模型或重复调参。

严重度定义：P1 为可能改变读者对方法或证据身份的理解，投稿前应改；P2 为需要补足的解释、分母或可复现细节；P3 为可选表达改进。没有发现需要替换冻结主结果的 P0 计算错误。“支持”均指在所观察的数据和固定流程下支持，不代表总体科学命题已证明。

## 1. 独立复核做了什么

实际运行：

```bash
/Users/lkc/miniforge3/envs/motortrust/bin/python tmp/jom/detailed_review_methods_checks.py
/Users/lkc/miniforge3/envs/motortrust/bin/python -m ruff check tmp/jom/detailed_review_methods_checks.py
```

两条命令均通过。第一条检查脚本只读取保存产物：直接用健康/故障两两分数比较重算 AUROC，按唯一分数阈值重算 average precision，用原始校准分数重算 p 值与报警，再从记录键重算比较和瞬态终点。详细结果为 `tmp/jom/detailed_review_methods_checks.json`。它覆盖 11 个冻结外部方法、20 个随机方法×seed 分组、3 个 KAIST 主方法折和 12 个瞬态方法；没有调用 `.fit()`。

| Category | Observed defects | Assessment |
|---|---|---|
| 冻结外部数值与报警规则（11 方法） | 0/11 方法出现点估计、p 值或严格阈值报警不一致 | 已检这 11 组，不代表所有原始信号重新提取过 |
| 随机方法逐块复核（20 方法×seed 组） | 0/20 组出现校准 p 值、报警、FAR 或记录宏平均不一致 | 原输出内部一致；未声称当前 sklearn 完全复现历史拟合 |
| KAIST 主方法（3 留出电机折） | 0/3 折出现分母或报警总数不一致 | 1608/1680 和 0/42 支持；仍属探索性 |
| 次级瞬态终点（12 方法） | 0/12 方法出现 176、60、120 分母或零检出不一致 | 数值支持；协议身份和观测输入需更详细披露 |
| 方法/统计论证 | 见第 2 节逐项发现，未用一个“通过率”掩盖解释问题 | 数字正确不能替代公平性、estimand 和推断范围审查 |

| Category | Observed defects | Assessment |
|---|---|---|
| 问题与结论可读性 | 主问题清楚；`healthy-only` 的广义含义会误导 | 应提前定义“拟合/校准健康数据”与“源故障开发选择”的分工 |
| 比较可读性 | 同一家族被读成严格只改变源数据；QR 维度未写出 | 需报告训练样本数、保留维度和数据自适应的默认参数 |
| 统计量可读性 | AUROC 匹配含义、AUPRC 基线、贡献比例单位需补足 | 表脚和图注应紧邻数据解释，不能仅在局限总段声明 |
| 次级协议可读性 | 主方法 27 维/3 s 块容易被带入瞬态 26 维/0.2 s 窗口分析 | 加一个紧凑方法段即可，无需新实验 |
| PDF 视觉质量 | 本轮方法审稿未重新检查排版 | 视觉 QA 属既有独立逐页检查；稿件再修改后须重新渲染受影响页面 |

以上两表是分项审查范围，不是互斥问题计数，不能相加得出“全论文缺陷率”。

## 2. 投稿前应执行的具体修订

### R1（P1）：健康数据拟合不等于从未使用故障标签选择模型

**原句/位置：** 主稿 §1（约 L73）“does healthy-only source assistance retain reliable…”；§4.1（L264–265）“The ridge fraction … was selected in source-only nested pseudo-target validation …; target faults did not select it.” 补充 S1（L123–125）仅说 “source-selected ridge fraction 0.01”。

**判断：部分支持，但关键选择规则遗漏。** 每次中心、尺度、协方差/一类模型拟合和目标健康报警校准确实只用允许的健康行；外部故障没有进入这些操作。可是 `scripts/select_log_covariance_ridge.py::pseudo_target_metrics()` 返回源伪目标故障检出率及源健康 FAR，实际 objective 是 `mean_source_validation_detection − 2 × mean_source_validation_far`。即源故障标签确实参与了 λ 选择。`results/log_ridge_selection/ridge_selection.csv` 的 12 个候选行完全符合该公式，3 个 outer fold 都选中 0.01。原协议 §4.1 明确允许源故障标签，不构成新发现的泄漏。

原句 “target faults did not select it” 对每个外层折是正确的，但读者容易把通篇 `healthy-only` 理解成连方法开发/超参数选择都不看任何故障。不同折中，某电机成为另一折的源伪目标，且全部 KAIST 数据又用于探索开发，这也是不能把 KAIST 写成 untouched confirmation 的原因。

**可执行修订：** 在第一次定义方法与 §4.1/S1 中明确：

> Healthy-only refers to detector fitting, normalization, and target-health calibration. Offline ridge development used labeled source faults in nested pseudo-target validation, maximizing source detection minus twice source false-alarm rate. The selected 0.01 ridge was fixed before external fault access; no external fault informed selection.

这只补足真实历史，不能把原 objective 改成健康-only 目标，也不能重新选择 λ。比较是固定流程下的比较，不能宣称各方法具有完全相同的标签开发预算。

### R2（P1）：MinCovDet 的同家族对照没有保留完全相同的特征子空间

**原句/位置：** §4.2（L291）“Every method uses the same representation…”；§5.3（L452–457）“The clearest transfer contrast holds the estimator family fixed… This supports conditional negative transfer from source augmentation…”；补充 S0/S3 的 same-estimator 描述。

**判断：同一家族/实现、相同 27 项输入候选、相同目标健康预算及校准规则支持；“只改变源信息”的解释不支持。** `results/external_pmsm_validation/run_metadata.json::oneclass_diagnostics` 和全部五 seed 拟合诊断显示，两子系统均为：

| 配置 | 健康训练行/子系统 | 输入候选维度 | 实际保留维度 | 丢弃坐标 |
|---|---:|---:|---:|---|
| target MinCovDet | 60 | 27 | 26 | `rms_ratio_c` |
| source+target MinCovDet | 240 | 27 | 27 | 无 |

QR 只查看训练健康行，身份合法；但特征 mask 随训练集合改变。`support_fraction=None` 的鲁棒支持大小也受 n/d 影响。Isolation Forest 的 `max_samples="auto"` 在本例由 60 行变为 240 行；OC-SVM 的 `gamma="scale"` 是数据自适应带宽。这些属于预定 pipeline 的机械结果，不能默认为数值参数和维度也完全不变。

独立按 48 条记录配对，target minus source+target 的 MinCovDet 平均为 +39.84375 pp，42 条 better、6 条 tie、0 条 worse；Isolation Forest +9.375 pp（32/15/1）；OC-SVM 0 pp（2/44/2），支持该具体源增强流程的条件性负迁移。它不隔离“原始源信息”单独的因果贡献。

**可执行修订：** 保留同家族比较和结果，但加上实际训练行/维度；将解释限定为：

> These are source-augmentation pipeline contrasts using the same estimator implementation, candidate input features, target-health allowance, and calibration rule. They also change training-set size and, for MinCovDet, the healthy-fit QR subset (26 versus 27 coordinates). They therefore do not isolate a causal effect of source information alone.

不应为了“公平”看故障后强行重设同一 mask 或重拟合。

### R3（P1）：单特征 AUROC 是共同支持内的 pooled AUROC，不是逐条件配对 AUROC

**原句/位置：** §5.4（L467）“Electrical fundamental frequency had matched single-feature AUROC 0.5038…”；Fig. 6 “Post-reveal matched single-feature discrimination…”；S6（L376–380）“comparing 384 fault blocks with 64 record-subsystem healthy blocks at matching loads and block positions.”

**判断：数值支持，estimand 标签应修订。** `scripts/analyze_external_feature_drift.py::same_block_feature_effects()` 的 AUC 是四个共同负载支持中全部健康/故障单位 pooled 后计算。每个单位为 15 窗的 record-subsystem-block 均值：64 健康、384 故障。计算 ROC 时没有限制健康/故障比较必须落在同一 load×subsystem×block；这些键的 many-to-one 配对仅用于 `matched_*_difference` 与 `dz`。因此 AUROC 仍包含跨位置、跨负载和跨子系统的分数比较。

独立两两分数比较重现：`fundamental_hz` raw/robust AUC 0.5037841797；`harmonic_3_ratio_mean` raw 0.9254964193、robust 0.9254150391；max raw 0.9266357422、robust 0.9330240885。数字本身不用变。四共同负载确实解决主 pooled AUROC 的负载支持不一致问题，但不是所有运行条件的条件化比较。

**可执行修订：**

> The single-feature AUROCs pool record-subsystem-block means within the four common loads. They share load support but are not conditional AUROCs within load, subsystem, and block strata. The paired feature differences additionally match those three keys.

图注和正文都要区分“共同支持”与“配对差值”，不能只改一处术语。

### R4（P1）：图 6 的 AUROC 与贡献比例使用不同单位及故障负载范围

**原句/位置：** §5.4（L470–474）“The mean and maximum third-harmonic ratios each had AUROC above 0.925, but together less than 0.6% fault contribution… This mismatch supports an operating-reference failure interpretation.”；S6 表和解释段。

**判断：所列数值支持，但此对照不是同一支持/同一窗口上的特征消融。** AUROC 用四共同负载的子系统块均值；fault contribution 用全部八负载的 384 个 physical system-block，每块只取触发最大分数的子系统/窗口。健康贡献 38.54% 则来自 32 个健康测试 system-block 的 winning windows。两类统计量的支持、聚合及单位都不同。贡献为每个 winner 的 `|c_j| / Σ_k |c_k|` 再平均，不是独立可加的解释方差，也不是用单特征 AUC 计算出来的权重。

重算/读取支持 `fundamental_hz` fault share 18.07094582%，health-test 38.5355%；两第三谐波 fault shares 合计 0.59165292%。对称 cross-term 分配和负贡献允许的说明正确。

**可执行修订：** 表脚/图注把两个分母写出；把 “supports … failure interpretation” 收紧为：

> The coexistence of these summaries motivates a hypothesis of misaligned frozen reference geometry. Because discrimination uses block means on common loads and contributions use system-winning windows over all fault loads, this comparison is descriptive and is not a condition-adjusted feature ablation.

无需重算其他消融或选新特征来增强图形结论。

### R5（P2）：AUPRC 接近 1 的主要背景是当前表中故障占比 92.31%

**原句/位置：** S2b（L161–173）AUPRC 列；primary 0.9583，target MinCovDet 0.9934。

**判断：AP 数值全部支持，但没有紧邻的类占比基线。** 当前评估拼接 384 fault 与 32 held-out health，fault prevalence 为 `384/416 = 92.3077%`。恒定分数/no-skill PR 基线即该比例。高 AP 不能解释为实际低故障发生率现场的报警 precision，更不能掩盖 primary 的 25% 阈值检出及 H1 失败。只读独立 AP 算法逐 unique-score threshold 重现全部 11 方法的保存 AP。

**可执行修订：** 表脚添加：

> Fault prevalence in this evaluation is 384/416 (92.31%), the no-skill average-precision baseline. AUPRC is prevalence dependent and does not estimate deployed alarm precision; load support is also unequal.

不必删除 AP；也不能为了给 AP 一个更好解释事后重平衡样本。

### R6（P2）：五 seed 列表的确在外部揭盲前存在，但外部五 seed 扩展是事后审计

**原句/位置：** §4.2（L302–303）和 §5.2（L418）“five previously fixed seeds”；S5（L364）“The frozen seeds are…”。

**判断：原列表先存在可证明；容易误读成整个外部五 seed 实验事前冻结。** 外部 sensitivity 脚本首次提交 `39e8149` 在故障首次计分后，不能据此认定所有 seed 都是在揭盲后才选。反证是 `git show fddf2f7:scripts/run_oneclass_baselines.py` 已包含 `(20260820,1201,2402,3603,4804)`，该 commit 为 2026-08-20 14:08:52 UTC，早于外部首次计分 14:26:55 UTC。原列表用于探索性 KAIST baselines。外部 sensitivity metadata 生成于 14:37:26 UTC，并明确标为 post-reveal；外部原 protocol 的 seed 711 是 bootstrap seed，不能与 detector 的五 seed 列表混为一谈。

**可执行修订：**

> The five-seed list was fixed for the exploratory KAIST baselines before external reveal and reused for this post-reveal external audit. Only the pre-reveal primary seed 20260820 defines the frozen external main result; no seed-stability acceptance criterion was fixed before reveal.

不能删除其真实的预先列表历史，也不能把外部五 seed 审计抬成确认性结果。`3/5 pass` 是审计结果，不是随机选 seed 的部署成功概率。

### R7（P2）：最大校准分数的相等情况不报警，应写出严格不等号

**原句/位置：** §4.3 p 值公式、`p ≤ 0.05`，以及 “Both thresholds equal the largest calibration score”。

**判断：公式和实现正确，但仅写 “threshold is maximum” 可能让读者误用 `score ≥ threshold`。** 因 calibration count 使用 `A_j ≥ A_b`，n=20 或 24 时，待检分数恰等于最大校准分数会至少有一个 exceedance，p 分别 ≥2/21、2/25，均不报警。必须 `A_b > max A_cal` 才有 p=1/21 或 1/25。11 方法全部 448 行及 20 seed 组各 448 行的严格阈值判定与保存报警一致。

**可执行修订：** “At these calibration sizes the alarm is exactly `A_b > max_j A_j`; ties at the calibration maximum do not alarm.” 保持保守 ties 规则和原始阈值。

### R8（P2）：bootstrap/调整 p 值需要更直接说明其依赖假设与后验选择

**原句/位置：** §4.3（L330–335）record bootstrap/paired contrasts；S3（L242–247）“Holm adjustment … adjusted p-values do not establish cross-motor generalization”。

**判断：完整记录配对比窗口 bootstrap 更合理；不能由此保证统计覆盖或 familywise type-I error。** 所观察的 48 记录是 6 turn-phase×8 指定负载的条件格子，非已经证明独立同分布的 48 次随机实验。turn-stratified bootstrap 在每层重加权 8 个负载记录，并没有独立 session/motor 扰动。还缺乏条件于单电机的记录交换性证据。完整记录 resampling 保留块内相关，但不能消除记录间依赖。Holm 只机械地作用于这些 resampling p 值，不使其成为有校准保证的检验。percentile interval 与 Holm p 值分别报告、不混称 adjusted CI 是正确做法。

**可执行修订：** 在 S3 紧邻统计表补一句：

> These intervals and centered-bootstrap p-values describe sensitivity to record reweighting in the observed condition grid. Record-level independence/exchangeability is unverified; Holm adjustment does not establish calibrated familywise-error control under this dependence or account for all post-reveal analysis choices.

这不要求新检验或删除配对效应量。正文避免用这些 p 值单独证明总体“significant superiority”。

### R9（P2）：次级瞬态不是相同 27 维、3 s system-block 的复刻，需披露预定差别

**原句/位置：** §5.4（L481–491）和 S9/S9.2 使用 “secondary transient … every detector”；S9.2 表 “Mean record AUROC”。

**判断：0/21 冻结失败和 post-reveal 单机身份清楚，但次级方法的关键差别过度压缩。** 原次级 protocol §3–6 和 validation metadata 显示：检测器只读测得 `ialbt_meas` 的 αβ，机械重建伪三相；真实零序不可恢复，故在源和目标预先排除 `zero_sequence_ratio`，使用 26 而非主两数据集的 27 维；源为 10 kHz KAIST feature arm。此处报警/校准单位是非重叠 0.2 s prefault 窗口，非主外部的 3 s dual-subsystem max。次级另包含 target Log-Euclidean comparator，故 12 而非 11 方法。它们是次级原先的协议，不能误写成修 parser 时才选择的新方案。

onset 由独立 `if_meas` 用固定 10 ms causal RMS，阈值 `max(b+10×1.4826MAD, 0.02×max RMS)`，首次 20 ms 持续达到阈值；prefault 保留至少 0.2 s guard。源故障分数不用来定位 onset。Mean record AUROC 逐 held-out record 比较其 prefault 与**首 1 s 的五窗口**，再对 12 records 平均，未使用 full 2 s 十窗口。独立重算 primary 为 0.54055399、target MCD 为 0.56388733，支持表中舍入。

**可执行修订：** 在 S9 添加紧凑方法段和表脚，交代上述输入、26 维、10 kHz source、window-unit calibration、独立 onset/guard、首 1 s AUC；保留 176/60/120 明确分母。不能用不兼容的 20 kW 四记录建立第二个量化终点。

### R10（P2）：source-only 描述的是协方差形状来源，仍使用目标健康对齐与校准

**原句/位置：** §5.3（L458）“pure-source covariance”；S2a “Source covariance | source healthy”。

**判断：源协方差方法确实不用目标协方差，但不是完全没有目标适配的 detector。** `run_external_pmsm_validation.py` 对所有方法应用目标 subsystem median/scale，source covariance 的 target score 也使用这个标准化；全部方法用相同 24 个目标健康校准块。因此 `pure-source` 容易被理解成不接触目标健康，和公平预算陈述发生误读。

**可执行修订：** 用 “source-covariance reference” 并在 S2a 表脚写 “Training/reference describes covariance shape or one-class fitting; all methods still use target-health normalization and calibration.” 不修改该 baseline。

### R11（P2）：采样率敏感性只能否定这一具体机械重采样的救援效果

**原句/位置：** S7（L484–486）“These results do not support source/target sampling-rate mismatch as the primary explanation…”。

**判断：未救援这一 pipeline 得到支持；“primary explanation” 比数据能排除的范围更宽。** 一个 `resample_poly` arm 不重建外部 ADC、模拟前置滤波、传感器响应、控制器以及拓扑，也不分别改变这些变量。外部 25.00→24.74%、AUC 0.6354→0.6331、1/32 不变，且 target-only 五对照逐 448 行不变，是有价值的机械控制。它不能普遍排除采样/测量链差异作为多个原因之一。

**可执行修订：** 使用正文已经更谨慎的表述：“This particular antialiased source-resampling arm did not rescue transfer. It does not reproduce or rule out other acquisition-chain differences.” 不增加另一个 filter/seed 来寻找救援。

### R12（P2）：S4 的“more opportunities”应区分逐块平均与 record-any

**原句/位置：** S4（L253–256）“The primary all-eight-block metric gives late high-speed blocks more opportunities to alarm”。

**判断：长 horizon 让 record-any 有更多报警机会，但八块平均中每块权重一样。** 后四块不比前四块得到更多单块权重；late operating points 分数较高，而任何一块都能使 whole-record-any 成功。这个措辞把 metric 的聚合和时间相关混在一起。冻结 primary 的全八块均值不能被前四块均值替换。

**可执行修订：**

> The all-eight-block detection rate equally weights each position. The record-any metric accumulates alarm opportunities over the full horizon and can be driven by late high-score positions; the fixed-prefix summaries describe early-trajectory coverage.

S4 的 192/48/16、336/48/28、384/48/32 分母已正确写出，应保留。

### R13（P2）：方向自由 AUC 和 top-eight 特征是同一揭盲数据上的筛选性描述

**原句/位置：** S6（L375–377）“The table shows the eight largest direction-free single-feature AUROCs…”；Fig. 6 的高单特征 discrimination。

**判断：数值与明确 post-reveal 标签支持；还应注明方向及排名都使用相同标签。** `max(AUC,1−AUC)` 消除方向，而选 top-eight 又利用当前数据排序，没有独立 feature-selection holdout。这不是八个预先选中特征的新验证；“fault-discriminating harmonic”在这里只能是观察到的同数据描述。winning-window contribution 也没有证明加大第三谐波权重会提高报警。

**可执行修订：** “Direction and the displayed top-eight ranking were chosen descriptively on the revealed dataset; these single-feature AUROCs are not independently validated feature performance and do not authorize feature selection.” 不需要多重比较检验给这些描述性筛选加一层伪确认。

### R14（P2）：robust scale 的零离散度回退规则有方法学影响

**原句/位置：** §4.1（L250–257）“coordinate-wise median … and robust scale … define…”；S1 的 robust centered/scaled。

**判断：健康数据角色支持，核心公式与实现一致；scale 的精确定义不完整。** 代码先用 `1.4826 × MAD`；若不大于 `1e−8 × max(|median|,1)`，回退到健康 standard deviation（`np.std`，`ddof=0`）；仍不足则用 1。固定 200 Hz 源频率是零离散度坐标，这个回退会影响 transfer geometry。此处不能以“robust scale”默认总是 nonzero MAD。

**可执行修订：** S1 补准确规则（含 `std` 的实现约定），正文可以用一句指向补充。这也是为何频率坐标与 scale-free 俗称必须保留限定，而不能宣称所有特征无量纲/速度不变。

## 3. 逐节审稿结论与确实被支持的论点

### 摘要与题目

摘要同时给出探索性 95.71% 和冻结外部 25.00%，健康 0/42、1/32、主 AUC 0.6354、Wilson 15.74% 未过 12%、MCD 70.05%、0/32 与 3/5 gate。没有选择性只呈现好结果。模拟审稿人会接受其可靠性/失败边界定位，仍会要求 R1/R2 的限定影响摘要中 “conditional negative transfer” 的含义。它不能被扩大为“PMSM transfer generally fails”。“ranking reversal”应明确为 primary 与 target MCD 的观测排序反转，而不是主方法原来是所有算法冠军。

### §1–2 引言与相关工作

问题是同族成功能否支撑跨数据集健康迁移报警，集中且适合现有证据。短路与不对称/谐波、运行条件污染 score 的解释在本数据上是机制动机；实际实验同时改变 motor topology、speed、load、采集/控制条件，不估计其中单一因素的 causal effect。§2.2 强调保持算法/表征/校准/目标预算共同是合理比较原则，但 R2 的实际实现差别需要写在对应方法和结果里。文献的逐条元数据与正文支持关系另由引用审计处理，本轮没有重新声称全部文献结论验证完成。

### §3 数据与冻结过程

KAIST 3 台 physical motors、45 唯一记录（3 健康/42 故障）、healthy 文件去重、0.2 s 窗/3 s 块、目标 4/guard/20/guard/14 health roles 说明完整。3 台健康各仅一个 acquisition，14×3 later blocks不是42个独立电机。KAIST faults 被用于开发而无法复原 untouched confirmation 的承认正确。

外部 8 health records、48 fault records、一个 physical dual-three-phase motor、2 子系统以及 24 calibration/32 health test/384 fault system-block 的分母正确；two subsystems 不是 two motors。八故障负载与四健康测试负载支持不同已明确。故障 turn×phase assignment U=1/3/5/6、V=2/4 混杂保留，既不当作故障相独立效应，也不把其48条条件记录当成48台电机。

“internal Git freeze”与“externally registered preregistration”已区分。冻前两处审计 corrections 与 first-fault-value access 的时间关系已保留，不因当前 JOM 题目变化重写原计划。R6 提醒 detector seeds、bootstrap seed、外部扩展身份是三个不同层次。

### §4 方法与统计

中心/尺度/covariance/oneclass 的健康行掩码与目标 calibration 角色确实分开。source health covariance 用 allowed 24 blocks；一类平衡版本每 source/target 用 4 whole blocks。这保证 entity 不因其更长 source record 被无限加权，但总训练行仍增加，不能称总 sample count 不变。

Log-Euclidean 每 entity covariance trace-relative ridge 的 SPD 处理、equal-matrix averaging 和 target 标准化 quadratic score 与代码对应。仍是冻结主方法；MCD 不应成为 post hoc 新主方法。R1/R2/R14 是需要补足的主要方法细节。

系统分数 `max_subsystem max_window` 与 `max_window max_subsystem` 等价；冻结阈值是**组合 system-score**上校准一次，没有给两个子系统分别 5% 再并集。共形公式、minimum n=19 的算术以及不保证交换性都正确。R7 只补 ties。

H1 是 preset descriptive rule，而非总体安全证明。n=32 时零报警 Wilson upper=10.7179%；1 次=15.7443%，即这个分母下 pooled 12% 分支实际只能由零报警通过。MCD 3/5 pass 恰对应其五 seed 中三个零报警，不构成第二项独立随机稳定性证据。主方法 1/32 未过 gate，也不等同于证明 population FAR > nominal 5%。正文对此已经谨慎。

### §5.1 探索性同族结果

只读逐块复核：1 kW 560/560、1.5 kW 504/560、3 kW 544/560，合计1608/1680；各14健康测试块无报警，0/42 Wilson upper约8.38%。三 motor/fault-record 等权在相同14 records×40 blocks下与 pooled比例相同，95.71% 分母正确。

不能称 algorithm 全面优越：source+target Isolation Forest 为96.07%且0/42；primary减它−0.36 pp的区间跨0。target Isolation Forest97.56%伴1/42及12.32%上界，预设H1不通过。已有稿件没有隐藏这些限制。低严重度天花板、非单调severity、预算和aggregation 的失败结果放在S10合理；这些不授权替换外部方法。

### §5.2 冻结外部结果与 seed

主方法96/384=25%、1/32、AUROC0.6354167的逐行对应支持；MCD269/384=70.0521%、0/32、AUROC0.9267578支持。全部48record×8blocks保留，没有用兼容性筛除来让数字更好。方法-specific thresholds相差数量级不代表某方法更宽松，因为 score刻度不同，稿件已明确。

MCD五seed检测为65.36–77.08%、health0–2/32、3/5H1；不能只选77.08或三个零报警seed。外部五seed audit既用原feature/roles又机械 recalibrate eachmodelhealthy score，这是合理事后稳定性描述，不能标为新的 untouched test。当前环境sklearn1.9.1与历史1.9.0的差别已披露，saved scores的对账不等于全部stochastic fits在当前runtime字节复现。

### §5.3 时间顺序、工况与源增强

主方法故障每block报警数为 `[0,0,0,5,7,11,25,48]`；健康为 `[0,0,0,0,0,0,0,1]`。因此48/48any与前四块5/192=2.60%、5/48any=10.42%的差异是真实且有部署解释价值。late alarms不代表实验测出了fault-onset latency；故障记录里的故障已存在，健康RPM只作matching-load proxy。主稿这些限定正确。

位置AUROC独立重现B0–B7为0.5260、0.4531、0.7344、0.8542、0.9115、0.9583、1、1，等权均值0.8046875。它说明 pooled across time可能压低这一 observed ranking，不修复负载支持或交换性，不作为改阈值理由。association with block/time/frequency/RPM proxy不是速度的孤立因果效应。

负载逐项 detection为56.25、35.42、27.08、18.75、18.75、16.67、14.58、12.50%，endpoint decline陈述支持。turn-phase范围及无单调性不能作severity-response证明。同家族negative-transfer数字支持，但其解释必须执行R2；主方法vs source covariance也同时改变aggregation/ridge，稿件已承认不能归因于source inclusion单因素。

### §5.4 几何、重采样与瞬态

所有448score的reconstruction最大误差3.638e−12、contribution sum最大7.276e−11证明保存几何被重建，不证明其fault-relevant。cross-term allocation非唯一、可以负、非causal重要性的解释正确。R3/R4/R13修订后可以保留图6为bounded诊断；无需feature重加权。

source resampling arm未救援主结果支持，但应执行R11。次级21recordprimaryparser0/21、no detector scores、postrepair12/12与4/9并保留80%gate失败是科学完整性的重要优点。8/176、9/176、每方法0/60及0/120都从window rows重现；缺陷是R9的方法说明，而不是这些分母。

### §6–7 讨论与结论

主稿明确one externalmotor、single sourcehealthy acquisition、turnphase混杂、unmatchedpooledAUROC、causalnonidentifiability、offline以及没有safety/prognosis/severity/embeddedclaim，科学边界稳健。部署建议应保持“建议核查/需新独立证据”的地位，不能变成已实验验证的补救方案。原primaryfailure不能被Paper3改进或者瞬态parser修复覆盖。

“useful result is reproducible ranking reversal”可以保留，建议标出具体primary↔targetMCD，以及reproducible指savednumericalevidence可对账。论文没有证明所有PMsM负载/设备的transfer同样失败；这项局限不能通过同一揭盲数据更多seed或label-driven窗口优化解决。

### 补充S0–S11总体

S0的证据身份矩阵有价值，需修R1/R6措辞；S1为准确重建应补R2/R14。S2保留完整11候选避免选择性展示，应加R5/R10。S3的pairedrecords和covariance差别限定有价值，需R8。S4已列每prefix分母和first-alarm proxy，有价值，需R12。S5保留所有seed与无稳定性gate，不选优，需R6。S6的数据对账准确但统计量含义需R3/R4/R13。S7无救援控制应收紧R11。S8hashregistry/不可作总体保证边界清楚。S9失败历史正确，补R9。S10保留探索性失败假设、12s不随看到6s高点而换、blockq90未选都合理。S11说明rawlicenses、originalJEEThistory和未publicrelease，没有冒充完整历史runtime或当前公开注册。

## 4. 审稿人最可能追问的五个问题及现有可回答范围

1. **“你是否把所有标签都隔离了？”** 外部faultlabels在冻结拟合/选择前隔离；sourcefaultlabels参与开发λ，KAIST探索faults也被看过。答案必须分层，不能只答“healthy-only”。
2. **“MCD优势是不是不同featuremask造成？”** 当前对照不能分离QRmask、样本数和sourceaugmentation本身；需如实披露pipelinecontrast。不能用已揭盲数据重新设计mask后替换确认结果。
3. **“95%区间和p<.001是否足以证明跨机器效应？”** 不足。它们是观察条件下的record-reweighting摘要，没有多台独立外部机器，也没有验证记录独立性。48record或384block都不是motor replication。
4. **“AUC高、record-any100%，为何叫失败？”** 主alarm在早期运行点漏报，primary全block25%且H1失败；AUROC/record-any和部署alarm目标不同。AP又受92.31%faultprevalence影响。
5. **“为什么不修好瞬态后改用第三数据集确认？”** 0/21失败已发生；repairpost-reveal且20kWgate失败，只剩一个motor sensitivity。正确处理是保留失败与单机描述，不能补上一个成功故事。

这五题可由当前产物和准确披露回答。额外独立motor/session才能解决的限制应留为限制，而不是扩大本次投稿前任务。

## 5. 建议的修订关闭标准

- 完成R1–R4的正文和紧邻表/图注修订；R5–R14用补充方法/表脚/一句限定关闭。
- 不改变任何冻结参数、记录、分母、seed主选择、主要数值或图的科学数据；原protocol和first-reveal输出保留。
- 由另一人/作者核读“健康-only定义”“pipelinecontrast”“pooledfeatureAUC”和“secondary26dim/windowprotocol”四处，确认全稿/cover/supp表述一致。
- 稿件文字改动后重建DOCX/PDF；实际复核变化页，不以本轮纯方法审查代替版式验收。
- 作者尚须对自身信息、声明、贡献与AI辅助范围作最终事实确认。统计审稿不能替作者签署批准事实。

本报告没有请求或授权新实验。完成上述披露修改后，本轮所发现的问题可在保持科学历史与负结果的前提下关闭；单外部电机及非独立记录的限制继续存在。
