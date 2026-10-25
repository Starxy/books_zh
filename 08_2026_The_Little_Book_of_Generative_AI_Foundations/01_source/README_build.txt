《生成式人工智能基础小册：直观数学导论》中文排版源码
英文书名：The Little Book of Generative AI Foundations: An Intuitive Mathematical Primer
底本：arXiv:2605.29713v2（2026-09-08）

本目录由用户提供的中文源码包展开，随后依据同版英文TeX校订。
2026-10-25已逐节对照前言、8章正文、结语及两篇附录，提取术语表，修正译法，
翻译插图说明文字，并检查重建PDF的版面。参考文献数据保持原样。
原始英文包及导入时的中文包保存在../00_originals；当前正式译文以本目录为准。

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
沿用上述字体族，中文强调文字使用同一字体的倾斜形式。
Noto CJK字体来自官方项目：https://github.com/notofonts/noto-cjk
需要简体中文的Serif、Sans、Sans Mono常规及粗体字体；不随本工程重复打包。
Windows下安装到用户字体目录后，还需确认TeX Live的Fontconfig能找到该目录。
可用fc-match检查上述字体族，不能将返回的替代字体误认为所需字体已安装。

编译方法
在本目录运行：
  python build.py
或：
  .\build.ps1
校订时先将结果放在工作目录，检查后再更新正式PDF：
  python build.py --output-directory ../../work/little_book_generative_ai/rebuilt

默认输出：../../00_books/The_Little_Book_of_Generative_AI_Foundations_cn_translated.pdf
指定其他目录时使用--output-directory；默认路径下已有PDF会在编译成功后被替换。
--output-directory的相对路径以运行命令时的当前目录为准；上例要求在本目录运行。
脚本复制源码到系统临时目录，再由latexmk调用XeLaTeX和Biber。
编译日志、中间文件保留在临时目录中；成功时默认清理本次临时目录，失败时保留以便查看错误。
使用--keep-work可在成功后保留临时目录。

资产与维护
chapters/保存章节，figures/保存TeX图与PDF图，references.bib保存参考文献。
figures/中的PDF是插图输入，不能作为重复成品删除。
译文排版设置见translation_style.md；版次与许可说明见README_zh-CN.md。
术语表位于../02_glossary/glossary_en_zh.md。

图中文字维护
PDF图的中文说明位于figures/labels_zh.json；转换程序为tools/localize_figures.py。
普通整书编译直接使用已保存的图形PDF，不需要运行转换程序。
重新生成时需要PyMuPDF、fontTools、英文TeX包的展开目录及NotoSansCJKsc-Regular.otf：
  python tools/localize_figures.py --english-source <英文源码根目录> --output-directory <临时图形目录> --font <字体文件绝对路径>
输出目录不能位于英文图形目录内。程序仅替换说明文字，保留原图路径、图像和数学标签；
另扩大原图中被裁切的坐标标签所在页面边界。生成后逐图查看，再复制到figures对应位置。
不要用中文成图作为转换输入；英文原图始终从../00_originals中的原版TeX包取得。
