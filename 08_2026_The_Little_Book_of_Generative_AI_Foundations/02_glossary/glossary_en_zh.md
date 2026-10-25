# 生成式人工智能基础小册：中英术语表

底本为 Tianhua Chen, *The Little Book of Generative AI Foundations: An Intuitive Mathematical Primer*, arXiv:2605.29713v2，2026-09-08。术语取自该版英文 TeX 和本书中文 TeX，按正文中的含义确定译法；章号是书中显示的章号，不是历史文件名中的数字。

同一英文词在不同语境下可以有不同译法。尤其注意：统计模型的 inference 译“推断”；向量微积分的 divergence 译“散度”，概率分布之间的 divergence 也译“散度”，二者的定义不同；score 指对数密度对数据的梯度，不能理解为分类器输出的分数。intractable 表示一般情形下难以有效求值，不表示数学上不可计算。

## 第1章：线性代数、PCA 与自编码器

来源：[cht_1_2_merged.tex](../01_source/chapters/cht_1_2_merged.tex)。

| 英文术语 | 本书译法 | 语境与区别 |
| --- | --- | --- |
| linear transformation | 线性变换 | 矩阵对向量的作用 |
| basis / change of basis | 基／基变换 | 向量的坐标表示变化，不是向量本身变化 |
| composition | 复合 | 线性变换的先后作用 |
| projection | 投影 | 向方向或子空间映射 |
| orthogonal projection | 正交投影 | 投影残差与目标子空间正交 |
| eigenvector / eigenvalue | 特征向量／特征值 | 矩阵保留的方向及其缩放因子 |
| eigendecomposition | 特征分解 | 用特征向量构成的基表示矩阵 |
| orthogonal / orthonormal | 正交／标准正交 | 后者还要求各向量为单位长度 |
| principal component analysis (PCA) | 主成分分析 | 方差最大化与最小重构误差两种表述 |
| principal component | 主成分 | PCA 的投影坐标或相应方向，按句意区分 |
| covariance matrix | 协方差矩阵 | 变量之间的二阶统计关系 |
| variance maximisation | 方差最大化 | PCA 的优化目标 |
| explained variance ratio | 解释方差比 | 所选主成分方差占总方差的比例 |
| trace | 迹 | 方阵对角元素之和 |
| similarity transformation | 相似变换 | 同一线性变换在不同基下的表示 |
| singular value decomposition (SVD) | 奇异值分解 | 输入、输出使用不同标准正交基 |
| singular value | 奇异值 | SVD 中的非负缩放因子 |
| rank-one transformation | 秩一变换 | 由两个向量的外积构成 |
| outer product | 外积 | 向量产生矩阵的乘积，不是三维叉积 |
| dimensionality reduction | 降维 | 用低维坐标表示高维数据 |
| reconstruction / reconstruction error | 重构／重构误差 | 从低维表示恢复输入及其误差 |
| autoencoder | 自编码器 | 联合学习编码器与解码器 |
| encoder / decoder | 编码器／解码器 | 从数据到潜在表示／从潜在表示到数据 |
| latent representation / latent code | 潜在表示／潜编码 | 低维内部表示 |
| subspace | 子空间 | 对线性组合封闭的向量集合 |
| span | 张成空间 | 一组向量全部线性组合的集合 |
| column space / range | 列空间／值域 | 此处指矩阵列向量张成的空间 |
| orthogonalisation | 正交化 | 改变表示子空间的基，不改变该子空间 |
| manifold | 流形 | 非线性解码器可描述的低维几何结构 |
| ambient space | 环境空间 | 容纳低维结构的高维空间 |

## 第2—3章：概率潜变量模型与变分推断

来源：[cht3.tex](../01_source/chapters/cht3.tex)、[cht4_new.tex](../01_source/chapters/cht4_new.tex)；高斯代数另见[附录A](../01_source/chapters/cht_appendix1.tex)。

| 英文术语 | 本书译法 | 语境与区别 |
| --- | --- | --- |
| probabilistic principal component analysis (PPCA) | 概率主成分分析 | PCA 的线性高斯潜变量模型 |
| latent variable / observed variable | 潜变量／观测变量 | 不直接可见的生成因素／实际看到的数据 |
| generative model | 生成模型 | 对数据生成机制的概率描述 |
| prior / posterior | 先验／后验 | 观测数据之前／给定数据之后的潜变量分布 |
| conditional distribution | 条件分布 | 给定另一变量时的分布 |
| joint distribution | 联合分布 | 多个变量共同的概率分布 |
| marginal distribution / marginalisation | 边缘分布／边缘化 | 对其余变量求和或积分消去 |
| likelihood / log-likelihood | 似然／对数似然 | 数据固定时关于模型参数的函数 |
| marginal likelihood | 边缘似然 | 消去潜变量后的观测数据似然 |
| maximum likelihood estimation | 最大似然估计 | 通过似然选择参数 |
| isotropic Gaussian noise | 各向同性高斯噪声 | 各方向具有相同方差 |
| affine transformation | 仿射变换 | 线性变换加平移 |
| completing the square | 配方法 | 高斯积分与条件分布推导 |
| closed-form solution | 闭式解 | 可由显式表达式给出 |
| analytically tractable | 解析可解／可解析计算 | 按所讨论的是解还是积分求值区分 |
| intractable likelihood | 难以计算的似然 | 通常不能高效精确求值；不译“不可计算似然” |
| gradient ascent / gradient descent | 梯度上升／梯度下降 | 最大化／最小化目标 |
| expectation–maximisation (EM) | 期望最大化 | 交替进行潜变量推断和参数更新 |
| E-step / M-step | E步／M步 | 期望步／最大化步 |
| expected complete-data log-likelihood | 完整数据对数似然的期望 | EM 的辅助目标 |
| Jensen's inequality | Jensen 不等式 | 凸、凹函数与期望之间的不等式 |
| convex / concave function | 凸函数／凹函数 | 注意 Jensen 不等式方向 |
| evidence lower bound (ELBO) | 证据下界 | 边缘对数似然的下界；保留标准术语中的“证据” |
| variational inference | 变分推断 | 在可处理的分布族中近似后验 |
| aggregate posterior | 聚合后验 | 在数据分布上平均得到的潜变量后验 |
| variational autoencoder (VAE) | 变分自编码器 | 概率编码器与解码器的生成模型 |
| variational posterior / approximate posterior | 变分后验／近似后验 | 编码器给出的后验近似 |
| Kullback–Leibler divergence (KL divergence) | Kullback–Leibler 散度（KL散度） | 有方向性；保留公式中两个分布的次序 |
| entropy | 熵 | 分布的不确定性 |
| reconstruction term / regularisation term | 重构项／正则化项 | VAE 目标中的两部分 |
| reparameterisation trick | 重参数化技巧 | 将采样写成固定噪声与可微变换的复合 |
| Monte Carlo estimate | Monte Carlo 估计 | 用样本平均近似期望 |

## 第4章：离散时间扩散

来源：[cht5_new.tex](../01_source/chapters/cht5_new.tex)、[附录B](../01_source/chapters/cht_appendix2.tex)。

| 英文术语 | 本书译法 | 语境与区别 |
| --- | --- | --- |
| denoising diffusion probabilistic model (DDPM) | 去噪扩散概率模型 | 离散时间扩散生成模型 |
| forward process / reverse process | 前向过程／反向过程 | 逐步加噪／逐步生成；连续时间章节也称逆向过程 |
| forward noising | 前向加噪 | 给干净数据逐步加入高斯噪声 |
| noise schedule | 噪声调度 | 各时间步的噪声强度安排 |
| Markov chain / Markov assumption | 马尔可夫链／马尔可夫假设 | 给定当前状态后不再依赖更早状态 |
| transition distribution | 转移分布 | 相邻时间状态之间的条件分布 |
| reverse posterior | 逆后验 | 给定当前带噪状态与干净样本的前一步分布 |
| true reverse posterior | 真实逆后验 | 与学习得到的逆向转移分布区分 |
| global ELBO / local ELBO | 全局ELBO／局部ELBO | 整条潜变量链／单步条件目标 |
| noise prediction | 噪声预测 | 预测前向加噪中使用的噪声 |
| mean squared error | 均方误差 | DDPM 简化训练目标 |
| training / sampling | 训练／采样 | 参数学习／利用已学模型生成样本 |

## 第5—6章：连续时间、得分与扩散

来源：[cht_diff_fund.tex](../01_source/chapters/cht_diff_fund.tex)、[cht_score_diffusion.tex](../01_source/chapters/cht_score_diffusion.tex)。专名沿用正文的拉丁字母形式，便于与公式及文献对应。

| 英文术语 | 本书译法 | 语境与区别 |
| --- | --- | --- |
| deterministic / stochastic dynamics | 确定性／随机动力学 | 是否含随机驱动 |
| trajectory | 轨迹 | 单个粒子的位置随时间变化 |
| ordinary differential equation (ODE) | 常微分方程 | 确定性连续时间运动 |
| stochastic differential equation (SDE) | 随机微分方程 | 含布朗噪声的连续时间运动 |
| contraction | 收缩 | 状态向原点或彼此靠近 |
| matrix exponential | 矩阵指数 | 线性连续时间系统的解 |
| Brownian motion / Wiener process | 布朗运动／Wiener过程 | 连续时间随机运动 |
| drift / diffusion coefficient | 漂移／扩散系数 | 系统性位移／噪声强度 |
| Ornstein–Uhlenbeck process (OU process) | Ornstein–Uhlenbeck过程（OU过程） | 线性恢复漂移与布朗噪声共同作用 |
| mean reversion | 均值回归 | 漂移使状态回到均值附近 |
| probability density / probability mass | 概率密度／概率质量 | 连续分布的局部密度／区域内的概率 |
| density evolution | 密度演化 | 一组粒子的概率分布随时间变化 |
| change of variables | 变量替换 | 密度经可逆变换后的换元公式 |
| transport | 输运 | 速度场携带概率质量运动 |
| probability flux | 概率通量 | 单位时间流过边界的概率量 |
| continuity equation / Liouville equation | 连续性方程／Liouville方程 | 确定性输运下的概率守恒 |
| total derivative | 全导数 | 显式时间变化与沿轨迹空间变化之和 |
| divergence of a vector field | 向量场的散度 | 局部净流出量，不是两分布的差异 |
| Jacobian matrix / determinant | Jacobian矩阵／Jacobian行列式 | 即雅可比矩阵／行列式，刻画局部形变 |
| Laplacian | Laplace算子 | 各坐标二阶偏导数之和 |
| Fokker–Planck equation | Fokker–Planck方程 | 漂移与扩散共同引起的密度演化 |
| Gaussian smoothing | 高斯平滑 | 与高斯核卷积 |
| score function / score field | 得分函数／得分场 | 对数密度关于数据坐标的梯度 |
| probabilistic drift field | 概率漂移场 | 得分引导粒子向较高密度区域运动 |
| Langevin dynamics / Langevin sampling | Langevin动力学／Langevin采样 | 得分漂移与噪声共同构成的采样动力学 |
| target distribution | 目标分布 | 希望采样获得的分布 |
| stationary distribution / stationarity | 平稳分布／平稳性 | 密度一旦达到该状态就不随时间改变；不等同于已证明收敛 |
| Fisher divergence | Fisher散度 | 两分布得分函数之间的平方差期望 |
| score matching | 得分匹配 | 学习数据分布的得分 |
| denoising score matching (DSM) | 去噪得分匹配 | 以已知扰动条件分布的得分作为训练目标 |
| corruption / corrupted sample | 扰动／受扰样本 | 向数据加噪，不指数据损坏 |
| noisy distribution / noisy score | 带噪分布／带噪分布的得分 | 分布经噪声平滑后的密度及其得分 |
| conditional score / marginal score | 条件得分／边缘得分 | 给定干净样本的得分／对干净样本边缘化后的得分 |
| noise scale | 噪声尺度 | 高斯扰动的标准差等强度量 |
| multiscale score learning | 多尺度得分学习 | 在多个噪声尺度上学习得分 |
| annealed Langevin dynamics | 退火Langevin动力学 | 按噪声从大到小依次采样 |
| reverse-time dynamics | 逆时间动力学 | 逆着原时间方向演化，注意时间微分的符号约定 |

## 第7章：精确密度模型

来源：[cht_8_9_merged_new.tex](../01_source/chapters/cht_8_9_merged_new.tex)。

| 英文术语 | 本书译法 | 语境与区别 |
| --- | --- | --- |
| exact density model | 精确密度模型 | 结构允许直接求值归一化密度 |
| normalising flow | 归一化流 | 用可逆变换构造密度 |
| base distribution | 基础分布 | 流模型变换前的简单分布 |
| invertible transformation | 可逆变换 | 存在逆映射 |
| volume change | 体积变化 | 由Jacobian行列式绝对值给出 |
| planar flow | 平面流 | 沿给定方向进行标量非线性修正 |
| coupling layer / affine coupling | 耦合层／仿射耦合 | 一部分变量控制另一部分的可逆变换 |
| triangular Jacobian | 三角Jacobian矩阵 | 行列式为对角元素乘积 |
| likelihood evaluation | 似然计算／似然求值 | 在给定样本处计算模型似然 |
| autoregressive model / factorisation | 自回归模型／自回归分解 | 将联合分布写成有序条件分布乘积 |
| probability chain rule | 概率链式法则 | 不应与求导的链式法则混淆 |
| conditional parametrisation | 条件分布参数化 | 根据前面的变量给出后续条件分布参数 |
| masking | 掩码 | 限制网络只能使用允许的先前输入 |
| parallel training / sequential sampling | 并行训练／顺序采样 | 完整观测可并行求损失，生成需依次给出变量 |

## 第8章：对抗学习与能量模型

来源：[cht10_new.tex](../01_source/chapters/cht10_new.tex)。

| 英文术语 | 本书译法 | 语境与区别 |
| --- | --- | --- |
| generative adversarial network (GAN) | 生成对抗网络 | 通过判别器比较分布来训练生成器 |
| generator / discriminator | 生成器／判别器 | 生成样本／区分真实与生成样本 |
| implicit distribution | 隐式分布 | 能采样但通常不能直接计算密度 |
| adversarial game | 对抗博弈 | 生成器与判别器的优化关系 |
| value function | 价值函数 | 衡量生成器和判别器组合的目标 |
| optimal discriminator | 最优判别器 | 固定生成分布时的最优函数 |
| Jensen–Shannon divergence (JS divergence) | Jensen–Shannon散度（JS散度） | 通过混合分布对称比较两个分布 |
| non-saturating loss | 非饱和损失 | 改善生成器梯度的替代目标 |
| mode / mode collapse | 模式／模式坍缩 | 分布中的主要聚集区域／生成器只覆盖其中一部分 |
| support | 支撑集 | 分布能够赋予概率质量的区域 |
| Wasserstein distance / Wasserstein GAN (WGAN) | Wasserstein距离／Wasserstein GAN | 用运输几何比较分布 |
| coupling | 耦合 | 以指定分布为边缘分布的联合分布；不同于第7章的耦合层 |
| critic | 评论器 | WGAN的实值评分函数，不是输出概率的判别器 |
| Lipschitz constraint | Lipschitz约束 | 限制函数对输入变化的敏感度 |
| weight clipping / gradient penalty | 权重裁剪／梯度惩罚 | 约束评论器的两种方法 |
| energy-based model (EBM) | 基于能量的模型／能量模型 | 用标量能量定义样本相对偏好 |
| energy function / energy landscape | 能量函数／能量景观 | 数据空间上的标量函数及其几何形态 |
| partition function / normalising constant | 配分函数／归一化常数 | 使未归一化密度积分为1 |
| unnormalised density | 未归一化密度 | 尚未除以配分函数的正值函数 |
| contrastive gradient | 对比梯度 | 数据期望与模型期望之差构成的梯度 |
| positive phase / negative phase | 正相／负相 | 降低数据能量／提高模型样本能量 |

## 结语中的后续方法

来源：[cht_closing_remarks.tex](../01_source/chapters/cht_closing_remarks.tex)。

| 英文术语 | 本书译法 | 语境与区别 |
| --- | --- | --- |
| flow matching | 流匹配 | 结语提及的生成建模方法 |
| rectified flow | 整流流 | 学习连接分布的流的方法，沿用正文译名 |
| consistency model | 一致性模型 | 结语提及的生成建模方法，不译作统计“一致估计” |

## 全书结构用语

| 英文 | 统一译法 | 说明 |
| --- | --- | --- |
| Overview | 概述 | 章首内容说明 |
| Concept Map | 概念导图 | 章首逻辑提纲；统一原译的“概念地图／概念图”等变体 |
| Summary and References | 本章小结与参考文献 | 章末概括与文献说明 |
| Bayes' rule / Bayes' formula | 贝叶斯公式 | 条件概率换向公式 |

本表用于约束后续校订，不凭术语是否出现判断章节是否翻译完整。正文的条件、量词、公式、图表和论证仍需分别对照原文。
