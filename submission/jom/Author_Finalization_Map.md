# JOM 作者字段与定稿源映射（历史只读快照）

> **历史记录，不是当前待填清单。** 下文行号、11个占位块和“尚未确认”状态仅对应2026-10-09 15:07 KST的旧稿及末尾列出的旧成品哈希。后续作者已提供电话/无传真，并确认无利益冲突、原创独投及数据许可，修订源稿已转录；这些项目不再索要。当前个人待确认事项仅为致谢（如有）、适用机构许可、最终稿批准及AI披露/责任确认。以当前 `author_metadata_REQUIRED.yaml`、主稿/补充/cover源及 `Detailed_Review_Editorial_Recheck.md` 的新位置为准。Portal上传途径、真实表单及费用仍是系统核实事项，不是重复补填已确认身份。

扫描时间：2026-10-09 15:07 KST。本文仅记录现有源稿及成品中的字段，不表示作者已经批准最终稿，不修改科学结果、稿件或构建器。适用快照为本文件末尾列出的 SHA-256。

## 1. 已确认事实：直接复用，不再索要

| 事实 | 已确认值 | 当前源位置 |
|---|---|---|
| 正式英文姓名 | LI KAICHEN | `author_metadata_REQUIRED.yaml:2`；`manuscript.md:7`；`cover_letter.md:57`；`supplementary.md:7` |
| 国籍；会员状态 | China；Not a member | YAML:3–4；`Author_Input_Form_CN.md:8–9`。国籍及单位不自动决定期刊收费类别。 |
| 官方院系；学校 | Department of Artificial Intelligence Convergence Engineering；Changwon National University | YAML:5–6；主稿:9；投稿信:59；补充:7 |
| 地址；邮编 | 20 Changwondaehak-ro, Uichang-gu, Changwon-si, Gyeongsangnam-do 51140, Republic of Korea；51140 | YAML:7–9；主稿:9；投稿信:61 |
| 邮箱 | lkcfqy@gmail.com | YAML:10；主稿:11；投稿信:63 |
| ORCID | 0009-0008-8743-3162 | YAML:13；主稿:16 |
| 经费 | This research received no funding. | YAML:14；主稿:559；投稿信:50 |
| 独作；实际贡献 | 个人完成全部研究和稿件工作；独作已确认 | YAML:17–18；主稿:568；投稿信:45；中文表:18–19 |

作者身份、经费和实际贡献已完成转录。现有“additional authorship requirements”占位不代表作者没有提供贡献事实；待核实的是最终批准、责任及适用要求。

## 2. 尚未确认的事实与批准：一次性源映射

下列仅为待回答字段清单，父任务已向作者汇总询问；本扫描不重复提问。DOCX 段落编号采用 `Document.paragraphs` 从 1 起计数，包含空段落，不是 Word 内显示的段落编号。

| 待确认项 | 现有 YAML 字段 | 需要同步的源位置 | 现有成品位置 |
|---|---|---|---|
| 通信电话；传真，或确认无传真 | `telephone` (11)、`fax` (12) | 主稿:13–14；投稿信:63；中文表:13；checklist:13；copyright:13 | 主稿 DOCX 段5 / PDF页1；cover 段15 / PDF页1；legacy DOC包含同一字段 |
| 财务及非财务利益冲突的真实声明 | `competing_interests_statement` (15) | 主稿:565–566；投稿信:50–53；中文表:16；checklist:19 | 主稿段101 / PDF页14；cover段10 / PDF页1 |
| 是否需要致谢；如需要，致谢内容及被致谢者许可 | `acknowledgments` (16) | 主稿:561；投稿信:50–53；中文表:17；checklist:19 | 主稿段99 / PDF页14；cover段10 / PDF页1 |
| 原创性、未发表、无同时投稿；如存在预印本/复用内容须如实披露 | `originality_and_no_concurrent_submission_confirmed` (19) 当前将数项合并为一个确认值，不能掩盖例外 | 投稿信:45–48；中文表:20；checklist:18；copyright:15 | cover段9 / PDF页1；当前主稿没有这个独立占位句 |
| 数据使用、图文复用、机构/雇主权利或适用伦理要求 | `data_and_institutional_permissions_confirmed` (20)；若有例外须附具体说明，不能只填 `true` | 主稿:570–572；投稿信:45–48；中文表:21；checklist:19；copyright:14–15 | 主稿段103 / PDF页14；cover段9 / PDF页1 |
| AI 辅助披露的准确范围；核查全文与引用后承担责任 | `ai_disclosure_and_responsibility_confirmed` (21)；最终披露文字目前没有独立 YAML 字段 | 主稿:574–579；投稿信:50–53；中文表:22；checklist:20 | 主稿段104 / PDF页14；cover段10 / PDF页1 |
| 最终稿、全部声明及标题批准；履行适用作者责任 | 当前 YAML **没有**独立 `final_manuscript_approval_confirmed` 或批准日期字段；应留真实批准记录 | 主稿:568、577–579；投稿信:45–48；checklist:5、21、26；copyright:9 | 主稿段102、104 / PDF页14；cover段9 / PDF页1 |

真实声明确认后，必须用适合期刊阅读的完整英文句子替换括号提示，不能把 `true`、`null`、作者问答或制作人员指令留在正文。不要自动把空白致谢或空白 COI 推断为“None”。

## 3. 制作与系统输入：不是尚缺的作者研究事实

| 位置 | 当前提示/问题 | 定稿处理与边界 |
|---|---|---|
| `cover_letter.md:6`；cover段2 / PDF页1 | `[SUBMISSION DATE]` | 实际准备发送/提交时填正确日期，不是需重复索要的个人资料。日期不能被当作投稿已完成的事实。 |
| `manuscript.md:592–594`；主稿段106 / PDF页14–15 | 确认代码/补充材料上传或托管途径 | 需要当前 portal 文件槽位信息。确认可随稿上传时再使用对应 availability 文字；不能虚构公开仓库 URL 或声称已公开发布。 |
| `cover_letter.md:40–43` | “Their upload category is subject to ... options.” | 系统操作提示；最后应删去或根据真实上传方式改成给编辑的明确附件说明。 |
| `supplementary.md:9–13` | 开头 “JOM preparation draft ...” | 制作草稿标签；当前 builder 未将这一 blockquote 导入 DOCX/PDF（页1从作者行进入 S0）。清理源草稿标签时必须保留冻结、事后诊断、单电机及 0/21 失败等科学身份。 |
| `supplementary.md:777–782`；补充段141 / PDF页22 | 将作者身份、经费等一并写成 “not asserted by this draft” | 已与已填姓名/单位和已确认无经费不一致。这段作者/版权/投稿责任交接说明适合内部审计，不适合最终科学补充文件；定稿时删除或改写制作说明，保留真实的历史协议与再现边界。 |
| 主稿:568、571、577–579 | 括号内有“review ...”“approve ...”“preparation draft” | 它们是作者确认控制，不是期刊正文。在相应事实/批准得到确认后去掉制作指令；不要删去实际贡献、伦理描述或 AI 事实披露。 |
| `Checklist_Preparation.md:5、26、28` | 标题最终版本、作者审阅日期、签名 | 标题及日期随最终批准填写；只在真实官方 checklist 要求时由本人签署。该 MD 是内部准备稿，不作为官方表单上传。 |
| `Copyright_Preparation.md:9–10、16–17` | 最终标题、article number、签署日期、签名 | article number 由 portal 分配；真实合同的日期、条款和签名由作者本人处理。本地准备稿不是版权合同，不能代签或上传替代合同。 |
| 文件名 `AUTHOR_INPUT_REQUIRED`；README/DELIVERY_INDEX/Costs/QA/delivery_status | 准备阶段状态标记 | 确认与清理后须同步交付清单及真实状态。现有 builder 的输出名仍固定含该标记；重建不会自动改名。历史 QA 不应被改写为“此前已批准”。 |
| 代码 ZIP 中 `[AUTHOR FULL NAME]` 等导出替换 | 隐私脱敏副本 | 故意脱敏，不是研究或投稿主稿的事实缺口；不得为了消除全局字符串命中而把真实联系方式重新写进可分享代码包。 |
| 官方 DOC 模板及网页快照 | 原始示例/空白字段 | 它们是保留的官方来源，不是作者定稿；不要修改原件或把示例姓名当作未填本人资料。 |

## 4. 当前成品扫描结果与上传阻碍

扫描当前三个 DOCX 的正文、表格、页眉与页脚，主稿有 **7 个**完整括号占位块，cover 有 **4 个**，补充为 **0 个**；表格/页眉/页脚没有另藏的作者占位块。对应 PDF 中主稿最后一块跨页14–15，因此单页 regex 会漏检，不能把页15看成无占位。当前 legacy DOC 内容沿用主稿同一组字段。

本次没有发现新的裁切、公式破坏或科学数字不一致；不重复宣称开展了另一轮逐页视觉检查。现有独立 QA 记录显示主稿28页、补充22页、cover1页均已实际逐页查看，legacy DOC 五公式/三表/六图已经 LibreOffice 重渲染检查。最后填字段或删制作文字会改变版面，必须重新构建并复看变化页面；旧 PNG 哈希不能代替改后检查。**原生 Microsoft Word 未验证**，需要区分这一能力限制。

当前影响直接上传的事项为：

1. 上述尚未确认的声明及11个字面占位块；补充 S11 和 cover 的内部制作说明仍需在定稿时清理。
2. 尚无真实官方 copyright/checklist 原件；准备 MD 不能代替。真实表单要求及是否需与主稿合成一个文件，应以作者获准访问的当前 portal 为准。
3. 当前 portal 是否接受 DOCX、legacy DOC、补充材料/代码及 AI 字段尚未核实；公开旧版 DOCX 拒收措辞不能被假定成当前 portal 全部行为。两种 Word 候选已备齐。
4. 中国籍、韩国大学单位、非会员身份的账户/会员要求及费率分类尚未解决；USD330–370 是8–12**出版页**按英文外国作者收费计算的基础/超页费，不是已确认的全部支出。其余强制费用和总额≤USD500仍需核实。

Paper 1 证据、lint、测试与可移植打包已有通过记录；四个 Paper 2–4 失败独立记载在 QA 报告，本扫描没有把它们变成 Paper 1 新实验前置条件。单外部电机、依赖、匝数/相位混杂、AUROC负载支持及离线分析是需要保留的论文局限，不是通过补字段就能消除的问题。

## 5. 源同步依赖与最小定稿顺序

`scripts/build_jom_submission.py:790–797` 直接从 `manuscript.md`、`supplementary.md`、`cover_letter.md` 构建成品。当前 YAML 在该脚本约619行用于导出脱敏，**没有将其字段自动注入主稿或 cover**。因此只填 YAML 后重建，11个可见占位块仍会存在。

最小顺序：获得尚缺的真实事实/批准 → 更新 YAML 及本表定位的三个源 MD → 清理内部制作提示并保留科学披露 → 完成当前 portal/真实表单/费用核查 → 重建 DOCX、PDF、legacy DOC及档案 → 逐页复查所有版面变化并更新最终 manifest/status。正式上传、联系编辑、付费、公开发布和签署不由这个映射或已确认身份事实自动授权。

## 6. 此映射绑定的成品快照

| 文件 | SHA-256 |
|---|---|
| 主稿 DOCX | `8c0530cf61f2f2ca3e7f9d18d074c87aa1058c99f2ca3f0d47000864d2ee841a` |
| 主稿 PDF | `16854cc6d5a786e2a666b2a891c7a08cdc3bc4ec52304bb8baf568f5dc9076f3` |
| 主稿 legacy DOC | `1cc8eb317220fa68ab3f9271e85d3c9a4f1ca38a674b7d49919d52fd25e61bf2`（已有 legacy QA 记录） |
| 补充 DOCX | `cff35e7fd9a924dfaeb19d3c508b1e2022ff9960d3d0cf5b793d4c23353124a5` |
| 补充 PDF | `72eb425640dff5a8460cb35d873a069b47c15d56756531eb16ce7ea04aedc739` |
| cover DOCX | `11e8dd6241409417a827c85b4b5149b80985c1d48b24ab7a30852eb2d47f2116` |
| cover PDF | `0c37f9007148649d8f50208fecf2dae771001b51d30c73333c60464e112d30ed` |

本映射只新增本文件，未改稿件、源码、Word、冻结结果或原有 QA 记录。
