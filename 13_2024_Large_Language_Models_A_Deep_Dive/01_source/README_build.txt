《大语言模型深度解析》编译说明

需要 Python 3.10+、TeX Live 的 XeLaTeX、latexmk 和 Perl。字体使用 TeX Live
自带的 Fandol（宋、黑、楷）、TeX Gyre Termes、Heros、Cursor 和 Termes Math。
文献由各章 TeX 文件中的条目排印。索引位于 index.tex 和 index_terms.tex，随 LaTeX 编译，无需另行运行索引程序。
assets/ 中的图形 PDF 来自同版英文 PDF。重绘图形使用工程中的 TikZ 源码。
编译从新的系统临时目录执行。控制台输出包含该目录，可在其中查看编译日志。

在本目录运行 python build.py，也可运行 .\build.ps1。
完整译本默认输出至仓库根目录 00_books/Large_Language_Models_A_Deep_Dive_cn_translated.pdf。
使用 --output-directory 可指定试排目录。编译通过后才替换目标文件。
