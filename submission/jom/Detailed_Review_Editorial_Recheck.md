# JOM 英文稿详细审稿：修订后复查

复查日期：2026-10-09 15:32 KST。完整复读修订后的主稿670行、补充864行及压缩后的cover57行；根任务最后追加的方法说明也已读入。只新增本复查报告，并按授权在旧作者映射顶部标明历史状态；**未改三份源稿、Word、构建器、科学输出或作者声明。** 此报告不代替尚待完成的新渲染逐页视觉检查，也不表示作者已批准最终稿。

## 复查结论

上一轮A1–A3均已有实质修订，当前没有发现新的研究身份矛盾。论文主线保持为固定协议下健康参考迁移的跨数据集可靠性案例，外部失败与局限没有因补方法解释而被弱化。英文可以供正式审阅，仍有少量衔接和术语定义可优化；这些不要求扩展实验或重算冻结结果。不能写“每项建议已全部照改”：结构精简只部分采用，几个C类建议尚未采纳或有合理保留，见逐项表。

摘要空白分词为**133词**；把斜线数字等另拆开的regex计数为142，均在100–150词范围内。关键词6个。摘要、主表、结果、结论及cover的95.71%、0/42、96/384=25.00%、1/32、0.6354、15.74%>12%、70.05%与3/5 seeds一致。本轮核对的是文字及已保存汇总，没有重新拟合以迎合这些锚点。

## 新增定义的一致性检查

| 新增说明 | 实际位置 | 复查 |
|---|---|---|
| Healthy-only限于健康参考拟合、归一和目标校准；源故障标签参与开发 | 主稿55–56、272–278；补充146–152 | 一致。没有将嵌套选ridge说成完全无监督；排除外层目标与KAIST整体exploratory两事实并存，不互相抵消。 |
| 外层source-label objective及lambda0.01 | 主稿272–277；补充149–152 | 目标函数、grid和三fold结果明确；原参数未改变。 |
| MCD同27输入、有效26/27维及60/240行差异 | 主稿304–318、473–480；补充154–158、281–283 | 一致；把差异归于整个冻结配置，未再称source信息净因果作用。 |
| IF的auto样本量、OC-SVM的data-adaptive gamma | 主稿313–314；补充294–297 | 与固定实现/不同数值fit参数兼容，不自相矛盾；没有暗示事后调参。 |
| 20/24校准块的strict > maximum、ties不报警 | 主稿333–337；补充159–161 | 与p公式的“≥”计数一致；没有把达到5%分辨率等同独立覆盖。 |
| 两侧95% Wilson upper endpoint；描述性bootstrap | 主稿25–26、236–242、349–355；补充161、214–219、285–297 | 层级清楚，当前15.74%没有被错叫单侧95%界；bootstrap没有被重新包装成人口保证。 |
| 共同支持pooled单特征AUROC vs matched差值 | 主稿491–499、Fig.6；补充425–439 | 正确区分。AUROC64health/384fault子系统块与贡献32health/384fault系统块的不同范围写明；方向选择、top-eight事后性、非ablation均披露。 |
| Source covariance/reference标签与target健康归一/校准 | 主稿481–483；补充177–178 | 比“pure-source”准确。该名称限定参考形状，不表示整个报警流程完全不用目标健康数据。 |
| block detection等权 vs record-any累计机会 | 补充301–305；主稿448–453 | 修正了此前“late blocks get more opportunities”的混淆；每位置在block平均中权重相同，any endpoint才累积机会。 |
| AUPRC基准92.31% | 补充175–176 | 384/416=92.3077%；明确prevalence依赖、不是实际部署precision。 |
| Secondary alpha–beta/26-feature/window校准、12配置及平均record AUROC范围 | 主稿507–518；补充619–630、652–657、674–687 | 与primary27输入、3s系统块、11配置是不同预定义协议；0/21失败、修复后200W-only及非确认身份完整保留。 |
| 5seed时间身份 | 主稿319–321、439–443；补充413–421 | KAIST之前固定seed列表，外部5seed audit是post-reveal，仅20260820为外部prespecifiedseed，未混称预先冻结外部5seed实验。 |

新S1.2的Hann去均值FFT、5Hz bins、fundamental搜索、harmonic/sideband启发式、orientation-invariant序比、MAD回退均与当前已核对的实现解释相容。它们没有把通用引用误写为这些具体特征的验证，也没有变成实时部署论证。

## 上轮每项意见的落实状态

| 原编号 | 状态 | 当前对应位置及说明 |
|---|---|---|
| A1 source faults / healthy-only | **已落实** | 主稿55–56、272–278；补充149–152，直接写出label use。 |
| A2 effective MCD feature mask | **已落实** | 主稿314–318、473–480；补充154–158、281–297；摘要也改为estimator-family configurations。 |
| A3 pooled feature AUROC身份与不同grain/support | **已落实** | 主稿491–499及Fig.6；补充425–439。 |
| B1工程特征与robust scale定义 | **已落实** | S1.2新增125–161；主稿250指向该节。 |
| B2 strict threshold/tie | **已落实** | 主稿333–337；S1.2。 |
| B3 descriptive bootstrap / nominal p | **主要已落实** | 外部表、方法和S3均已改。S10的KAIST paired表头仍写“Paired 95% interval”（730行）；可统一描述性标签，但其exploratory身份及完整记录重采样已披露。 |
| B4 pairwise ranking reversal | **已落实** | 主稿385–389、435–437，明确LE vs target MCD且primary不是总体冠军。 |
| B5 z记号、绝对share、非ablation解释 | **已落实** | 主稿487–499；补充434–439明确每winningwindow的绝对share及平均顺序。 |
| B6 sampling control结论范围 | **已落实** | 主稿532–536；补充546–549保留其它测量链差异。 |
| B7 internal-project prose | **已落实** | 主稿移除Paper1/later-paper项目指令；S11删去身份/经费未asserted陈旧交接；cover删上传slot制作句。未确认作者批准保留是正确状态控制。 |
| B8集中结构与冗余压缩 | **部分落实** | KAIST几组重复paired CIs已移只留S10；S0标题变diagnostic purpose。Introduction/2.2及2.1尚有小范围重复；保留结构是可接受编辑选择，不需全稿推倒。 |
| B9 secondary 12 vs primary11 | **已落实** | S9.2 652–653直接解释target-only log-ridge额外控制。 |
| C1 Frozen修饰位置/短题 | **可选未采用** | 保留原统一题目，不造成新结果或贡献错配。 |
| C2摘要motor/domain句 | **已落实** | 19–20行改为across motors/conditions/domains。 |
| C3摘要same-estimator wording | **已落实** | 27–29行paired estimator-family与完整pipeline。 |
| C4 shared algorithm表述 | **已落实** | 主稿133–135及304–318解释common input与fit masks。 |
| C5 scale-free历史名称 | **已落实** | 主稿251–255明确historically named，仍含frequency。 |
| C6 Proposed缩写标签 | **历史标签保留** | 主稿322–323有定义；补充仍多用Proposed。可在Technical summary首次称“primary Log-Euclidean (archived label: Proposed)”，不是必须更改历史图表。 |
| C7 sole primary-seed method | **已落实** | 主稿413行“sole method ... at the prespecified seed”。 |
| C8 Spearman rho明确 | **未采用的小建议** | 461行仍称associations，数值可理解；可写rank correlations (ρ)，不追加p值。 |
| C9 load endpoints措辞 | **保留可接受** | 原保存record summary分组均值确实从56.25、35.4167、27.0833、18.75、18.75、16.6667、14.5833到12.5单调不增，declined符合描述；已有非因果限定，没必要为这句新作分析。 |
| C10 448分母范围 | **未采用的小建议** | 487行未补“across all56records”；S6.1说明allphysicalrecord block scores，主fault384及health32未变，可加短解释减少分母疑问。 |
| C11 top-eight排序依据 | **部分落实** | 补充429–430披露事后选top8，但仍未点明按robust-z direction-free AUC排序。 |
| C12 d_z分母定义 | **尚未落实** | S6与Fig.6说matched dz而没有mean difference / sample SD定义；建议补一句，不需计算任何新数字。 |
| C13 failure-boundary措辞 | **已收窄** | 摘要30行和结论579–582行明确protocol-specific/oneexternalmotor；没有估计全PMSM部署包络。 |

因此不能把C12等说成已经完成，但没有理由因可选题目或保留历史label而扩展实验。

## 最后一轮可采用的小修句（不改冻结证据）

1. **Introduction 55–58的衔接。** 插入healthy-only定义后，“Negative transfer is otherwise possible”中的otherwise现在紧接label-use，指代不自然。可独立写：“Source augmentation can also reduce performance, a form of negative transfer [citations].” 这只是衔接，不能暗示label use引发negative transfer。
2. **Background 2.1重复。** 94–95及100–101两次在同段用Urresty支持order tracking随speed/load变化。后半可简为：“Physical-data models have also addressed PMSM diagnosis at rapidly varying speed [Li2024].” 不需要删前半真实物理背景。
3. **方法/结果的冠词及记号。** 481行“still exceeded source-covariance reference”改“still exceeded **the** source-covariance reference”。266行可补“sample covariance of the standardized healthy reference”。461行可改“Spearman rank correlations (ρ)”。
4. **S6最低定义补全。** 写：“The displayed eight features are ordered by robust-z direction-free AUROC. Matched d_z is the mean paired difference divided by its sample standard deviation; reused healthy units preclude independent-sample inference.” 这同时落实C11/C12，不重算或选择新feature。
5. **S0统计重复与物理存在。** 28–30行“Neither [secondary dataset] ... creates an independent motor replication”本意是没有可用确认性复制，但S9确实描述两个实际物理电机。建议更明确：“The failed frozen secondary audit and its repaired single-motor sensitivity do not add confirmatory independent-motor replication to the primary external result. The two subsystems of the primary motor are not motor replicates.” 避免看起来否认次级电机本身存在。
6. **S10表头一致性。** 730行“Paired 95% interval”可改“Descriptive paired bootstrap interval”，在附近注明percentiles；保留所有表值和exploratory身份。

这些建议不是“论文需要更多实验”的意见，也不意味着三处A问题仍未修正。由根任务统一整合，避免多人写同一稿件。

## Cover与作者事实状态

压缩cover的科学内容与主稿一致，仍包括内部95.71%/外部25%、15.74%gate失败、MCDseed波动、单外部电机、非外部注册、secondarypost-reveal身份和完整配置对比。现文字没有冒称已投稿完成或作者最终批准。

电话+82-10-3915-7350、无传真、无利益冲突、原创/独投及数据许可已按后续真实确认转录。本人待确认继续是致谢、适用机构许可、最终稿批准及AI责任；portalroute是制作/系统事项。当前源主稿有5个括号控制块，cover有3个（含日期），补充0个：这不是旧作者映射中7+4计数。旧映射顶部已标为历史快照，不能当作当前再次向作者索要电话/COI的表单。

## 本轮边界与下一步

本轮是全文文字/论证复查，未宣称新DOCX/PDF已逐页验证。新增加S1.2、较长methods限定、短Fig.6caption及压cover会改变页流，必须用第二轮构建的新PNG重新检查，尤其公式附近、main声明/图注页、supp新定义及宽表。原生MicrosoftWord仍未验证。作者最终批准/签署与正式上传权限继续独立于文字复查。

此轮不引入新的算法、数据集、硬件、收费服务或更多seed。科学局限继续保留；根任务完成最后小修后可进入渲染QA及交付，不为寻找更好结果继续实验。

## 完整复读所绑定的源快照

| 源 | SHA-256（2026-10-09 15:31 KST核查） |
|---|---|
| 主稿 `manuscript.md`（670行） | `b4cad5240b5071183fa5f35accdfca28fa4896f029e9ff386180278089a9a687` |
| 补充 `supplementary.md`（864行） | `ed12fa7a655c4eff99571cd90dec20f118a7f3c130a536b8b56b9558f1d2e53d` |
| cover `cover_letter.md`（57行） | `db0c60b8dcffc1b2f864b4a2d2a0ae993e6e6a51104af845b363676cbb710a29` |

后续编辑须作为新快照记录；本报告具体位置与未采用项只对应上表，不反向宣称旧稿已修正。
