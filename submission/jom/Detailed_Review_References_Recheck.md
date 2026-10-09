# 详细引用审查修订复核

日期：2026-10-09（Asia/Seoul）。对 [Detailed_Review_References.md](Detailed_Review_References.md) 的 R1–R6，以及主稿/补充/cover letter 新增的研究边界表述进行只读复核。本轮没有改动稿件、Word、科学代码、冻结结果、表单或上传状态，也没有扩展实验或重新探索投稿门户。

本次读取文件及哈希保存在 [revised_source_snapshot.json](reference_evidence/detailed_support_review/revised_source_snapshot.json)：

| 文件 | 本轮复核版本 SHA-256 |
|---|---|
| [manuscript.md](manuscript.md) | `f985542898ddbd4212389a19d07a062eb6a1706f5f36d4e054dd7e846f547d29` |
| [supplementary.md](supplementary.md) | `ea6b53150649cf8f0248f2e1a3811f43a5426ef7f55d228a2111ab74e4d01099` |
| [cover_letter.md](cover_letter.md) | `5d517bfc26a8f1ee1d431852159e64d869346a267c1cf5dcb252337b52dc3171` |

## R1–R6 处理结果

| 项目 | 修订后的对应文本与支持性结果 |
|---|---|
| R1 特征—文献对应 | **主稿已解决。** Introduction 增加 Urresty，将背景概括为 current-based indicators；§2.1 分开 sequence/current-vector 与 current harmonics，且明确这些不同指标并不验证本稿特征集。Li 的原始 §3 支持负序向量模平方的二次谐波；Urresty 原始研究摘要支持相电流谐波的变速/负载 order tracking。当前未声称本稿实现这两篇的特定方法。Supplement S1.2 更明确本稿固定FFT近邻bin heuristics **不是 order tracking**，与文献的使用边界一致。 |
| R2 Wilson 尾部定义 | **主稿、补充及cover letter已解决。** 摘要与§3.3明确 two-sided 95% Wilson upper endpoint；Supplement S1.2 明确不是 one-sided 95% limit；cover letter也使用 two-sided。正文后文简写 Wilson upper bound 可以由前述定义解释。15.74%、1/32、12% H1 保留，无冻结规则改变。133词摘要按空格计数，仍处于官方100–150词范围；最终Word摘要及任何后续修改仍需构建器核对。 |
| R3 多数据集与独立复制 | **主稿已解决。** §2.2 使用 collaborative multimachine generalization / multi-dataset fault-diagnosis benchmarking 的存在性表述，没有再把它们称为更充分的 independent replication。Li 2023 本轮全文访问不足，因此这种窄表述更适当；Zhao 的原始机构摘要支持 benchmark 的存在与范围。Discussion继续将缺少独立电机/会话列为本稿限制。 |
| R4 工况确定关系/因果范围 | **主稿已解决。** Introduction 使用 healthy distributions “can differ”，随后将rating/topology/chain/trajectory列为两个域的差异，明确不能隔离各差异的作用。Discussion 使用changed together并保留未独立操纵的限制。Cover letter仍有一个可选精度修订，见下方C1；当前没有明说识别单因素因果，但可进一步避免暗示。 |
| R5 探索开发与独立确认 | **主稿已解决。** Discussion 明确 “Confirming a remedy requires a new untouched motor or laboratory test”，后续 adaptation 为 separate exploratory development、不能回写冻结结果。未把新电机/硬件当本次论文提交前置条件；允许诚实报告现有 post-reveal 诊断。 |
| R6 建议检查与通用验收标准 | **主稿已解决。** “diagnostic checks for future evaluations”替代普遍acceptance checks；后段仍明确无remedy/safety guarantee。单机失败据此提供工程检查启示，没有提升为普遍充分条件。 |

## 新增或收紧段落的支持复核

这些内容主要是自身协议、算法实现或结果的披露。外部文献提供背景/理论边界，不能代替细粒度结果与代码审计。本次支持审查核对了陈述的推断范围；未代替项目数值验证器重新计算所有新增数值。

| 新表述 | 复核结论 |
|---|---|
| Introduction 将 healthy-only 限定为reference fitting、normalization和target alarm calibration，并承认source development使用source fault labels | 避免误导为整个开发过程完全unsupervised；§4.1和Supplement S1.2进一步给出source-label objective、候选ridge与outer-target exclusion。此为本稿协议事实，应由保存的ridge selection输出和代码追溯，不能说外部literature证明该协议。本稿仍保留KAIST exploratory，不因source-label disclosure升级确认身份。 |
| Introduction “public data acquired by an independent laboratory” | 清楚区分作者使用公开外部数据与亲自做实验，且没有将internal freeze称external registered preregistration。与§3.3、Supplement S0和cover letter一致。 |
| MinCovDet 60 rows /26 features vs240 rows /27 features | §4.2、§5.3、Supplement S1.2/S3.2、cover letter均披露fit-derived feature masks。Wang §3需要比较同一个算法A；本稿现在更准确地称“same estimator family”“complete frozen configurations”，未说fixed-feature-space source effect。此差异属于augmentation pipeline的观测对照，不是孤立source information的因果估计。 |
| source-assisted one-class uses moretotal rows butsame target adaptation allowance | 公平对照条件被限定到共同input definitions/calibration/target-health allowance，而不是声称effective representation/totalrows完全相同。source rows增加是所评pipeline的一部分。继续公开mask与rowcounts即可；不能揭盲后equalize masks并包装冻结比较。 |
| 五seed来自KAIST baseline固定列表、外部audit为post-reveal | §4.2的修订比“external seed-stability protocol预先冻结”更谨慎；Supplement S5明确没有pre-reveal formalstability gate。primaryseed及原结果不改变；gate3/5仅稳定性描述，不选择bestseed。 |
| §4.3阈值strictlygreater、ties不报警 | 与 p=(1+#cal≥test)/(n+1)、n=20/24、α=.05的算术一致。最小p分别1/21、1/25，第二等级2/21、2/25都>.05。因此strictlyabove calmax才可能报警。该正确算术不提供依赖数据中的population coverage，相关免责声明保留。 |
| §4.3将bootstrappercentiles称descriptive record-weighting sensitivities、未校准populationCI | 与单机、相似加速轨迹和未证实independent sessions相容。保留Holm值为resamplingdiagnostics，不把小p解释成跨电机总体显著性。这个限制不需靠增加同机文件“修复”。 |
| §5.4/S6区分feature AUROC的subsystem-block means、commonfourloads，与allocation的winningwindow/systemblocks/allfaultloads | 现在明确了不同grain/support，且 max(AUROC,1−AUROC)是post-revealorientation选择。比原“feature discriminates butlowcontribution→failure”的直接因果暗示更准确。Locked-reference misalignment是hypothesis/consistentinterpretation，不是ablation或causalimportance；lowallocation不证明irrelevance。没有据此重新选特征。 |
| §5.4/S7 nominal sampling-rate matching未救回 | 保留25.00→24.74、0.6354→0.6331、1/32，并限定fixedextractor；Discussion/S7仍承认sensor/analogfilter/controller/noise等其他chain差异未排除。不能扩大成“采样链无影响”，现稿没有这样写。 |
| Supplement S0当前scikit-learn1.9.1与历史metadata1.9.0、历史完整lock未找到 | 将saved-resultverification与current-runtime stochasticrefit分开，避免byte-identical历史重建承诺。环境版本事实需环境审计支持；引用文献不解决这一限制。保留该披露，不改变原scores。 |
| cover letter’sresultandscopeclaims | 95.71%、0/42；96/384=25.00%、1/32、AUROC.6354；MinCovDet70.05%、0/32、threeoffiveseeds通过，与主稿锚点一致。Singlemotor、turn/phaseconfounding、loadsupport、offline、secondaryparser、internalfreeze均有披露。作者原创/独投/利益冲突/许可证/最终批准陈述是否已确认属于authoradministrativefacts，本轮引用支持审查不代作者签署或批准。 |

## 仍可压缩的两处措辞

**C1，cover letter第二段，非结果或方法改动：** 当前 “The study evaluates these competing influences ...” 可能被理解为分别评价速度、负载、拓扑和测量条件的影响。与主稿的compoundshift表述进一步一致的替换为：

> The study evaluates alarm reliability under their combined change through a fixed healthy-reference fitting and calibration pipeline with target-only controls.

这是明确迁移评估的对象，不主张识别每个因素的因果贡献。其余单机与有限推断段已足以表明范围，C1不要求新增分析。

**C2，§2.1第一段，纯压缩：** Urresty/ordertracking的“changing speed and load”在同段出现两次，且均用同篇引用。可删第二次重复ordertracking句，直接连接physical-data rapidlyvaryingspeed文献；第一处已经给足同样支持。重复本身不是科学错误。

## 原始来源访问限制仍保留

本轮使用前一详细审查已实际读取的原始来源，没有把文献元数据成功视为全文支持。来源层级、链接和定位详见 [Detailed_Review_References.md](Detailed_Review_References.md)。实际全文/指定段落包括Li2024IEICE、ParkJOM、Wang原作者v4、Wheat原作者repositoryPDF、Angelopoulos/Bates作者preprint、ChernozhukovPMLR、BarberPMLR。多篇其他来源仅核到originalpublisher/institutionabstract；**Jeong2017和Li2023本轮详细全文仍不可访问**，算法起源四篇未全部全文重读。新增窄存在性表述与这些限制相匹配；若作者后续恢复详细phase-localization、exactreplicationcounts或性能主张，必须再核原文对应段落。

旧 [Reference_Audit.md](Reference_Audit.md) 的Wang定位已由§2更正为§3，顶部添加详细审查及本复核链接，说明后来的来源访问层级和收窄结论优先于原报告的概括性支持印象。原bibliography、已归档metadata与历史JEET材料保持不变。

本轮**未发现R1–R6中需要重新实验才能解决的剩余引用矛盾**；C1/C2为限定与压缩建议。结论仅对应上述哈希版本，后续作者编辑需再核一致性。本报告不等于最终页面视觉QA或已可直接上传；Word/PDF渲染、作者批准和官方实际表单/系统步骤须分别完成。

## 最后压缩版本补记（2026-10-09）

已只读核对最后措辞：cover letter第二段现在评价健康电流拟合/校准的报警在跨数据集条件下的可靠性，不再称为分别评价 “competing influences”；§2.1保留一次Urresty的order-tracking背景，删除重复句，并仍明确本稿特征与文献专门指标不同。**C1/C2均已处理**。此补记保留上文原审查发现与当时哈希，不回写审查历史。补充材料仍保留seed列表与外部audit的不同时间身份、fit-derived masks、feature诊断的post-reveal orientation/grain/support和runtime限制；本次未发现这些限定被删去。

最后读取的源文件哈希见 [final_source_endnote_snapshot.json](reference_evidence/detailed_support_review/final_source_endnote_snapshot.json)：main `30bfbfc0d0e7fbb27cb21f3ff4c36d962fc226edb45d2dc61beb5bccec3338c1`；supplement `26dbf42fefaf3de350667ef33c96c8f2e4588c6ebc30a9f0bf374773bf5656ec`；cover letter `db0c60b8dcffc1b2f864b4a2d2a0ae993e6e6a51104af845b363676cbb710a29`。摘要仍为133词（空格计数）。文献原始摘要/元数据的访问局限与之前说明相同，未升级为全部全文已审。

页面版式审查等待最后构建输出，另记录实际DOC/PDF/PNG哈希；源文支持复核不能替代该视觉检查。

### Legacy DOC 转换路径诊断补记

第一次独立检查按 `原DOC → 临时DOCX → documents renderer PDF/PNG` 的额外往返路径进行，30/30页均已实际查看。第7页的额外往返结果丢失公式tilde并改变上下标；但随后**直接从原DOC导出PDF**并实际查看第7页，tilde、lambda上标及precision dagger均正确。因此不能将额外DOC→DOCX导出损坏误报为原DOC直接显示错误，也未据此改写可编辑的主DOCX公式。主DOCX及额外往返PDF第21页存在空白页，负责构建的主代理已开始修复分页。原DOC副本、额外往返文件、direct-DOC PDF及逐页诊断记录保留在 [legacy_doc_roundtrip_draft_review.json](reference_evidence/legacy_doc_roundtrip_draft_review.json) 对应路径；本次不宣称legacy最终通过。

除上述问题，额外往返路径的正文/参考文献1–30/三张Roman表/六张灰度图均可读，未发现裁切或缺字。最终兼容检查将直接 `原DOC → PDF → PNG`，避免额外导出到DOCX；仍不会称为原生Microsoft Word验证。Fig6图内旧panel title “Same-block discrimination”可能弱化pooled AUROC与matched dz的区别，已向主代理建议收窄展示标题；正文和caption已经分别定义二者。
