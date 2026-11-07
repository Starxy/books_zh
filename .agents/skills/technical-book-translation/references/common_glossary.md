# 按场景使用的通用术语表

本表固定各场景的默认正文写法，供新译、续译和校订时选用；只有英文词项与语境/义项同时符合时才适用。具体书籍的首次出现位置、缩写介绍和例外写入该书 `02_glossary`，不在此表登记各书进度。

## 使用与维护

- 术语选择优先级见 [按语境维护术语](book-profiles.md#按语境维护术语)。先选择适用场景，再将本轮涉及的条目纳入本书术语表；已有定译与本表不同时，核对义项和用户约定，在本书表中明确采用的写法及理由。
- “默认正文写法”是行文中采用的形式。中文译名的首次英文括注、保留英文时的可选中文说明，按 [英文术语保留规则](book-profiles.md#英文术语保留规则) 及其后的首次介绍规则处理。中文释义不是英文保留词的替换词；已经介绍的缩写可按本书约定使用。
- 同一义项在正文、标题、图注、表格和索引中统一；不同义项分开登记。扫描或替换时查看上下文，不按英文词形全书替换。
- 并行分工前由集成者把选定条目及本书例外交给各执行者；新词和改译先集中到本书术语表。只有维护本 skill 或用户要求更新通用约定时才修改本表，单书特例不自动成为其他书的默认写法。

按内容查阅：

- [深度学习与语言模型中的英文保留词](#深度学习与语言模型中的英文保留词)
- [生成模型、扩散与表征](#生成模型扩散与表征)
- [信息论与编码](#信息论与编码)
- [优化、数值计算与博弈](#优化数值计算与博弈)
- [智能、学习与控制论](#智能学习与控制论)
- [统计与因果推断](#统计与因果推断)
- [跨场景的同形词](#跨场景的同形词)

## 深度学习与语言模型中的英文保留词

| 英文 | 默认正文写法 | 语境与说明 |
|---|---|---|
| Transformer | Transformer | 架构或模型名称；首次可用中文简述其含义。 |
| token / tokens | token / tokens | 模型处理的离散单元；首次可按本书语境说明为“数据元”。单复数依原文语义与本书约定使用。 |
| softmax | softmax | 函数或算子名称；保持规范大小写及数学、代码中的写法。 |
| BERT | BERT | 模型缩写；原文给出的全称和解释仍须保留。 |
| GPT | GPT | 模型缩写；原文给出的全称和解释仍须保留。 |
| CLIP | CLIP | 模型或方法缩写；原文给出的全称和解释仍须保留。 |
| DDIM | DDIM | 扩散模型或采样方法缩写；原文给出的全称和解释仍须保留。 |

## 生成模型、扩散与表征

| 英文 | 默认正文写法 | 语境与说明 |
|---|---|---|
| autoencoder (AE) | 自编码器 | AE 可在首次介绍后使用。 |
| Bayes optimal denoiser | 贝叶斯最优去噪器 | 去噪估计问题中的最优性按原文定义。 |
| classifier guidance | 分类器引导 | 生成模型的条件引导。 |
| classifier-free guidance (CFG) | 无分类器引导 | CFG 可在首次介绍后使用。 |
| complete / overcomplete | 完备／过完备 | 用于表征、字典或基的相应性质；一般叙述中的 complete 按句意处理。 |
| consistency model | 一致性模型 | 模型类别，不与下列 consistent representation 混写。 |
| consistent representation | 一致表征 | 表征之间的一致关系或性质。 |
| cross attention / cross-attention | 交叉注意力 | 两种英文拼写按同一概念处理。 |
| denoising | 去噪 | 去噪过程或任务。 |
| diffusion process / diffusion models | 扩散过程／扩散模型 | 分别对应过程与模型类别。 |
| embedding | 嵌入 | 特征、向量或空间的嵌入；对象由上下文明确。 |
| empirical distribution | 经验分布 | 由样本确定的分布。 |
| few-step model | 少步模型 | 生成或采样所需步数较少的模型。 |
| flow matching | 流匹配 | 生成建模方法。 |
| generalization | 泛化 | 模型对训练数据以外情形的表现；数学论述中的“推广”另按语境判断。 |
| ground truth | 真实值 | 本书已确认“真值”时沿用；数据标注语境可明确为真实标注，不把参考标签表述成无误事实。 |
| latent / latent space | 潜在／潜在空间 | 变量、状态等完整词组按其对象译写；latent variable 的已有“潜变量”定译可沿用。 |
| memorization | 记忆 | 模型对训练数据的记忆。 |
| noise predictor | 噪声预测器 | 预测目标为噪声。 |
| representation autoencoder (RAE) | 表征自编码器 | RAE 可在首次介绍后使用。 |
| sampling | 采样 | 从模型或分布生成样本；统计调查中的抽样见后表。 |
| text prompt | 文本提示 | 文本条件或输入提示。 |
| transport map | 传输映射 | 分布传输语境中的映射，保留原文对映射的定义。 |
| velocity predictor | 速度预测器 | 速度或速度场的预测；具体参数化以原文为准。 |

## 信息论与编码

| 英文 | 默认正文写法 | 语境与说明 |
|---|---|---|
| coding rate | 编码率 | 单位和归一化方式按原文保留。 |
| coding rate reduction | 编码率降低 | 与 coding rate 使用同一“编码率”写法。 |
| compressive sensing | 压缩感知 | 信号采集与重建语境。 |
| cross-entropy | 交叉熵 | 信息量或损失函数，按原文区分。 |
| differential entropy | 微分熵 | 连续分布语境，不与离散熵混同。 |
| entropy | 熵 | 具体定义、对数底和单位按原文。 |
| Jensen–Shannon (JS) divergence | Jensen–Shannon 散度 | 首次介绍后可用“JS 散度”；人名拼写保留。 |
| KL divergence | KL 散度 | 保留 KL；原文展开全称时同时保留。 |
| Kolmogorov complexity | 柯尔莫哥洛夫复杂性 | 算法信息论语境。 |
| lossy coding rate | 有损编码率 | 允许失真的编码率。 |
| mutual information | 互信息 | 按原文区分互信息与条件互信息。 |
| rate distortion / rate-distortion | 率失真 | 指编码率与失真的关系；rate-distortion function 写作“率失真函数”。定义与译名说明见下段。 |
| total variation (TV) distance | 总变差距离 | 首次介绍后可用“TV 距离”；与总变差正则项区分。 |

率失真函数描述给定失真限制下可达到的最低编码率，与一般的有损编码率分开登记。[斯坦福 EE276 讲义，第 3 节](https://web.stanford.edu/class/ee276/files/previous_notes/lecture_13.pdf)；中文“率失真函数”的对应可参见 [《有损图像编码理论与实际性能的差距》](https://just.ustc.edu.cn/cn/article/doi/10.52396/JUSTC-2024-0138)。图片中的“失真编码率”不直接作为 rate distortion 在所有语境下的默认译名；本表据上述概念区别采用“率失真”。

## 优化、数值计算与博弈

| 英文 | 默认正文写法 | 语境与说明 |
|---|---|---|
| adjoint | 伴随 | 依对象写作伴随算子、伴随变量或伴随方程等。 |
| alternating optimization | 交替优化 | 按原文保留交替更新的对象。 |
| automatic differentiation (AD) | 自动微分 | AD 可在首次介绍后使用。 |
| convex / strongly convex | 凸／强凸 | 用于函数、问题等原文指定对象。 |
| gradient descent | 梯度下降 | 优化方法。 |
| ill-conditioned | 条件不良的 | 数值条件性质，不与 ill-posed（不适定的）混同。 |
| Kronecker factorization | 克罗内克分解 | 保留原文的分解结构及近似条件。 |
| learning rate | 学习率 | 与步长是否等同按具体算法判断。 |
| line search | 线搜索 | 确定步长的搜索过程。 |
| Nash equilibrium | 纳什均衡 | 博弈论语境。 |
| oracle | 预言机 | 理论上的查询机制或理想信息来源；实验对照中的 oracle 需说明其实际含义。 |
| proximal gradient descent | 近端梯度下降 | 保留近端算子和梯度步骤的区别。 |
| scalable | 可扩展 | 明确扩展的是数据、模型或计算规模。 |
| Stackelberg equilibrium | 斯塔克尔伯格均衡 | 领导者与跟随者博弈语境。 |
| (sub)gradient | （次）梯度 | 原文合写时保留概括方式；分别出现时 gradient 为“梯度”，subgradient 为“次梯度”。 |
| tractable | 易处理的 | 强调可求解性时可用“可解的”，保留原文对计算资源和问题条件的限定。 |

## 智能、学习与控制论

| 英文 | 默认正文写法 | 语境与说明 |
|---|---|---|
| AI program | 人工智能纲领 | 指人工智能研究的纲领或路线；软件语境见“跨场景的同形词”。 |
| cybernetics program | 控制论纲领 | 指控制论研究纲领，不泛指控制程序。 |
| embodied AI | 具身智能 | 智能与身体、感知及环境交互的语境。 |
| imitation learning | 模仿学习 | 学习方法。 |
| ontogenetic | 个体发育的 | 形容词，不单独补出“智能”；修饰 intelligence 时使用下一条。 |
| ontogenetic intelligence | 个体成长智能 | 个体在自身生命历程中学习与适应；对应图片中省略了中心词的写法。 |
| open-ended | 开放式 | 具体修饰任务、学习或过程，保留原文对其开放性的含义。 |
| parsimony | 简约性 | 建模或理论原则。 |
| representation | 表征 | 学习得到的编码或内部结构；数学中的“表示”见后表。 |
| representation learning | 表征学习 | 学习数据表征的方法或任务。 |
| scientific intelligence | 科学智能 | 智能的形式或层次，具体定义由原文给出。 |
| self-consistency | 自洽性 | 理论、系统或闭环表征的内部相容性；语言模型的方法名称见后表。 |
| societal intelligence | 社会智能 | 社会层面的智能，保持原文对个体与社会层次的区别。 |

这里将 ontogenetic 与 ontogenetic intelligence 分列，依据其形容词用法及个体学习语境；研究纲领中的 program 也与软件程序分开。[作者教材第一章：An Informal Introduction to Intelligence](https://ma-lab-berkeley.github.io/deep-representation-learning-book/Ch1.html) 提供了这些语境，中文写法沿用图片约定并补足适用范围。

## 统计与因果推断

本组承接 skill 原有的义项区分，供相关书籍使用。

| 英文 | 默认正文写法 | 语境与说明 |
|---|---|---|
| statistical inference | 统计推断 | 从数据进行统计推断；不采用模型运行语境的“推理”。 |
| causal inference | 因果推断 | 因果效应、识别与估计语境。 |
| average causal effect (ACE) | 平均因果效应 | 保留 ACE 对应的原文概念。 |
| average treatment effect (ATE) | 平均处理效应 | 与 ACE 分开登记；是否在特定模型中相同须按原文判断。 |
| hazard ratio | 风险率比 | 不与 risk ratio 混同。 |
| risk ratio | 风险比 | 不与 hazard ratio 混同。 |
| estimand | 估计目标 | 所要估计的量。 |
| estimator | 估计量 | 用于估计的统计量或规则。 |
| estimate | 估计值 | 估计得到的具体结果。 |
| identifiability | 可识别性 | 从观测分布及假设确定目标量的性质。 |
| dependence | 相依 | 不自动等同于 correlation。 |
| correlation | 相关 | 保留原文指定的相关性定义。 |
| sampling | 抽样 | 从总体或抽样框选取调查、研究单位；从概率模型生成样本时按“采样”处理。 |

潜在结局、反事实结局、可交换性、正值性、一致性、标准化、逆概率加权和目标试验等继续按本书术语表；图模型中的 collider、潜变量、干预节点与双向边按本书术语及图例处理。靶向学习中的 targeted learning、TMLE、nuisance parameter、clever covariate 等也须结合目标书定义确定。组学、影像等场景保留基因/蛋白名称、单位、维数和图像标识，不由本表替换这些专门命名。

## 跨场景的同形词

先选义项，再使用本表前面的正文写法；下表补充容易混用的场景。

| 英文与场景 | 默认正文写法 | 区分方法 |
|---|---|---|
| inference：模型运行阶段 | 模型推理／推理阶段 | 指运行模型得到输出，与统计推断区分。 |
| reasoning：推理能力或过程 | 推理／推理能力／推理过程 | 按句法明确能力或过程，不能与模型运行阶段直接互换。 |
| policy：决策、强化学习 | 策略 | 决策规则或行为选择。 |
| policy：公共治理 | 政策 | 社会、机构或政府治理语境。 |
| token：编译器 | 词法单元 | 按目标书已有定译；不套用语言模型中保留英文的规则。 |
| token：身份认证 | 令牌 | 凭据或认证机制；代码中的标识符仍保留原样。 |
| program：软件 | 程序 | AI program 指软件时写“人工智能程序”，不使用研究纲领的译法。 |
| representation：群、代数等数学结构 | 表示 | 不套用学习模型中“表征”的译法。 |
| self-consistency：语言模型多路径采样与答案汇总方法 | 自一致性 | 与系统性质的“自洽性”分开登记；本书已有方法名称时沿用。 |

跨场景示例参考本仓库 [世界模型术语表](../../../../10_2026_A_Definition_and_Roadmap_for_World_Models/02_glossary/glossary_en_zh.md) 中 self-consistency 的系统性质义项，以及 [大语言模型术语表](../../../../13_2024_Large_Language_Models_A_Deep_Dive/02_glossary/glossary_en_zh.md) 中的方法名称义项。来源与图片适配说明见 [provenance.md](provenance.md#通用术语表的来源与适配)。
