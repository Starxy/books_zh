# 沿用的译排设置

本文件说明导入源码中已有的排版设置，不评价翻译质量。正文、图表和参考文献保持所提供中文源码包的内容。

- 底本：Tianhua Chen，*The Little Book of Generative AI Foundations: An Intuitive Mathematical Primer*，arXiv:2605.29713v2，书名页日期为2026-09-08。
- 入口：`main.tex`；使用 `ctexbook`、12pt、单面排版，页边距为1英寸。
- 语言字体：拉丁文字为 Noto Serif；中文正文字体为 Noto Serif CJK SC，无衬线与等宽字体分别为 Noto Sans CJK SC 和 Noto Sans Mono CJK SC。
- 结构：前言、目录、8章正文、结语、附录A—B及参考文献；章节顺序由 `main.tex` 中的 `include` 指定，保留原包的章节文件名。
- 定义、例、定理分别按章计数；保留源码中的公式标签和交叉引用。
- 框注沿用 `ConceptBox`、`DerivBox`、`InsightBox`；保留常见问题、练习和要点总结环境。
- 插图由 `figures/` 中的 TeX 和独立 PDF 提供，保持原有相对引用。
- 参考文献使用 `biblatex` 和 Biber，配置为 `style=numeric`、`sorting=nyt`，数据来自 `references.bib`。
- 此次输入没有独立术语表；未从正文另行提取或更改译名。

编译方法和环境要求见 `README_build.txt`。
