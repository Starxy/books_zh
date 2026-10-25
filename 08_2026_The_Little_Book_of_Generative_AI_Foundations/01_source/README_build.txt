《生成式人工智能基础小册：直观数学导论》中文排版源码
英文书名：The Little Book of Generative AI Foundations: An Intuitive Mathematical Primer
底本：arXiv:2605.29713v2（2026-09-08）

本目录由用户提供的中文源码包展开，原有TeX、图表、参考文献和00README.json保留原内容。
本次导入只整理目录并添加构建入口，未执行整书编译，也未检查译文质量。
根目录00_books中的PDF是用户提供的既有译本，不是本次构建生成的文件。

入口与依赖
主文件：main.tex。
需要Python 3、TeX Live中的latexmk与XeLaTeX，以及Biber；程序需在PATH中。
main.tex使用biblatex，后端为Biber。不要改用BibTeX处理本书参考文献。
主要宏包包括ctex、fontspec、TikZ、tcolorbox、amsmath、biblatex等，以main.tex为准。
主文件指定以下字体，编译环境需要能按这些字体族名称找到它们：
  Noto Serif
  Noto Serif CJK SC
  Noto Sans CJK SC
  Noto Sans Mono CJK SC
本次没有更换字体。缺少字体时应先安装对应字体，再重新编译。

编译方法
在本目录运行：
  python build.py
或：
  .\build.ps1
首次重新编译时，可将结果放在工作目录，与已导入PDF分别保存：
  python build.py --output-directory ../../work/little_book_generative_ai/rebuilt

默认输出：../../00_books/The_Little_Book_of_Generative_AI_Foundations_cn_translated.pdf
指定其他目录时使用--output-directory；默认路径下已有PDF会在编译成功后被替换。
脚本复制源码到系统临时目录，再由latexmk调用XeLaTeX和Biber。
编译日志、中间文件保留在临时目录中；成功时默认清理本次临时目录，失败时保留以便查看错误。
使用--keep-work可在成功后保留临时目录。

资产与维护
chapters/保存章节，figures/保存TeX图与PDF图，references.bib保存参考文献。
figures/中的PDF是插图输入，不能作为重复成品删除。
现有译文排版设置见translation_style.md；原包说明见README_zh-CN.md。
