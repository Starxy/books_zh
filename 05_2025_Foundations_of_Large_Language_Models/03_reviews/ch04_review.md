> 当前状态（2026-10-24）：全书中文译稿已编译完成，成品为 `00_books/Foundations_of_Large_Language_Models_cn_translated.pdf`（285页）。当前源码为 `../01_source/`，构建方法见该目录的 `README_build.txt`。以下为历史制作/校对依据，其中阶段进度、旧文件名及临时路径仅作追溯，不代表当前交付状态。

# 第4章《对齐》译校报告

状态：已完成，目标 `01_source/Chapter10/` 已冻结，可纳入六章合并。唯一依据为只读 `00_originals/tex_v4_en/Chapter10/`；未使用旧 PDF 或社区译本。

## 交付及编译

- 书内章号：4；目录名：`Chapter10`。
- 完成正文、标题、图注、脚注、原有框内文本、表格及全部 11 幅 TikZ 图的中文化。普通问答、数学题提示和回答、Self-Instruct 指令及字段均已译为中文。
- 修改文件：`chapter10.tex` 及 `Figures/` 下全部 11 个 `.tex` 文件，共 12 个文件；未编辑共享文件或其他章节。
- 正文保留 1217 行源文对应关系，其中 360 行有译文替换；正文约 25802 个汉字。
- 独立编译：`build_book.py --chapter 4 --tag ch4agent_first`。
- 最终快照：`work/llmbook_v4/builds/ch4agent_first_20261023_152612/project/`。
- PDF：快照下 `out/LLMFoundations.pdf`，共 56 页，其中本章正文为 PDF 第 6–49 页，共 44 页（印刷页码 1–44）；其余为导言/目录及参考文献。
- 日志检查：缺字 0、Overfull 0、未定义引用 0；索引页码稳定。
- 完整机器审计：`audit.json`；正文映射：`line_mapping.json`；图标签映射：`figure_mapping.json`；冻结文件散列：`file_manifest.json`；编译元数据：`final_build.json`。

## 结构及忠实性核对

| 项目 | 原文 | 译文 |
|---|---:|---:|
| 章标题 | 1 | 1 |
| section | 5 | 5 |
| subsection | 13 | 13 |
| subsubsection | 6 | 6 |
| figure / 图注 / 图文件 input | 11 / 11 / 11 | 11 / 11 / 11 |
| tabular | 6 | 6 |
| table 浮动环境 | 0 | 0 |
| 原有 tcolorbox | 7 | 7 |
| 脚注 | 8 | 8 |
| eqnarray 公式环境 | 86 | 86 |
| itemize | 8 | 8 |
| label | 44 | 44 |
| ref | 51 | 51 |
| 引用命令 / 引用键出现次数 | 62 / 87 | 62 / 87 |
| 可见索引 mindex | 48 | 48 |

所有环境的类型、顺序、引用键、label/ref/input 路径均一致。所有正文行内数学按源行核对一致；86 个公式环境中有 8 个仅翻译 `text` 叙述标签，标准化这些文字后公式逐字一致。具体修改保存在 `audit.json`，包括“置为 0”“计算损失”“策略”“环境动态”“被选中”“损失”“惩罚”“依赖/不依赖参数”等，以及英译中任务中的中文指令。数学变量、数值、运算符、数据字符串、自动公式编号机制均保留。

## 图形与视觉检查

| 图 | 文件 | 状态 |
|---|---|---|
| 4.1 | figure-pretrain-then-align.tex | 中文完成 |
| 4.2 | figure-sft-forward-and-backward.tex | 中文完成 |
| 4.3 | figure-sft-multi-round-prediction.tex | 中文完成 |
| 4.4 | figure-self-instruct.tex | 中文完成 |
| 4.5 | figure-small-models-for-llms.tex | 中文完成 |
| 4.6 | figure-sft-vs-rlhf.tex | 中文完成 |
| 4.7 | figure-llm-as-policy.tex | 中文完成 |
| 4.8 | figure-reward-model-architecture.tex | 中文完成 |
| 4.9 | figure-rlhf-diagram.tex | 中文完成 |
| 4.10 | figure-rlhf-vs-dpo.tex | 中文完成 |
| 4.11 | figure-reasoning-paths-for-process-based-approaches.tex | 中文完成 |

共 211 处标签替换。11 幅图均核对节点、连线、坐标、作用域、颜色及数学内容；拓扑完全一致，未改节点标识符。删除源图 `tikzstyle` 定义后的多余分号，未删除 draw/node 正常结束分号。没有移动节点或修改数据。

已检查本章 44 页联系表，并使用 Poppler 对 11 幅图所在页（PDF 7、10、12、15、22、24、25、30、35、41、47）逐页渲染至 1500 像素长边检查。另检查正文首页 PDF 6 和公式密集页 PDF 26。复杂图 Self-Instruct、五种小模型使用方式、RLHF 训练流程、两条推理路径均清晰，无遮挡、缺字、跨框或裁切。渲染文件在 `qa_first/`，页文本映射在 `pdf_pages.json`。

## 保留英文的明确理由

- 翻译任务依赖语言方向，保留原英语 `practice indeed helps.`、对应法语 `La pratique aide effectivement.`，以及原英语 `How's the weather today?`；任务指令和字段已译中文。
- 数学中的 `Instruction`、`User-input`、`Output`、`Sample`、`Loss`、`summary` 等原始变量/占位数据字符串保持字面形式。图 4.4 的普通指令、字段说明和步骤名称已经中文化。
- 分类标签 `correct`、`incorrect`、`neutral` 作为数学数据保留，并在正文给出中文含义；图 4.11 中普通评价文字已译为“正确”“有问题”。
- 模型、论文、人名、数据集及专名保留；图 4.11 的 Jessica 与 The International Junior Math Olympiad 为原专名，题目和两个回答的普通语言已全部中文化。
- `inference` 与 `reasoning` 都译“推理”；前者依语境写“模型推理”“推理阶段”，后者写“推理步骤/路径”等；无“推断”旧术语残留。

## 本章术语及建议补录

| English | 中文 |
|---|---|
| reward shaping | 奖励塑形 |
| ratio function | 比率函数 |
| trust region | 信赖域 |
| pairwise comparison | 成对比较 |
| pairwise ranking | 成对排序 |
| listwise ranking | 列表式排序 |
| pointwise supervision | 逐点监督 |
| learning-to-rank | 排序学习 |
| underdetermination | 欠定性 |
| aspect-based sentiment analysis | 基于方面的情感分析 |
| hinge loss | 合页损失 |
| reward gaming | 奖励取巧 |
| reward hacking | 奖励投机 |
| oracle reward model | 理想奖励模型 |
| model cascading | 模型级联 |
| dynamics | 环境动态 |
| baseline | 基线 |
| trajectory | 轨迹 |
| discount factor | 折扣因子 |
| Markov decision process | 马尔可夫决策过程 |
| action-value function / Q-value function | 动作价值函数 / Q 价值函数 |
| dense reward / sparse reward | 稠密奖励 / 稀疏奖励 |
| curriculum learning | 课程学习 |
| intrinsic motivation | 内在动机 |
| hindsight experience replay | 事后经验回放 |
| instruction following | 指令遵循 |
| single-round / multi-round prediction | 单轮预测 / 多轮预测 |
| online / offline reinforcement learning | 在线 / 离线强化学习 |
| reranking | 重排序 |
| ensemble learning | 集成学习 |

Q-value function 在本章写“Q 价值函数”，与前面的“动作价值函数”同义；主代理如统一简称，可采用“Q 值函数”。术语表与共享索引由主代理维护，本代理未改共享文件。

## 源文疑点及处理

以下均按原 TeX 保留，没有替作者更正技术内容。行号均指只读英文 `Chapter10/chapter10.tex`：

1. 最大化性能函数的段落使用 `gradient descent` 表述（式 4.18–4.20 附近）；译文忠实保留“梯度下降”。
2. 第 572 行将批次均匀经验权重写作 `Pr_theta(tau)=1/|T|`；第 574 行的相应梯度式使用 `1/m`，本处没有显式说明 m 与批次大小的关系；两处均保留。
3. 第 782 行的重要性采样梯度等式右侧没有保留概率比的分母；未改公式。
4. 正文使用 `theta_ref`，图 4.9 使用 `theta_old`，且旧策略与 KL 参考策略的区分不总明确；保留原有记号。
5. 第 913 行将所引 PPO 目标的第一项称为 `U_ppo-clip`；式中拆分项使用 `U_clip`，命名按源保留。
6. 第 915–917 行奖励平方和正则项前为负号；未改变符号。
7. 第 1024 行叙述中的 log 与 exp 括号范围不明确；第 1052 行 exp 表达式的字面括号不配对；均按源保留，不改数学。
8. 图 4.11 回答 2 中的有意错误步骤与最终正确答案全部保留；红色背景及“有问题”标记与原图对应。

本章翻译及排版无未决项。源文技术疑点作为译校记录交由主代理全书编辑时处理。
