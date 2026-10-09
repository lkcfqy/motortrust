# Paper 1 证据与代码审计

核查日期：2026-10-09（Asia/Seoul）。审计对象：Paper 1 保存的细粒度预测、协议、揭盲记录和代码；没有新拟合、选 seed、改阈值或追加实验。

## 结论

所有要求的科学锚点从保存的细粒度输出复算一致。不存在需要更正外部冻结检出率、误报率或 AUROC 的实质计算错误。当前证据足以支持**一台外部物理电机上的条件性方法排名反转与报警失效报告**；不足以证明跨电机总体可靠性、实时能力或因果机制。

原始 `paper/manuscript.md` 和 JEET 包属于历史投稿准备版本。新 JOM 稿为另存的投稿呈现，不改写冻结协议或执行历史。原协议仍有旧题目、“预注册”、Windows 命令和揭盲前状态标题；必须结合执行后注和 reveal log 阅读。本文的冻结是内部 Git 冻结，不是外部注册的预注册。

## 冻结链与首次揭盲

| Commit | 身份 |
|---|---|
| `fddf2f752fb469008cf9552f35a64ffeaf32963c` | 原方法、特征、11 方法集合、外部协议及合成测试冻结 |
| `ca7a1c99945c007873ef4ccce0a9e5e214990515` | 健康校准分数、阈值与健康测试记录 |
| `e01edcf5206f9811c799157a18954e6293905367` | 48 文件官方揭盲清单 |
| `a6d44a965b6eac1fe476d2c5a267e55d1fc2f5de` | 首次读故障前，把 bootstrap 执行对齐到已写明的匝数分层 |
| `a3ab29a70d98c1c1121524b9fcae1aab311314bd` | 首次读故障前，增加保留子系统分数的输出；比较器角色澄清 |
| `e0b58449a583310571736b7b10ea23796116cbe7` | 仅校验下载并行化 |
| `c9f0029cae3f9d3a2b8979b6621fb549a43956e4` | 次级瞬态协议冻结 |
| `e1e2c5ddca6d4c033bd91c492fb675f959c4aa05` | 次级瞬态解析和评估代码冻结 |
| `c09cc4331438934bd68e2a1655c4fa24baca2851` | 次级瞬态首次执行前 clean checkpoint |
| `be0ca5443179b4df16a69cfc8a449499edb86c88` | 保存次级瞬态 0/21 首次失败的结果提交；不是执行前 checkpoint |
| `df31a5a16f90bfc7c80ad7ce258201916604811e` | opt-in、post-reveal 隐式时间解析修复 |

外部首次特征读取完成于 `2026-08-20T14:26:28Z`，首次计分完成于 `2026-08-20T14:26:55Z`。次级瞬态首次解析于 `2026-08-20T16:54:35Z`。UTC 历史时间按原 log 保存；本次审计日期使用 Seoul 本地日期。

## 从低粒度输出复算的关键结果

| 证据 | 分母、复算值 | 来源 |
|---|---|---|
| KAIST Log-Euclidean | 故障 1,608/1,680 = 95.7142857%；健康 0/42；每折 AUROC 平均 0.9993197 | `results/healthy_covariance_v0/target_{1kW,1.5kW,3kW}/scale_free/log_euclidean_entity_covariance/block_predictions.csv` |
| KAIST balanced Isolation Forest | 健康 0/42；42 故障记录宏平均 96.0714286% | `results/oneclass_baselines/record_summary.csv`，固定 seed 20260820 |
| KAIST 比较 | Log-Euclidean 减 balanced IF = −0.3571 百分点；配对记录 bootstrap 区间跨 0 | `comparison_to_proposed.csv`；不能声称主方法全面优越 |
| 外部原冻结主方法 | 故障 96/384 = 25.0000%；健康 1/32 = 3.125%；AUROC 0.6354167 | 主方法 `system_block_predictions.csv` |
| 外部 H1 | Wilson upper 0.1574426382 = 15.7443% > 12%；最大负载健康 FAR 12.5% ≤ 15%；总体 gate 失败 | 同一 32 健康块重算 |
| 外部 target MinCovDet | 故障 269/384 = 70.0520833%；健康 0/32；AUROC 0.9267578；主 seed H1 通过 | `target_min_cov_det/system_block_predictions.csv` |
| 五 seed target MinCovDet | 251–296/384 = 65.3646%–77.0833%；0–2/32 健康误报；3/5 H1 通过 | `external_seed_sensitivity/block_predictions_by_seed.csv.gz`；不是仅抄 range 表 |
| 次级瞬态首揭盲 | 0/21 解析兼容；没有 detector scores | `transient_feature_build/record_compatibility.csv` |
| 次级瞬态修复 | 200 W：12/12；20 kW：4/9，44.44% < 冻结 80% gate | `transient_feature_build_post_reveal_implicit_time/record_compatibility.csv` |
| 200 W post-reveal | 主方法健康 8/176，首秒 0/60，完整两秒 0/120，mean-record AUROC 0.540554；target MCD 健康 9/176、0/60、0/120、AUROC 0.563887 | `transient_pmsm_validation_post_reveal_200w/window_predictions.csv.gz`；12 个方法均无首秒报警 |

外部五 seed 的全部结果如下；不得择优替换 seed 20260820。

| seed | 故障检出 | 健康误报 | H1 |
|---:|---:|---:|---|
| 20260820（固定主 seed） | 269/384（70.05%） | 0/32 | pass |
| 1201 | 293/384（76.30%） | 2/32 | fail |
| 2402 | 262/384（68.23%） | 0/32 | pass |
| 3603 | 296/384（77.08%） | 1/32 | fail |
| 4804 | 251/384（65.36%） | 0/32 | pass |

## 细粒度一致性与身份核查

新增只读 `scripts/audit_jom_evidence.py` 实际执行通过，输出 `submission/jom/evidence_audit.json`。它：

- 对全部 11 个外部方法检查系统分数为两子系统最大值；24 校准块和适配/校准/测试负载角色保持冻结划分；从校准分数重新生成每一行 p 值和报警。
- 检查 4 个随机比较器 × 5 seeds 共 20 组逐块输出；主 seed 的分数与冻结输出一致到绝对误差 1e-8 内，报警完全一致。全 seed 输出无需重新拟合即可审计。
- 对瞬态逐窗输出重新计算首秒、两秒、误报和 mean-record AUROC；检查 heldout/fit/calibration 记录无交叠、校准窗不少于 19、逐窗报警等价于 p≤0.05。
- 核对 reveal log 中 7 个原始兼容性、onset 和计分输出文件 SHA-256，全部匹配；未改写它们。历史 metadata 的路径可能需要在导出 ZIP 中脱敏，因此这些 metadata 的原始哈希仍在项目和 reveal log 保留，不能把脱敏导出件称为同 bytes 原件。

另外只在原项目中核对 3 个 transient 原始 run metadata 与 4 个 processed inputs 的哈希，均与原 reveal log/冻结 metadata 一致。该额外核对在 `tmp/jom/original_artifact_hash_check.json`；导出包不要求包含这些原始本机路径字段。

原 `scripts/validate_manuscript_evidence.py` 也执行通过，baseline 输出另存 `tmp/jom/evidence_baseline.json`，没有覆盖 `results/manuscript_evidence_validation/evidence.json`。

## 必須保持的科学限制

1. KAIST 目标故障在开发时已被观察，因此是 exploratory；3 台源族电机各只有 1 条唯一健康记录。
2. 外部 48 条故障记录、384 宏块和两个子系统来自 1 台物理电机。任何 block、window 或 subsystem 都不能增加独立电机样本数；记录 bootstrap 区间仅条件于此电机的记录工况。
3. 外部匝数 1/3/5/6 固定相 U，2/4 固定相 V；匝数与相别不完全交叉，不能分离效应。
4. pooled AUROC 将 8 个故障负载与 4 个 held-out 健康负载比较，是非负载匹配的描述性 ranking statistic。
5. 工况、block 位置、速度与分数共变不能证明单一因果作用；速度 proxy 来自同负载健康轨迹，不能冒称每个故障记录的实测速度。
6. Wilson 区间和共形 p 值受依赖结构、不同负载支持和缺少独立健康 sessions 的限制；不构成总体风险/安全保证。
7. 全部离线；未进行 feature latency、memory 或嵌入式 numerical stability 测试。
8. transient 0/21 是解析合同失败；修复后 200 W null sensitivity 是 post-reveal、单物理电机、非确认性，不能替换原失败或称第三数据集确认。
9. Paper 3 的条件化改进不进入 Paper 1 冻结结果；本次未借用或重拟合该研究。

## 现有诊断足够性

现有诊断覆盖具体审稿质疑：early-trajectory coverage（首 4/7/8 block）、负载和匝相分层、同算法 target-only 对照、五 seed 稳定性、score/block association、块位置 AUROC、冻结几何重建及特征贡献、100 kHz→10 kHz 的单因素敏感性、次级解析/起点可行性审计。它们已足以解释条件性失败并界定部署注意事项；本次没有默认添加深度模型、新数据或硬件实验。

主方法 block 0–2 故障报警均为 0/48，block 7 为 48/48，唯一健康误报也在 block 7。第一四块检出 2.60%，第一七块 14.29%，全部八块 25.00%。因此 48/48 record-any 不能作为早期检测成功。现有 sampling control 为 25.00%→24.74%、AUROC 0.6354→0.6331、健康仍 1/32，不能断言采样率不影响任何其他模型/条件。

需要新增独立电机、实验室或健康 sessions 才能解决的限制保持限制，不能通过当前已揭盲数据反复调参解决。

## 代码基线与必要修复

全部使用 `/Users/lkc/miniforge3/envs/motortrust/bin/python`。当前 Python 3.12.15、numpy 2.5.3、pandas 3.0.6、scipy 1.18.1、scikit-learn 1.9.1。原外部输出 metadata 记 scikit-learn 1.9.0；未找到完整的原冻结环境 lock。当前环境用于证据复算和构建，不能声称与原训练环境 bitwise 等同。

| 检查 | 结果 / 日志 |
|---|---|
| `python -m pip check` | pass，`tmp/jom/pip_check_baseline.log` |
| 原 evidence validator | pass，`tmp/jom/evidence_validator_baseline.log` |
| 初始 Ruff：`python -m ruff check src scripts tests` | pass，`tmp/jom/ruff_baseline.log` |
| 初始全测试 | 271 个测试：266 pass / 5 fail，`tmp/jom/pytest_baseline.log` |
| Wilson 修复后，不含 4 个已知 Paper 2–4 失败模块的广泛回归 | 263 pass，`tmp/jom/pytest_after_wilson_fix.log` |
| 最后相关回归：fault baseline / seed / feature drift / evidence validation | 19 pass，`tmp/jom/paper1_fix_tests.log` |
| 修改过的 Paper 1 文件 Ruff | pass，`tmp/jom/paper1_fix_ruff.log` |
| 改后的真实冻结特征加载（不计分） | 两个 loader 均读到 27,000 source / 13,440 external rows、27 features；geometry loader 448 frozen blocks，`tmp/jom/portable_feature_loaders.log` |

**修复 1 — Wilson 数值边界。** `wilson_interval(0,42)` 原返回下界 6.9388939039e-18，违背既有 exact-zero 测试；显式令 k=0 下界=0、k=n 上界=1。上界公式、1/32 interval 和所有 frozen files 不变；没有科学结论、H1 判定或打印百分比变化。

**修复 2 — 保存路径的可移植加载。** `run_external_seed_sensitivity.py` 与 `analyze_external_feature_drift.py` 原直接使用 metadata 内历史 Windows absolute input paths，在本机不成立。新增显式 `--source-features` / `--external-features`；历史路径不存在时回到项目固定 input filename。已有 SHA-256 验证仍在读取前执行，不能引入不同特征或替换数据。原 metadata 不变；仅实际验证加载并运行已有测试，未重拟合 stochastic baseline。

保留范围外问题：Paper 2/3/4 的 3 个 PDF audit 因共享 JEET renderer 的 Windows 字体路径失败；Paper 3 supplement 的路径分隔符使生成文本不同。它们不会进入独立 JOM renderer/稿件；不在本次修复或重建 Paper 2–4。

本报告的 baseline 不是最终包的全文数字/交叉引用/视觉 QA；最终构建、ZIP 和逐页结果见 `QA_Report.md`。
