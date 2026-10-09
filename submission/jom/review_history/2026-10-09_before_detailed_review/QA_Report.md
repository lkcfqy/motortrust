# Paper 1 / Journal of Magnetics 最终 QA 报告

核查日期：2026-10-09（Asia/Seoul）。状态：**作者最终审阅准备包；尚不能直接上传**。作者联系信息用于私有审阅，不作公开发布。本任务未执行正式投稿、编辑联系、付款、公开发布或版权签署。

## 研究与历史保护

- 工作分支 `codex/paper1-jom`；初始 `main` 工作区干净，适用路径未发现 AGENTS.md。旧 JEET 包、`paper/` 原稿、全部原冻结结果及协议保留，Paper 2–4 未并入研究。
- 新 JOM 稿、補充材料、投稿信使用独立源。内部 Git 冻结、首次读取前执行调整、揭盲与后诊断分别说明；内部冻结不是外部注册的预注册。
- 未新拟合、改窗口/特征/划分/阈值/指标/排除，未选择 seed 或把 MinCovDet 换作主方法。现有诊断足以回答本轮具体审稿质疑，没有默认添加深度模型、硬件实验或新数据集。
- 当前 scikit-learn 1.9.1 与历史 metadata 1.9.0 有差异；未找到完整原训练环境锁。保存的预测及揭盲哈希是参考，未将当前环境重训输出覆盖冻结证据；未宣称完成全原始信号重训。

## 科学锚点与呈现一致性

| 核验项 | 细粒度复算 / 结论 |
|---|---|
| KAIST 主方法 | 1608/1680 = 95.71%；健康 0/42；exploratory |
| 外部冻结 Log-Euclidean 主方法 | 96/384 = 25.00%；健康 1/32；pooled AUROC 0.6354 |
| 外部健康 gate | Wilson upper 15.7443% > 12%；gate 失败 |
| 外部 target-only MinCovDet | 固定主 seed 269/384 = 70.05%；健康 0/32；预先实现比较器 |
| MinCovDet 五 seeds | 检出 65.36%–77.08%；健康误报 0–2/32；gate 3/5 通过 |
| 次级瞬态 | 冻结解析器 0/21 保留；修复后两电机 gate 仍失败；200 W-only 是 post-reveal、非确认性 |
| 次级窗口分母澄清 | 176 是 12 个 held-out 记录合计健康窗；每记录 5 个首秒及 10 个两秒故障窗；结果字节不变 |

所有外部方法从系统块输出核验 p 值、两子系统最大值、角色划分和报警；20 个随机方法×seed组合及主 seed 一致性核验完成。瞬态逐窗端点、记录划分和七个不可变文件 SHA-256 通过。追溯路径见 `Evidence_Audit.md` 和 `evidence_audit.json`。

摘要 124 词、6 个关键词。主稿、摘要、表图、补充材料和 cover letter 对外部失败、主/比较器身份和局限保持一致；30 条主稿引用元数据与正文支持关系核验完成。Park 2025 JOM 文献是绕线同步电机 FEM 研究，未误称 PMSM 或借用实时结论。Wang 2019 的官方 CVF/IEEE 页码冲突已记录，JOM 显示条目省略争议页码。引用审计见 `Reference_Audit.md`。

## 必要开发、环境与测试

所有科学检查、authoring 和打包使用 `/Users/lkc/miniforge3/envs/motortrust/bin/python`，未误用系统 Python。文档渲染使用单独的 Codex bundled Python + headless LibreOffice。

| 检查 | 最终结果 |
|---|---|
| pip check | 通过，无 broken requirements |
| 原稿证据验证器 | 通过，输出到 tmp，未覆盖冻结验证报告 |
| 新细粒度 JOM 审计 | 通过，只读原结果 |
| Ruff，src/scripts/tests | 通过 |
| git diff --check | 通过 |
| 全项目 pytest | **272 passed / 4 failed**，最终复核 4.73 s |
| Paper 1 相关回归（含 5 新测试） | **24 passed** |
| 独立解包代码 ZIP | 两验证器、Ruff、**134 passed（2.74 s）**；导入来自最终 final4 解包 src |

最终全项目日志：`tmp/jom/final_pytest_full_after_delivery.log`。4 个全项目失败均在范围外：`test_paper2_supplementary_pdf.py`、`test_paper3_supplementary_pdf.py`、`test_paper4_supplementary_pdf.py` 使用旧共享 JEET renderer 的 Windows 字体路径；`test_paper3_supplementary_material.py` 的既有补充稿路径分隔符不同。它们不进入 JOM 构建器，不影响本次 Paper 1 验证；没有为获得全绿测试扩展或重建其他论文。

实质修复只有 Wilson k=0/n 端点浮点残差和冻结输入路径可移植读取。前者不改上界、1/32 区间或结论；后者保留原输入 SHA 验证，显式不存在的 override 报错。新构建器还处理字体、A4/双倍行距、Roman 表页、独立图注、编号可编辑 OMML 公式、引文、灰度图件、导出脱敏和手工 Word 修改保护。

## 文档渲染与逐页视觉检查

- 主稿 DOCX → 实际 LibreOffice PDF：**28/28 页逐页看 PNG**；5 个可编辑 OMML 公式、inline 下标、30 连续引用、表 I–III、6 核心灰度图均可读，无蓝线、裁切、重叠、缺字或错误图号。
- 补充 DOCX → 实际 PDF：**22/22 页逐页看 PNG**。七张宽表拆成重复主键的配对表，值和顺序不变；S0 将“主方法与11比较器”更正为主方法与10比较器（总计11方法），不改输出；避免断数字和狭窄列。5 个补充图、完整失败诊断和页码通过。最后一次计数措辞修正后第1页已实际复看，其余21个 PNG 与已审页面哈希完全相同。
- Cover letter DOCX → 实际 PDF：**1/1 页逐页看 PNG**；标题、数字、真实独作/无经费信息及待确认声明完整，无裁切。
- 具体已审页面 SHA 记录在 `reference_evidence/final_*_visual_review.json`。`delivery_status.json` 每次打包将当前渲染 PNG 与这些已审 SHA 逐一比较；更改文字/字段/字体/图件后若不一致，必须重新做视觉 QA，不能借用旧结论。
- 本机常用安装路径未发现 Microsoft Word。已用可用 LibreOffice 作实际检查；**原生 Word 字段更新、字体替代及页面复核仍需作者执行**。主稿 Word 页数是双倍行距审阅页数，不是计费出版页数。
- Legacy DOC 的当前二进制已实际重渲染并核验与逐页检查的 28 页 PNG 全部相同，正文/五公式/三表/六图内容完整；与 DOCX 的微小间距差异不影响内容。逐页转换检查另存 `reference_evidence/legacy_doc_visual_review.json`；以该记录为准，不能把 LibreOffice 验证称作 Microsoft Word 验证。

## 可复现包及重建

从项目根目录执行：

```bash
/Users/lkc/miniforge3/envs/motortrust/bin/python scripts/package_jom_delivery.py
```

该命令调用核心 builder 完成两个证据验证、DOCX/PDF/legacy DOC、图件和代码 ZIP，再生成图源 ZIP 与完整私有审阅 ZIP。该完整默认命令已实际执行成功（exit 0），最终实际命令日志为 `tmp/jom/delivery_rebuild.log`，构建元数据为 `build_metadata.json`，交付 CRC/manifest 为 `delivery_archive_metadata.json`。若直接编辑 Word，新构建器会保护与上次哈希不同的 Word；先同步修改至 Markdown，只有明确选择 `--overwrite-docx` 才覆盖。

代码 ZIP 独立解包验证：没有 raw/processed 数据、大型无关文件、Paper 2–4 实验、credentials、作者真实联系方式或本机执行绝对路径。所有 result CSV/gzip 与原文件逐字节一致；metadata 脱敏是导出副本，不冒称原始 metadata bytes。最大代码包单文件约 1.00 MB。完整审阅 ZIP 包含真实作者信息，是**私有作者资料**；不含第三方参考论文全文 PDF 或临时页面图片。ZIP CRC 与 manifest 全量核验通过，最终代码 ZIP 为 7,539,054 bytes、567 manifest 项（另加 manifest 自身），SHA-256 `247a2075054077b6119277ac98f591fad154ecf64729bcae0fd44022c32c3894`。完整私有ZIP最终大小/哈希以机器记录为准。

随包 `Current_Environment.txt`、`Reproducibility_Guide.md`、公开数据 DOI/许可与实际 CLI 命令均已检查。无需下载约 GB 级原始档即可核验保存证据；信号级重算另需原数据，写入独立 tmp 输出并与冻结证据对照，不能称新确认。

## 费用与未满足的验收项

官方公开规则核查日期为 2026-10-09，链接和快照保存。外国作者英文计费条件下，8–12 个最终出版页基础/超页费为 **USD330–370**。作者中国籍、韩国单位、非会员的类别适用性及会员要求、彩图和其他强制费用未由公开页解决，**不能确认总支出已低于USD500**。默认灰度核心图降低付费彩印需求，但不是官方免收费承诺。

| 未完成事项 | 原因 / 最少作者行动 |
|---|---|
| 电话/传真、利益冲突、致谢 | 尚未提供事实；本人填写/确认 |
| 原创/无同时投稿/权限、AI责任与最终批准 | 必须真实确认；当前明确占位，不替作者批准 |
| 真实官方 checklist / copyright | 公开页找不到当前原件；由作者登录系统取得、转填并签署；本包为未签署准备稿 |
| 投稿账户、Word类型、supp/code槽位、AI字段 | 官方旧 DOCX 措辞和会员规则有冲突；确认当前 portal |
| 所有强制费用与学校认可 | 核实身份费率、总额≤500及学校规则 |
| 原生 Word 最终字段/页复核 | 本机可行检查已完成；作者提交前更新全部字段并看生成审阅文件 |

尚有这些作者/官方信息缺口，因此交付称**完整作者审阅准备包**，不称可直接上传。科学局限仍是单外部物理电机、依赖结构、匝数与相位混杂、pooled AUROC 支持不同及工况关联不能识别因果；共形/Wilson不构成总体安全保证，全部离线。此轮已达到可核验的研究与制作范围，停止扩展实验。
