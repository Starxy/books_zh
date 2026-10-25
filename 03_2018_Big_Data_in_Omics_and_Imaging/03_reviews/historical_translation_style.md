> 当前状态（2026-10-24）：全书中文译稿已编译完成，成品为 `00_books/Big_Data_in_Omics_and_Imaging_cn_translated.pdf`（673页）。当前源码为 `../01_source/`，构建方法见该目录的 `README_build.txt`。以下为历史制作/校对依据，其中阶段进度、旧文件名及临时路径仅作追溯，不代表当前交付状态。

# 全书翻译体例：Big Data in Omics and Imaging

## 当前任务

用户已确认第一章样章，要求开始完整翻译。以样章的行文、术语与版式完成其余六章及原书前后材料；无需再次请求体例批准。只翻译原书，忽略读者后加划线、高亮、批注。

## 开工读取

1. 本文及 BOOK/02_glossary/glossary_en_zh.md。
2. PROJECT/chapters/ch01a.tex 与 ch01c.tex，作为已批准的正文、公式与图示范例。
3. PROJECT/preamble.tex，确认宏；PROJECT/docs/ch01_review.md给出本书编号体系及已发现的文本抽取风险。
4. SCRATCH/source_inventory.json里本章的权威书签，用其逐条规划节次。

- BOOK = 03_2018_Big_Data_in_Omics_and_Imaging
- PROJECT = 03_2018_Big_Data_in_Omics_and_Imaging/01_source
- SCRATCH = work/omics
- 原文：BOOK/00_originals/chapters_en/；文本：SCRATCH/en/chNN.txt，带PDFPAGE页标。分章页码从1开始，原书印刷页码另在页眉。
- Python：python。
- XeLaTeX：xelatex。
- PyMuPDF已在SCRATCH上级elements_packages中；可参考SCRATCH/prepare.py顶部导入方式。不要运行其initialize，它会重置共享工程。
- 用已有Python执行SCRATCH/render_chapter.py并传入章号，可将本章无批注页面渲染至SCRATCH/pages/chNN/p001.png等；复杂图可从原PDF另作高分辨率裁剪。

## 文件所有权

每名译者只写指定章的 chapters/chNN.tex、chNNa.tex等分段文件、figures/chNN* 和独立校对报告。共享preamble.tex、main.tex、术语表、其他章节只读。缺宏用providecommand在本章局部补充，报告给集成者。

第1—6章已完成合稿并通过结构、编号及视觉核验，阶段PDF569页，术语表533项。第1—6章均已冻结。当前最终批次为第7章A/B/C三段，精确分界及文件所有权见各自任务说明和SCRATCH/ch07_plan.json；根代理创建ch07.tex。A段含唯一chapter，B/C不含chapter，禁止改旧章或运行旧章生成脚本。

第4章分界在原分章PDF第88页：A段包含表4.13及表后3行正文，止于4.6标题之前；B段从该页下部4.6标题开始。A段写chapters/ch04a.tex及ch04a*分段，独占figures/ch04a*，图4.1—4.25和全部13张表；B段写chapters/ch04b.tex及ch04b*分段，独占figures/ch04b*，图4.26—4.27及后续附录、习题。A段含唯一chapter命令，B段不含chapter。双方局部宏分别用纯字母chFourA、chFourB前缀，常规TeX控制序列名不能含数字；ch04.tex合章封装由集成者最后创建。B段测试使用临时第4章，并将section设为5，让首节自然得到4.6；这些计数仅写于测试驱动。第6章独占ch06*文件，局部宏用chSix前缀。

## 译文与结构

- 逐条对应原书章、节、小节、四级标题、章导言、脚注、软件说明、附录、习题。完整翻译，不以概述替代段落，不因篇幅长而省略证明或算法。
- 教材口吻，长句按中文习惯拆分；重点术语章内首现“中文（English）”。人名、年份、et al.、and和文献标识保持原书形式。
- 统一：反事实结局、平均因果效应、可交换性、条件可交换性、正值性、一致性、标准化、逆概率加权、目标试验；rare variant=罕见变异；orthonormal matrix=正交归一矩阵；subdifferential calculus=次微分运算；confounder=混杂因子。新增词在报告列出，由集成者合入共享术语表。
- 第一批统一词：next-generation sequencing=下一代测序；logistic regression=逻辑回归；Hilbert space=希尔伯特空间；RKHS=再生核希尔伯特空间；evaluation functional=求值泛函；functional canonical correlation analysis=函数型典型相关分析。feature map在核方法中译特征映射，在卷积网络中译特征图，术语表已分义。一般组学数据normalization依既定语境译标准化，勿全局机械替换为归一化。
- 框注按本章原书实际结构保留；原书没有Fine Point/Technical Point时不额外造框。

## 数学、编号与图表

- 所有展示公式、矩阵、表格与图都看原页；文本层常将Θ识别成Q、Σ识别成S，且会丢括号、负号、上下标和不等号。不能仅凭抽取文本重建数学。
- 编号公式用tag显式保留原号，未编号公式仍不编号。多行用equation+aligned，tag置于aligned之外。
- 定义、定理、例、算法、Result各自按印刷编号排，Result译“结论”。用bookdefinition、booktheorem、bookexample、bookalgorithm等显式编号环境；不要用自动共用计数器替代本书原号。新类别可用段首加粗显式编号。
- 图用origfig{章内序号}{中文图注}，表用origtable{章内序号}{中文表注}。机制图、流程图和可确认的网络用TikZ重绘，节点/箭头/虚实线/面板号逐项对应。多面板节点名唯一。
- 实验散点、热图、曲线、真实影像及密集实测网络保留原始图形数据，TikZ补中文轴标、图例或节点名；不随机生成替代数据，不猜造连边。无法可靠还原处在报告说明。
- 原书数学或引用疑点：正文保留可见印刷式，报告原页、式号和疑点，不自行推导“正确版本”顶替。
- 章附录用section*及addcontentsline；保持普通节计数。习题保留原题号。

## 排版与编译

逐段编译；长章按节界拆分成多个tex文件以控制核验规模。长公式依中文行宽换行，不用不可断行hbox包住整段数学。跨页前避免孤立标题，必要时Needspace；不以扩大页面文字区挤占页脚。

测试驱动和编译中间文件在SCRATCH下。独立章测试在include之前设置chapter=N−1；正式章文件不含章计数设置、临时章标题或part命令。ctexbook、fontset=windows、zihao=-4，input共享preamble即可。最终独立XeLaTeX连续两遍通过，检查错误、溢出和缺字；所有译稿页、每幅图都目视检查。合稿后由集成者另作整书检查。

LaTeX通过Python生成或严格转义补丁写入；复读控制字节。可用字符§占位反斜杠，再以chr(92)替换，参考SCRATCH/prepare.py的texwrite函数；避免shell吞掉begin、tag等反斜杠。

第一批发现未转义的百分号会无声吞掉同一行后半段。文本百分数一律写转义形式；完整行注释可以保留，正文行不使用裸百分号。局部辅助宏必须带章及分段前缀，避免合稿时覆盖其他章。原书书签有时漏收深层实际标题：仍按可见原页保留并在报告列明，不能为匹配不完整书签而删标题。

## 交稿条件

仅在本章全部内容写出、图表齐全且最终两遍编译与视觉核验完成后报告完成。报告存BOOK/03_reviews/，包含：

- 文件清单与原页覆盖；完整节次、附录、习题范围。
- 每个公式、图、表以及定理类编号清单；缺失或重复需解释。
- 自测页数、错误/溢出/缺字与残留提示，视觉检查范围。
- 新增术语（英→中）、原书疑点、刻意版式差异、未解决项及原因。

集成者按批合稿并更新可编译成品；未完成段落、占位图或未核验公式不得标记为完整翻译。


## 更深标题的共享写法

第五级（如5.3.2.3.1）使用 `bookdeepheading{paragraph}{5.3.2.3.1}{中文标题}`；第六级（如3.1.4.5.4.1）使用 `bookdeepheading{subparagraph}{3.1.4.5.4.1}{中文标题}`，命令前加正常反斜杠。该宏显式印原号、独立成行、带唯一锚点，并加入相应目录/书签层级。tocdepth已设为5；secnumdepth仍为3，避免把原书重复/错号自动改掉。第三级/四级仍用正常subsection/subsubsection自动节号。


## 最终批次补充

第7章A为章首及7.1，止于源54页7.2标题前；B为7.2、7.3和软件，包含54页表7.2及83页顶部软件续文；C从83页附录7.A标题开始，含A—J附录和全部7题。详见各自WAVE3分段说明。

第七级编号使用bookdeepheading{booklevelseven}{原号}{标题}，目录及书签深度由共享preamble统一控制。章节内禁止hypersetup覆盖bookmarksdepth：上一批发现这种设置即使位于begingroup也会影响后续章。其他第五/六级写法沿用。

新增统一：profile likelihood剖面似然、gapped alignment有缺口比对、stride步长、ReLU修正线性单元、mean field method平均场方法、functional principal component函数主成分、predetermined variable预定变量。词表为准。

第7章图7.4/7.5为示意散点图，有原PDF精确矢量坐标，应据此用TikZ重建，不随机生成。原书特殊号1.769、7.3A22和7.231跳7.332，以及两个不同结论都印7.21，均按原页保留。源书签未收7.1.4.5.4.1及.2，仍保留并入目录。
