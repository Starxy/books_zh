Big Data in Omics and Imaging: Integrated Analysis and Causal Inference
组学与影像大数据：整合分析与因果推断
更新时间：2026-10-25

状态：全书中文译稿已编译完成。
成品（仓库根目录）：00_books/Big_Data_in_Omics_and_Imaging_cn_translated.pdf
页数：673
说明：7章、书前材料、参考文献与索引；索引保留原版定位页码。

目录用途
00_originals：英文PDF、英文分章资料，以及适用时的原版TeX源码。
01_source：与上述中文成品对应的中文TeX工程、图形资产及构建脚本。
02_glossary：本书中英术语对照。
03_reviews：当前整理核验和历史校对、制作依据；历史进度不代表当前交付状态。
05_references：补充参考资料（若有）。

重新编译
进入01_source后执行 python build.py，或在PowerShell中执行 .\build.ps1。
主文件：01_source/main.tex。
编译依赖和可选参数详见01_source/README_build.txt。
中间文件只写入系统临时目录；成功后才更新同名成品。
