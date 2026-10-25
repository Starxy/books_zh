Agentic Large Language Models
智能体大语言模型
更新时间：2026-10-25

状态：全书中文译稿已编译完成。
成品（仓库根目录）：00_books/Agentic_Large_Language_Models_cn_translated.pdf
页数：382
说明：依据arXiv:2610.13455v1源码；23章、7个分部引言及按章参考文献。

目录用途
00_originals：英文整书PDF与原版TeX源码包。
01_source：与上述中文成品对应的中文TeX工程、图形资产及构建脚本。
02_glossary：本书中英术语对照。
03_reviews：当前整理核验和历史校对、制作依据；历史进度不代表当前交付状态。
05_references：补充参考资料（若有）。

重新编译
进入01_source后执行 python build.py，或在PowerShell中执行 .\build.ps1。
主文件：01_source/main.tex。
编译依赖和可选参数详见01_source/README_build.txt。
中间文件只写入系统临时目录；成功后才更新同名成品。
