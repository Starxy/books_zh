《世界模型的定义与发展路线图》编译说明

中文工程
入口：main.tex
正文：sections/下八个TeX文件，输入次序与原包一致。
文献：wm-pjlab.bib，使用plainnat和natbib的作者—年份格式。
样式：原包colm2025_conference.sty与ailablogo.pdf，原样保留。
中文排字：chinese_typography.tex，在原模板上设置中文字号、行距、标题、段落、图注、脚注与文献间距。
图形：figs/下九张PNG及training-paradigm.pdf，均直接来自原包，内容未改动。
表格：sections/architecture.tex中的原TeX表格，只翻译文字，保留原行列和格式。
原始TeX压缩包与英文PDF保存在../00_originals；编译所需样式、图形已放入本目录。

依赖
Python 3（构建脚本仅使用标准库）。
TeX Live及其latexmk、XeLaTeX、BibTeX，xeCJK、fontspec、fontenc、etoolbox、indentfirst、caption、needspace、xurl及原工程宏包。
文档类沿用article，版式沿用colm2025_conference的preprint设置与原geometry参数。
中文采用TeX Live自带的Fandol字体；T1编码保留原样式的URW Palladio西文字体及mathpazo数学字体。
纸张、版心、标题层级、页眉页脚、图表调用尺寸与浮动位置选项、参考文献体系沿用原工程。
正文11pt、行距17.6pt，宋体正文配黑体标题，首行缩进两字；图注10/15pt，脚注9/13.5pt，文献9.5/12.5pt。
目录后另起正文，页底允许自然留白，图文混排页至少保留12%的正文高度；公式（9）分两行排印，数学内容与编号保留。具体设置见translation_style.md。
本工程无独立索引、外部代码高亮或必须开启shell escape的步骤。

运行
在本目录运行：
  python build.py
或：
  .\build.ps1

在仓库根目录运行：
  python 10_2026_A_Definition_and_Roadmap_for_World_Models/01_source/build.py

构建器复制01_source到新的系统临时目录，在其中调用latexmk，由其按依赖运行XeLaTeX、BibTeX并重编目录与引用。
使用-no-shell-escape；检查未解析的引用、引文与缺字后，才复制PDF到根目录00_books。
编译失败保留临时目录和console.txt，不覆盖已有成品。

过程预览
  python build.py --output-directory ../../work/world_models_preview --keep-work
--keep-work保留临时源码、日志及中间文件，便于查看具体页面；正常成功构建会清理其新建的临时目录。
--output-directory仅改变PDF复制位置，不改变正文与图形输入。

维护图文
修改正文或文献后重新运行构建，并检查受影响页面、目录与引用。
原包没有提供十幅图的图内源码，因此保留原图及图内英文，不从PDF提取后重修，不遮字或重绘。
只翻译TeX中的图注、表题及已有TeX表格文字；保留原有位置、尺寸与表格格式。
原文笔误处理见translation_style.md；长URL由xurl断行，保持链接目标完整。

仓库检查
完整成品归档、更新根目录README与00_file_organization.json后，在根目录执行：
  python scripts/check_repository.py
所有PDF和原始源码压缩包依照.gitattributes使用Git LFS。
