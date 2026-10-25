# 译排设置

本书以提供的中文源码为起点，依据同版英文 TeX 校订。2026-10-25 已对照正文和前后材料，并检查重新编译的页面；以下约定用于后续维护。

- 底本：Tianhua Chen，*The Little Book of Generative AI Foundations: An Intuitive Mathematical Primer*，arXiv:2605.29713v2，书名页日期为2026-09-08。
- 入口：`main.tex`；使用 `ctexbook`、12pt、单面排版，页边距为1英寸。
- 语言字体：拉丁文字为 Noto Serif；中文正文字体为 Noto Serif CJK SC，无衬线与等宽字体分别为 Noto Sans CJK SC 和 Noto Sans Mono CJK SC。
- 中文强调采用正文族的倾斜形式；长章标题按语义断行，目录与书签使用不带换行的完整标题。目录页码栏容纳三位页码。
- 结构：前言、目录、8章正文、结语、附录A—B及参考文献；章节顺序由 `main.tex` 中的 `include` 指定，保留原包的章节文件名。
- 定义、例、定理分别按章计数；保留源码中的公式标签和交叉引用。
- 框注沿用 `ConceptBox`、`DerivBox`、`InsightBox`；保留常见问题、练习和要点总结环境。
- 插图由 `figures/` 中的 TeX 和独立 PDF 提供，保持原有相对引用。说明文字译为中文，曲线、散点、数值和数学符号沿用原图；人名、缩写与数学下标保留。PDF 图的文字替换表及生成方法见 `README_build.txt`。
- 参考文献使用 `biblatex` 和 Biber，配置为 `style=numeric`、`sorting=nyt`，数据来自 `references.bib`。
- 术语见 `../02_glossary/glossary_en_zh.md`，按语境区分：统计 inference 为“推断”，intractable 为“难以计算”，noisy score 为“带噪分布的得分”。不把可计算性与实际求值困难混为一谈。
- 参考文献题录保留英文可检索信息。原书没有索引，不增设索引。

原文中的数学限制用明确的“译注”说明，保留原推导：第1章说明 PCA 最优方向可能不唯一、总方差不变需要正交基变换、对称矩阵的 SVD 中取同一组左右奇异向量还需半正定条件；第4章说明狄拉克分布的对数不能直接当作有限常数，并指出保留首步重构项的推导方式；第5章说明光滑函数不一定等于其无穷 Taylor 级数。译注与作者正文区分。

编译方法和环境要求见 `README_build.txt`。
