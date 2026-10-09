# JOM 门户可提交性：补充只读核查

核查日期：2026-10-09（韩国时间）。这是对已有规则审计的定向补充，未替换原始核查记录。作者随后明确：**尚无投稿账户**。按作者最新要求，此处停止门户探索，回到论文详细审阅。

## 已解决到哪一步

| 项目 | 可查证结论 | 官方来源或留档 |
|---|---|---|
| 真实作者登录入口 | 官方 Online Submission 按钮指向 `/submission/login.jsp?ViewFlag=author`，跳转到作者登录页。实际公开界面提供 Author / Reviewer / Editor、Email address、Password、LOGIN。 | [官方作者登录入口](https://jom.magnetics.or.kr/submission/login.jsp?ViewFlag=author)；`reference_evidence/portal_readiness/login_public_2026-10-09.html` |
| 国际作者注册入口 | 登录页分别提示学会会员用 Society ID，国际作者用 Create account。该可见链接指向 `/users/join.vm`。这证明存在国际作者投稿账号注册路径，**不证明中国籍、韩国单位的非会员可免入会或免会费投稿**。 | [官方国际作者注册首页](https://jom.magnetics.or.kr/users/join.vm)；`international_account_public_2026-10-09.html` |
| 注册第一步边界 | root 的实际浏览器及本次公开 HTML 均显示 Personal Information Collection and Use Agreement、未勾选的 Agreement、Email(ID)、NEXT。协议涉及 ID/password、姓名、生日、单位、职位、手机、邮箱及账户存续期留存。表单后续是 POST，不能为了查看后续界面代作者接受协议。 | 同上；`international_account_parsed.json` 保存字段 `_confirm1`、`_email`、NEXT。未勾选、未输入、未点击 NEXT。 |
| 当前 DOC 模板 | 官方下载仍为 `JoM_Template.doc`，与已归档 36,352 字节文件逐字节一致。只读检查其原始 Compound File 目录及此前转换的 DOCX：未发现嵌入对象或附加版权/checklist 文件，模板正文也没有这些表单。 | [官方模板](https://jom.magnetics.or.kr/download/JoM_Template.doc)；`official_template_attachment_check.json`、`original_doc_compound_directory.json` |
| checklist/copyright 获取位置 | 官方公开投稿页要求在投稿系统中查看两种表单。公开页面的附件链接、模板内部及限定官方域名的定向检索，仍未找到可下载的实际空白表。不能说表单不存在；只能说在当前未登录范围内未找到。 | [官方投稿步骤](https://jom.magnetics.or.kr/submission/journal/pages/online_submission.vm)、[官方作者指南](https://jom.magnetics.or.kr/submission/journal/pages/instructions_authors.vm) |
| 研究生会员公开费用 | 学会英文会员页列 Graduate Student Member 的 Annual Membership Fee 为 **50,000 KRW**，Subscription Fee 栏为 **20,000 KRW**。该页没有说明国际作者是否必须购买会员/订阅，故不得将二者自动加为作者必缴款。 | [学会 About Membership](https://www.magnetics.or.kr/eng/html/about_membership.vm)；`about_membership_public_2026-10-09.html` |

## 尚未解决的问题及确切查看位置

1. **账户/资格**：作者本人进入 [Create account](https://jom.magnetics.or.kr/users/join.vm)，决定是否接受隐私协议并注册。只读核查未见注册后字段或会员验证，因此不能预先断言国籍、居住地或单位会如何判定作者类别。公共投稿页的“仅学会会员可投稿”与登录页的国际作者路径仍有适用性歧义。
2. **实际表单和文件槽位**：作者注册、以 **Author** 登录后，在系统的新投稿流程内查找官方明示的 **Copyright Transfer Form**、**Author's Check List Form**。该流程的具体菜单名、是否下载文件或电子勾选、签署时点、附件槽位、补充材料限制，未在当前公开界面验证；不猜测菜单或按钮。准备稿不能替代实际表单。
3. **收费类别**：在作者账户及投稿流程提供的身份/费用说明中确认本人是否适用外国作者 USD 300（前5出版页）及 USD 10/额外页、是否强制入会或订阅、全部附加费。若界面没有给出明确答案，费用仍待官方确认；本任务未联系编辑。灰度图方案已准备，未申请付费彩印。
4. **提交前复核**：正文作者电话/传真与未确认声明、实际表单及当前接受的 Word 格式须落实；检查系统生成的审阅文件，再由作者决定是否进行最后提交。

## 能否真正“一键终提交”

**现在不能承诺。** 作者无账户，隐私协议由本人决定，登录后实际表单/槽位及非会员费率仍未验证。完整论文文件包能减少上传准备，但不等于已完成系统要求。当前最少门户动作是：本人注册登录 → 核实资格/费用及官方表单 → 完成实际必填项和表单 → 检查系统审阅文件 → 本人执行最终提交。无需因此扩展实验。

只读证据目录：[portal_readiness](reference_evidence/portal_readiness/)；来源与哈希：[SOURCE_MANIFEST.json](reference_evidence/portal_readiness/SOURCE_MANIFEST.json)。既有[费用与上传指南](Costs_and_Upload_Guide_CN.md)仍适用。

本次未登录、未创建账户、未接受条款、未联系编辑、未付款、未签署、未上传或提交。已停止进一步门户探索。
