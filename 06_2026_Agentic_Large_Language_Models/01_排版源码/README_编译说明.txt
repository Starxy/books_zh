《智能体大语言模型》中文排版源码
英文书名：Agentic Large Language Models
当前状态：全书中文译稿已编译完成；目录于2026-10-24整理。
对应成品（仓库根目录）：00_books/Agentic_Large_Language_Models_cn_translated.pdf（382页）
收录范围：依据arXiv:2610.13455v1源码；23章、7个分部引言及按章参考文献。

入口与依赖
主文件：main.tex。其余章节、图像、TikZ、参考文献、样式与数据文件均按相对路径引用。
环境：Windows中文字体、TeX Live 2026（XeLaTeX）与 Python 3；相关程序需在 PATH 中。
更换字体或TeX环境可能改变分页，应重新检查目录、公式、图表和索引。
assets/references 中是按章参考文献的固定 TeX 排版源；assets/code_typesetting 中是原版随附并经当前译稿使用的固定代码高亮排版源与索引。build_config.json 记录这些源文件在临时工程中的别名。脚本只在临时目录恢复 BibTeX/minted 所需文件名，不在正式源码内留下 .bbl 或 .minted 文件；无需运行 BibTeX、Pygments 或教材示例代码。改动代码内容或文献时须同步维护这些排版源。

编译方法
在本目录打开终端，运行：
  python build.py
或在PowerShell中运行：
  .\编译.ps1
在仓库根目录指定其他PDF保存目录：
  python "06_2026_Agentic_Large_Language_Models/01_排版源码/build.py" --output-directory "work/compiled/06_2026_Agentic_Large_Language_Models"

脚本在系统临时目录复制工程并编译，直到目录与交叉引用稳定。
成功后仅把完整PDF复制到输出目录，再清除本次临时工程；不会把日志、辅助文件或分章稿写回排版源码。
默认输出到仓库根目录00_books，成功后更新同名成品。编译失败不会覆盖现有PDF；诊断文件保留在终端提示的临时目录。
需要保留编译诊断时使用 python build.py --keep-work；请勿把临时目录复制回正式源码。
本工程以以上脚本为正式构建入口。

文档位置
术语表：../02_术语表/；校对与历史制作记录：../03_校对记录/。
当前译文直接维护在本目录的中文TeX中。不另设独立中文译稿目录。
源图中的照片、实验曲线及数据图等必要资产保留；图形用PDF文件属于排版输入，不能当作整书成品删除。

本次整理核验（2026-10-24）
从清理后的源码在独立临时目录复编通过。与现有成品的页数、全部书签、逐页文字及全部页面96dpi渲染像素一致。具体记录见同级03_校对记录/目录整理核验_2026-10-24.json。
