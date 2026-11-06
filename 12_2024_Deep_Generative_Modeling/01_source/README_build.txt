《深度生成建模（第二版）》编译说明

入口为 main.tex，共用设置在 preamble.tex。frontmatter.tex 收录书前材料，正文按 chapters/ch01.tex 等文件组织。图形在 figures/，引用文献按章编排，具体底本及页码对应见 translation_style.md。

依赖 Python 3.10+、TeX Live 的 latexmk 和 XeLaTeX，以及 ctex、Fandol、TeX Gyre、newtxmath、graphicx、caption、fvextra、tcolorbox、emptypage 等入口所加载的宏包。编译所需图形和代码片段随 01_source 保存。各章参考文献和 index.tex 直接由 TeX 排版。编译不执行书中示例，也不需要启用 shell escape。

在 01_source 运行 python build.py 或 .\build.ps1。
也可在仓库根目录运行 python 12_2024_Deep_Generative_Modeling/01_source/build.py。
使用 --output-directory 可指定输出目录。构建脚本在系统临时目录用源码副本编译，并输出 PDF 路径和日志目录。

默认输出到仓库根目录的 00_books/Deep_Generative_Modeling_cn_translated.pdf。从仓库根目录试排时，可追加 --output-directory work/deep_generative_modeling 将输出放在工作目录。
