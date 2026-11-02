临床研究设计，第五版：中文译排工程

依赖：Python 3.10或更新版本、TeX Live 2026（或具有所列宏包的 TeX Live）、XeLaTeX、latexmk。
字体使用 TeX Live 自带的 Fandol 宋体、黑体、楷体及 TeX Gyre Termes 西文和数学字体。
主要宏包：ctexbook、geometry、fontspec、unicode-math、microtype、longtable、
booktabs、tabularx、enumitem、etoolbox、tcolorbox、tikz、hyperref、bookmark、fancyhdr、xurl。
参考文献按原书各章书目保留作者、题名、期刊等检索信息，不依赖 BibTeX。

在仓库根目录运行：
python 11_2023_Designing_Clinical_Research/01_source/build.py

构建时复制正式源码到新的系统临时目录，由 latexmk 调用 XeLaTeX，直到目录和引用
不再要求重编译。日志保存在终端返回的临时目录，不写回中文源码目录。
完整译本默认输出：
00_books/Designing_Clinical_Research_cn_translated.pdf
输出路径相对于仓库根目录；可用 --output-directory 指定其他目录。

build_config.json 的 source_status 为 translated_tex 时才采用完整成品名和默认成品目录。
如果将来退回 translation_in_progress，构建器改用工作目录和明确的阶段文件名，
并拒绝向00_books及其子目录输出。编译失败不覆盖已有PDF。

内容组织、原书疑点处理和术语约定见 translation_style.md。
书末索引保留英文纸本定位号，不应当作中文页码；章节对应表通过源页标签自动生成中文页码。
