# Paper 1 / JOM 逐段文字与论证审稿

审阅日期：2026-10-09。本报告审阅的是本次源稿快照：主稿全部643行、补充全部782行、cover全部63行，并为两项指标/比较解释只读核对了现有实现及保存的 metadata。**没有重训、没有选 seed、没有改变任何冻结结果或源稿。** 这是内部模拟审稿意见，不是期刊接收预测或作者最终批准。

## 总体判断

当前稿件已经把外部25.00%失败、1/32健康报警、15.74%上界未过12% gate、单外部物理电机、seed波动、事后诊断与0/21解析失败放在读者可见位置，不能说只保留了95.71%的好结果。问题和结果总体一致，也没有把MinCovDet升格为新主方法。不过，**在提交前仍应修正三处会影响读者理解研究身份的实质表述**：healthy-only与使用源故障标签选ridge的关系；MinCovDet配对比较的26/27维差异；单特征AUROC被写成“matched”的指标身份。它们可以通过忠实补充已有实现与结果的说明解决，不需要新增模型或实验，更不能重算一个更好看的确认结果。

工程贡献是：在明确的源/目标健康分工和固定报警协议下，相关电机族上的高检出并未保持到新实验室的一台双三相PMSM；记录任一报警率会隐藏大部分早期轨迹未报警；加入源健康参考的整条处理流程可能劣于目标健康基线。这样的失败报告具备PMSM电磁信号监测的具体内容。其局限同样明确：它是一个可追溯的跨数据集失败案例，不能代表所有PMSM的总体排名或适用工况边界。

优先级含义：**A**为投稿前应修的研究身份或指标解释问题；**B**为有实际审稿价值的方法清晰度/结构修订；**C**为较小文字优化。作者声明占位另见 `Author_Finalization_Map.md`，本报告不把尚未确认的事实填成“无”或“已批准”。

## A1. Healthy-only 的定义需要与源故障标签选ridge明确区分

**位置及原句：** 主稿§4.1，264–265行：“The ridge fraction λ=0.01 was selected in source-only nested pseudo-target validation ...; target faults did not select it.” 标题、摘要、§1、§4又多次使用 healthy-only。

**问题：** “source-only”说明的是电机来源，不说明标签使用。当前读者容易理解为全部开发和超参数选择均只用健康样本。实际 `scripts/select_log_covariance_ridge.py:88–91、122–128` 用源电机已标注故障的检出率和健康误报率构成 `mean_detection − 2 × mean_far`；每个外层目标被排除在这个嵌套选择之外。这不违反外部故障封存，但不等于完全无故障标签的开发流程。仅说“target faults did not select it”不够。

**建议英文：**

> Here, healthy-only refers to fitting the reference distribution, normalization, and target alarm calibration without target fault data. Development was not fully unsupervised: the ridge was selected by nested validation on the source motors using their labeled faults and held-out healthy blocks. The objective was mean source fault-block detection minus twice the source healthy false-alarm rate; the outer target motor was excluded from each selection. The selected value, 0.01, was frozen before external fault access.

主稿§1首次使用healthy-only时给一句简短定义，完整目标函数放§4.1或补充。保留KAIST目标故障在开发中已被检查、所以整个KAIST结果为exploratory的既有披露；“外层选ridge排除目标”不能被用来重新宣称KAIST整体未触碰。此处应改披露，**不改ridge、结果或原冻结协议**。

## A2. 同一估计器家族不等于固定了MinCovDet有效特征掩码

**位置及原句：** 主稿§4.2，291行：“Every method uses the same representation ...”；300–301行称MinCovDet用健康fit行的QR去冗余；§5.3，452–457行：“The clearest transfer contrast holds the estimator family fixed ... This supports conditional negative transfer from source augmentation ...”。补充S3.2、S0技术摘要也使用同类解释。

**保存证据：** `results/external_pmsm_validation/run_metadata.json` 的 `oneclass_diagnostics` 在两子系统均显示：target-only MinCovDet 60个fit行、26个有效特征、丢弃`rms_ratio_c`；source+target MinCovDet 240个fit行、27个特征、没有丢弃项。`results/external_seed_sensitivity/fit_diagnostics.csv`保留相应fit审计。特征筛选是预先实现、只读健康fit行的机制，并不是事后用故障标签筛选。

**问题：** 39.84个百分点差异确实是两个冻结配置的观察差异，但除了源行加入，样本数和健康数据确定的有效维度也不同。将其写成固定表征下源信息的净因果作用，或据此单独归罪于源健康信息，会超出比较。

**建议英文（方法）：**

> All methods start from the same 27 input features and share the target calibration and alarm rule. MinCovDet additionally applies the preimplemented healthy-fit-only rank selection. In each external subsystem, target-only fitting retained 26 features from 60 rows, whereas source-plus-target fitting retained all 27 from 240 rows; the target-only mask excluded `rms_ratio_c`.

**建议英文（解释）：**

> The paired MinCovDet configurations belong to the same estimator family but differ in training rows and the resulting rank-selected feature mask. Their 39.84-point gap describes the effect of the frozen source-augmentation pipeline as a whole; it does not isolate the causal contribution of source information.

摘要最后两句、§6和补充Technical summary应使用同一限定。可保留“conditional negative transfer”，但第一次出现应解释为此冻结处理流程的检测下降。**不要事后强行统一掩码再包装为原比较**；那属于新分析。原10个比较器、原主方法和全部数值保留。

## A3. 单特征AUROC是共同支持上的pooled统计量，不是配对条件AUROC

**位置及原句：** 主稿§5.4，467–470行：“Electrical fundamental frequency had matched single-feature AUROC 0.5038 ...”；Fig.6图注636–639行：“Post-reveal matched single-feature discrimination ... Matching uses ... corresponding block/subsystem position”；补充S6，374–378行。

**实现核对：** `scripts/analyze_external_feature_drift.py:557–567`将限定负载集合内健康和故障的record-subsystem-block特征均值直接送入`roc_auc_score`。在all-block汇总中，这是64个健康单元对384个故障单元的**pooled** AUROC，含跨块位置/负载的排序比较；不是只在一一匹配的健康/故障对内求AUROC。590–605行的差值与`d_z`才使用按load、subsystem、block的多对一配对。方向自由AUROC实际定义为`max(AUC, 1−AUC)`。

**另一范围差别：** AUROC部分限于四个held-out healthy loads，384个故障**子系统块**来自该四负载；fault contribution share部分汇总八个负载的384个故障**物理系统块**获胜窗口。两个“384”代表不同单元和范围。当前caption没有把这一区别说清，容易被理解为完全相同单元上的直接比较。

**建议英文：**

> Single-feature AUROCs pool record-subsystem-block means over the four held-out healthy loads, with common load and block-position support. They are not pair-conditional AUROCs. The reported direction-free value is max(AUC, 1−AUC); matched differences and d_z separately use the corresponding load, subsystem, and block position. Frozen-score contribution shares instead average winning-window absolute allocations over system blocks, using all eight fault loads and the held-out health loads.

§5.4把“matched single-feature AUROC”改为“pooled single-feature AUROC on common load support”。图注应区分pooled方向自由AUROC、matched `d_z`与winning-window贡献。**现有Fig.6图轴已经分别标明AUROC和matched `d_z`，无需为了这项文字修订重绘或重算图。** 0.5038、18.07%、38.54%、harmonic值均保留。

## B1. 电磁特征目前只有名称，欠缺最必要的计算定义

**位置及原句：** 主稿§4.1，242–244行列举“sequence ratios, normalized harmonics, sideband ratios ...”；补充S1第120行给27个代码列名。

**问题：** 电流不对称与谐波是JOM读者判断物理合理性的核心，但代码列名不能说明FFT处理、频率搜索、sequence方向约定或sideband所指。读者也可能把`sequence_unbalance`理解成固定负序/正序比，而当前实现是两旋转序分量模的较小值/较大值，处理相序方向不确定。

**建议：** 在补充新增一个短S1.2定义表或两段文字，主稿只加一处指向。依据现有 `signal_features.py`写清：每相去均值、Hann加窗、实FFT及幅度归一；0.2 s给5 Hz离散频点；20–500 Hz内三相平均谱幅最大点为fundamental；2–5次谐波取最近频点并按同相基波归一；lower/upper sidebands在0.75/1.25倍fundamental附近；sequence ratio是`min(|I1|,|I2|)/max(|I1|,|I2|)`；RMS ratio以三相平均RMS归一。不要改成更好的order tracking，也不要将FFT频点值叫准确测得转速。

还应说明源/目标robust scale的1.4826×MAD及近零时std/1.0回退（见`external_validation.py:18–35`与`baseline.py`），定义式中的`r_m`目前仅叫“robust scale”。这是一项再现文字补全，不是新方法。

## B2. 报警规则应明确严格大于阈值及ties

**位置及原句：** 主稿§4.3，315–318行：“An alarm occurs when p_b≤0.05 ... Both implemented thresholds are calibration maxima ...”。

**问题：** 用最大值作为阈值时，读者容易实现`A≥max(calibration)`；当前p值公式使用`A_j≥A_b`计数，所以与最大值相等不能报警。这个一字符差别会影响再现。

**建议英文：**

> With 20 or 24 calibration blocks, this rule is equivalent to A_b exceeding the calibration maximum strictly. A score tied with that maximum is not alarmed.

不修改实际阈值，不把p值的算术分辨率解释成覆盖保证。

## B3. Bootstrap“95%”应明确是描述性重采样区间

**位置及原句：** 主稿§5.2，391–396行“95% ... record-bootstrap interval”；§4.3，330–335行；补充S3有大量极小bootstrap/Holm p值。

**问题：** 正文已说明单电机和依赖，但普通“95% interval / p”仍可能被当作有效总体覆盖或跨电机显著性。记录位于一个固定turn–phase×load网格，完整记录重采样比窗口重采样合理，却没有证明这些记录是独立同分布抽样。Holm不会消除这一依赖。

**建议：** 第一次定义为“descriptive 2.5th–97.5th percentile record-bootstrap interval”，后面简称“descriptive bootstrap interval”；在补充S3说明名义p值和多重调整仅为此重采样方案的诊断汇总，未验证其在本依赖结构下的频率学覆盖。继续给原区间和p值，不把它们升级成总体证据，也不需要删除所有统计量。

## B4. “Ranking reversal”需要明确是哪两个配置的排名

**位置及原句：** §1，80行“exposes a ranking reversal”；§5.2标题；§7，553行“this reproducible ranking reversal”。

**问题：** 主方法在KAIST并非检出率最高的全部11方法；target Isolation Forest为97.56%，source+target Isolation Forest为96.07%。当前“ranking reversal”是Log-Euclidean相对target-only MinCovDet从95.71% vs89.82%到25.00% vs70.05%的倒转，不能暗示总体冠军换位。KAIST双方health gate也不同。

**建议英文：**

> The ordering of Log-Euclidean and target-only MinCovDet reversed: their exploratory KAIST detection was 95.71% and 89.82%, respectively, whereas external detection was 25.00% and 70.05%. This is a protocol-specific pairwise reversal, not evidence that either estimator is universally best.

这句话可置§5.2或§6，不再重复全部表格。保留原primary designation。

## B5. 贡献分解的记号、归一及解释要比“特征权重”更精确

**位置及原句：** §5.4，465–466行：“For precision matrix P, the contribution allocation c_j=x_j(Px)_j sums to x^T Px ...”；§6，505–508行“shows ... a strong operating-point direction ...”。

**问题：** §4的`x`是原始特征、`tilde x`才是target-standardized坐标。这里换回`x`容易让读者误解用原始量分解。报告百分比也不是`c_j/s`，而是每个获胜窗口`|c_j|/Σ|c_k|`再取均值，允许有负贡献；单变量分离度高而绝对份额低并不能证明该特征对阈值决策没用。

**建议：** 统一使用target-standardized坐标记号；在S6明确absolute-share分母与平均顺序。主稿可写：

> The allocation is consistent with an operating-reference mismatch, but low absolute allocation does not prove that a feature is irrelevant to the multivariate decision. The decomposition is coordinate dependent and was not used to select features.

§6把“shows”改为“is consistent with”，保留已有非唯一/非因果限定。重构误差3.64×10^-12只证明实现复现，不证明物理解释因果成立。

## B6. 采样率控制排除的解释范围应收窄

**位置及原句：** 补充S7，484–486行：“These results do not support source/target sampling-rate mismatch as the primary explanation ...”；§6，508行“narrows a plausible explanation”。

**问题：** 从100 kHz降采样到10 kHz控制了本提取器的采样率差异，但没有同步传感器、模拟滤波器、控制器、噪声与测量链。一次未改善结果不能排除所有测量域因素。主文当前说“under this pipeline”较稳妥，补充结尾更强。

**建议英文：**

> Matching the nominal source sampling rate by this resampling procedure did not recover performance. It narrows the nominal sampling-rate explanation under the fixed extractor, while leaving other acquisition-chain differences unresolved.

保留24.74%、0.6331和1/32；不增加第二个降采样参数或滤波器搜索。

## B7. 主稿仍有与科学读者无关的项目内部指令

**位置及原句：** §6，518–520行“Later-paper improvements cannot be used to rewrite the Paper 1 ...”；§5.4，490行“neither restores a third validation dataset”；补充S11，777–782行包括JEET、作者身份/版权/投稿途径“not asserted by this draft”；cover，42–43行留有上传类别待查句。

**问题：** 保留历史与作者责任很必要，但这些句子像给制作团队的操作要求，削弱科学叙事。尤其补充称identity/funding不被asserted，已经与已填姓名、单位及作者确认无经费不同步。它们不应以制作交接语言出现在最终期刊内容里。

**建议：** §6用“Any subsequent adaptation would constitute a separate exploratory development and requires untouched validation.”表达科学边界；次级结果用“provides post-reveal descriptive evidence only”表达身份；JEET、Paper 1–4项目名称和版权签字交接移至内部审计。补充仍应保留internal Git非外部注册、冻结/事后身份、原协议留档、环境版本和数据来源。未确认作者字段/批准目前继续保留，不能为清稿而提前声称完成。

## B8. 结果叙事可以更集中，避免重复完整表格和防御性解释

**位置：** Introduction后三段与§2.2重复cross-machine、target-only、conformal边界；§5.1同时有11行Table II、Fig.2及多项bootstrap数值；§5.4把几何诊断、降采样、次级失败放在一小节；S0同时有status表、reviewer-question表和Technical summary。

**问题：** 主线是外部固定报警失效，读者在到达§5.2前需要穿过大量开发/审计细节。正文中6.61、5.42、-0.36等KAISTbootstrap差异对外部论点贡献有限，补充已经完整给出。S0的“Reviewer question”不像正式补充方法标题。

**建议结构，不增加篇幅：**

1. Introduction保留物理问题、为什么目标健康基线必要、研究问题与三项贡献；§2.2合并重复文献综述或缩至一个校准边界段。
2. §5.1保留1608/1680、0/42、89.82%配对反转背景及“not best overall”说明；将两组三位区间的解释只留S10，不删除失败或低severity非单调结果。
3. §5.3以“early trajectory coverage”与“source-augmentation pipeline”两个短段落明确区分观察。
4. §5.4保留支持诊断的关键现象，次级0/21失败另设短段或小标题，详表继续S9。
5. S0的诊断目的表改为“Diagnostic purpose, data boundary, and interpretation”，保留预/事后身份，删去“JOM revision / reviewer question”制作语气。

主稿无需大改成全新算法文章；也不必为了压页数删掉外部25%或科学局限。

## B9. 次级12方法与主评估11方法的范围应解释

**位置及原句：** 摘要21行“eleven detectors”；补充S2标题11方法；S9.2表582–593行12方法，包括独立的“Target Log-Euclidean covariance”。

**问题：** 全文读取后能看到范围不同，但第一次读S9会怀疑漏报或新增事后比较器。原次级协议120–127行已经冻结12方法，target log-ridge是其额外控制，所以无需新增或删除结果。

**建议英文：**

> The secondary protocol specified twelve configurations, including a target-only log-ridge covariance control in addition to the eleven configurations of the primary two-dataset evaluation.

放S9.2表前。全文“eleven”限定主评估；次级0/21冻结失败仍是首要结局，后12配置都是repair后敏感性结果。

## C类：逐句语言与术语建议

| 位置 / 当前文字 | 具体问题 | 建议 |
|---|---|---|
| 标题：“Frozen Cross-Dataset Reliability ...” | 被freeze的是评估协议，reliability本身不是冻结对象。标题目前可理解，属可选优化。 | 可用“A Frozen Cross-Dataset Evaluation of Healthy-Only PMSM Stator-Fault Detection”；若保留现题，摘要明确frozen protocol即可，无需为了改题连锁重命名。 |
| 摘要20–21：“a PMSM changes ... measurement domain” | motor变化与数据集/测量域变化混在一起。 | “Current-based healthy-only alarms may not retain reliability across motors, operating conditions, and measurement domains.” |
| 摘要29–30：“same-estimator controls reveal ... negative transfer” | “reveal”略强；A2掩码差异不能隐藏。 | “Paired estimator-family configurations show reduced detection under the frozen source-augmentation pipeline.” |
| §2.2，128–130：“Keeping the algorithm ... common” | 所有11算法当然不同；这里应限定同一family pair的比较。 | “Within an estimator-family pair, the shared input definitions, target-health allowance, calibration set, and alarm rule aid interpretation of source augmentation; fit-derived masks are reported separately.” |
| §4.1，244：“scale-free” | 内部命名，仍含有量纲的频率；已披露但第一次阅读会误会。 | “the frozen 27-feature arm, historically named scale-free”或“predominantly amplitude-normalized arm”；保留频率事实。 |
| §4.2，305及Supplement大量“Proposed” | 容易误导成新算法优越性；表/图为历史label已解释，原artwork应保留历史。 | 正文统一“primary Log-Euclidean”；补充首次写“Primary Log-Euclidean (archived label: Proposed)”后以Primary简称，表中历史label可保持。 |
| §5.2，396：“sole primary-seed method” | “primary”既指主方法又指seed，使句子一瞬间难解。 | “the only method that passed H1 at the prespecified seed”。 |
| §5.3，440：“Spearman associations of ...” | 缺相关系数符号，易被误认为p值。 | “Spearman rank correlations (ρ) were ...”；不添加未计算的p值。 |
| §5.3，447：“declined from ... to ...” | 两端数值可描述，不能顺带变成独立负载因果或普遍单调关系。 | “Detection was 56.25% at 0 N m and 12.50% at 35 N m ...”；继续保留load-resolved图及因果边界。 |
| §5.4，464：“all 448 frozen primary block scores” | 448包含健康fit/calibration/test与fault；读者可能把它当384fault分母变动。 | 补“across all 56 records”；主fault endpoint仍384，held-out health仍32。 |
| SupplementS6，375：“eight largest direction-free ... AUROCs” | 两列raw/robust-z，排序指标不明。 | “the eight largest robust-z direction-free AUROCs”；各指标定义参考A3。 |
| SupplementS6，385：“Matched robust-z dz” | 未定义标准化差值的分母。 | 定义`d_z = mean(paired differences) / sample SD(paired differences)`，注明复用健康单元、不作独立样本效应推断。 |
| §7，552–554：“concrete deployment failure boundary” | 并未估计精确的可部署工况边界。 | “a documented failure of this alarm protocol under a compound cross-dataset shift”；仍可讨论部署前注意事项。 |

## 标题、摘要、结论及JOM适配的审阅结论

- **标题与问题：** 当前题目准确指向跨数据集可靠性，不声称新算法；“Frozen”修饰位置可优化，但不是科学硬阻碍。Healthy-only定义必须落实A1。
- **摘要：** 124词、6关键词，包含内部95.71%与外部25%、1/32、15.74%>12%、target-MCD70.05%和3/5seed gate，比例取舍正确。修A1/A2用一句定义或精准最后两句，并重新计数保持100–150词；不应为缩摘要隐藏失败。
- **研究贡献：** 定位为电流信号与健康迁移的alarm reliability case study是可信的。多算法公平协议、失败轨迹、同类目标基线比“新SOTA”更有信息。A2要求把公平理解为共同目标健康预算与报警规则，而非所有有效特征、训练量完全相同。
- **JOM范围：** 文章涉及PMSM定子短路、电流不对称、谐波/电磁监测，具有具体机器背景；不是只把通用ML换一个数据集名称。改B1能让电磁诊断读者理解实际提取器。Park2025同刊文献在§2.1被限制为绕线同步机FEM/current-stray-flux背景，未冒称PMSM跨机实证；不需要硬加更多同刊引用。
- **结论边界：** 已写单外部电机、fault phase/turn confounding、AUROC unequalload、非因果、离线和非总体安全。主要再收窄“reproducible ranking reversal”“boundary”“explains failure”的措辞。缺少独立电机不是此次改稿可消除的缺点，应继续如实声明，不能以更多seed、特征试错或Paper3结果顶替。

## 最小修改验收建议

先修A1–A3及B1–B3，这些直接影响诚实、可再现的理解；选择性采用B4–B9与C类句子，不需要大规模重写或扩大研究。修改后检查摘要/§1/方法/§5.3/结论/cover对healthy-only和source-augmentation含义一致；主稿Fig.6、补充S6与实际CSV对AUROC及贡献范围一致；原11/次级12方法范围清楚。

保持所有冻结数字、原主方法、lambda0.01、原输入/窗口/健康角色/阈值/seed不变。仅新增的披露不能被标成新冻结分析。重新构建和渲染变化页面；作者批准、COI、致谢、权限和AI责任仍等待真实确认。完整声明缺口与portal/版权/费用问题使用现有作者映射和指南，不混入科学实验要求。

## 审阅快照

| 源 | SHA-256（2026-10-09 15:15 KST只读核查） |
|---|---|
| `submission/jom/manuscript.md` | `3f65952fa7ccf149f627bbc71a8a0c8599c2d8bb1e5db57d57edec61de17e377` |
| `submission/jom/supplementary.md` | `c18e669e2f353390cbdf0925b97d79914d402aae81a7f376743ae47a6d1672c2` |
| `submission/jom/cover_letter.md` | `e7d8a3286e0178dfc5f422bb461c475fc6a5d2e422b6caf412a3882dafa980db` |

本报告的行号与原句对应上述快照；父任务随后整合的修订应另记录，不将这份意见改写成此前稿件已经通过。
