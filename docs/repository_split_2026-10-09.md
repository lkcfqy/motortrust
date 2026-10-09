# MotorTrust 四篇论文独立仓库说明

整理日期：2026-10-09（Asia/Seoul）。四篇论文从原 MotorTrust 项目分别整理，来源提交为
`0cbfc7e5b2868f482902f16d6d0b0c71f9d01f11`。原
[motortrust](https://github.com/lkcfqy/motortrust) 保留历史项目与提交记录，各独立仓库建立自己的提交历史。

## 仓库与数据入口

| 论文 | 代码、稿件和冻结证据 | 原始数据附件 |
|---|---|---|
| Paper 1：健康样本迁移、跨数据集故障检测与失败诊断 | [motortrust-paper1](https://github.com/lkcfqy/motortrust-paper1) | [raw-data-2026-10-09](https://github.com/lkcfqy/motortrust-paper1/releases/tag/raw-data-2026-10-09) |
| Paper 2：转矩曲线代理模型的共形区间与设计分布偏移 | [motortrust-paper2](https://github.com/lkcfqy/motortrust-paper2) | [raw-data-2026-10-09](https://github.com/lkcfqy/motortrust-paper2/releases/tag/raw-data-2026-10-09) |
| Paper 3：调试校准迁移与独立 PMSG 确认 | [motortrust-paper3](https://github.com/lkcfqy/motortrust-paper3) | [raw-data-2026-10-09](https://github.com/lkcfqy/motortrust-paper3/releases/tag/raw-data-2026-10-09) |
| Paper 4：电热模型、校准与温度不确定性的跨电机迁移 | [motortrust-paper4](https://github.com/lkcfqy/motortrust-paper4) | [raw-data-2026-10-09](https://github.com/lkcfqy/motortrust-paper4/releases/tag/raw-data-2026-10-09) |

每个仓库保存本篇论文需要的源代码、协议、文稿、图表、投稿材料、冻结结果和适用的处理数据。
文件沿用原项目相对路径；复制时保留原始字节，并以各仓库的文件清单与 SHA-256 核对。
论文所需的共享模块、参考文献和文稿构建工具按实际依赖复制，因此少数工具仍沿用原文件名。
独立目录不要求克隆其它三篇论文仓库才能检查已保存证据。

原始数据与源码分开保存，各自 Releases 使用标签 `raw-data-2026-10-09`。
这些附件只保存本次本地实际存在、属于该篇范围的数据；数据上传不代表补齐原来缺失的文件，
也不代表重新运行实验。四个 Release 的全部 61 个分卷及清单附件已经上传、校验并发布。
各仓库附有 `scripts/restore_raw_data.py`；从项目根目录使用 `--parts-dir` 指向下载附件目录即可恢复。

## 获取与检查

1. 克隆需要的论文仓库，例如：

   ```sh
   git clone https://github.com/lkcfqy/motortrust-paper2.git
   cd motortrust-paper2
   ```

2. 按该仓库根 README 和论文目录的 `README_REPRODUCE.md` 建立独立 Python 环境，
   先执行保存证据与文件哈希检查。安装依赖不等于恢复冻结实验的软件版本；应同时核对
   `run_metadata.json` 中记录的平台、依赖、输入哈希和实验配置。
3. 需要原始数据重跑时，从对应已发布 Release 下载数据附件及其清单。普通 `git clone`
   不包含这些附件。如提供分卷，必须下载清单列出的全部分卷，再按该 Release 的说明恢复，
   不要把单个分卷当作完整压缩包。
4. 按附件清单检查大小与 SHA-256，将数据放回仓库要求的原相对路径。原始数据的来源、
   作者归属及许可说明应一起保留。原始数据恢复与冻结结果重新生成是不同步骤。
5. 完整实验会重新写入结果与图表。先保留冻结证据，在单独工作副本中执行复现命令；
   不要用新平台生成的输出覆盖已有结果后仍称其为原冻结证据。

预制 Word/PDF 可以直接查看。部分原构建器依赖 Windows 字体；非 Windows 环境的构建或
测试限制以各仓库 README 和实际检查记录为准，不能把拆分后的文件检查称为完整科学复现。

## Paper 3 已有原始数据缺口

Paper 3 独立 PMSG 确认所需的 **225 个原始 MAT 文件在本次拆分前已不在本地项目中**。
已保存的处理特征、输入哈希、协议和冻结结果仍可检查，但这些材料不能恢复缺失的 MAT 信号。
Paper 3 的本次数据 Release 不应被描述为包含这 225 个原始文件。

官方恢复来源：

- DOI：[10.5281/zenodo.15741561](https://doi.org/10.5281/zenodo.15741561)。
- 官方记录：[Zenodo 15741561](https://zenodo.org/records/15741561)。
- 来源项目：[InnovaPower/MitDev-Eletrica，v1.1.0](https://github.com/InnovaPower/MitDev-Eletrica/tree/v1.1.0)。
- 原项目记录的来源提交：`e02fba475cf82b375412a7382143dc29da5241ef`，这是 PMSG 来源项目的提交号。

获取原始数据后，应按 Paper 3 的协议、输入清单和哈希核对版本，再尝试重跑该数据链。
数据缺失发生在拆分之前，拆分过程没有生成或补造原始信号。

## 排除范围与旧草稿状态

本次不上传 `.venv`、Python 解释器和环境二进制、`__pycache__`、测试与静态检查缓存、
`tmp/`、临时渲染文件、可重建的包安装元数据、操作系统缓存、原项目本地 `.git` 数据库及
原始数据来源仓库的嵌套 `.git` 元数据。GitHub 上新建的仓库历史与本地旧 Git 数据库是不同对象。
环境需根据依赖声明及冻结实验记录重新建立。

原仓库标签 `research-snapshot-2026-10-08` 对应的 Release 实际是未完成草稿：只有三个说明附件，
没有完整数据分卷和 `release-manifest.json`。它不能作为已经可下载、可恢复的完整备份。
原 `recovery/RESTORE_CN.txt` 与相关说明保留为历史资料；本次获取数据应使用上表各论文仓库
已发布的 `raw-data-2026-10-09` Release 及其实际附件清单。
