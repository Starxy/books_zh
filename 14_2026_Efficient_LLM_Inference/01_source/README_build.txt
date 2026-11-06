《大语言模型高效推理》编译说明

使用 Python 3.10+、XeLaTeX、latexmk 和 Perl。TeX Live 2026 的 ctex、
Fandol、Latin Modern、AMS 数学宏包、fancyhdr、tcolorbox、TikZ、listings、
booktabs、tabularx、longtable 和 hyperref 为所需依赖。封面示意图使用 TikZ，
附录论文导读随正文排印。示例代码仅作排版输入。

在本目录运行 python build.py，或运行 .\build.ps1。
整书完成后默认生成仓库根目录 00_books/Efficient_LLM_Inference_cn_translated.pdf。
--output-directory 可指定输出目录。--chapter N 单独试编第 N 章，默认将
chNN_preview.pdf 写到仓库 work/efficient_llm_inference。过程稿同样写到 work。

脚本从系统临时目录中的新源码副本运行，控制台会显示临时目录。latexmk
按辅助文件变化重编目录和书签，最多 6 轮。生成成功后才替换目的 PDF。
