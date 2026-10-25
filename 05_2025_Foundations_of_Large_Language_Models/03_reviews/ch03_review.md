> 当前状态（2026-10-24）：全书中文译稿已编译完成，成品为 `00_books/Foundations_of_Large_Language_Models_cn_translated.pdf`（285页）。当前源码为 `../01_source/`，构建方法见该目录的 `README_build.txt`。以下为历史制作/校对依据，其中阶段进度、旧文件名及临时路径仅作追溯，不代表当前交付状态。

# 书内第 3 章《提示方法》交付报告

唯一原文：`00_originals/tex_v4_en/Chapter9/`。已逐段完成正文、标题、脚注、表格字段、原有框内指令与普通语言示例、图注，以及全部有效 TikZ 说明标签的中文翻译。主文件原文及译文均为 3067 行，654 个源行具有中文文本映射，分块映射保存在本工作目录的 `translation_*.tsv` 与 `revisions.tsv`。未使用旧中文译本或原始 PDF。

## 页数与编译

- 本章正文 53 页；独立测试 PDF 共 65 页，包含前置页、参考文献与索引。
- 最终测试命令：`python work/llmbook_v4/build_book.py --chapter 3 --tag ch3delivery`。
- 在正文分页稳定后另运行 `python work/llmbook_v4/ch3/finalize_index.py`，执行一次 upmendex→XeLaTeX，同步索引页码；已向主代理报告共享构建脚本的这一顺序问题。
- 最终 PDF：`work/llmbook_v4/builds/ch3delivery_20261023_144457/project/out/LLMFoundations.pdf`。
- 编译诊断：0 缺字、0 overfull、0 未定义引用。
- 诊断、书签及页数快照：`final_build.json`。逐项结构审计：`structure_audit.json`。

构建顺序修正证据：原测试流程在首轮 XeLaTeX 后生成索引，再插入 BibTeX 引文并重排，导致 AutoML 的索引页为 40、正文实际为 41，DTG 的索引页为 30、正文实际为 31。对稳定分页后的 idx 重新运行 upmendex→XeLaTeX 后，索引分别正确变为 41 和 31，PDF 仍为 65 页且无缺字、溢出或未定义引用。相应抽查记录在 `final_build.json` 的 `index_spot_checks` 中，过程日志为 `upmendex.exe.final_index.log` 和 `xelatex.exe.final_index.log`。主代理已接手将共享构建脚本及交付构建入口改为“引用与正文稳定后生成索引，再验证 idx 稳定性”的流程；本章未修改共享构建文件。

## 修改文件

仅修改交付目录 `01_source/Chapter9/` 中下列 9 个文件；未修改共享主文件、样式、术语表或其他章。

1. `chapter9.tex`
2. `Figures/figure-compressing-context-with-summary-tokens.tex`
3. `Figures/figure-contex-distillation.tex`
4. `Figures/figure-ensembling-methods.tex`
5. `Figures/figure-hard-prompt-and-soft-prompt.tex`
6. `Figures/figure-prefix-finetuning.tex`
7. `Figures/figure-prompt-pattern-soft-and-hard-prompts.tex`
8. `Figures/figure-prompt-tuning.tex`
9. `Figures/figure-soft-prompts-in-llms.tex`

八幅 TikZ 的全部解释性标签均已中文化，共涉及 68 个标签行。保留原节点名称、数学、颜色、连线与箭头；8 文件共 292 个 `node` 命令、190 个 `draw` 命令，源译一致。只作一处标签排版调整：图 3.9 左侧“第 i−1 步”改为与上一行右对齐，避免中文标签触及虚线框。另清理源图 16 个 `tikzstyle` 定义末尾多余分号，所有 `draw/node` 结尾分号保留。

## 原文与译文结构计数

| 项目 | 原文 | 译文 |
|---|---:|---:|
| 章标题 | 1 | 1 |
| section | 4 | 4 |
| subsection | 12 | 12 |
| subsubsection | 8 | 8 |
| figure / caption | 9 / 9 | 9 / 9 |
| table 浮动体 | 0 | 0 |
| tabular（包括示例排列表格） | 11 | 11 |
| 脚注 | 9 | 9 |
| 原有 tcolorbox | 83 | 83 |
| 列表 item | 38 | 38 |
| 索引条目 | 29 | 29 |
| eqnarray 环境 | 25 | 25 |
| equation 环境 | 1 | 1 |
| 自动编号展示公式行 | 27 | 27 |
| 行内数学片段 | 364 | 364 |

所有环境的开始/结束序列一致，11 个 tabular 的列格式一致，主文件有效 `&` 数量均为 133，表格行列及原始结构保留。

## 公式、引用与标签保存情况

- 20 个 `label`、23 个 `ref`、61 次引用调用、8 条 `input` 路径逐项同序一致。61 次引用包含 82 个键出现次数、75 个不同文献键；全部键保留。
- 364 个行内数学片段、25 个 eqnarray 与 1 个 equation 的内容逐项核对通过。全章沿用原自动计数机制，未添加 `tag` 或测试计数器。
- 仅翻译 8 处数学中的说明性文本：`Length→长`、`Width→宽`、`Depth→深`、`liters→升`、`trainable→可训练`（2 处）、`previous layer output→上一层输出`、`token embeddings→词元嵌入`。将这份说明性标签白名单归一化后，所有数学内容完全同序一致。
- 八幅 TikZ 中的数学序列全部原样保留；所有绘制路径几何相同。

## 英语保留项与理由

以下保留内容都是原文中的具体语言对象、符号、命令或专名，不能据此视为未译叙述。框内任务指令、角色设定、普通问答、数学解题、故事、诗歌、环境问题回答等均已中文化。

- 英译中开篇的 `The early bird catches the worm.` 是翻译源句；中英词语对照中的 `now/come/go/boy` 等是指定目标语言的答案。
- 英语语法纠错示例保留 `She don't...`、`There is.../There are...`、`Me and my friend.../My friend and I...` 等原句，保持错误与纠正之间的字面关系；所有角色与输入输出字段已译。
- 代码风格英德翻译中的 `[English]/[German]` 键及英语、德语句子，英西翻译中的英语源句和西班牙语译文，均是语言转换对象。
- 中译英自我改进示例中的初始英语译文、改进后的英语译文及绿色修改词，以及 DTG 示例中的随机错误英语译文，均保留，才能展示译文中的具体错误和修改。
- 末字母拼接任务的 `Elon Musk`、`Renata Mariela Mona Kristin`、相应字母和拼接结果保留；说明与推理步骤已译。
- 分类标签 `Positive/Negative/positive/negative/neutral` 是与公式标签集合及标签映射对应的具体数据，保留字面；情感样本文本和任务说明已译。
- 命名实体抽取中的 `Tom Jenkins`、`European Tourism Organisation`、`UK`、`Europe` 保留同一字面形式，保证文本与抽取结果对应；周围叙述及实体类型已译。
- 硬提示示例的 `Translate the sentence into Chinese.`、`Consider it done!`，图 3.3 的逐词输入，以及图 3.5/3.6 的 `Look/out/!` 是与词元或向量位置对应的对象。正文另提供了硬提示指令的中文释义。
- SCAN 指令与动作序列、硬币结果 `HHH/HTT/...`、特殊词元、变量占位符、Python 可执行代码、工具调用命令及 API 键保留行为和符号。Python 注释已译。
- Q/A 模板保留这一对用于解释英语缩写约定的字段，John/David 等人名及模型、数据集、文献名称保留。数学数据中的 `premise` 与英语字符串原样保留。

## 渲染检查

采用 PDF 技能及 Poppler 将生成稿渲染为 PNG；未读取原始书籍 PDF。已目视检查正文页、公式密集页，以及图 3.1—3.9 所在页，覆盖全部有效图。最终图像无缺字、遮挡或明显溢出。

- 正文：PDF 物理第 6 页。
- 复杂框图：物理第 26 页，图 3.1 的四格推理示例；共享中文高亮兼容宏修复后，绿色高亮和中文下划线已正确换行。
- 公式密集页：物理第 51、52 页，蒸馏目标、KL 散度和前缀表示公式。
- 模型结构图：物理第 41、49、51、53、54、55、57 页，覆盖集成、硬/软提示、上下文蒸馏、前缀微调、提示微调、软提示组合与上下文压缩。
- 图像保存在 `qa/`；图 3.9 最后一次标签修正的核验图为 `qa/verified_page_57.png`。
- 最终交付构建的正文、图 3.1、公式页、术语页和压缩图又渲染为 `qa/delivery_page_*.png` 并复核。

## 术语

已统一采用共享术语：inference / reasoning 均译“推理”；least-to-most prompting 译“由简到繁提示”；DTG 译“先思考后生成”；AutoML 译“自动化机器学习”；prompt embedding 译“提示嵌入”。

以下术语在当前共享表中尚未单列，供主代理统一补充：

| English | 本章译法 |
|---|---|
| prompt template | 提示模板 |
| system prompt | 系统提示 |
| one-shot learning | 单样本学习 |
| named entity recognition | 命名实体识别 |
| information extraction | 信息抽取 |
| self-refinement | 自我改进 |
| model ensembling | 模型集成 |
| prompt ensembling | 提示集成 |
| output ensembling | 输出集成 |
| hypothesis selection | 假设选择 |
| minimum Bayes risk search | 最小贝叶斯风险搜索 |
| prompt optimization | 提示优化 |
| performance estimation | 性能估计 |
| pseudo embedding | 伪嵌入 |
| summary token | 摘要词元 |
| multi-hop question answering | 多跳问答 |
| compositionality | 组合性 |
| meta-learning | 元学习 |

## 未决问题与源文异常

翻译和本章排版无待完成项。以下原文问题未擅自修订，供主代理记录勘误或独立审校：

1. `chapter9.tex:1277–1281` 的 Mary 苹果题，题目未给出“种了八棵树”，解答却使用了该条件；按原文保留，未补题设。
2. `chapter9.tex:2332` 被标为“正确”的硬币预测 1，先说“只有 HHH、HHT、HTH、THH 是相关的”，下一句却正确列出恰好一个正面的 HTT、THT、TTH；原文中间句矛盾照译，未删改。
3. `chapter9.tex:1869` 说明修改子问题生成函数 G 时，原文写“dynamically generate answers”，但随后公式生成的是子问题；保留其“动态生成答案”的字面表述。
4. 前缀向量从 p0 写到 pn，而参数数量仍写 L×n×d；未改原数学约定。
5. `figure-prefix-finetuning.tex` 的 l−1 与 l+1 两行隐状态下标为 0、1、3、4、5，中间 l 层为 0、1、2、3、4；未改数学节点。
6. `figure-compressing-context-with-summary-tokens.tex` 左上两个灰色历史隐状态都标为 h1；保留源节点标签。
7. 图 3.3 的英语提示样本与正文硬提示样本措辞不同，这是源文件已有差异，分别按各自原文保留。

可复现脚本：`apply_translation.py` 重建正文译稿，`translate_figures.py` 重建译图，`audit.py` 执行结构与数学核对。交付目录不含测试生成物。
