> 状态更新（2026-10-24）：本术语表随已完成的全书中文译稿保留。成品：`00_books/Causality_cn_translated.pdf`（349页）。历史批次说明仅用于追溯。

# 因果推断术语表（中英对照）

> 适用：《Causality: Models, Reasoning, and Inference》(2nd ed., Judea Pearl, 2009) 中文译稿
> 编制：2026-10-22　版本 v1（第 1—3 章）
> 规则：同一英文术语在全书中只对应一个中文译名；首次出现时用「中文（English）」标注，其后只用中文。

---

## 一、概率与统计基础

| 英文 | 中文 | 备注 |
|---|---|---|
| probability theory | 概率论 | |
| degree of belief | 信念度 | 贝叶斯解释下的主观概率 |
| subjective probability | 主观概率 | |
| proposition | 命题 | |
| event | 事件 | |
| sure proposition | 必然命题 | |
| joint distribution / joint probability | 联合分布 / 联合概率 | |
| marginal probability | 边缘概率 | |
| marginalization | 边缘化 | |
| conditional probability | 条件概率 | |
| conditional independence | 条件独立 | |
| independence | 独立 | |
| dependence | 相依（相关） | 表示统计关联时用「相依」，避免与「相关」混淆 |
| chain rule | 链式法则 | |
| law of total probability | 全概率公式 | |
| Bayes' theorem / Bayes' rule | 贝叶斯定理 / 贝叶斯法则 | |
| Bayes' inversion | 贝叶斯反演 | |
| prior probability | 先验概率 | |
| posterior probability | 后验概率 | |
| likelihood | 似然 | |
| odds | 几率 | 不等于「优势比」 |
| odds ratio | 优势比 | |
| risk ratio | 风险比 | |
| random variable | 随机变量 | |
| discrete variable | 离散变量 | |
| continuous variable | 连续变量 | |
| realization / value | 取值 | |
| configuration | 配置（组合取值） | |
| expectation | 期望 | |
| conditional expectation | 条件期望 | |
| variance | 方差 | |
| standard deviation | 标准差 | |
| correlation | 相关 | |
| regression coefficient | 回归系数 | |
| density function | 密度函数 | |
| multivariate normal | 多元正态 | |
| sufficient statistic | 充分统计量 | |
| factorization | 分解（因式分解） | |
| product decomposition | 乘积分解 | |
| collapsibility | 可压缩性 | |
| estimator / estimation | 估计量 / 估计 | |
| identification / identifiable | 识别 / 可识别 | 全书统一「识别」，不用「辨识」 |
| nonidentifiable | 不可识别 | |

## 二、图与贝叶斯网络

| 英文 | 中文 | 备注 |
|---|---|---|
| graph | 图 | |
| directed graph | 有向图 | |
| undirected graph | 无向图 | |
| directed acyclic graph (DAG) | 有向无环图 | 首次出现标注缩写 DAG |
| acyclic | 无环的 | |
| cyclic | 有环的 | |
| node / vertex | 节点 / 顶点 | 正文统一用「节点」 |
| edge / arc / link | 边 / 弧 / 连线 | 有向边称「弧」，无向边称「边」 |
| directed path | 有向路径 | |
| path | 路径 | |
| trail | 通路 | 不要求方向一致的连通序列 |
| chain | 链 | |
| fork | 分叉 | |
| collider | 碰撞点 | 即 v-结构中的汇合节点 |
| v-structure | v 结构 | |
| parent | 父节点 | |
| child | 子节点 | |
| ancestor | 祖先 | |
| descendant | 后代 | |
| root node | 根节点 | |
| leaf | 叶节点 | |
| adjacent / adjacency | 邻接 | |
| skeleton | 骨架 | 去掉箭头方向后的图 |
| subgraph | 子图 | |
| complete graph | 完全图 | |
| tree | 树 | |
| polytree | 多树 | |
| chain graph | 链图 | |
| moral graph | 端正图（moral graph） | 惯用译法，保留英文 |
| ancestral graph | 祖先图 | |
| d-separation | d-分离 | |
| d-connected | d-连通 | |
| blocked path | 阻断路径 | |
| unblocked path | 未阻断路径 | |
| Markov property | 马尔可夫性 | |
| Markov condition | 马尔可夫条件 | |
| ordered Markov condition | 有序马尔可夫条件 | |
| parental Markov condition | 父节点马尔可夫条件 | |
| causal Markov condition | 因果马尔可夫条件 | |
| minimal Markov condition | 极小马尔可夫条件 | |
| faithfulness / stable distribution | 忠实性 / 稳定分布 | 二者同义，正文用「稳定（忠实）」 |
| graphoid | 图拟（graphoid） | 保留英文，指满足对称性、分解性、弱联合性、收缩性的结构 |
| intersection | 交性质 | graphoid 第五条性质 |
| Bayesian network | 贝叶斯网络 | |
| belief network | 信度网络 | |
| network parameter | 网络参数 | |
| conditional probability table (CPT) | 条件概率表 | |
| inference | 推断（推理） | 概率计算意义下用「推断」 |
| belief updating | 信念更新 | |
| evidence | 证据 | |
| evidential reasoning | 证据推理 | |
| diagnostic / predictive | 诊断的 / 预测的 | |
| observational equivalence | 观测等价 | |
| Markov equivalence | 马尔可夫等价 | |
| pattern / equivalence class | 模式 / 等价类 | |

## 三、因果模型与干预

| 英文 | 中文 | 备注 |
|---|---|---|
| causality | 因果性 | |
| causation | 因果关系 | |
| causal model | 因果模型 | |
| probabilistic causal model | 概率因果模型 | |
| functional causal model | 函数因果模型 | |
| structural equation model (SEM) | 结构方程模型 | |
| structural equation | 结构方程 | |
| structural parameter | 结构参数 | |
| functional mechanism | 函数机制 | |
| mechanism | 机制 | |
| autonomous | 自主的 | 结构方程的自主性 |
| invariant / invariance | 不变的 / 不变性 | |
| exogenous variable | 外生变量 | |
| endogenous variable | 内生变量 | |
| disturbance term | 扰动项 | |
| error term | 误差项 | |
| unobserved / latent variable | 未观测变量 / 潜变量 | |
| omitted variable | 遗漏变量 | |
| intervention | 干预 | |
| intervention variable | 干预变量 | |
| intervention distribution | 干预分布 | |
| postintervention | 干预后 | |
| preintervention | 干预前 | |
| do(x) | do(x) | 算子形式，正文不译 |
| do-calculus / calculus of intervention | do 演算 / 干预演算 | |
| graph surgery / mutilation | 图手术 / 切除 | 「mutilated graph」译「切除图」 |
| augmented network | 增广网络 | |
| causal effect | 因果效应 | |
| total effect | 总效应 | |
| direct effect | 直接效应 | |
| indirect effect | 间接效应 | |
| controlled direct effect | 控制直接效应 | |
| average causal effect (ACE) | 平均因果效应 | |
| causal influence | 因果影响 | |
| causal relationship / causal relation | 因果关系 | |
| causal structure | 因果结构 | |
| causal diagram | 因果图 | |
| causal Bayesian network | 因果贝叶斯网络 | |
| causal sufficiency | 因果充分性 | 指无未观测混杂因子 |
| Markovian model | 马尔可夫模型 | |
| semi-Markovian model | 半马尔可夫模型 | |
| truncated factorization | 截断分解 | |
| oracle for interventions | 干预的「神谕」（oracle） | 保留英文以示意 |
| causal beam | 因果束 | |
| influence | 影响 | |
| spurious correlation | 伪相关 | |
| spurious association | 虚假关联 | |
| confounding | 混杂 | |
| confounder | 混杂因子 | |
| confounding bias | 混杂偏倚 | |
| deconfounding | 去混杂 | |
| adjustment | 调整 | |
| adjustment formula | 调整公式 | |
| back-door criterion | 后门准则 | |
| front-door criterion | 前门准则 | |
| instrumental variable | 工具变量 | |
| surrogate experiment | 替代实验 | |
| randomization | 随机化 | |
| randomized experiment | 随机化实验 | |
| observational study | 观测研究 | |
| ignorability | 可忽略性 | |
| exchangeability | 可交换性 | |
| conditional exchangeability | 条件可交换性 | |
| positivity | 正值性 | |
| consistency | 一致性 | 反事实框架中的 consistency，与「无矛盾」义区分 |
| standardization | 标准化 | |
| inverse probability weighting (IPW) | 逆概率加权 | |
| target trial | 目标试验 | |
| propensity score | 倾向评分 | |
| exogeneity | 外生性 | |
| endogeneity | 内生性 | |
| path coefficient | 路径系数 | |
| causal inference | 因果推断 | |
| causal discovery | 因果发现 | |
| causal explanation | 因果解释 | |
| explanation | 解释 | |
| counterfactual | 反事实 | |
| counterfactual outcome | 反事实结局 | |
| potential outcome | 潜在结局 | |
| counterfactual variable | 反事实变量 | |
| twin network | 孪生网络 | |
| probability of causation | 因果概率 | |
| actual cause | 实际原因 | |
| attribution | 归因 | |
| ramification | 后果（推演） | 指从假设推出的可检验蕴含 |
| testable / falsifiable | 可检验的 / 可否证的 | |
| experimentally testable | 实验可检验的 | |
| identifiability | 可识别性 | |
| identifying model | 可识别模型 | |
| nonidentifying model | 不可识别模型 | |
| parametric identification | 参数识别 | |
| nonparametric | 非参数 | |
| hedge / bow pattern | 弓形模式 | 图中一条混杂弧跨接于因果边 |
| dormant independence | 休眠独立 | |
| eq. (x) | 式 (x) | 正文引用公式用「式」 |

## 四、学习与推断算法

| 英文 | 中文 | 备注 |
|---|---|---|
| inductive game | 归纳博弈 | |
| minimal model | 极小模型 | |
| minimality | 极小性 | |
| Occam's razor | 奥卡姆剃刀 | |
| simplicity | 简约性 | |
| likelihood of a structure | 结构的似然 | |
| stable distribution | 稳定分布 | |
| IC algorithm | IC 算法 | 保留英文缩写 |
| IC\* algorithm | IC\* 算法 | |
| orientation | 定向 | |
| edge orientation | 边定向 | |
| latent structure | 潜结构 | |
| latent projection | 潜投影 | |
| inducing path | 诱导路径 | Pearl 原书术语 |
| Verma constraint | Verma 约束 | |
| d-separation criterion | d-分离准则 | |
| PC algorithm | PC 算法 | |
| pattern | 模式 | 部分有向图 |
| Markov blanket | 马尔可夫毯 | |
| Bayesian approach | 贝叶斯方法 | |
| prior | 先验 | |
| posterior | 后验 | |
| score-based | 基于评分的方法 | |
| constraint-based | 基于约束的方法 | |
| statistical time | 统计时间 | |
| nontemporal causation | 非时间性因果 | |
| temporal ordering | 时间顺序 | |
| genuine causation | 真正因果 | |
| coincidence | 巧合 | |

## 五、写作与排版统一约定

1. **人称与语气**：教材口吻，多用「我们」，避免「笔者」。论证性段落用陈述句，不堆砌「众所周知」「显而易见」。
2. **术语首现**：`反事实结局（counterfactual outcome）`，之后只写「反事实结局」。
3. **缩写**：DAG、CPT、ACE、SEM 首现给全称+缩写，此后用缩写，不加句号。
4. **数学**：变量斜体 $X, Y, x, u$；集合与算子正体 $\mathrm{do}(x)$、$\mathrm{ACE}$、$\Pr$；公式编号沿用原书 `(1.1)` 形式，便于对照原书。
5. **图表编号**：沿用原书编号（图 1.1、表 1.1），不重新编号。
6. **脚注**：原书脚注保留，编号沿用原书（如脚注 25）。
7. **引文**：章首题词保留原文人名与年份，诗句译出后加括号保留英文原句。
8. **文献引用**：`Pearl (1988b)`、`Spirtes et al. (1993)` 保持原格式，不译作者名、不改年份与字母后缀。
9. **标点**：中文正文用全角标点；括号内若为纯英文则用半角；破折号用「——」。
10. **数字与单位**：正文中的阿拉伯数字保持半角，范围用「—」（如 p. 23—62）。

---

## 六、第 4—11 章补充术语（v2，2026-10-22）

> 规则同上：一术语一译名，首现标英文，其后只用中文。本表为第 4—11 章定稿用词，
> 与第 1—3 章冲突时以本表为准并回改前文。

### 6.1 行动、计划与政策（第 4、11 章）

| 英文 | 中文 |
|---|---|
| conditional action | 条件行动 |
| stochastic policy | 随机策略 |
| conditional plan | 条件计划 |
| sequential back-door criterion | 序贯后门准则 |
| action-avoiding path | 避开行动的路径 |
| policy evaluation | 政策评估 |
| G-identifiability | G-可识别性 |
| admissible sequence | 可容许序列 |
| closed-form expression | 闭式表达式 |
| control query | 控制查询 |
| decision tree | 决策树 |
| influence diagram | 影响图 |
| mechanism modification | 机制修改 |
| STRIPS-like action | STRIPS 式行动 |
| enabling precondition | 启用前提 |
| evidential decision theory | 证据决策论 |
| causal decision theory | 因果决策论 |
| imaging | 映像 |
| closest world | 最接近世界 |
| nonmodularity | 非模块性 |
| external variation | 外部变化 |
| surgery | 手术 |
| POMDP | 部分可观测马尔可夫决策过程 |

### 6.2 结构方程与计量经济学（第 5 章）

| 英文 | 中文 |
|---|---|
| structural equation modeling (SEM) | 结构方程建模 |
| path diagram / path analysis | 路径图 / 路径分析 |
| path coefficient | 路径系数 |
| partial correlation | 偏相关 |
| partial regression coefficient | 偏回归系数 |
| recursive model | 递归模型 |
| saturated model | 饱和模型 |
| just identified | 恰识别 |
| overidentified | 过度识别 |
| covariance equivalent | 协方差等价 |
| edge reversal | 边反演 |
| single-door criterion | 单门准则 |
| suppressor effect | 抑制效应 |
| self-containment | 自足 |
| isolation / pseudo-isolation | 隔离 / 伪隔离 |
| orthogonality condition | 正交性条件 |
| weak / strong / superexogeneity | 弱 / 强 / 超外生性 |
| variation-free | 变差自由 |
| reparameterization | 重参数化 |
| unfalsifiable | 不可否证的 |
| robustness | 稳健性 |
| k-identified | k-可识别的 |
| bow arc | 弓形弧 |
| latent common parent | 潜公共父节点 |

### 6.3 辛普森悖论与混杂（第 6 章）

| 英文 | 中文 |
|---|---|
| stable unbiasedness | 稳定无偏 |
| incidental unbiasedness | 偶然无偏 |
| associational criterion | 关联准则 |
| barren proxy | 贫瘠代理 |
| closed-world assumption | 封闭世界假设 |
| incidental cancellation | 偶然抵消 |
| sure-thing principle | 确定事件原则 |
| common-cause principle | 共同原因原则 |
| nontrivial sufficient set | 非平凡充分集 |
| change-in-parameter method | 参数变化法 |
| risk difference | 风险差 |
| reference class | 参考类 |
| meta-statistical | 元统计的 |

### 6.4 反事实与结构语义（第 7 章）

| 英文 | 中文 |
|---|---|
| structure-based counterfactual | 基于结构的反事实 |
| potential response | 潜在响应 |
| potential response function | 潜在响应函数 |
| submodel | 子模型 |
| modifiable structural equation | 可修改结构方程 |
| causal world / causal theory | 因果世界 / 因果理论 |
| abduction | 溯因 |
| transduction | 转导 |
| epistemic inference | 认知推断 |
| material implication | 实质蕴含 |
| defeasible | 可废止的 |
| twin network | 孪生网络 |
| firing squad | 行刑队 |
| intrinsic nondeterminism | 内在非确定性 |
| objective chance | 客观概率 |
| explanandum | 被解释项 |
| general cause / singular cause | 一般原因 / 单一原因 |
| local surgery | 局部手术 |
| integrity constraint | 完整性约束 |
| nonmonotonic reasoning | 非单调推理 |
| privileged variable | 特权变量 |
| counterfactual antecedent | 反事实前件 |
| ceteris paribus | 其他条件不变 |
| composition / effectiveness / reversibility | 复合性 / 实效性 / 可逆性 |
| recursiveness | 递归性 |
| soundness | 可靠性 |
| null action | 空行动 |
| weak right decomposition | 弱右分解 |
| strong union | 强并 |
| token causation | 殊型因果 |
| quasi-deterministic | 准确定性的 |

### 6.5 不完美实验与因果概率（第 8、9 章）

| 英文 | 中文 |
|---|---|
| imperfect experiment | 不完美实验 |
| indirect experiment | 间接实验 |
| imperfect compliance | 不完美依从性 |
| noncompliance | 不依从 |
| complier | 依从者 |
| never-taker / always-taker | 永不接受者 / 总是接受者 |
| defier / contrarian | 违抗者 / 违拗者 |
| principal stratification | 主分层 |
| intention to treat (ITT) | 意向性治疗 |
| encouragement design | 鼓励设计 |
| sharp bounds | 锐界 |
| natural bounds | 自然界的 |
| canonical partition | 典范划分 |
| instrumental inequality | 工具不等式 |
| assumption-transparent | 假设透明 |
| response variable | 响应变量 |
| mapping variable | 映射变量 |
| probability of causation (PC) | 因果概率 |
| probability of necessity (PN) | 必要性概率 |
| probability of sufficiency (PS) | 充分性概率 |
| probability of necessity and sufficiency (PNS) | 必要且充分性概率 |
| probability of disablement (PD) | 阻抑概率 |
| probability of enablement (PE) | 促成概率 |
| excess risk ratio (ERR) | 超额风险比 |
| attributable risk | 归因风险 |
| causal power | 因果力 |
| local invertibility | 局部可逆性 |
| noisy OR / noisy AND | 噪声或 / 噪声与 |
| disjunctive mechanism | 析取机制 |
| monotonicity | 单调性 |
| susceptibility | 易感性 |

### 6.6 实际原因（第 10 章）

| 英文 | 中文 |
|---|---|
| actual cause | 实际原因 |
| production | 生产 |
| dependence | 依赖 |
| sustenance | 维持 |
| causal beam | 因果束 |
| natural beam | 自然束 |
| sustaining set | 维持集 |
| contributory cause | 贡献原因 |
| preemption / temporal preemption | 抢先 / 时间性抢先 |
| overdetermination | 过度决定 |
| quasi-dependence | 准依赖 |
| path-switching causation | 路径切换因果性 |
| contingency | 列联 |
| structural / circumstantial contingency | 结构性 / 情境性列联 |
| "but for" test | “若非”检验 |
| INUS condition | INUS 条件 |
| NESS | 充分集中的必要元素 |
| sufficient component | 充分成分 |
| normality | 常规性 |

### 6.7 统计方法（跨章）

| 英文 | 中文 |
|---|---|
| propensity score matching | 倾向评分匹配 |
| sensitivity analysis | 敏感性分析 |
| auxiliary experiment | 辅助实验 |
| g-estimation | G-估计 |
| sequential deconfounding | 序贯去混杂 |
| irreducible set | 不可约集 |
| ETT (effect of treatment on the treated) | 处理对受处理者的效应 |
| balance | 平衡 |
| noise term | 噪声项 |
| time reversal | 时间反转 |
| Gibbs sampling | 吉布斯抽样 |
| Dirichlet prior | 狄利克雷先验 |
| statistical time | 统计时间 |
