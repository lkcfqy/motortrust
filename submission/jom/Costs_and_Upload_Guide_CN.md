# JOM 费用、上传清单与中文提交指南

核查日期：**2026-10-09，韩国时间**。本包为作者最终审阅准备包。文件名含 `AUTHOR_INPUT_REQUIRED`、有作者占位符或未签署表单的材料，不能直接上传。

## 费用估算

依据 JOM [官方收费页](https://jom.magnetics.or.kr/submission/journal/pages/publication_charges.vm)，英文说明为外国作者前5个**最终出版页** USD 300，第6页起每页 USD 10。以下不含尚未确定的费用。

| 最终出版页数 | 基础及超页费（USD） | 距 USD 500 预算余量 |
|---:|---:|---:|
| 5 | 300 | 200 |
| 8 | 330 | 170 |
| 10 | 350 | 150 |
| 12 | 370 | 130 |

公式：`300 + 10 × max(出版页数 − 5, 0)`。8–12页是本稿编辑目标，不是官方硬限制。审阅PDF的双倍行距页数及另附图表页数不等于出版页数。上述基础方案低于500美元，但**总支出尚不能确认**。

待核实项目一次列出：

1. 作者已说明为中国籍、韩国大学单位、当前非学会会员；此身份适用哪一收费类别仍待核实。英文 domestic-member 300,000韩元与同页韩文250,000韩元不同，不能自行用较低价格。
2. 作者确认尚无 JOM 投稿账户。[官方投稿页面](https://jom.magnetics.or.kr/submission/journal/pages/online_submission.vm)要求学会会员，[登录页](https://jom.magnetics.or.kr/submission/journal/pages/login.vm?ViewFlag=author)另有国际作者注册；此身份是否必须入会、会费是否为强制支出，未能从公开页解决。[官方会员说明](https://www.magnetics.or.kr/eng/html/about_membership.vm)列研究生年会费50,000韩元及订阅栏目20,000韩元；是否为本作者强制费用尚未核实，不推断免除或相加。
3. 彩图额外收费金额与在线/印刷的区别。官方仅说需承担额外费用，没有在线彩图免费承诺。本包主稿和 `figures/Fig*` 默认使用灰度可辨核心图，原始彩色矢量源保留在 `figures/color_sources/`；原始彩色源存在不代表已申请免费彩印。若作者选择上传彩图，先确认全部费用。
4. 补充材料、代码文件、税费、付款手续费及其他强制费用，公开页未给出完整说明，不能假定为零。

不购买润色、可选印刷品或其他付费服务。接受最终费用前核对所有强制项，保证合计不超过USD 500。本任务没有付款、发信、签字或正式投稿。

## 文件清单与用途

所有路径均位于 `/Users/lkc/Downloads/motortrust/submission/jom/`。

| 文件或目录 | 用途 / 上传状态 |
|---|---|
| `Main_Manuscript_AUTHOR_INPUT_REQUIRED.docx` | 可编辑英文主稿；已填作者提供的姓名、单位、地址、邮箱、ORCID及无经费、独作事实；电话/无传真/无利益冲突已转录；仍需致谢、机构要求及最终批准。官方公开页对旧版DOCX有拒收说明，不能仅依赖此文件上传。 |
| `Main_Manuscript_AUTHOR_INPUT_REQUIRED.doc` | 兼容公开页要求的legacy Word副本；剩余字段更新后重新生成并在Word核对。以最终portal接受的格式为准。 |
| `Main_Manuscript_AUTHOR_INPUT_REQUIRED.pdf` | 配套审阅PDF；不是替代官方要求的Word主稿。 |
| `Supplementary_Material.docx` / `.pdf` | 英文补充材料及审阅版；需确认portal补充材料上传类别和允许格式。 |
| `figures/Fig*.tif` | 官方偏好格式的独立主图；按图号上传。 |
| `figures/Fig*.pdf` / `.png`, `figures/captions.txt` | 灰阶图件预览、图注；彩色矢量原件在 `figures/color_sources/` 和 `figure_sources/`；必要时按portal要求使用。 |
| `figures/color_sources/` | 原始彩色图源，仅留档；选为投稿图件前核实彩图费用。 |
| `figure_sources/` | 可编辑图源及绘图脚本；留档或按编辑请求提供。 |
| `Cover_Letter_AUTHOR_INPUT_REQUIRED.docx` / `.pdf`, `cover_letter.md` | JOM投稿信草稿；姓名、单位和邮箱已按作者提供信息填入；未发表/无其他在审及数据许可已确认；最终批准和责任声明仍需本人审阅。 |
| `Paper1_Reproducibility_Code.zip`, `Reproducibility_Guide.md` | 可复现代码、环境、命令、公开数据获取说明；不要默认portal接受代码ZIP。 |
| `Checklist_Preparation.md` | 作者检查准备稿，非官方表单，不能当作正式checklist上传。 |
| `Copyright_Preparation.md` | 未签署准备稿，非官方合同，不能当作真实版权文件上传或代签。 |
| `Author_Input_Form_CN.md` | 作者真实身份及声明待填表；仅本地填写，不作为论文附件。 |
| `Reference_Audit.md`, `Evidence_Audit.md`, `English_Change_Log.md`, `QA_Report.md`, `evidence_audit.json`, `build_metadata.json` | 审计与QA留档；默认不上传。文件是否已完成以最终QA报告为准。 |
| `official_forms/` | 官方网页快照、DOC模板及来源/hash清单；未发现公开可下载的版权/checklist原件。 |

若本清单中的文件尚未生成，属于尚未完成项；不得以清单代替实际交付。

## 最少提交步骤

1. 姓名 LI KAICHEN、官方单位与地址、邮箱、ORCID、无经费及个人承担全部工作的独作事实已保存，无需重复提供。电话、无传真、无利益冲突、未发表且无其他在审、数据许可已确认并写入稿件。仅需在 `Author_Input_Form_CN.md` 补充致谢（确无也请确认）、机构提交要求及实际状态，并在审阅新主稿与补充材料后确认最终批准和 AI 辅助披露下的作者责任。
2. 逐项复核摘要、主图、表格、补充材料及投稿信。保留外部主方法25.00%、失效gate、单电机和事后诊断等披露。作者信息、署名或声明改动后重新构建并看PDF。无原生Word时的已完成检查与仍需Word字段/页面复核，见QA报告。
3. 在官方系统查看实际文件类型、会员/国际作者规定、补充材料和AI披露问题，并取得当前官方copyright/checklist。公开页面要求将主稿及相应表单作为单文件；登录后如果portal的现行文件槽位要求不同，以经作者核实的当前portal流程为准，保留截图或文字记录。
4. 将本包的核查信息转填到**真实官方**表单；只由作者最终确认、按实际表单签署。不要上传本地准备稿，不伪造签名和批准。
5. 核对费用身份、彩图和所有强制费用。登录系统填写元数据；检查其生成的审阅文件和状态。本包没有代为执行正式提交。

主稿文件格式存在官方页面陈旧措辞：公开页面拒绝MS2007/2008 `.docx`，同时要求MS Word并链接 `.doc` 模板。保留DOCX作为编辑源，legacy DOC作为提交候选，上传前必须核实当前portal是否接受现代DOCX及DOC转换后的公式/图表。

作者指南、收费和伦理原文与核查结论见 [JOM官方要求核查](../../docs/jom_submission_requirements_2026-10-09.md)。公开页未明确的事项已经列出，不通过推断免除。
