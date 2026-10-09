# Paper 1 逐段论点—引用详细审查

审查日期：2026-10-09（Asia/Seoul）。审查对象是 [JOM 主稿](manuscript.md)的完整正文；重点逐段检查 Introduction 5 段、Background 6 段、Discussion 6 段，并交叉检查 §3.3、§4.3、§5.3 和摘要中的统计表述。实际阅读版本 SHA-256 为 `3f65952fa7ccf149f627bbc71a8a0c8599c2d8bb1e5db57d57edec61de17e377`。逐段原文、引用键和哈希保存在 [current_paragraph_scope.json](reference_evidence/detailed_support_review/current_paragraph_scope.json)。本报告不修改正文、Word、冻结方法或结果；后续修订需另行核对。本报告补充并收紧原 [Reference_Audit.md](Reference_Audit.md) 的支持性结论，不能把“30/30 元数据通过”理解为“30/30 全文及所有论点均已验证”。

## 审查结论与修订优先级

当前稿件的核心失败叙事与文献并无根本冲突，且已经较好地区分了物理电机、文件、宏块、窗口，以及探索性与冻结外部结果。需要在投稿前处理的主要问题是 **一种特征被另一种特征的文献支持、Wilson 尾部定义含糊，以及多数据集被称作独立复制**。这些都能用精确改稿解决，无须重新调参或扩大实验。

| 编号 | 程度与位置 | 问题、原始证据及建议 |
|---|---|---|
| R1 | 应修；§2.1 第一段，并联动 Introduction 第一段 | `Jeong 2017; Li 2024` 支持负序/电流向量指标，不能直接支持本稿的 **normalized harmonic ratios**。Li 的原文 §3 构建的是负序电流向量模平方的二次谐波；Paper 1 使用的归一化相电流谐波比与它不同。Urresty 的原始研究摘要直接涉及相电流第三谐波、零序电压及变速/变负载 order tracking，更适合支持一般谐波诊断背景。建议拆开两个论点，避免读者以为本稿复现或验证了 Li 的专门指标。 |
| R2 | 应修；摘要、§3.3 与结果第一次定义 | **15.74% 是双侧 95% Wilson score 区间的上端点**。单侧 95% 上限使用不同的 z 值，1/32 时约为 12.86%。当前冻结计算并没有错；含糊的 “95% Wilson upper bound” 容易被读作单侧上限。需写明双侧区间的上端点，保留 15.74%、原 H1 判定及依赖结构免责声明。不可更改冻结规则来使 gate 通过。 |
| R3 | 应修；§2.2 第一段 | “provide broader machine and dataset replication” 超出本轮可核实的支持。Zhao 的原始摘要明确是八个公开与两个自采数据集的 benchmark；多数据集本身并不证明每个结果拥有独立物理电机/独立 session 的复制。Li 的原文详细实验本轮未能取得，只可稳妥支持 collaborative multimachine generalization 已有研究。建议改为存在性描述，不比较“独立复制”的强弱。 |
| R4 | 建议修；Introduction 第一段 | “The healthy reference changes with power rating, winding topology, controller response, sensor chain, speed, and load” 给出一长串确定关系，却没有逐项因果证据。Zafarani 的原始机构摘要支持运行工况、短路路径电阻及控制器动作影响故障指标；本稿只观察复合迁移。建议使用 “can differ across machines and operating conditions”，把额定功率/拓扑/传感链表述为两数据域之间的条件差异，不暗示本稿分别证明其作用。 |
| R5 | 建议修；Discussion 第三段 | “Such development requires a new untouched motor or laboratory test” 会把 **探索性开发** 与 **独立确认** 混为一谈。当前数据可以支持明确标为 post-reveal 的探索性改进；验证改进仍需新未触碰证据。建议将主语改为 “Confirming any such remedy ...”。这是澄清研究边界，不要求本次新增电机实验。 |
| R6 | 可选；Discussion 第二段 | 失败诊断支持建议检查的项目，却尚未验证一套普遍的上线验收标准。“concrete acceptance checks” 可收窄为 “diagnostic checks for future evaluations”。本稿不能从单电机结果给未来部署系统提供普遍充分条件。 |

推荐的可直接审阅英文替换如下；作者或主编辑仍应决定最终合并位置：

**R1，§2.1：**

> An interturn fault changes current symmetry and the relation between phase currents. Sequence and current-vector indicators have been used to detect winding asymmetry [Jeong 2017; Li 2024]. Fault-sensitive current harmonics have also been evaluated using order tracking under changing speed and load [Urresty 2013]. These are distinct indicators; their diagnostic response depends on the machine and operating context [Zafarani 2018].

可保留原段其余变速、采样链与物理—数据模型内容，不需要声称本稿实现了文献中的 order tracking。Introduction 可相应改为：

> Current-based indicators include negative-sequence components, current-vector measures, and fault-sensitive harmonics [Zafarani 2018; Jeong 2017; Li 2024; Urresty 2013].

**R2，§3.3：**

> The predeclared H1 health gate requires the pooled upper endpoint of a descriptive two-sided 95% Wilson score interval to be no greater than 12%, and a maximum per-motor or per-test-load empirical false-alarm rate no greater than 15%.

摘要可压缩为 “Its descriptive two-sided 95% Wilson upper endpoint (15.74%) exceeded the preset 12% gate.” 最终摘要仍应重新核对 100–150 词；本报告不替换原摘要，也不重新定义历史协议。

**R3，§2.2：**

> Cross-machine generalization predates this work. Prior studies address collaborative multimachine generalization and multi-dataset fault-diagnosis benchmarking [Li 2023; Zhao 2024].

**R4，Introduction：**

> Healthy current distributions can differ across machines and operating conditions. The source and external datasets differ in power rating, winding topology, acquisition chain, and speed/load trajectory; the present comparison does not isolate the contribution of each difference.

**R5，Discussion：**

> Confirming any such remedy requires a new untouched motor or laboratory test. Improvements selected on the revealed faults remain exploratory and cannot rewrite the Paper 1 frozen external result.

## 逐段覆盖记录

“支持”指对应的窄论点得到实际可访问的原始来源支持；不等于认可来源的所有结论。“自身证据”指本稿结果/协议的解释，不需要借外部文献冒充实验依据。

| 段落 | 对应论点和引用 | 审查结果与具体边界 |
|---|---|---|
| Introduction P1 | ITSC、负序/向量/谐波；Zafarani、Jeong、Li | 负序与向量背景支持；谐波应分开并用 Urresty；不能把 Li 的派生向量二次谐波等同本稿归一化相电流谐波。复合工况解释需收窄，见 R1/R4。 |
| Introduction P2 | healthy-only 使用情境、公平 target-only 参照、negative transfer；Wang、Kumar | Wang §3 定义必须固定算法，比较 A(S,T) 与 A(∅,T)。Kumar 支持机械故障研究存在负迁移问题，但其 source-free UDA 用伪标签，未证明本稿健康阈值。当前不借其准确率，合理。首句 “must” 可改为 “In this healthy-only setting, ...” 以明确这是本稿情境。 |
| Introduction P3 | DG 与多数据集已有；Li 2020、Li 2023、Zhao | 原始摘要/标题支持存在性。分类 accuracy 与固定报警阈值是不同终点，本稿 AUROC 与 record-any 的提醒属于评估逻辑，且 §5.3 给出具体证据；无需从监督分类文献借用报警保证。 |
| Introduction P4 | 切分和重复单位；Wheat、Roberts、Hurlbert | Wheat 原文明确比较 run-to-run、day-to-day、part-to-part holdout；Roberts 支持依赖结构下的 blocking 原则；Hurlbert 支持重复实验单位原则。当前未借用精确“>40%”数值，也未宣称已量化 KAIST 随机切分偏差，合适。 |
| Introduction P5 | 本稿贡献、冻结历史与失败 | 自身证据；不需要文献证明本稿冻结。内部 Git freeze 不是外部注册预注册，且正文 §3.3 已明确。此段未把 MinCovDet 替换为主方法，保留。 |
| §2.1 P1 | current symmetry、指标、工况、order tracking 与 physical-data；五篇文献 | 需 R1。Li 原文直接承认负序电流幅值受速度和负载影响；Urresty 窄支持变速/负载谐波处理；Li Minglei 2024 支持油钻 PMSM 快速变速诊断背景。没有一篇证明本稿 normalization 已消除漂移。 |
| §2.1 P2 | 同刊 Park 2025 | 原文十页已读；6400 kVA、转子励磁电流和 winding/damper 情境，属于 wound-field 同步机 FEM，不是 PMSM 单健康迁移。稿件已明确该边界。可选补充其 §4.3 stator case 的电流 FFT 未见显著谐波变化，以说明并非任意同步机 ITSC 都有相同谐波响应。 |
| §2.1 P3 | covariance precision 放大正常变化，不保证 invariance | 由 s=xᵀPx 和健康参考逻辑可直接推出“可能”；本稿 §5.4 的分解支持这种解释，但未证明单变量因果。当前否认 phase localization/severity estimation，符合数据的 turn/phase confounding。 |
| §2.2 P1 | 多机/benchmark、频域 DG source emphasis | R3 要收窄“replication”；Liu 2025 的原始摘要明确把源域特征过度强调作为 negative transfer 动机，可支持当前一句。不能从其生成模型推断本稿 remedy 有效。 |
| §2.2 P2 | OC-SVM/IF/MCD/LE 起源及公平比较 | 引用用于算法起源，适当；未借 Arsigny 的 DTI 实验充当电机证据。healthy calibration 是本稿统一评估设计，不能说三种算法原始论文都规定本稿的独立校准方式。Wang §3 更直接支持最后的 same-estimator 要求。 |
| §2.2 P3 | conformal、dependent variants、industrial precedent | 作者 tutorial、PMLR 两篇全文和工业原始摘要支持窄背景。3 s 聚块不是 Chernozhukov 的 block permutation；也没有验证 Barber 的 stationarity/β-mixing。当前明确无 5% population guarantee，应保留。 |
| Discussion P1 | 内部成功、外部失败、target-only 对照 | 自身 §5.1–5.3；95.71% vs 25.00% 与 70.05% 的工程对照成立。topology/chain/load/speed changed together 的写法已避免单因素原因。不能把 LE vs MinCovDet 的差异单独称为 negative transfer；§5.3 的同算法对照才是该判断的根据。 |
| Discussion P2 | late alarms、load coverage、geometry、sampling-rate control | 自身 §5.3–5.4。48/48 record-any 与 96/384 block result 可同时成立；“inflated”在此是终点对照，不是错误计算指控。10 kHz control 未救回只能收窄该 pipeline 中的采样率解释，不能排除其他传感/采样链差异。建议 R6。 |
| Discussion P3 | remedies/future untouched evidence、Paper 3 不能回写 | 边界正确；R5 只澄清探索性开发允许与独立确认条件。增加算法、反复 seed 或同机文件不能创造独立物理电机重复，不需新增文献或强制新实验。 |
| Discussion P4 | fit health vs nominal rank resolution、零报警风险 | §4.3 的有限 rank 算术正确，n≥19 时最小 p≤0.05；n=20/24 只能对严格超出 calibration maximum 的分数报警（有 ties 时保守）。这不建立 exchangeability、独立校准或 5% 风险。0/32 与 0/42 都不等于零部署风险。 |
| Discussion P5 | 物理电机、session、phase-turn、pooled load、intervals、parser | 对应 §3 与 §5；当前完整披露，没有把两子系统/48文件当48电机，也没有将 repaired secondary 当第三确认集。temperature 未独立操作，不应添加因果温度解释。Wilson/record bootstrap 是 recorded conditions 的描述。 |
| Discussion P6 | offline 与实时/嵌入式/安全边界 | 未做 latency/memory/numerical benchmarking 的限制写法准确；0.2 s/3 s 是分析分辨率，不是部署性能测量。Park 等文献的 realtime 表述不可借来弥补本稿验证。无需为了这篇离线可靠性稿强制新增硬件实验。 |

## 原始来源的具体支持与访问层级

以下引用的是**原始作者、期刊、出版社或作者机构**提供的内容。读取层级严格区分：全文或指定原文段落、原始摘要、仅原始元数据。付费/反自动化限制没有被绕过。简短直接引文用于定位，其余为转述。

### 电机信号与同刊文献

1. **Li Dongdong et al. 2024，`li2024negativesequence`，全文。** [IEICE 原始 PDF](https://globals.ieice.org/en_publications/elex/10.1587/elex.21.20240550/_pdf)，§2.2、§3、§5，六页。该文推导相电流不对称造成的负序电流向量，并对向量模平方提取二次谐波；其 §3 明确写 “Since the amplitude of NSC is affected by the motor speed and load”。对应 R1：它不是本稿相电流第三谐波比的直接验证。故障相位估计依赖该模型/指标，不能迁移给当前 phase/turn 混杂数据。本轮浏览工具能读取官方 PDF；普通 requests 下载返回 405，下载记录诚实保留该区别。
2. **Zafarani et al. 2018，`zafarani2018itscreview`，原始作者机构摘要。** [METU 原始机构记录](https://open.metu.edu.tr/handle/11511/41067)，DOI 10.1109/JESTPE.2018.2811538。该文不是纯二手综述，还结合自己的 FEM、drive model 与 testbench；摘要支持故障指标随 fault intensity、operating conditions、short-path resistance、controller action 改变。未在本轮取得期刊全文，所以不声称全文核对过某个传感器/额定功率因果结论。
3. **Jeong et al. 2017，`jeong2017negativesequence`，原始元数据/作者机构发表记录。** DOI [10.1109/TIE.2017.2677355](https://doi.org/10.1109/TIE.2017.2677355)。本轮 IEEE 全文受限，作者机构记录支持题名中的 early-stage negative-sequence diagnosis；未独立全文核实“归一化谐波比”或全部速度鲁棒结论。相关页面里的后续论文摘要不能当作 Jeong 原文。这是支持审查的访问限制，不能以元数据通过掩盖。
4. **Urresty et al. 2013，`urresty2013nonstationary`，原始作者上传的论文摘要。** DOI [10.1109/TPEL.2012.2198077](https://doi.org/10.1109/TPEL.2012.2198077)，[作者提供的原始研究记录](https://www.researchgate.net/publication/230757856_Diagnosis_of_Interturn_Faults_in_PMSMs_Operating_Under_Nonstationary_Conditions_by_Applying_Order_Tracking_Filtering)。该研究的相电流第三谐波与零序电压分量使用 Vold–Kalman order tracking，在变速与不同负载下评估。只以此支持一般谐波/工况背景；本稿没有 voltage 输入，不能说实现或验证了完整方法。本轮全文链接未取到，报告不称全文复核。
5. **Li Minglei et al. 2024，`li2024physicaldatapmsm`，原始出版社摘要。** [出版社页面](https://www.sciencedirect.com/science/article/pii/S0952197624000964)，DOI 10.1016/j.engappai.2024.107938。背景为高温油钻、快速变速与稀疏真实故障样本的物理—数据方案；支持 varying-speed diagnosis 的存在，不支持健康-only 告警概率、无故障标签迁移或嵌入式能力。
6. **Park, Harmony, Baek 2025，`park2025electromagnetic`，官方全文。** [JOM 原始十页 PDF](https://www.magnetics.or.kr/upload/jom/upfile_260106095352151.pdf)，DOI 10.4283/JMAG.2025.30.4.596。Table 2、模型说明与 §4.3 分别支持 wound-field 同步机条件及 stator fault 的电流/stray-flux 对照；§4.3 写 “FFT analysis did not reveal significant changes in the harmonic content”。因此它适合作同刊电磁监测背景及信号可辨识性依赖情境的例子，不适合证明所有 PMSM ITSC 谐波必然增大。不能借其实时用语替本稿离线分析作部署证明。

### 迁移与验证

7. **Wang et al. 2019，`wang2019negativetransfer`，原作者全文版本。** [作者 arXiv v4 PDF](https://arxiv.org/pdf/1811.09751)，§3、PDF 第2页，式 (3)–(4)；[CVF 原始发表页](https://openaccess.thecvf.com/content_CVPR_2019/html/Wang_Characterizing_and_Avoiding_Negative_Transfer_CVPR_2019_paper.html)。核心要求是固定算法比较有/无源数据，原文写 “one should focus on a specific algorithm at a time”。本稿 MCD 与 IF 成对对照满足这个逻辑；LE 与 MCD 的跨算法差距不能单独识别 source inclusion effect。本轮阅读的是作者全文，旧 Reference_Audit 的 §2 locator 应改为 **§3**。其定义使用 expected target risk，本稿只声称 observed/conditional negative transfer，边界适当。
8. **Kumar et al. 2024，`kumar2024negativetransfer`，原作者机构摘要。** [NYCU 原始记录](https://scholar.nycu.edu.tw/en/publications/mitigating-negative-transfer-learning-in-source-free-unsupervised/)。mean-shift/cosine pseudo-label 与 weight-aware regularization 用于 source-free UDA；可支持 machinery negative transfer 已有研究，不可把监督分类/伪标签准确率当作本稿健康阈值性能。
9. **Li et al. 2020，`li2020domaingeneralization`，出版社原始摘要。** [原始出版社页面](https://www.sciencedirect.com/science/article/pii/S0925231220308092)，DOI 10.1016/j.neucom.2020.05.014。source augmentation、adversarial features、metric learning 与 rotating-machinery 数据支持 DG 已有方法；不提供本稿所需的 target-health false-alarm 验证。
10. **Li et al. 2023，`li2023causalconsistency`，原始题名/元数据，本轮详细全文受限。** DOI [10.1109/TII.2022.3174711](https://doi.org/10.1109/TII.2022.3174711)。仅以题名及原审计支持 collaborative multimachine bearing generalization 已有研究。搜索得到的第三方“6 machines/43 bearings”摘要未当本轮 primary evidence；不引用其精确实验数或独立 session 假设，建议 R3。
11. **Zhao et al. 2024，`zhao2024dgbenchmark`，原作者机构摘要与原作者代码。** [Politecnico di Milano 原始记录](https://re.public.polimi.it/handle/11311/1278084)，[作者 benchmark 仓库](https://github.com/CHAOZHAO-1/Domain-generalization-fault-diagnosis-benchmark)，DOI 10.1016/j.ress.2024.109964。八公开、两自采数据集支持 benchmark 的范围；数量不等于当前研究所要求的独立物理电机或独立 session 重复。没有借其 benchmark 精度比较本稿 AUROC。
12. **Liu et al. 2025，`liu2025frequencyguided`，出版社原始摘要。** [原始出版社页面](https://www.sciencedirect.com/science/article/pii/S0263224125003483)。摘要明确认为 regularization 对 source features 的过度强调可能导致 negative transfer；频率指导的 latent-diffusion/reconstruction 是其方案。故当前 source-emphasis 背景句有依据，不能说本稿几何分析验证了其生成模型。
13. **Wheat et al. 2024，`wheat2024dataleakage`，原作者全文。** [McMaster 原始 PDF](https://macsphere.mcmaster.ca/bitstream/11375/31458/1/Impact_of_Data_Leakage_in_Vibration_Signals_Used_for_Bearing_Fault_Diagnosis.pdf)，摘要、§I、§III；DOI 10.1109/ACCESS.2024.3497716。六个 bearing pipelines、两数据集和 run/day/part holdout 实验支持切分改变实测性能。稿件当前不借其具体跌幅，不把其轴承实验直接当 PMSM 效应大小，适当。
14. **Roberts et al. 2017，`roberts2017structuredcv`，原始出版社摘要。** [Ecography 原始页面](https://nsojournals.onlinelibrary.wiley.com/doi/abs/10.1111/ecog.02881)。temporospatial/hierarchical dependence 支持 structured CV；原文也提醒 blocking 可引入外推而改变评估目标。因此可支持为何需要清楚 holdout unit，不能说任意 blocking 都自动无偏。当前窄句没有该过度保证。
15. **Hurlbert 1984，`hurlbert1984pseudoreplication`，原始摘要及原文大学托管扫描。** [出版社记录](https://esajournals.onlinelibrary.wiley.com/doi/10.2307/1942661)，[UCF 托管原文](https://sciences.ucf.edu/biology/pascencio/wp-content/uploads/sites/24/2016/11/Hurlbert1984.pdf)。讨论 treatments 未重复或 repeats 不独立时以 samples 增加 inferential repetition 的问题。支持实验单位原则，不是本稿 motor count 的来源；motor count 必须来自项目数据审计。

### 告警理论、区间与算法起源

16. **Angelopoulos/Bates tutorial，`angelopoulos2023conformal`，作者原始全文版本。** [作者 arXiv PDF](https://arxiv.org/pdf/2107.07511)，本轮实际读取 2022 作者版本，尤其 §4.4 Outlier Detection、Proposition 3 和 §4.5 distribution shift；[2023 原始出版页](https://www.nowpublishers.com/article/Details/MAL-101)。结论对应 exchangeable/IID null calibration/test observations 及固定 score construction 下的 marginal guarantee。本稿 dependent blocks 未验证这些条件。需诚实区分作者版本与2023期刊排版页码，本轮未称阅读出版版所有页。
17. **Chernozhukov et al. 2018，`chernozhukov2018dependentconformal`，PMLR 全文。** [PMLR 原始 PDF](https://proceedings.mlr.press/v75/chernozhukov18a/chernozhukov18a.pdf)，§2.2 structured block permutations 与条件性/近似有效性说明。它提供专门的 dependent procedure；本稿仅把窗口分成3 s宏块，不是该算法，不能自动获得其 theorem。
18. **Barber et al. 2026，`barber2026timeseriesconformal`，PMLR 全文。** [PMLR 原始页面](https://proceedings.mlr.press/v313/barber26a.html)，其页面链接的 [原始 PDF](https://raw.githubusercontent.com/mlresearch/v313/main/assets/barber26a/barber26a.pdf)，摘要、§1.1、早期理论部分。coverage loss bounds 涉及 stationary β-mixing processes；fit/calibration/test 的时间依赖也需处理。稿件没有验证 stationarity 或 mixing coefficient，不应引用作当前保证；目前明确披露，合适。
19. **Farouq 2021、Farouq 2022、Diallo 2025，原始出版社摘要/公开引言。** [2021 Mondrian fleet](https://www.sciencedirect.com/science/article/pii/S0925231221012005)、[2022 fleet framework](https://www.sciencedirect.com/science/article/abs/pii/S095741742200313X)、[2025 false-alarm comparison](https://www.sciencedirect.com/science/article/pii/S0959152425001234)。前两者为 district-heating/heterogeneous fleet 的 precedent；后者为 PCA/autoencoder、Tennessee Eastman process 的 marginal/conditional threshold 对照，并讨论 IID 条件。仅支持领域先例和校准限制背景，不支持本稿 motor population risk 或某个 adjusted method 在本稿有效。
20. **Wilson 定义，官方技术依据。** [NIST/SEMATECH 原始方法说明](https://www.itl.nist.gov/div898/handbook/prc/section2/prc241.htm) 的 Wilson formula 对双侧区间使用 z_(1−α/2)，单侧 bound 改用 z_(1−α)。独立复算：1/32，z=1.959963984540054 →15.7442638200%；z=1.6448536269514722 →12.8581990646%。此处核对的是命名，不是重新选择方法；在当前依赖结构下两种都不能当总体安全保证。见 R2。
21. **OC-SVM、IF、MCD、Log-Euclidean 原始出处。** [OC-SVM](https://doi.org/10.1162/089976601750264965)、[Isolation Forest](https://doi.org/10.1109/ICDM.2008.17)、[MCD](https://doi.org/10.1080/00401706.1999.10485670)、[Log-Euclidean](https://doi.org/10.1002/mrm.20965)。当前用作算法来源，元数据已核；本轮未把四篇全文再次全部读取。它们不证明本稿阈值协议或电机性能，也不支持把 “healthy calibration untouched” 写成所有原算法自带性质。无需为算法起源增加更多装饰性文献。

## JOM 范围与论文工程意义

[官方英文 aims and scope](https://jom.magnetics.or.kr/submission/journal/pages/aims_scope.vm) 包含磁测量、磁应用/装置及相关交叉领域。由此推断，以 PMSM 定子故障的电流电磁指标和工程报警失效为中心的稿件具有范围相关性；**这是范围解释，不是编辑接收保证**。Park 的同刊论文提供具体 electromagnetic diagnosis 联系，但不能把同刊引用数量当可接收性证据。现稿避免 SOTA、全新算法优越或已部署宣称，定位较准确。

工程意义应紧扣三个实测信息：冻结主方法从95.71%降至25.00%；同算法 target-only/source-assisted 对照揭示条件性负迁移；48/48 record-any 隐藏早期轨迹覆盖不足。不能扩大成“所有 source-assisted 方法都会失败”或“MinCovDet 在任何 PMSM 最佳”。第三谐波结果是在当前冻结数据上的 post-reveal 描述，不授权重新选特征或重写主方法。

## 剩余核查与结束条件

本轮发现的是表述和引用对应问题；没有发现需变更冻结结果才能解决的文献矛盾。Jeong、Li 2023 以及部分算法来源本轮全文访问不足的事实仍应明确，不能以题名/元数据代替细节审读。保留窄存在性/算法起源引用可以继续成稿；若恢复详细性能、phase localization 或独立 replication 数量主张，则需实际原文对应段落后才能写。

作者需要审阅这些限定与声明，但当前不应为追求更好看的外部结果新增 seed、删文件、改阈值或调用 Paper 3 结果。新物理电机/独立 healthy session 属于未来泛化和 remedy 确认的必要证据，不是本稿必须伪造或靠同机重复分析补齐的前置实验。

本报告建议按 R1–R3 优先修订、R4–R5 澄清范围，然后核对全文/补充/摘要/cover letter 的用词一致性和摘要词数。修订后的段落应保存新哈希及简短对应复核；报告不宣称未经本次审阅的后续版本已通过。

本轮可访问原始文件的下载状态和 SHA-256 已保存在 [download_manifest.json](reference_evidence/detailed_support_review/download_manifest.json)；全文工作副本位于 `tmp/jom/reference_downloads/`，不列为投稿附件。原始网页快照位于 [detailed_support_review](reference_evidence/detailed_support_review/)；门户探索已停止，边界见 [Portal_Readiness_2026-10-09.md](Portal_Readiness_2026-10-09.md)。
