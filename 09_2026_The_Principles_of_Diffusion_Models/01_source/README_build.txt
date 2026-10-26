《扩散模型原理》项目初始化说明
英文书名：The Principles of Diffusion Models
作者：Chieh-Hsin Lai、Yang Song、Dongjun Kim、Yuki Mitsufuji、Stefano Ermon
英文底本：arXiv:2510.21890v3，英文PDF封面日期2026-08-27，522页。
本目录年份2026取自本次v3底本日期。封面中的MIT Press 2027是预告出版信息，不作为本次底本版次。

当前范围
2026-10-25归档用户提供的英文TeX包、英文PDF和450页既有中文PDF，整理中英术语。
对应中文TeX已缺失。01_source目前只有构建入口、配置和体例说明，没有恢复正文。
尚未开始整本译文复核、数学校订、版面复核或中文TeX重建，未编译整书。
目录与章节标题可用于初始化结构对应，但不能证明中文内容逐节完整或与v3完全相同。

文件位置
../00_originals/arXiv-2510.21890v3.tar.gz：用户提供的原始英文源码包，去掉下载文件名中的“(2)”。
../00_originals/2026_The_Principles_of_Diffusion_Models_arXiv-2510.21890v3_EN.pdf：英文PDF。
../00_originals/tex_v3_en/：原包展开后的英文文件，保留原始文件名和内容。
../02_glossary/glossary_en_zh.md：从英文底本和既有中译PDF整理的术语、变体与取词页序。
../../00_books/The_Principles_of_Diffusion_Models_cn_translated.pdf：用户提供的既有中文PDF，内容未改动。
既有中文PDF的原下载文件名为“扩散模型原理_中文译本.pdf”；文件大小与SHA-256记录在根目录00_file_organization.json。

结构
英文主文件为tex_v3_en/main_v2.tex。正文有四个分部，第1—11章；尾声与展望内为第12章。
附录A—D、参考文献，以及摘要、致谢、前言与路线图、符号说明均在底本中。
Chapter-0-Diffusion-High-Level.tex是B部分的引入材料，不能按文件名将其另计为第0章。
英文文件名中的Chapter数字与实际章号并非一一相同，后续以主文件输入顺序和显示章号为准。
原版没有独立索引。此处只登记结构，未逐页检查中文译本的覆盖。

构建入口
统一入口为build.py和build.ps1：
  python build.py
  .\build.ps1
目前配置source_status为missing_chinese_tex，main为null。
运行入口会说明中文TeX尚未恢复并退出，不会输出PDF或覆盖已归档的中文PDF。
仅恢复并检查中文主文件后，才能将main设为实际TeX路径并调整source_status及依赖。

英文工程依赖与后续重建
原包00README.json声明主文件main_v2.tex及pdflatex引擎；主文件使用nowfnt-arxiv类和Biber。
原包保留main_v2.bib、main_v2.bbl、nowfnt-arxiv.cls、nowfnt.cls、相关文献样式、
fnfix.tex、math_commands.tex、theorems.tex、scaffolding.tex、图形PDF等输入。
不要将原包.bbl、样式或图形PDF当作临时成品清理。
本次未验证英文工程编译；也未将英文主文件作为中文构建目标。
build_config.json中的XeLaTeX和Biber是中文重建时的预备配置，不表示原中文工程已经恢复或验证。
恢复工作启动后，应以英文TeX中的公式、标签和图形为底本，利用既有中文PDF保留译文，
结合实际页面恢复中文排版。字体、中文类和编号环境届时按本书确认，不套用其他书的设置。
阶段稿和编译中间文件放work/或系统临时目录；正式PDF仍只保存在根目录00_books。
