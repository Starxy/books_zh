# 书籍中文翻译

用于持续开展书籍的中文翻译、校订、排版与成品归档。每本书独立维护底本、中文源码、术语表和校对记录，共用翻译规范与工具，支持不断加入新的书籍和领域。

翻译根据底本选择流程：有 TeX 源码时在原工程上译写；只有文本 PDF 或扫描 PDF 时，先提取或识别内容，再重建中文排版。译文以忠于原意、术语准确和符合中文阅读习惯为目标，保留章节结构、数学公式、图表、代码及书前书后材料。

## 阅读与工作入口

- **阅读译本：** [00_books](00_books/) 集中存放已完成的完整中文 PDF。
- **查看或修改某本书：** 从下方书目进入对应目录，查阅源码、术语表、编译说明和校对记录。
- **开展翻译或校订：** 阅读 [AGENTS.md](AGENTS.md) 和 [书籍翻译 skill](.agents/skills/technical-book-translation/SKILL.md)。
- **核对文件与来源：** 查看 [文件整理记录](00_file_organization.json)；[分章拆分总览](00_chapter_split_overview.md) 记录英文原版分章情况。

## 目录组织

```text
00_books/                         已完成的完整中文 PDF 汇总
NN_YYYY_English_Book_Title/        每本书的独立目录
├── 00_originals/                  原版 PDF、原版 TeX、版次与来源信息
├── 01_source/                     中文 TeX、图表、文献、构建脚本和编译说明
├── 02_glossary/                   本书的中英术语与用法约定
├── 03_reviews/                    内容覆盖、疑点、核验和交付记录
└── 05_references/                 辅助文献和参考材料
.agents/skills/                    共用翻译流程、模板与工具
scripts/                          仓库维护检查工具
```

目录和文件名统一使用英文 ASCII 字符。新增维护文件使用小写英文与下划线，例如 `translation_style.md`、`glossary_en_zh.md`、`ch01_review.json`；书籍目录、成品名与原版英文工程资产保留既有命名。文档正文和说明仍使用中文，参考资料目录保留 `05` 编号以延续归档结构。

中文 TeX 是正式译文，直接在 `01_source/` 中维护。完整成品命名为 `English_Book_Title_cn_translated.pdf`，英文单词用下划线连接，每本书仅在根目录 `00_books/` 保留一份完整译本。

有有效 TeX 底本的书保留源码包和英文整书 PDF，按源码章节组织翻译；只有 PDF 底本的书保留用于译校的分章 PDF。

尚未完成的书在自己的校对记录中注明进度。阶段预览、单章测试、提取文本和编译中间文件放在 `work/` 或系统临时目录；完整译本通过核验后再进入成品目录。

校对记录中的 `work/`、`outputs/` 和旧构建目录名称用于追溯历史制作过程，其中临时产物未随仓库归档。记录内的阶段页数、文件名和哈希对应当时的检查结果；当前源码与完整成品以各书正式目录为准。

## 当前书目

以下为已归档的中文译本。书名链接进入对应工程，PDF 链接打开汇总目录中的成品；页数为中文排版页数。

| 原书与工程 | 中文书名 | 完整译本 | 页数 |
|---|---|---|---:|
| [Causality: Models, Reasoning, and Inference](01_2009_Causality/) | 因果性：模型、推理与推断 | [PDF](00_books/Causality_cn_translated.pdf) | 349 |
| [Elements of Causal Inference: Foundations and Learning Algorithms](02_2017_Elements_of_Causal_Inference/) | 因果推断基础：基础与学习算法 | [PDF](00_books/Elements_of_Causal_Inference_cn_translated.pdf) | 197 |
| [Big Data in Omics and Imaging: Integrated Analysis and Causal Inference](03_2018_Big_Data_in_Omics_and_Imaging/) | 组学与影像大数据：整合分析与因果推断 | [PDF](00_books/Big_Data_in_Omics_and_Imaging_cn_translated.pdf) | 673 |
| [Targeted Learning in Data Science: Causal Inference for Complex Longitudinal Studies](04_2018_Targeted_Learning_in_Data_Science/) | 数据科学中的靶向学习 | [PDF](00_books/Targeted_Learning_in_Data_Science_cn_translated.pdf) | 541 |
| [Foundations of Large Language Models](05_2025_Foundations_of_Large_Language_Models/) | 大语言模型基础 | [PDF](00_books/Foundations_of_Large_Language_Models_cn_translated.pdf) | 285 |
| [Agentic Large Language Models](06_2026_Agentic_Large_Language_Models/) | 智能体大语言模型 | [PDF](00_books/Agentic_Large_Language_Models_cn_translated.pdf) | 382 |
| [Causal Inference: What If](07_2026_Causal_Inference_What_If/) | 因果推断：如果 | [PDF](00_books/Causal_Inference_What_If_cn_translated.pdf) | 346 |
| [The Little Book of Generative AI Foundations: An Intuitive Mathematical Primer](08_2026_The_Little_Book_of_Generative_AI_Foundations/) | 生成式人工智能基础小册：直观数学导论 | [PDF](00_books/The_Little_Book_of_Generative_AI_Foundations_cn_translated.pdf) | 196 |
| [The Principles of Diffusion Models](09_2026_The_Principles_of_Diffusion_Models/) | 扩散模型原理 | [PDF](00_books/The_Principles_of_Diffusion_Models_cn_translated.pdf) | 450 |

《生成式人工智能基础小册》于2026-10-25依据同版英文TeX完成译文与排版走查，补建[术语表](08_2026_The_Little_Book_of_Generative_AI_Foundations/02_glossary/glossary_en_zh.md)，修正译法、图中文字和版面问题，重新生成196页中文PDF。原文中需要补充数学条件的表述以译注说明。

《扩散模型原理》于2026-10-25初始化：归档英文v3源码与PDF、用户提供的450页中文PDF，并整理[术语表](09_2026_The_Principles_of_Diffusion_Models/02_glossary/glossary_en_zh.md)。对应中文TeX已缺失，整本复核与源码重建尚未启动；汇总目录中的PDF沿用用户提供的文件。

当前底本与内容范围：

- **Causality：** 2009 年第二版，11 章与结语。
- **Elements of Causal Inference：** 10 章、附录 A—C、参考文献及索引。
- **Big Data in Omics and Imaging：** 7 章、书前材料、参考文献与索引；索引保留原版定位页码。
- **Targeted Learning in Data Science：** 8 个分部、30 章、基础附录和参考文献。
- **Foundations of Large Language Models：** 依据 arXiv:2501.09223v4 源码，6 章、参考文献及中文索引。目录中的 2025 是归档年份，具体底本以 v4 为准。
- **Agentic Large Language Models：** 依据 arXiv:2610.13455v1 源码，23 章、7 个分部引言及按章参考文献。
- **Causal Inference: What If：** 3 个分部、23 章、引言、参考文献及索引；当前中文成品为包含书后材料的 346 页版本。
- **The Little Book of Generative AI Foundations：** arXiv:2605.29713v2，2026-09-08；8章、前言、结语、附录A—B和参考文献，已对照英文源码校订并重新编译。
- **The Principles of Diffusion Models：** 英文底本为arXiv:2510.21890v3，封面日期2026-08-27；四个分部、第1—12章（第12章属尾声与展望）、附录A—D和参考文献，另有摘要、致谢、前言及符号说明。中文PDF已归档，中文TeX待恢复。

## 新增与维护书籍

1. 按现有命名方式建立独立书籍目录，记录原书名称、作者、版次、来源和翻译范围。归档年份与底本版本分别记录。
2. 使用翻译 skill 中的体例模板，先确定专业术语、章节结构及公式、图表、框注等内容的处理方式。校对模板仅在用户明确要求独立报告时使用。
3. 在书籍目录内维护源码和进度，逐章核对原文覆盖、语言、技术内容及版面；完整交付还需检查书前书后材料。
4. 从干净源码编译并核验最终 PDF，发布到根目录 `00_books/`，记录 SHA-256，更新当前书目及文件整理记录。

整理文件或更新清单后，在仓库根目录运行 `python scripts/check_repository.py`，检查英文路径、必要目录、构建入口、书目清单、PDF 与原始资料哈希及 LFS 属性。加 `--include-local` 可同时检查 `work/` 和 `outputs/` 中的路径。该检查不能代替译文校对或整书编译。

## 编译

先阅读目标书 `01_source/README_build.txt`，确认引擎、字体、文献和索引工具。前八本工程在 Windows、Python 3、TeX Live 2026 及相应中文字体环境下验证；《扩散模型原理》因中文TeX缺失，当前入口只说明缺失状态并退出。新增或待恢复工程按自身说明记录依赖。

进入对应书籍的 `01_source/`，运行：

```powershell
python build.py
```

也可使用工程提供的 `build.ps1`。现有构建脚本在系统临时目录编译，成功后将完整 PDF 输出到根目录 `00_books/`，编译失败保留已有成品。Foundations of Large Language Models 还使用 BibTeX 和 upmendex；The Little Book of Generative AI Foundations 使用 Biber，由 latexmk 调用。具体依赖和执行顺序以各书说明为准。

修改正文、文献或图表后，重新核对目录、引用、页码、索引及受影响版面。源码中的图形 PDF、数据、样式和固定文献排版源可能是必要构建输入，清理时依据工程依赖判断。

## Git 与 Git LFS

中文源码、术语表、校对记录、原始资料和必要资产纳入版本管理。所有 PDF 使用 Git LFS，包括原版、分章、图形资产和中文成品；原始 TeX 压缩包作为底本证据保留。过程目录、编译缓存和重复成品压缩包由 [.gitignore](.gitignore) 排除。

安装 Git LFS 后，首次使用仓库执行：

```powershell
git lfs install --local
```

从支持 Git LFS 的远端克隆后，用 `git lfs pull` 获取实际 PDF。新增或更新 PDF 时正常执行 `git add` 和 `git commit`，用 `git lfs ls-files` 检查追踪状态。

仓库说明统一维护在本文件；具体书籍的编译细节和校对结论保留在各自目录。
