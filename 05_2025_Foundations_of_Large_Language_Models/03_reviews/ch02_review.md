> 当前状态（2026-10-24）：全书中文译稿已编译完成，成品为 `00_books/Foundations_of_Large_Language_Models_cn_translated.pdf`（285页）。当前源码为 `../01_source/`，构建方法见该目录的 `README_build.txt`。以下为历史制作/校对依据，其中阶段进度、旧文件名及临时路径仅作追溯，不代表当前交付状态。

# 第 2 章《生成式模型》译稿交付报告

## 范围与完成情况

- 书内第 2 章，对应 `Chapter8`，依据唯一原文 `00_originals/tex_v4_en/Chapter8/`。
- 正文 1808 行已逐段完整翻译，473 条原文行号映射已保存；章节标题、正文、脚注、表头/表内说明、图注、全部提示与回答示例、原有框内内容及 12 幅 TikZ 图的说明性标签均已处理。
- 用户最新术语决定已执行：inference 和 reasoning 均译为“推理”，必要处保留英文释义；本章没有遗留“推断”。
- 未阅读旧译本或原始 PDF；没有修改共享主文件、样式、术语表或其他章节。

## 自测与页数

最终构建记录由 `build_result.json` 保存，最终 PDF 路径见该记录及本目录 `最终构建.txt`。

- 独立章测试使用 `build_book.py --chapter 2`，自动计数为第二章。
- 测试 PDF 共 **69 页**，其中本章正文 **54 页**（PDF 第 6—59 页，印刷页码 1—54）；其余为测试工程的前置页与参考文献。
- XeLaTeX/BibTeX/索引流程成功。最终缺字 **0**，未定义引用 **0**，Overfull **0**。
- 已渲染并目视检查 PDF 第 6、9、14、17、18、20、25、26、32、35、38、42、44、46、48、50、52、53、56、58 页。覆盖全部 12 幅图、复杂 RLHF/KV 缓存/kNN 图、公式密集页、表格、正文及长下划线示例。
- 渲染 PNG 位于 `renders/`，审计结果位于 `qc.json`，英文保留项与数学差异均已人工核对。

## 结构计数：原文 → 译文

| 项目 | 原文 | 译文 |
|---|---:|---:|
| chapter | 1 | 1 |
| section | 4 | 4 |
| subsection | 15 | 15 |
| subsubsection | 14 | 14 |
| 标题合计 | 34 | 34 |
| figure | 12 | 12 |
| table | 4 | 4 |
| tabular（包括未编号示例表） | 7 | 7 |
| caption | 16 | 16 |
| footnote | 17 | 17 |
| tcolorbox | 24 | 24 |
| eqnarray | 98 | 98 |
| equation | 2 | 2 |
| 全部数学跨度（正文，含行内数学） | 780 | 780 |
| label | 52 | 52 |
| 交叉引用命令 | 49 | 49 |
| 文献引用命令 | 105 | 105 |
| 引用键出现次数 | 131 | 131 |
| 唯一文献引用键 | 109 | 109 |
| input | 12 | 12 |
| mindex/mindexraw | 50 | 50 |

环境序列、标题类型序列、所有 label/ref/cite/input 的键及顺序均与原文一致。全部 750 个 TikZ 节点名称与 179 条绘图命令数量原样保留；连线拓扑、数据、坐标与数学符号均保存。

## 公式与说明标签

公式的变量、运算符、参数、数值、上下标、自动编号机制均未改变。陈列数学仍由原环境自动编号，章内编号至 2.105。经过仅将以下叙述性标签还原为原英文的归一化比较，正文与全部图文件的数学跨度均完全一致，缺失或新增数学为 0：

- 输入/输出示例中的任务说明与回答：“计算这个数的平方。”“结果是 4。”；上下文（输入）、预测（输出）。
- 工作节点（worker）、节点（node）。
- 模型扩展、数据集扩展、不可约误差。
- 分段函数中的“当”（if）。
- 固定大小缓存图中的“大小”（Size）。

数学中没有遗留误替换的全角括号或标点。父代理的原始严格比较会把上述标签中文化标为两文件的数学文本差异，这是已逐项解释的预期差异，见 `qc.json` 的允许映射。

## 英文保留项及理由

以下保留项均是研究对象、变量或专名，译成中文会改变语言学或程序演示机制：

- 语法判断中的 `John seems happy today.`、`LLMs are powerful models but are expensive to build.`，以及作为分类标签的 `Yes/No`。
- 情感分类中的四个英语句子及 `Positive/Negative/Neutral` 标签。
- 中译英示例中的 `Hello`、`Thank you`、`Good Morning`。
- `{*sentence*}` 占位变量、特殊词元、概率示例词元、模型/数据集/人名、参考文献键和 URL。
- Python 与 C 程序代码、函数/变量名及字符串 `Hello, World!`。程序周边任务指令和错误说明均已译为中文。
- RoPE 图中的带位置下标的两个英语句子，以及 `cat`、`sleeping` 词元；其说明标题和图注已全部翻译。
- CoT 触发语句首次介绍时保留论文所用 `Let's think step by step.`，同时给出完整中文；后面的提示框使用中文。
- 各术语首次出现的英文释义、LLM/SFT/QKV/ALiBi/T5 等缩写或专名，以及数学中作为变量的 `input/output/Mask/Mem` 等。

故事、食谱、环保生活的四组 RLHF 回答、角色设定、对话、算术推理及 RAG 示例已经完整译为中文，没有以“示例”为由保留整段一般英语正文。

## 排版修复

- 移除 16 个 `tikzstyle` 定义行末多余分号，消除 nullfont 的裸分号告警。
- 移除 kNN 图原第 63 行 TikZ 命令末尾多余的裸 `]`，保留整条节点命令和拓扑。
- RLHF 四输出示例表位于 0.9 倍正文宽的 parbox 内，原列宽之和 0.92 倍正文宽导致溢出；仅将第二列 0.74 改为 0.70，行列数与全部内容不变。
- 三个 PGFPlots 图文件调整纵轴标题的局部 yshift，避免中文轴名与刻度重叠；位置外推/插值图的绘图区宽度设为 0.95 倍正文宽，以容纳外移后的轴名。坐标范围、数据点、曲线和轴的数学含义均不变。

## 源文异常与未决问题

没有未完成翻译或阻塞编译的问题。以下属于原文的记号或技术表述异常，译文忠实保留，交由主代理/作者决定是否作独立勘误：

1. 正文第 194 行：上一公式定义 `J_theta`，随文解释却使用 `L_theta`。
2. 正文第 449 行：关于 SFT 反向传播“仅经过输出对应网络部分、其余网络不变”的说法易产生歧义；译文保持原意，没有擅自改写为算法结论。
3. 正文第 1515 行：将 `[1,20]` 全部除以 2 后称其落在 `[1,10]`，其下端实际为 0.5。
4. 正文第 1743 行：称 `k=d/2` 的最后一维为“最高频率维度”，而前文频率公式随 k 递减。译文仍写“最高频率”。
5. T5/ALiBi 偏置图的 T5 子图写 `n_b=3`，同时绘制 `u_0` 至 `u_3` 四种偏置值；原图内容未擅改。

## 新术语/建议补录 EN → ZH

| English | 本章译法 |
|---|---|
| internal covariate shift | 内部协变量偏移 |
| root mean square layer normalization | 均方根层归一化 |
| micro-batch | 微批次 |
| collective operation | 集合操作 |
| all-reduce | 全归约 |
| tile-based parallel algorithm | 分块并行算法 |
| attention sink | 注意力汇聚点 |
| datastore | 数据存储库 |
| vector store | 向量存储库 |
| forced decoding | 强制解码 |
| memory capacity | 记忆容量 |
| compressive Transformer | 压缩式 Transformer |
| continuous-space attention | 连续空间注意力 |
| needle-in-a-haystack | 大海捞针 |
| passkey retrieval | 口令检索 |
| copy memory task | 复制记忆任务 |
| double descent | 双下降 |

## 修改文件

交付源文件位于 `01_source/Chapter8/`：

1. `chapter8.tex`
2. `Figures/figure-a-curve-of-scaling-laws.tex`
3. `Figures/figure-fixed-size-memory.tex`
4. `Figures/figure-knn-models-for-llms.tex`
5. `Figures/figure-lm-decoder-only-architecture.tex`
6. `Figures/figure-long-context-llm-architectures.tex`
7. `Figures/figure-model-performance-against-model-size-and-training-dataset-size.tex`
8. `Figures/figure-positional-embedding-extrapolation-and-interpolation.tex`
9. `Figures/figure-rlhf-overview.tex`
10. `Figures/figure-rotation-examples.tex`
11. `Figures/figure-sharing-for-the-KV-cache.tex`
12. `Figures/figure-T5-and-Alibi-biases.tex`
13. `Figures/figure-T5-buckets.tex`
