世界模型的定义与发展路线图
A Definition and Roadmap for World Models

作者：Physical Intelligence Team, Shanghai AI Laboratory
中文署名：上海人工智能实验室物理智能团队
底本：用户提供的 arXiv-2607.06401v1 (1).tar.gz。
版本标识取自该文件名；本次不混入其他版本内容。原文自称perspective article，中文摘要保留“观点文章”这一定位。

文件
00_originals/arXiv-2607.06401v1.tar.gz：用户原始源码包，内容未改动，仅规范归档文件名。
00_originals/2026_A_Definition_and_Roadmap_for_World_Models_arXiv-2607.06401v1_EN.pdf：
  使用原包main.tex、colm2025_conference.sty、图形和BibTeX，在本机TeX Live 2026中重建的58页英文PDF。
  该PDF用于比对版面与编号，不是另行下载的英文版本。
01_source/main.tex：完整中文译文入口；各节正文位于sections/。
01_source/colm2025_conference.sty、ailablogo.pdf：原包样式与首页标识，内容未改动。
01_source/chinese_typography.tex：原模板上的中文排字调整，正文11pt、行距17.6pt，宋体正文配黑体标题。
01_source/figs/：原包的十幅成图，因未提供图内源码，保持原图及图内英文；图注在TeX中翻译。
01_source/wm-pjlab.bib：原包文献数据库，保持原始内容。
02_glossary/glossary_en_zh.md：本篇论文的术语与语境约定。
../00_books/A_Definition_and_Roadmap_for_World_Models_cn_translated.pdf：完整中文成品。

范围
摘要、目录、第1—8节及全部28个小节、贡献者名单与参考文献。
保留1个定义、19个编号公式、10幅原图、1张比较表，以及原有脚注与引文。
译本以原article文档类、colm2025_conference样式和Letter纸张为基础，保留原版心、标题层级与页眉；字体、字号、行距和段落按中文阅读需要调整。图表布局保持原样；表格有TeX源码，仅翻译文字。
参考文献按原文引用生成253条；未合并原数据库中不同键对应的重复文献。
原包没有活动附录或独立索引。
原文的明确笔误与编号问题按01_source/translation_style.md说明处理，必要处标识译注。

构建
请读01_source/README_build.txt。统一入口为build.py和build.ps1，使用XeLaTeX、BibTeX和latexmk。
完整成品只保存在仓库根目录00_books；阶段稿、页面渲染和构建日志放work/或系统临时目录。
原包、英文PDF与成品PDF的SHA-256和页数，统一记录在根目录00_file_organization.json。
