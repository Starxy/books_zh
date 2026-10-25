# arXiv:2605.29713v2 中文翻译版源码

- 原作：Tianhua Chen，*The Little Book of Generative AI Foundations: An Intuitive Mathematical Primer*。
- 本目录为中文翻译版 TeX 源码，对应 `arXiv:2605.29713v2`。
- 该版 [arXiv 页面](https://arxiv.org/abs/2605.29713v2) 的许可链接指向 [arXiv 非独占分发许可](https://arxiv.org/licenses/nonexclusive-distrib/1.0/license.html)，并非 CC BY 4.0；中文导入稿原有的 CC BY 4.0 标注已删除。原书前言中的再利用说明保留。
- 2026-10-25 已依据英文 TeX 逐节走查译文并重新编译，修正术语、图中文字、长标题断行及图内重叠。
- 数学公式、标签、交叉引用、文献引用键以及参考文献题录保持原结构；对原文需要限定条件的数学表述另加明确译注。
- 正文、章节标题、图题、TeX 图及独立 PDF 图中的说明文字已中文化；人名、模型缩写、变量和数学下标保留。
- [术语表](../02_glossary/glossary_en_zh.md)按英文术语及语境维护。[译排设置](translation_style.md)说明字体、编号与译注处理。

## 编译

需要 XeLaTeX、Biber、`ctex` 以及 Noto CJK 字体。在本目录运行：

```powershell
python build.py
```

主文件：`main.tex`。依赖和工作目录输出方法见 [README_build.txt](README_build.txt)。正式 PDF 位于仓库根目录 `00_books/`。
