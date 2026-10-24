> 状态更新（2026-10-24）：本术语表随已完成的全书中文译稿保留。成品：`00_books/Causal_Inference_What_If_cn_translated.pdf`（346页）。历史批次说明仅用于追溯。

# 《Causal Inference: What If》术语表（第 1 章已定术语）

> 全书统一。新增术语先查此表；表中已有的一律照用，不得另创译名。
> 标记：★ = 用户指定术语；▲ = 本书体例名（Fine Point / Technical Point 等）。

## 一、因果推断核心概念

| 英文 | 中文 | 备注 |
|---|---|---|
| causal effect | 因果效应 | ★ |
| individual causal effect | 个体因果效应 | |
| average causal effect | 平均因果效应 | ★；不作“平均处理效应” |
| counterfactual outcome | 反事实结局 | ★ |
| potential outcome | 潜在结局 | 与“反事实结局”同义，按原文择用 |
| factual outcome | 事实性结局 | |
| treatment / exposure | 处理 / 暴露 | 按原文语境择一，不混用 |
| outcome | 结局 | |
| intervention | 干预 | |
| consistency | 一致性 | ★ |
| exchangeability | 可交换性 | ★ |
| conditional exchangeability | 条件可交换性 | ★ |
| positivity | 正值性 | ★ |
| standardization | 标准化 | ★ |
| inverse probability weighting | 逆概率加权 | ★ |
| target trial | 目标试验 | ★ |
| identifiability / identified | 可识别性 / 可识别 | 不用“可辨识” |
| sharp causal null hypothesis | 严格因果零假设 | |
| causal null hypothesis | 因果零假设 | |
| causal risk difference | 因果风险差 | |
| causal risk ratio | 因果风险比 | |
| causal odds ratio | 因果优势比 | |
| effect measure | 效应度量 | |
| association | 关联 | |
| association measure | 关联度量 | |
| independence | 独立（性） | |
| mean independence | 均值独立 | |
| confounding | 混杂 | |
| confounder | 混杂因子 | 不用“混杂因素” |
| interference | 干扰 | |
| SUTVA (stable unit treatment value assumption) | 稳定单元治疗取值假设 | 首见处保留英文缩写 |
| super-population | 超总体 | |
| sampling variability | 抽样变异 | |
| random variability | 随机变异 | |
| nondeterministic counterfactuals | 非确定性反事实 | |
| number needed to treat (NNT) | 需治疗人数 | 保留缩写 NNT |
| risk | 风险 | |
| probability mass function / density / cdf | 概率质量函数 / 概率密度函数 / 累积分布函数 | |
| expected value | 期望值 | |
| functional | 泛函 | |
| contrast | 对比 | |
| marginal probability | 边缘概率 | |
| conditional probability | 条件概率 | |
| randomized experiment | 随机化实验 | |

## 二、本书体例名

| 英文 | 中文 | 说明 |
|---|---|---|
| Fine Point | 精要 | ▲ 原书全宽浅灰底框，按章编号（精要 1.1） |
| Technical Point | 技术注记 | ▲ 原书细框，按章独立编号（技术注记 1.1） |
| Part | 部分 | 第一部分／第二部分／第三部分 |
| Chapter | 章 | 第一章、第二章…… |

## 三、排版约定

- 公式编号沿用原书：(1.1)、(1.2)……用 `\tag{}` 硬编码，正文引用写“式 (1.1)”。
- 表、图沿用原书编号：表 1.1、图 1.1，正文写“表 1.1”“图 1.1”。
- 原书边注（marginalia）以 `\mnote{}` 排入外侧页边，不改为脚注。
- 人名、文献、软件名保留英文原名，不音译。

## 四、第 2–11 章新增术语

**第 2 章**　pseudo-population 伪总体；stratification 分层；effect modification 效应修饰；positivity 正值性；identified / unidentified 可识别／不可识别；crossover experiment 交叉实验；carryover effect 延续效应；risk period 风险期；MCAR 完全随机缺失；MAR 随机缺失；MNAR 非随机缺失；covariate 协变量；FR-CISTG 完全随机化因果解释结构树图；exogeneity 外生性

**第 3 章**　observational study 观察性研究；identifiability condition 可识别条件；well-defined intervention 定义良好的干预；ENDE 有效无直接效应干预；target trial emulation 目标试验模拟；transportability 可迁移性；attributable / excess / etiologic fraction 归因分数／超额分数／病因分数；one-step-ahead counterfactual 一步前瞻反事实；recursive substitution 递归替换；pragmatic trial 实用性试验；intention-to-treat effect 意向性治疗效应；compliers 依从者；point intervention 时点干预；eligibility criteria 合格标准

**第 4 章**　effect modifier 效应修饰因子；heterogeneity of treatment effects 处理效应的异质性；qualitative effect modification 定性效应修饰；effect-measure modification 效应度量修饰；surrogate / causal effect modifier 替代／因果效应修饰因子；transportability 可移植性；target population 目标总体；matching 匹配；restriction 限制；collapsibility 可压缩性；pooling 合并；SMR 标准化发病比；partial exchangeability 部分可交换性；external validity 外部效度；odds difference 优势差

**第 5 章**　joint intervention 联合干预；additive / multiplicative scale 加法／乘法尺度；superadditive / subadditive 超加性／次加性；supermultiplicative / submultiplicative 超乘性／次乘性；response type 反应类型；doomed / immune / helped / hurt 注定型／免疫型／受益型／受害型；sufficient cause 充分原因；component cause 成分原因；minimal sufficient cause 最小充分原因；sufficient-component cause 充分成分原因；background factors 背景因素；synergism / antagonism 协同作用／拮抗作用；sufficient cause interaction 充分原因交互作用；compositional epistasis 组合性上位效应；monotonicity 单调性；biologic interaction 生物学交互作用；causal pies 因果饼图

**第 6 章**　causal diagram 因果图；node / edge 节点／边；DAG 有向无环图；parent 父节点；ancestor / descendant 祖先／后代；causal Markov assumption 因果马尔可夫假设；NPSEM 非参数结构方程模型；path 路径；causal / noncausal path 因果路径／非因果路径；collider 对撞节点；d-separation d 分离；d-connected d 连通；blocked / open path 阻断的／开放的路径；faithfulness 忠实性；moralization 道德化；SWIG 单一世界干预图；do-calculus do 演算；influence diagram 影响图；decision node 决策节点；systematic bias 系统性偏倚；bias under the null 零假设下的偏倚；conditional bias 条件偏倚；measurement / information bias 测量偏倚／信息偏倚；dose-finding trial 剂量探索试验；causal risk factor 因果风险因子

**第 7 章**　backdoor path 后门路径；backdoor criterion 后门准则；descendant / non-descendant 子孙／非子孙；healthy worker bias 健康工人偏倚；confounding by indication 适应证混杂；channeling 渠道偏倚；reverse causation 反向因果；linkage disequilibrium 连锁不平衡；population stratification 群体分层；residual confounding 残余混杂；unmeasured confounding 未测量混杂；structural confounding 结构性混杂；sufficient set 充分集；M-bias M 偏倚；surrogate confounder 替代混杂因子；signed causal diagram 带符号的因果图；natural value of treatment 处理的自然取值；selection box 选择框；difference-in-differences 双重差分；negative outcome control 负结局对照；negative treatment control 负处理对照；additive equi-confounding 加法等量混杂；proximal causal inference 近端因果推断；front door criterion / formula 前门准则／前门公式；noncollapsible effect measure 不可收缩的效应度量

**第 8 章**　censoring 删失；loss to follow-up 失访；informative censoring 信息性删失；competing event 竞争事件；frailty 脆弱性；noncollapsibility 不可折叠性；multiplicative survival model 乘法生存模型；augmented causal diagram 增广因果图；haplotype 单体型；selection bias under the null 零效应下的选择偏倚

**第 9 章**　measurement error 测量误差；misclassification 错分；nondifferential / differential 非差异／差异的；recall bias 回忆偏倚；validation sample 验证样本；construct / measure / indicator 构念／测量／指标；noncausal diagram 非因果图；hidden factor 隐藏因素；path-specific effect 通路特定效应；ancillary care 辅助照护

**第 10 章**　estimand 估计目标；estimator 估计量；estimate 估计值；standard error 标准误；calibrated / conservative / anticonservative 标定／保守／反保守；coverage 覆盖率；honest (uniform) 诚实（均匀）；randomization-based inference 基于随机化的推断；ancillary statistic 辅助统计量；conditionality principle 条件性原理；continuity principle 连续性原理；nuisance parameter 冗余参数；curse of dimensionality 维数灾难；compatibility interval 相容区间；quantitative bias analysis 定量偏倚分析；credible interval 可信区间

**第 11 章**　conditional mean 条件均值；parametric / nonparametric estimator 参数／非参数估计量；saturated model 饱和模型；parsimonious 简约的；smoothing 平滑；bias–variance trade-off 偏倚—方差权衡；functional form 函数形式；dose-response curve 剂量—反应曲线；OLS 普通最小二乘法；residual 残差；predicted value 预测值；semiparametric model 半参数模型；link function 连结函数；kernel regression 核回归；bandwidth 带宽；GAM 广义可加模型；GEE 广义估计方程；Fisher consistent estimator Fisher 一致估计量

## 五、第 12–21 章新增术语

**第 12 章**　stabilized / nonstabilized weights 稳定化／非稳定化权重；marginal structural mean model 边缘结构均值模型；null preservation 空值保持；faux marginal structural model 虚假边缘结构模型；structural zero 结构性零；structural / random violations 结构性／随机性违背；joint positivity 联合正值性；homoscedasticity 同方差；bootstrapping 自助法

**第 13 章**　structural positivity 结构性正值性；doubly robust 双重稳健；plug-in estimator 插入式估计量；augmented IP weighted estimator 增广 IP 加权估计量；bag of little bootstraps 小自助袋；clever covariate 聪明协变量；iteratively reweighted least squares 迭代重加权最小二乘；empirical distribution 经验分布；second-order bias 二阶偏倚；TMLE 基于目标最小损失的估计量

**第 14 章**　rank preservation 秩保持；rank-preserving structural model 秩保持结构模型；structural nested mean model 结构嵌套均值模型；g-estimation g 估计；blip 瞬时效应；estimating equation 估计方程；score test 得分检验；closed form 闭式解

**第 15 章**　balancing score 平衡评分；prognostic score 预后评分；matched population 匹配总体；nonpositivity 非正值；measures of predictive power 预测力度量

**第 16 章**　instrument 工具；relevance condition 相关性条件；exclusion restriction 排除限制；usual IV estimand 通常的 IV 估计目标；two-stage least squares 两阶段最小二乘；weak instrument 弱工具；Wald estimator Wald 估计量；effect homogeneity 效应同质性；always-takers / never-takers / compliers / defiers 永远接受者／永不接受者／依从者／违抗者；principal strata 主层；natural / sharp bounds 自然／锐界；partial identification 部分识别；Mendelian randomization 孟德尔随机化；regression discontinuity design 回归断点设计

**第 17 章**　hazard 风险率；hazard ratio 风险率比（≠风险比）；survival curve 生存曲线；cumulative incidence 累积发病；administrative censoring 行政删失；staggered entry 错时进入；person-time 人时；Kaplan-Meier estimator Kaplan-Meier 估计量；cause-specific hazard 特定原因风险率；accelerated failure time 加速失效时间（AFT）；artificial censoring 人为删失；restricted mean survival time 限制平均生存时间

**第 18 章**　variable selection 变量选择；high-dimensional data 高维数据；tuning parameter 调优参数；ridge regression 岭回归；lasso 套索；shrinkage 收缩；forward / backward / stepwise selection 前向／后向／逐步选择；overfitting 过拟合；cross-validation 交叉验证；sample splitting 样本拆分；cross-fitting 交叉拟合；overadjustment 过度校正；random forests 随机森林；AIC 赤池信息准则

**第 19 章**　treatment strategy 处理策略；static / dynamic treatment strategy 静态／动态处理策略；sequentially randomized experiment 序贯随机化实验；sequential exchangeability 序贯可交换性；time-varying confounding 时变混杂；modified treatment policy 修正处理政策

**第 20 章**　treatment-confounder feedback 处理—混杂反馈；time-varying confounder 时变混杂因子；treatment history 处理史；g-null test / theorem g 零检验／g 零定理；dose-response function 剂量—反应函数；cumulative treatment 累积处理；new-user design 新使用者设计；net bias 净偏倚

**第 21 章**　ICE 迭代条件期望；big g-formula 大 g 公式；g-null paradox g 零悖论；multiply robust 多重稳健；factuals 事实量
