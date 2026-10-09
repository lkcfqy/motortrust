# Paper 1 方法审稿修订复核

日期：2026-10-09。复核者为上一轮独立方法/统计审稿代理。本文件逐项回应 `Detailed_Review_Methods.md` 的 R1–R14，属于对最新正文、补充材料与 cover letter 的只读审查；没有编辑这些源稿，也没有重拟合任何模型。

**结果：R1–R14 均已实质关闭。** 修订补足了先前遗漏的方法选择边界、实际拟合维度、统计量分母、依赖条件和次级协议，而没有改变主方法、冻结数据、主要数字或研究历史。本结论不是“论文所有科学局限消失”或“可直接上传”，也不替代作者信息/声明确认与新版 PDF 的视觉检查。

## 读取的最新源稿

| 文件 | SHA-256 |
|---|---|
| `submission/jom/manuscript.md` | `b4cad5240b5071183fa5f35accdfca28fa4896f029e9ff386180278089a9a687` |
| `submission/jom/supplementary.md` | `ed12fa7a655c4eff99571cd90dec20f118a7f3c130a536b8b56b9558f1d2e53d` |
| `submission/jom/cover_letter.md` | `db0c60b8dcffc1b2f864b4a2d2a0ae993e6e6a51104af845b363676cbb710a29` |

行号基于这些读取版本，后续排版文字变动可能移动行号；以章节和所引短句定位。

## 逐项关闭证据

| 编号/原严重度 | 最新措辞与位置 | 核验与关闭判断 |
|---|---|---|
| R1 / P1：健康拟合与源故障选参 | 主稿 §1 L55–56：`healthy-only describes reference fitting, normalization, and target alarm calibration; source-domain development can use labeled source faults`；§4.1 L272–279：`Development was not fully unsupervised`，列出源故障 objective；S1.2 L149–152 同步 | **关闭。** objective 与 `select_log_covariance_ridge.py` 及 12 个候选行一致；0.01 在三个 outer folds 选中。外层 target exclusion、KAIST exploratory 与 external fault-blind 身份不再混淆。 |
| R2 / P1：同家族≠同 mask/样本数 | §4.2 L304、L313–318 报告共同27输入候选、IF `max_samples`、OC-SVM `gamma` 的数据依赖以及 MCD 60行/26维对240行/27维；§5.3 L477–480 明确 `whole, not an isolated causal effect of source information`；S1.2/S3 同步 | **关闭。** 原 metadata 和五 seed diagnostics 都支持两子系统的26/27差别。source-augmentation pipeline contrast 的结论保留，未强制等维重拟合。cover letter 也披露 different fit-derived feature masks。 |
| R3 / P1：feature AUROC 的 estimand | §5.4 L491–498 改为 `pooled single-feature AUROC ... common load support`；S6 L425–432 明确 `not pair-conditional AUROC`，matched differences 才匹配3键；Fig.6 L663–665 分开 AUROC 与 dz | **关闭。** 与 `same_block_feature_effects()` 实现一致。64/384 record-subsystem-block 均值和4共同负载明确；数字0.5038、0.925/0.933未改变。 |
| R4 / P1：图6不同单位/支持 | Fig.6 L663–668 列 64/384 subsystem means 对32/384 system winners、4/8负载差别；S6 L434–439 给 `|c_j|/sum_k|c_k|` 再平均；§5.4 L498 用 `motivate a hypothesis` | **关闭。** 不再将两个摘要当作 ablation。坐标依赖、非唯一、负贡献、非causal以及低allocation不等于irrelevance明确。 |
| R5 / P2：AUPRC背景 | S2 L175–176：`Fault prevalence is 384/416 (92.31%), the no-skill average-precision baseline`，`does not estimate deployed alarm precision` | **关闭。** 384/416=0.923076923，与 AP 输入相同。完整11方法的 AP 数值仍与独立 unique-threshold 重算一致。 |
| R6 / P2：五 seed 的不同冻结身份 | §4.2 L320–321 是 exploratory KAIST list reused for post-reveal external audit；S5 L413–420 明确 list先固定而externalaudit事后、primary20260820、无formalstabilitygate | **关闭。** 与 fddf2f7 的现有五 seed列表及14:37 UTC的external audit metadata一致。没有错误改写成“所有额外seed揭盲后才选择”，也没有把事后外部扩展包装成预注册确认。 |
| R7 / P2：threshold ties | §4.3 L335–337：`strictly exceed`、`A tie ... is not alarmed`；S1.2 L159–160重复精确规则 | **关闭。** 和公式里的 `A_j >= A_b` 及11方法/20seed组保存判定一致。未改threshold或conformal实现。 |
| R8 / P2：bootstrap/Holm推断保证 | §4.3 L351–356：`descriptive record-weighting sensitivities, not calibrated population confidence intervals`、未建立coverage/p validity；S3 L289–297：依赖grid、Holm不移除依赖/不覆盖所有post-revealchoices | **关闭。** percentile intervals与Holm p分开，不再暗示校准总体CI或错误控制保证。全部effect sizes与观察conditiongrid的原statisticalscheme保留。 |
| R9 / P2：独立瞬态协议 | S9 L619–630：αβ→pseudoabc、不可观测zero sequence、26feature/10kHz source、独立fault-current onset、20ms at-or-above与0.2s guard、windowcal；S9.2 L652–657列12配置及176/60/120；L674–676注明首1s record AUROC | **关闭。** 与原secondaryprotocol及code一致。复核还促成一个小精度修正：`continuous exceedance`改为`continuously at or above the threshold`，精确匹配`rms >= threshold`。26维和window-unit差别没有冒充修parser后才做的设计选择。 |
| R10 / P2：source-only仍使用targethealth | §5.3 L481改为`source-covariance reference`；S2 L177–178：training/reference指shape/oneclass，all methods用targetnormalization/calibration | **关闭。** 标题/表内历史methodidentifier `source-only` 可保留，紧邻解释已消除“完全不接触目标健康”的错误理解。 |
| R11 / P2：source-resampling不排除采集链 | §5.4 L501–505用`did not rescue ... under this pipeline`；S7 L546–549列sensor/analogfilter/controller/noise等未解决 | **关闭。** 未用一个机械resamplingarm宣称已排除全部measurement差异，也未新加filter/seed来挽救结果。 |
| R12 / P2：allblock平均/record-any | S4 L302–306：`weights each position equally`，record-any累积机会、latehighscore驱动，prefix是earlytrajectory | **关闭。** 与原8块均权和192/48/16等prefix分母一致；未改变fullinterval主endpoint。 |
| R13 / P2：方向/top-eight选择 | S6 L428–430：`choosing orientation after reveal`、top-eight也用revealedlabels选、`not independently validated feature performance`；正文及Fig6同步direction-free定义 | **关闭。** 没有把同数据筛选摘要升级成预先选feature的独立验证；固定feature和score没有改变。 |
| R14 / P2：robust scale 精确定义 | S1.2 L146–149：1.4826 MAD、`1e-8 times max(|median|,1)` floor、population SD fallback、仍小则1 | **关闭。** 与`np.std(..., ddof=0)`及允许healthyrows的掩码一致。S1.2还明确Hann/FFT、5Hz bins、2–5harmonic、0.75/1.25sideband、sequence orientation、entropy等固定feature规则，足以指向可审代码。 |

这些修订是方法披露与解释范围的关闭，不是相应科学限制被实验解决。特别是 MCD 的 mask/sample差别、不同数据单位、单外部电机和记录依赖仍然存在。

## 实际再次运行的只读证据检查

```bash
/Users/lkc/miniforge3/envs/motortrust/bin/python tmp/jom/detailed_review_methods_checks.py --output tmp/jom/detailed_review_methods_recheck.json
/Users/lkc/miniforge3/envs/motortrust/bin/python -m ruff check tmp/jom/detailed_review_methods_checks.py
```

两条命令通过；将重核 JSON 与上一轮 `tmp/jom/detailed_review_methods_checks.json` 比较，除读取源稿 SHA 外，所有核算/拟合诊断/seed历史内容完全相同。这一只读检查覆盖11外部方法、20方法×seed组、3 KAIST folds、12瞬态方法，未调用 fit。

再次支持的主要锚点：KAIST主方法1608/1680、0/42；外部主方法96/384、1/32、AUROC0.6354167、Wilson upper0.1574426382；MCD269/384、0/32、AUROC0.9267578以及3/5seedgate；首次瞬态无scores、postrepair单200W各method0/60和0/120、主方法8/176/MCD9/176。外部first4与record-any、same-family contrasts和feature geometry的原数字不因写作修订而改变。

## 核查后的残余边界

主稿、补充和coverletter现在对primaryfailure、MCDcomparator身份、internalGit非外部preregistration、oneexternalmotor、unmatchedpooledAUROC、postrevealdiagnostics、完整configuration的源增强对照及offline一致。sourcefaultdevelopment在正文/补充明确；coverletter“fitted and calibrated on healthy currents”与该定义一致，没有说整个development都未看sourcefaultlabels。

没有发现仍未关闭的R1–R14严重问题，也没有发现新数字矛盾。仍须保留并由作者理解：单外部电机/无独立sessions、turnphase混杂、共同shift的因果不可分、bootstrap/Wilson/conformal无总体保证，以及瞬态parserfailure不能被repair覆盖。不能由这次措辞改进宣称population可靠性、embedded/real-time能力或新method优越。

**视觉QA状态：本复核完成时新版补充PDF尚在重建。** 本文件只关闭方法审稿；应按新PNG实际逐页检查，并在本文件下方记录最终PDF/PNG身份与检查结果后再交付作者。
