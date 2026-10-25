> 当前状态（2026-10-24）：全书中文译稿已编译完成，成品为 `00_books/Foundations_of_Large_Language_Models_cn_translated.pdf`（285页）。当前源码为 `../01_source/`，构建方法见该目录的 `README_build.txt`。以下为历史制作/校对依据，其中阶段进度、旧文件名及临时路径仅作追溯，不代表当前交付状态。

# 书内第 6 章《推理能力（Reasoning）》交付报告

唯一原文为 `00_originals/tex_v4_en/Chapter12/`，仅依据该目录的 TeX 源码逐段翻译，未读取旧 PDF 或既有中文译本。正文、标题、图注、表格、脚注、原有框内内容、普通语言数学解题示例及两幅 TikZ 图的全部解释性标签均已译成中文。主文件原文及译文均为 833 行，297 个源行具有中文文本映射，映射保存在 `translation_1.tsv` 至 `translation_7.tsv` 与 `revisions.tsv`。

## 页数与编译

- 本章正文 28 页，位于独立测试 PDF 物理第 6—33 页；独立 PDF 共 39 页，另含前置页、参考文献及索引。
- 最终命令：`python work/llmbook_v4/build_book.py --chapter 6 --tag ch6final`。
- 最终 PDF：`work/llmbook_v4/builds/ch6final_20261023_152034/project/out/LLMFoundations.pdf`。
- 编译结果：0 缺字、0 overfull、0 未定义引用，索引页码已稳定。
- `final_build.json` 保存编译结果，`structure_audit.json` 保存结构与数学逐项审计，`supplemental_audit.json` 保存引文计数和索引抽查。
- `numbering_audit.json` 确认全部 11 个带标签的自动编号与源 TeX 编译结果一致；`navigation_audit.json` 确认全部页面锚点与 PDF 页面标签一致。

## 修改文件与图形

仅修改交付源码 `01_source/Chapter12/` 下三个文件，未改共享主文件、样式、术语表或其他章：

1. `chapter12.tex`
2. `Figures/figure-generative-verfication.tex`
3. `Figures/figure-comparision-of-sft-ps-opd.tex`

两幅 TikZ 共 27 个说明标签行完成中文化；57 个节点和 17 条绘制路径与原文相同，数学表达式、几何、节点名、连线、方向和颜色含义均保留。未作几何调整。清理了源文件 3 个 `tikzstyle` 定义末尾的多余分号，所有正常 `draw/node` 结束分号保留。

## 原文与译文结构计数

| 项目 | 原文 | 译文 |
|---|---:|---:|
| 章标题 | 1 | 1 |
| section | 7 | 7 |
| subsection | 17 | 17 |
| subsubsection | 14 | 14 |
| figure | 2 | 2 |
| table / tabular | 1 / 1 | 1 / 1 |
| caption | 3 | 3 |
| 脚注 | 2 | 2 |
| 原有 tcolorbox | 2 | 2 |
| 列表 item | 38 | 38 |
| 索引条目 | 16 | 16 |
| eqnarray 环境 | 32 | 32 |
| equation 环境 | 1 | 1 |
| 自动编号公式 | 33 | 33 |
| 无编号展示数组 | 1 | 1 |
| 行内数学片段 | 265 | 265 |

全部环境的开始和结束序列一致；表格列格式一致。全章有效 `&` 数量均为 92，表格行列和数学对齐结构保留。

## 数学、引用与标签保存情况

- 11 个 `label`、12 个 `ref`、60 次引用调用和 2 条 `input` 路径逐项同序一致。引文包含 73 个键出现次数、63 个不同键，全部保留。
- 265 处行内数学、32 个 eqnarray、1 个 equation、1 个无编号展示数组逐项核对一致，沿用源 TeX 自动编号，未添加手工 `tag` 或测试用计数器。
- 仅将数学中的 12 类说明性文本归一化后比较：鞋子、衬衫和折扣示例中原有 `text` 叙述（8 类），分段验证函数中的 `if / returns the correct result / otherwise`（3 类），`Accuracy→准确率`（1 类）。所有嵌入这些叙述的数字、变量、金额和运算表达式均另外核对，未改变。
- 两幅图内数学表达式及绘制路径均一致。
- 抽查 COCONUT、同策略蒸馏、结果奖励模型的索引条目，页码均可对应本章实际出现位置。

## 保留英语的具体理由

- `<think>` 与 `</think>` 是模型的特殊格式词元，保留字面；标签内的普通解题过程已译成中文。
- 生成式验证器概率公式中的 `Correct / Incorrect` 是被比较概率的具体词元，保留字面，正文已加“正确／错误”释义。
- 图 6.2 的 `This / The / cat / is / cute / lovely / .` 与离散词元、词元分布及图中位置对应，必须保留原词面。图内其他叙述性标签全部中文化。
- `LLM`、`ORM`、`PRM`、`GRPO`、`OPD`、`COCONUT`、`Quiet-STaR`、模型与数据集名、标准指标 `Pass@k / Cons@k / Consensus@k`、公式符号和引文元数据保留规范形式；章节中均有中文说明。
- 未翻译原源注释和已注释掉的草稿；这些不属于有效正文。

## 渲染检查

已渲染并目视检查最终 PDF 物理第 6、11、18、25、26、28、39 页，覆盖正文、唯一表格、全部两幅图、公式密集页和索引。图形节点和公式无缺字、遮挡或明显溢出。此前另检查过物理第 13 页的公式页。最终图像在 `render/page_*.png`，初次检查图在 `qa/initial_page_*.png`。

## 术语

全章遵照共享术语，inference 与 reasoning 均译“推理”；依语境采用“模型推理”“推理阶段”“推理能力”“推理路径”等。章标题“推理能力（Reasoning）”用于两个主题同名时的必要消歧。演绎推理、归纳推理、溯因推理、顿悟、同策略蒸馏、异策略蒸馏、潜空间推理等均采用共享译法。

下列术语尚未在当前共享表单列，供主代理统一补录：

| English | 本章译法 |
|---|---|
| credit assignment problem | 信用分配问题 |
| reward shaping | 奖励塑形 |
| telescoping sum | 裂项相消求和 |
| functional linguistic competence | 功能语言能力 |
| mechanistic interpretability | 机制可解释性 |
| natural language auto-encoder | 自然语言自编码器 |
| activation verbalizer | 激活语言化器 |
| activation reconstructor | 激活重构器 |
| consensus | 共识 |
| verifier hallucination | 验证器幻觉 |

## 源文疑点与处理

以下保留原文论述和符号，不擅自修改作者结论或公式：

1. `chapter12.tex` 第 421、424 行称形式系统判断“100% 可靠”，并将代码无错运行且产生有效输出作为推理步骤正确的判据。这一表述未区分执行有效性与推理语义正确性，译文按源保留。
2. 第 578 行把 `log Pr_theta` 称为生成步骤的“概率”，符号实际为对数概率；译文保留原叙述和公式。
3. 第 724 行的文字使用 `a_hat_maj`，前后公式使用带问题索引的 `a_hat_i^maj`；原记号差异保留。
4. 图 6.2 (c) 学生预测分布的标签写作 `Pr^s`，KL 目标中的学生分布为带参数的 `Pr_theta^s`；保留这一源文记号差异。

翻译与章内排版没有未决阻塞项。全书合并后的参考文献、索引和分页由主代理统一复核。
