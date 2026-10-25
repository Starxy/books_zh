固定排版源资产

references/：逐章参考文献的TeX排版源，保留原始文献题名与作者信息。
code_typesetting/：代码高亮的TeX排版源及固定索引数据。

build_config.json给出源资产与编译器所需别名的对应表。build.py仅在临时工程中生成这些别名；正式工程不保留.bbl、.minted、日志或辅助文件。代码和文献排版源属于完整成品的依赖，不能删除。
