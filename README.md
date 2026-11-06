# 书籍中文翻译

本项目整理技术书籍的中文译本，涵盖因果推断、人工智能、临床研究等领域。每本书独立维护原版资料、中文 LaTeX 源码、术语表和校对记录，完整中文 PDF 集中存放在 [00_books](00_books/)。

## 当前书目

点击 PDF 阅读译本，点击原书名查看源码与相关资料。页数为中文 PDF 页数。

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
| [A Definition and Roadmap for World Models](10_2026_A_Definition_and_Roadmap_for_World_Models/) | 世界模型的定义与发展路线图 | [PDF](00_books/A_Definition_and_Roadmap_for_World_Models_cn_translated.pdf) | 63 |
| [Designing Clinical Research](11_2023_Designing_Clinical_Research/) | 临床研究设计 | [PDF](00_books/Designing_Clinical_Research_cn_translated.pdf) | 515 |
| [Deep Generative Modeling](12_2024_Deep_Generative_Modeling/) | 深度生成建模（第二版） | [PDF](00_books/Deep_Generative_Modeling_cn_translated.pdf) | 341 |
| [Large Language Models: A Deep Dive](13_2024_Large_Language_Models_A_Deep_Dive/) | 大语言模型深度解析：贯通理论与实践 | [PDF](00_books/Large_Language_Models_A_Deep_Dive_cn_translated.pdf) | 462 |
| [Efficient LLM Inference](14_2026_Efficient_LLM_Inference/) | 大语言模型高效推理 | [PDF](00_books/Efficient_LLM_Inference_cn_translated.pdf) | 55 |
| [Mathematical Foundations of Artificial Intelligence: Basics of Manifold Theory](15_2026_Mathematical_Foundations_of_Artificial_Intelligence_Basics_of_Manifold_Theory/) | 人工智能的数学基础：流形理论基础 | [PDF](00_books/Mathematical_Foundations_of_Artificial_Intelligence_Basics_of_Manifold_Theory_cn_translated.pdf) | 359 |

《扩散模型原理》目前收录用户提供的中文 PDF，中文 TeX 缺失，源码恢复与整本复核尚未完成。各书的底本与校订说明见对应目录。

## 目录组织

```text
00_books/                         完整中文 PDF
NN_YYYY_English_Book_Title/        每本书的独立目录
├── 00_originals/                  原版资料与来源说明
├── 01_source/                     中文 LaTeX 源码、图表与编译入口
├── 02_glossary/                   中英术语表
├── 03_reviews/                    校对记录与进度
└── 05_references/                 辅助参考资料
```

中文译文直接在 `01_source/` 中维护。阶段稿和编译中间文件放在 `work/` 等临时目录，不纳入 Git。

## 获取 PDF

仓库中的 PDF 使用 Git LFS 管理。克隆仓库后，安装 Git LFS 并在仓库根目录运行以下命令，获取实际 PDF 文件：

```powershell
git lfs install --local
git lfs pull
```

## 编译与维护

先阅读目标书的 `01_source/README_build.txt`，准备所需的 TeX 引擎、字体和其他依赖，再进入该书的 `01_source/` 运行：

```powershell
python build.py
```

也可使用 `build.ps1`。编译成功后，完整 PDF 输出到根目录 `00_books/`。

翻译、校订或新增书籍，请先阅读 [项目约定](AGENTS.md) 和 [翻译流程](.agents/skills/technical-book-translation/SKILL.md)。文件来源与归档信息见 [文件清单](00_file_organization.json)，英文原版的分章情况见 [分章总览](00_chapter_split_overview.md)。整理文件或更新清单后，在仓库根目录运行 `python scripts/check_repository.py` 检查。
