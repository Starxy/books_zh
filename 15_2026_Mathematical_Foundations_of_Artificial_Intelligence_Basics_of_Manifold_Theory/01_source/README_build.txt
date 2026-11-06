《人工智能的数学基础：流形理论基础》中文工程

需要 Python 3.10+、TeX Live 的 XeLaTeX、latexmk 与 Perl。中文字体使用
TeX Live 自带的 Fandol，西文与数学使用 TeX Gyre Pagella。主文件为 main.tex。
章末书目和索引使用 TeX 文件中的固定排版条目。

在本目录运行 python build.py 或 .\build.ps1。编译从新的系统临时目录执行。
终端输出列出构建目录，可在其中查看日志。--output-directory 可指定输出位置。
完整译本默认输出至仓库根目录 00_books/Mathematical_Foundations_of_Artificial_Intelligence_Basics_of_Manifold_Theory_cn_translated.pdf。
预览时用 --output-directory 指定 work/ 中的目录。编译失败时保留已有 PDF。
