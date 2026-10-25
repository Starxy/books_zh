The Little Book of Generative AI Foundations: An Intuitive Mathematical Primer
生成式人工智能基础小册：直观数学导论
作者：Tianhua Chen
版本：arXiv:2605.29713v2，书名页日期为2026-09-08。
导入日期：2026-10-25

状态
用户提供的既有中文译本。本次仅整理目录、源码位置、构建入口和书目，未重新编译或检查翻译质量。
中文PDF按提供文件原样归档，共196页：
  ../00_books/The_Little_Book_of_Generative_AI_Foundations_cn_translated.pdf
英文PDF共195页。以上页数仅用于识别文件。

目录用途
00_originals/：英文PDF、英文TeX压缩包，以及用户提供的中文源码压缩包。
01_source/：从中文源码包展开的TeX、图表和参考文献；保留原包内的英文文件名及相对路径。
02_glossary/：供后续维护术语；此次输入未提供独立术语表。
03_reviews/：供后续校订使用；本次未新增校对报告。
05_references/：供后续存放补充参考资料。

原始输入与归档位置
2605.29713v2.pdf
  -> 00_originals/2026_The_Little_Book_of_Generative_AI_Foundations_arXiv-2605.29713v2_EN.pdf
arXiv-2605.29713v2 (1).tar.gz
  -> 00_originals/arXiv-2605.29713v2.tar.gz
arXiv-2605.29713v2_zh-CN_source.tar.gz
  -> 00_originals/arXiv-2605.29713v2_zh-CN_source.tar.gz
arXiv-2605.29713v2_zh-CN (1).pdf
  -> ../00_books/The_Little_Book_of_Generative_AI_Foundations_cn_translated.pdf

源码与编译
主文件：01_source/main.tex。
依照主文件，工程包含前言、8个正文章节、结语、附录A—B和参考文献。
保留原有章节组织、排版设置和图表；没有按书名或章节内容改写文件。
在01_source/运行 python build.py 或 .\build.ps1。
引擎、字体、Biber依赖和输出方式见01_source/README_build.txt。
原源码包随附说明保留于01_source/README_zh-CN.md。
