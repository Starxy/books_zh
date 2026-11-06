# 深度生成建模术语表

术语随本书译排更新。统计和贝叶斯语境中的 inference 译“推断”，大语言模型运行阶段的 inference 译“推理”，reasoning 也译“推理”并用上下文区分。

| English | 中文 | 用法 |
|---|---|---|
| deep generative modeling | 深度生成建模 | 书名和建模范式。 |
| deep generative model (DGM) | 深度生成模型 | 学习概率分布的模型。 |
| discriminative model | 判别模型 | 第 1 章的条件分布建模。 |
| generative process | 生成过程 | 决定随机变量的产生及依赖关系。 |
| uncertainty | 不确定性 | 模型对输入、环境或决策的认知。 |
| joint / marginal / conditional distribution | 联合分布／边缘分布／条件分布 | 分布与质量、密度函数分别按语境表述。 |
| representation learning | 表示学习 | 从数据提取供后续任务使用的表示。 |
| disentangling | 解耦 | 表示中的因素分离。 |
| equivariant representation | 等变表示 | 输入变换后表示按相应规律变换。 |
| information bottleneck | 信息瓶颈 | 序中用来解释 VAE 的类比。 |
| generalization | 泛化 | 在未见数据上表现良好。 |
| likelihood / log-likelihood | 似然／对数似然 | 数据给定时关于参数的函数。 |
| probabilistic graphical model (PGM) | 概率图模型 | 用图表示变量的依赖关系。 |
| mixture model / mixture of Gaussians (MoG) | 混合模型／高斯混合模型 | 保留本书缩写 MoG。 |
| probabilistic circuit (PC) | 概率电路 | 用和、积单元组合概率分布。 |
| autoregressive model (ARM) | 自回归模型 | 保留本书缩写 ARM。 |
| causal convolution | 因果卷积 | 自回归顺序中卷积不能访问未来位置。 |
| flow-based model / normalizing flow | 基于流的模型／归一化流 | 区分模型类别与可逆变换方法。 |
| change of variables | 变量变换 | 概率密度及概率质量的变换。 |
| coupling layer | 耦合层 | 可逆流模型的组成单元。 |
| latent variable / latent space | 潜变量／潜在空间 | 与直接观测的变量及数据空间区分。 |
| probabilistic PCA (pPCA) | 概率主成分分析 | 保留 pPCA 的大小写。 |
| variational inference | 变分推断 | 统计推断语境。 |
| variational autoencoder (VAE) | 变分自编码器 | 首次出现保留英文全称和缩写。 |
| evidence lower bound (ELBO) | 证据下界 | 统计意义上的对数边缘似然下界。 |
| prescribed model / implicit model | 指定分布模型／隐式模型 | 本书区别是否预先指定分布族。 |
| generator / discriminator | 生成器／判别器 | GAN 中的两个模型。 |
| generative adversarial network (GAN) | 生成对抗网络 | 保留本书缩写。 |
| energy-based model (EBM) | 基于能量的模型 | 按上下文可称能量模型。 |
| partition function | 配分函数 | 玻尔兹曼分布的归一化量。 |
| restricted Boltzmann machine (RBM) | 受限玻尔兹曼机 | 与一般玻尔兹曼机区分。 |
| score function / score matching | 得分函数／得分匹配 | 得分指对数密度对数据的梯度。 |
| score-based generative model | 基于得分的生成模型 | 第 9 章术语。 |
| flow matching | 流匹配 | 学习连续流的速度场，与离散可逆流区分。 |
| neural compression | 神经压缩 | 用神经网络建模的压缩方法。 |
| large language model (LLM) | 大语言模型 | 保留缩写 LLM。 |
| generative AI system (GenAISys) | 生成式人工智能系统 | 保留本书架构缩写。 |
| inference (probabilistic / LLM runtime) | 推断／推理 | 区分概率查询或后验估计与模型运行。 |
| natural language processing (NLP) | 自然语言处理 | 第 11 章的语言处理任务。 |
| token / tokenizer | 词元／词元化器 | 字符级和子词级处理均适用。 |
| embedding / positional embedding | 嵌入／位置嵌入 | 与位置编码的实现区别按原文。 |
| foundation model (FM) | 基础模型 | 通用预训练模型。 |
| pre-training / fine-tuning | 预训练／微调 | 区分训练阶段。 |
| low-rank adaptation (LoRA) | 低秩适配 | 原权重冻结，学习低秩增量。 |
| mixture of experts (MoE) | 混合专家 | 路由器选择专家。 |
| selective state space model (S3M) | 选择性状态空间模型 | 保留原文缩写，表 11.1 的 S4M 是另一个条目。 |
| retrieval-augmented generation (RAG) | 检索增强生成 | 数据库检索结果参与生成。 |
| data encoder / retrieval-storage module | 数据编码器／检索／存储模块 | 保留 DE 和 R/S。 |
| compositionality | 可组合性 | 系统和组成部件的讨论。 |
| continual learning | 持续学习 | 与遗忘旧表示的问题相关。 |
| direct preference optimization (DPO) | 直接偏好优化 | 与使用单独奖励模型的 RLHF 流程区分。 |
| cross-entropy | 交叉熵 | 根据上下文区分分类损失和分布间交叉熵。 |
| independent and identically distributed | 独立同分布 | 保留本书小写 iid。 |
| log-sum-exp (LSE) | 对数和指数函数 | 先逐项取指数、求和，再取对数。 |
| expectation-maximization (EM) | 期望最大化 | 混合模型的训练算法。 |
| fully factorized model | 完全因子分解模型 | 全部变量相互独立。 |
| decomposability / smoothness | 可分解性／平滑性 | 概率电路的积单元和和单元性质。 |
| finite memory / long-range dependency | 有限记忆／长程依赖 | 自回归模型的输入依赖。 |
| dilation / causal convolution | 膨胀率／因果卷积 | 不接触未来位置的卷积。 |
| discretized logistic distribution | 离散化逻辑斯蒂分布 | 与类别分布的离散化区分。 |
| base distribution | 基分布 | 流模型用于变换的起始分布。 |
| uniform / variational dequantization | 均匀／变分去量化 | 将离散观测转成连续建模输入。 |
| integer discrete flow (IDF) | 整数离散流 | 保留原书缩写。 |
| straight-through estimator (STE) | 直通估计量 | 前向离散运算时的梯度近似。 |
| amortized variational posterior | 摊销变分后验 | 跨样本共享推断参数。 |
| posterior collapse / mode collapse | 后验坍塌／模式坍塌 | 分别见 VAE 和 GAN。 |
| aggregated posterior | 聚合后验 | 变分后验在数据分布上的平均。 |
| hole problem | 空洞问题 | 先验与聚合后验的覆盖差异。 |
| importance weighting | 重要性加权 | 区别于单样本 ELBO。 |
| generative topographic mapping (GTM) | 生成式拓扑映射 | 先验建模方法，保留缩写 GTM。 |
| inverse autoregressive flow | 逆自回归流 | 变分后验使用的流。 |
| hyperspherical latent space | 超球面潜在空间 | 与欧氏潜在空间区分。 |
| diffusion-based deep generative model (DDGM) | 基于扩散的深度生成模型 | 区分前向扩散和反向扩散。 |
| parameterization sharing | 参数化共享 | 第 6 章联合建模使用的术语。 |
| free energy | 自由能 | RBM 消去隐藏变量后的能量表示。 |
| contrastive divergence (CD) | 对比散度 | 与持续对比散度（PCD）区分。 |
| subspace restricted Boltzmann machine | 子空间受限玻尔兹曼机 | 保留 subspaceRBM。 |
| annealed importance sampling | 退火重要性采样 | 近似配分函数。 |
| integral probability metric (IPM) | 积分概率度量 | 与 KL 散度的用途区分。 |
| maximum mean discrepancy (MMD) | 最大均值差异 | 基于样本集合的分布比较。 |
| stochastic gradient Langevin dynamics (SGLD) | 随机梯度朗之万动力学 | 与一般朗之万动力学区分。 |
| probability flow ODE (PF-ODE) | 概率流常微分方程 | 与产生同一边缘分布路径的 SDE 区分。 |
| variance exploding / variance preserving | 方差爆炸型／方差保持型 | 原缩写 VE／VP。 |
| continuous normalizing flow (CNF) | 连续归一化流 | 用常微分方程定义。 |
| instantaneous change of variables | 瞬时变量变换 | 由连续性方程得到。 |
| conditional flow matching (CFM) | 条件流匹配 | 参照条件概率路径。 |
| stochastic interpolants | 随机插值量 | 用于连续生成的构造。 |
| codec / bitstream | 编解码器／比特流 | 压缩系统语境。 |
| rate / distortion | 码率／失真 | 区分压缩后长度和解码误差。 |
| bits per pixel (bpp) | 每像素比特数 | 原缩写 bpp。 |
| differentiable quantization / codebook | 可微量化／码本 | 压缩中的离散表征。 |
| entropy coding model | 熵编码模型 | 根据概率为符号编码。 |
| scale hyperprior | 尺度超先验 | 生成分布尺度参数的先验。 |
