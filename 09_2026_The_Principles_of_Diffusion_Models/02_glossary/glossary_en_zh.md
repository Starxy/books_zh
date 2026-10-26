# 扩散模型原理：中英术语表

英文底本：*The Principles of Diffusion Models*，arXiv:2510.21890v3，英文 PDF 封面日期 2026-08-27。中文依据用户提供的 450 页既有译本；对应中文 TeX 已缺失。此表仅作初始化与术语准备，未开展逐节翻译复核、公式校订或全书版面复核，也未修改现有中文 PDF。

表内“现译”表示在相应章节范围的中文 PDF 文字层中定位到的用词，不代表已经确认全文统一。建议译名及需要继续确认的变体写在说明中，待后续恢复源码或复核时结合原句处理。同一词有不同义项时分别处理，不进行无语境替换。

E、C 分别指英文、中文 PDF 的 **1 基物理页序**，不是印刷页码。给出的是本次取词位置，不承诺是全书首次出现位置；并列变体各自标明页序。英文原始 TeX 文件链接用于定位底本，不能当作已恢复的中文源码。

本书优先区分：score function 为对数密度梯度的“得分函数”，guidance 中的 reward/score 还须按奖励或评分语境判断；flow 是概率输运中的“流”；flow map 为连接两个时刻状态的“流映射”；probability path 是分布族，与一条样本轨迹不同；统计后验近似的 inference 建议采用“推断”，生成运行语境再采用“推理”。


## 第1—2章：生成建模与变分视角

英文源码：[Prologue-Deep-Generative-Modeling.tex](../00_originals/tex_v3_en/Prologue-Deep-Generative-Modeling.tex)、[Chapter-1-Varational-Perspective-From-VAE-to-DDPM.tex](../00_originals/tex_v3_en/Chapter-1-Varational-Perspective-From-VAE-to-DDPM.tex)。

| 英文术语 | 中文译法与状态 | 语境与维护说明 | 取词位置 |
| --- | --- | --- | --- |
| deep generative model | 深度生成模型 | 缩写 DGM；建模对象为数据分布。 | E 21；C 19（深度生成模型） |
| data distribution | 数据分布 | 保留 p_data 一类数学下标。 | E 21；C 19（数据分布） |
| prior distribution | 先验分布 | 区分先验与后验。 | E 29；C 26（先验分布） |
| likelihood | 似然 | 不是“概率”一词的全局替代。 | E 23；C 21（似然） |
| maximum likelihood estimation | 最大似然估计 | 缩写 MLE。 | E 23；C 21（最大似然估计） |
| explicit model | 显式模型 | 与隐式模型的密度表示方式区分。 | E 32；C 28（显式模型） |
| implicit model | 隐式模型 | 不因“隐式”就改写为潜变量模型。 | E 32；C 28（隐式模型） |
| autoregressive | 自回归 | 联合分布的有序条件分解。 | E 21；C 19（自回归） |
| energy-based model | 基于能量的模型 | 缩写 EBM。 | E 21；C 19（基于能量的模型） |
| partition function | 配分函数 | 归一化常数在能量模型中的名称；后续统一前先核实语境。 | E 27；C 24（配分函数） |
| normalizing constant | 归一化常数 | 与数值标准化操作区分。 | E 27；C 22（归一化常数） |
| normalizing flow | 归一化流 | 缩写 NF；与流匹配不是同一个模型名称。 | E 21；C 19（归一化流） |
| generative adversarial | 生成对抗 | 保留 GAN 模型缩写。 | E 26；C 23（生成对抗） |
| autoencoder | 自编码器 | 与概率化的 VAE 区分。 | E 29；C 19（自编码器） |
| encoder | 编码器 | 编码方向由模型定义决定。 | E 29；C 19（编码器） |
| decoder | 解码器 | VAE 中也承担条件生成器的角色。 | E 29；C 26（解码器） |
| variational autoencoder | 变分自编码器 | 缩写 VAE。 | E 29；C 19（变分自编码器） |
| latent variable | 潜变量 | 与观测变量区分。 | E 29；C 26（潜变量） |
| observed variable | 观测变量 | 原文 observed，不改为隐藏变量。 | E 44；C 39（观测变量） |
| posterior | 后验 | 依据语境补“分布”或“概率”。 | E 45；C 40（后验） |
| inference joint | 推断联合分布 | VAE 中由真实数据与编码器组成的联合分布，与生成联合分布区分。 | E 47；C 41（推断联合分布） |
| Evidence Lower Bound | 证据下界 | 缩写 ELBO。 | E 29；C 26（证据下界） |
| reconstruction | 重构 | 与生成新样本区分。 | E 29；C 39（重构） |
| reparameterization | 重参数化 | 不改动相应变量变换公式。 | E 60；C 53（重参数化） |
| hierarchical VAE / hierarchical variational autoencoder | 层次变分自编码器 | 保留 HVAE 缩写。 | E 42；C 38（层次变分自编码器） |
| Denoising Diffusion Probabilistic Model | 去噪扩散概率模型 | 缩写 DDPM。 | E 33；C 29（去噪扩散概率模型） |
| forward process | 前向过程 | 本书中通常指数据到噪声的过程。 | E 54；C 48（前向过程） |
| reverse process | 反向过程；逆过程 | 区分过程方向与时间变量的积分方向。 | E 42；C 38（反向过程），C 47（逆过程） |
| noise prediction | 噪声预测 | 预测噪声变量，不等于预测带噪样本。 | E 42；C 38（噪声预测） |
| mean prediction | 均值预测 | 与噪声预测、数据预测参数化分别记录。 | E 60；C 38（均值预测） |

## 第3章：得分、去噪得分匹配与 NCSN

英文源码：[Chapter-2-Score-Based-Perspective-From-EBMs-to-NCSN.tex](../00_originals/tex_v3_en/Chapter-2-Score-Based-Perspective-From-EBMs-to-NCSN.tex)。

| 英文术语 | 中文译法与状态 | 语境与维护说明 | 取词位置 |
| --- | --- | --- | --- |
| score function | 得分函数 | 指对数密度对数据变量的梯度。 | E 68；C 60（得分函数） |
| score matching | 得分匹配 | 缩写 SM；与分类器评分区分。 | E 68；C 60（得分匹配） |
| denoising score matching | 去噪得分匹配 | 缩写 DSM。 | E 68；C 60（去噪得分匹配） |
| Fisher divergence | Fisher 散度 | 分布间得分差异所定义的目标。 | E 88；C 78（Fisher 散度） |
| Langevin dynamics | Langevin 动力学 | 采样动力学名称。 | E 68；C 60（Langevin 动力学） |
| annealed Langevin dynamics | 退火 Langevin 动力学 | 逐级降低噪声水平的采样过程。 | E 94；C 82（退火 Langevin 动力学） |
| Noise Conditional Score Network | 噪声条件得分网络 | 缩写 NCSN。 | E 68；C 60（噪声条件得分网络） |
| perturbation kernel | 扰动核 | 条件加噪分布；不是神经网络卷积核。 | E 92；C 81（扰动核） |
| isotropic | 各向同性 | 噪声协方差的性质。 | E 80；C 70（各向同性） |
| noise level | 噪声水平 | 与采样步长区分。 | E 68；C 60（噪声水平） |
| Tweedie | Tweedie | 本书中的后验均值公式名称保留人名。 | E 68；C 60（Tweedie） |
| base measure | 基测度 | 指数族表示中的测度。 | E 85；C 75（基测度） |
| log-partition | 对数配分函数 | 不是配分函数本身。 | E 85；C 75（对数配分函数） |
| conditional cumulant | 条件累积量 | 高阶条件统计量。 | E 86；C 75（条件累积量） |
| mixing | 混合 | 此处指采样链探索分布的能力，不是混合分布模型。 | E 75；C 66（混合） |

## 第4章：连续时间得分框架

英文源码：[Chapter-3-Diffusion-Models-Today-Score-SDE-Framework.tex](../00_originals/tex_v3_en/Chapter-3-Diffusion-Models-Today-Score-SDE-Framework.tex)。

| 英文术语 | 中文译法与状态 | 语境与维护说明 | 取词位置 |
| --- | --- | --- | --- |
| stochastic differential equation | 随机微分方程 | 缩写 SDE。 | E 99；C 87（随机微分方程） |
| ordinary differential equation | 常微分方程 | 缩写 ODE。 | E 100；C 88（常微分方程） |
| Wiener process | Wiener 过程 | 本书的布朗噪声过程。 | E 101；C 90（Wiener 过程） |
| drift | 漂移 | SDE 的确定性局部运动项。 | E 102；C 89（漂移） |
| diffusion coefficient | 扩散系数 | 与模型整体名称中的“扩散”区分。 | E 102；C 89（扩散系数） |
| reverse-time SDE | 逆时间 SDE | 保留时间方向及漂移符号。 | E 99；C 86（逆时间 SDE） |
| probability flow ODE | 概率流 ODE | 缩写 PF-ODE；与一般流映射区分。 | E 99；C 86（概率流 ODE） |
| marginal distribution | 边缘分布 | 与整条路径的联合分布区分。 | E 99；C 86（边缘分布） |
| time-dependent score | 依赖于时间的得分函数；依赖时间的得分函数 | 时间是条件输入。 | E 98；C 86（依赖于时间的得分函数），C 87（依赖时间的得分函数） |
| Fokker-Planck equation | Fokker–Planck 方程 | 描述概率密度演化。 | E 99；C 87（Fokker–Planck 方程） |
| simulation-free | 免模拟 | 本书主要用于可直接采样扰动边缘的训练方式，不等于生成采样无需积分。 | E 104；C 92（免模拟） |
| Variance Explosion / variance-exploding | 方差爆炸 | 缩写 VE，原文介绍 VE 时用 Explosion。 | E 123；C 109（方差爆炸） |
| variance preserving / variance-preserving | 方差保持 | 缩写 VP。 | E 123；C 109（方差保持） |
| accumulated perturbation kernel | 累积扰动核 | 区分局部转移与累积加噪分布。 | E 127；C 113（累积扰动核） |
| linear Gaussian | 线性高斯 | 前向过程的仿射均值与高斯噪声结构。 | E 106；C 93（线性高斯） |
| pushforward | 前推 | 由映射诱导的分布变换；本书存在词序变体。 | E 113；C 99（前推） |

## 第5—6章：流匹配与统一参数化

英文源码：[Chapter-4-Flow-Based-Perspective-From-NFs-to-Flow-Matching.tex](../00_originals/tex_v3_en/Chapter-4-Flow-Based-Perspective-From-NFs-to-Flow-Matching.tex)、[Chapter-5-They-Are-All-Equivalent.tex](../00_originals/tex_v3_en/Chapter-5-They-Are-All-Equivalent.tex)。

| 英文术语 | 中文译法与状态 | 语境与维护说明 | 取词位置 |
| --- | --- | --- | --- |
| flow-based | 基于流；流式 | 现译存在两种表述；此处 flow 指概率输运，不是数据流处理。 | E 138；C 160（基于流），C 123（流式） |
| flow matching | 流匹配 | 缩写 FM。 | E 138；C 123（流匹配） |
| conditional flow matching | 条件流匹配 | 缩写 CFM。 | E 155；C 138（条件流匹配） |
| Gaussian flow matching | 高斯流匹配 | 采用高斯条件概率路径的情形。 | E 149；C 133（高斯流匹配） |
| continuous normalizing flow / continuous-time normalizing flow | 连续归一化流；连续时间归一化流 | 连续时间可逆变换模型。 | E 144；C 128（连续归一化流），C 128（连续时间归一化流） |
| neural ODE | 神经 ODE；神经常微分方程 | 由神经网络参数化向量场。 | E 138；C 123（神经 ODE），C 126（神经常微分方程） |
| change-of-variables / change-of-variable | 变量变换 | 分清一次可逆变换公式与瞬时公式。 | E 138；C 123（变量变换） |
| instantaneous | 瞬时 | 用于连续时间密度变化率公式。 | E 146；C 129（瞬时） |
| continuity equation | 连续性方程 | 确定性流下的密度守恒关系。 | E 140；C 124（连续性方程） |
| velocity field | 速度场 | 向量场随位置和时间变化。 | E 138；C 123（速度场） |
| flow map | 流映射 | 连接两个时刻状态的映射，不等同于瞬时速度。 | E 140；C 125（流映射） |
| probability path | 概率路径 | 随时间变化的分布族，不是单个样本轨迹。 | E 139；C 123（概率路径） |
| conditional velocity | 条件速度 | 依赖指定条件的速度场。 | E 139；C 123（条件速度） |
| marginal velocity | 边缘速度 | 对条件信息取相应条件期望得到的速度。 | E 139；C 124（边缘速度） |
| coupling | 耦合 | 具有指定边缘分布的联合分布。 | E 140；C 125（耦合） |
| conditional expectation | 条件期望 | 区分被条件化变量与求平均变量。 | E 167；C 148（条件期望） |
| Eulerian | Euler | 现译可保留人名；固定空间位置的描述，后续可统一为“欧拉视角”。 | E 154；C 137（Euler） |
| Lagrangian | Lagrange | 现译可保留人名；沿轨迹的描述，后续可统一为“拉格朗日视角”。 | E 162；C 144（Lagrange） |
| canonical affine flow | 典范仿射流 | 保留本书对 canonical 的具体定义。 | E 175；C 154（典范仿射流） |
| rectified flow | 整流 | 现译可简写为“整流（RF）”，后续确认是否统一为“整流流”。 | E 149；C 133（整流） |
| interpolation | 插值 | 此处连接端点的条件路径，不必是边缘 ODE 的直线轨迹。 | E 153；C 133（插值） |
| parameterization | 参数化 | 区分网络预测量与训练损失比较量。 | E 155；C 127（参数化） |
| clean prediction / data prediction | 干净数据预测 | 预测去噪后的数据，与噪声预测区分。 | E 189；C 160（干净数据预测） |
| velocity prediction | 速度预测 | 不自动等同于任何标为 v 的参数化，仍须看本书定义。 | E 155；C 138（速度预测） |
| log signal-to-noise ratio | 对数信噪比 | 缩写 log-SNR；保留定义中是否含平方及系数。 | E 194；C 170（对数信噪比） |
| importance sampling | 重要性采样 | 与时间权重和采样分布分别记录。 | E 193；C 169（重要性采样） |
| oracle | 预言机 | 表示可访问精确目标的理论情形，不改写为已训练网络。 | E 176；C 155（预言机） |

## 第7章：最优输运与 Schrödinger 桥

英文源码：[Chapter-4-plus-OT-and-Diffusion-Model.tex](../00_originals/tex_v3_en/Chapter-4-plus-OT-and-Diffusion-Model.tex)。

| 英文术语 | 中文译法与状态 | 语境与维护说明 | 取词位置 |
| --- | --- | --- | --- |
| optimal transport | 最优输运 | 缩写 OT。 | E 214；C 188（最优输运） |
| entropic optimal transport / entropic OT | 熵正则化最优输运 | 缩写 EOT。 | E 214；C 188（熵正则化最优输运） |
| Monge | Monge | 用于映射形式的最优输运问题。 | E 217；C 189（Monge） |
| Kantorovich | Kantorovich | 用于耦合形式的最优输运问题。 | E 217；C 189（Kantorovich） |
| transport cost | 输运代价 | 目标函数中的搬运代价。 | E 217；C 190（输运代价） |
| Monge map | Monge 映射 | 确定性输运映射。 | E 220；C 192（Monge 映射） |
| Schrödinger bridge | 薛定谔桥 | 缩写 SB。 | E 214；C 188（薛定谔桥） |
| path law | 路径律；路径分布 | 整条随机轨迹的概率律。 | E 224；C 196（路径律），C 196（路径分布） |
| reference process | 参考过程 | SB 中作为比较对象的随机过程。 | E 224；C 188（参考过程） |
| stochastic control | 随机控制 | 本章 SB 的控制表述。 | E 224；C 196（随机控制） |
| half-bridge | 半桥 | 仅约束一个端点的桥问题。 | E 217；C 190（半桥） |
| Sinkhorn | Sinkhorn | 算法与形式中的人名保留。 | E 223；C 195（Sinkhorn） |
| Brenier | Brenier | 最优映射存在性定理的人名。 | E 217；C 189（Brenier） |

## 第8章：引导与可控生成

英文源码：[Chapter-6-Guidance.tex](../00_originals/tex_v3_en/Chapter-6-Guidance.tex)。

| 英文术语 | 中文译法与状态 | 语境与维护说明 | 取词位置 |
| --- | --- | --- | --- |
| guidance | 引导 | 对生成动力学增加条件或偏好信息。 | E 251；C 220（引导） |
| conditional generation | 条件生成 | 以条件信息控制生成结果。 | E 251；C 220（条件生成） |
| unconditional | 无条件 | 与有条件模型输出区分。 | E 251；C 220（无条件） |
| classifier guidance | 分类器引导 | 缩写 CG。 | E 251；C 220（分类器引导） |
| classifier-free guidance | 无分类器引导 | 缩写 CFG。 | E 251；C 220（无分类器引导） |
| training-free guidance | 免训练引导 | 采用现有辅助模型或目标进行引导的语境。 | E 251；C 220（免训练引导） |
| guidance potential | 引导势 | 引导项的标量势函数。 | E 255；C 222（引导势） |
| Diffusion Posterior Sampling | 扩散后验采样 | 缩写 DPS。 | E 268；C 233（扩散后验采样） |
| reinforcement learning | 强化学习 | 缩写 RL。 | E 256；C 224（强化学习） |
| alignment | 对齐 | 本章指模型输出与偏好或奖励的关系，不是排版术语。 | E 251；C 220（对齐） |
| Direct Preference Optimization | 直接偏好优化 | 缩写 DPO。 | E 256；C 223（直接偏好优化） |
| supervised fine-tuning | 监督微调 | 缩写 SFT。 | E 272；C 236（监督微调） |
| reward model | 奖励模型 | 与采样器和生成模型分别记录。 | E 251；C 220（奖励模型） |
| policy | 策略 | 强化学习中的 policy。 | E 256；C 223（策略） |
| implicit reward | 隐式奖励 | 由策略或路径概率关系诱导的奖励。 | E 272；C 236（隐式奖励） |
| path posterior | 路径后验 | 整条路径上的条件分布。 | E 278；C 241（路径后验） |

## 第9章：数值求解与快速采样

英文源码：[Chapter-7-Sophisticated-Solvers-for-Fast-Sampling.tex](../00_originals/tex_v3_en/Chapter-7-Sophisticated-Solvers-for-Fast-Sampling.tex)。

| 英文术语 | 中文译法与状态 | 语境与维护说明 | 取词位置 |
| --- | --- | --- | --- |
| numerical solver | 数值求解器 | 采样中的数值积分方法。 | E 283；C 245（数值求解器） |
| number of function evaluations | 函数求值次数 | 缩写 NFE，与步数不是总相等。 | E 287；C 248（函数求值次数） |
| single-step method | 单步方法 | 使用当前一步内部的信息构造更新。 | E 287；C 247（单步方法） |
| multistep method | 多步方法 | 使用历史步骤的信息。 | E 287；C 247（多步方法） |
| stage | 阶段 | 数值方法内部的 stage，区别于时间步；后续可按数值分析术语用“级”。 | E 293；C 252（阶段） |
| step size | 步长 | 时间离散间隔。 | E 315；C 251（步长） |
| local truncation error | 局部截断误差 | 与全局误差区分。 | E 317；C 270（局部截断误差） |
| globally first order | 全局一阶 | 数值方法的全局精度阶数。 | E 303；C 259（全局一阶） |
| exponential integrator | 指数积分器 | 处理半线性动力学的积分方法。 | E 284；C 245（指数积分器） |
| Denoising Diffusion Implicit Model | 去噪扩散隐式模型 | 缩写 DDIM。 | E 295；C 253（去噪扩散隐式模型） |
| DEIS | DEIS | 模型方法名保留，英文展开以原章为准。 | E 283；C 245（DEIS） |
| DPM-Solver++ | DPM-Solver++ | 保留连字符和加号。 | E 283；C 245（DPM-Solver++） |
| DPM-Solver | DPM-Solver | 与 DPM-Solver++、其阶数分别记录。 | E 283；C 245（DPM-Solver） |
| Lagrange interpolant | Lagrange 插值 | 用于历史预测值的多项式插值。 | E 313；C 267（Lagrange 插值） |
| extrapolant | 外推 | 区别于区间内插值。 | E 312；C 267（外推） |
| predictor | 预测器 | 预测—校正数值方法中的角色。 | E 288；C 248（预测器） |
| corrector | 校正器 | 与模型参数训练的“修正”区分。 | E 340；C 291（校正器） |
| Runge-Kutta | Runge–Kutta | 保留 RK2 等阶数缩写。 | E 284；C 245（Runge–Kutta） |
| fixed point | 不动点 | 迭代求解的数学语境。 | E 287；C 247（不动点） |
| parallel-in-time / time-parallel | 时间并行 | 沿时间轴并行推进计算。 | E 342；C 252（时间并行） |
| ParaDiGMS | ParaDiGMS | 方法名保留；英文书签中也出现 ParaDiGMs 写法，后续统一大小写。 | E 293；C 252（ParaDiGMS） |

## 第10—11章：蒸馏与流映射模型

英文源码：[Chapter-8-Post-Training-Methods-for-Fast-Sampling.tex](../00_originals/tex_v3_en/Chapter-8-Post-Training-Methods-for-Fast-Sampling.tex)、[Chapter-9-Learning-Fast-Generator-from-Scratch.tex](../00_originals/tex_v3_en/Chapter-9-Learning-Fast-Generator-from-Scratch.tex)。

| 英文术语 | 中文译法与状态 | 语境与维护说明 | 取词位置 |
| --- | --- | --- | --- |
| distillation | 蒸馏 | 本书主要指减少采样步骤，不默认表示缩小网络。 | E 350；C 299（蒸馏） |
| teacher | 教师 | 通常为预训练扩散模型及其采样器。 | E 350；C 299（教师） |
| student | 学生 | 学习快速生成的模型。 | E 350；C 299（学生） |
| distribution level distillation / distribution-based distillation | 基于分布的蒸馏 | 学生学习教师输出分布的蒸馏路线。 | E 350；C 299（基于分布的蒸馏） |
| flow map level distillation / flow-map distillation | 流映射蒸馏 | 以时刻间映射为学习目标。 | E 350；C 299（流映射蒸馏） |
| progressive distillation | 渐进式蒸馏 | 缩写 PD。 | E 350；C 299（渐进式蒸馏） |
| semigroup property | 半群性质 | 跨多个时段的流映射复合关系。 | E 362；C 310（半群性质） |
| consistency model | 一致性模型 | 缩写 CM；不译为统计“一致估计”。 | E 365；C 312（一致性模型） |
| consistency function | 一致性函数 | 指向共享端点的映射。 | E 370；C 316（一致性函数） |
| stop-gradient | 停止梯度 | 保留计算图中阻断梯度的操作意义。 | E 370；C 305（停止梯度） |
| self consistency / self-consistency | 自一致性 | 与局部一致性、全局一致性区分。 | E 374；C 320（自一致性） |
| local consistency | 局部一致性 | 近邻时刻之间的约束。 | E 354；C 302（局部一致性） |
| global consistency | 全局一致性 | 一般时刻之间的约束。 | E 374；C 320（全局一致性） |
| consistency trajectory model | 一致性轨迹模型 | 缩写 CTM。 | E 367；C 314（一致性轨迹模型） |
| mean flow | 平均流 | 保留 Mean Flow 方法名称及其平均速度定义。 | E 367；C 314（平均流） |
| average drift | 平均漂移 | 时间区间上的平均量，与瞬时速度区分。 | E 371；C 317（平均漂移） |
| Jacobian-vector product | 雅可比矩阵–向量积 | 缩写 JVP。 | E 399；C 342（雅可比矩阵–向量积） |
| tangent normalization | 切向归一化 | 连续时间一致性模型训练中的处理。 | E 385；C 329（切向归一化） |
| tangent warm-up | 切向预热 | 与时间嵌入分别记录。 | E 385；C 329（切向预热） |
| time embedding | 时间嵌入 | 网络输入的时间表示。 | E 385；C 329（时间嵌入） |

## 第12章：离散状态下的概率演化

英文源码：[Chapter-10-Epilogue-and-Outlook.tex](../00_originals/tex_v3_en/Chapter-10-Epilogue-and-Outlook.tex)。

| 英文术语 | 中文译法与状态 | 语境与维护说明 | 取词位置 |
| --- | --- | --- | --- |
| discrete-time Markov chain | 离散时间马尔可夫链 | 离散时间转移矩阵。 | E 419；C 358（离散时间马尔可夫链） |
| continuous-time Markov chain | 连续时间马尔可夫链 | 缩写 CTMC。 | E 409；C 351（连续时间马尔可夫链） |
| transition matrix | 转移矩阵 | 区分转移概率与转移速率。 | E 417；C 357（转移矩阵） |
| rate matrix | 率矩阵 | 连续时间链的局部转移速率。 | E 421；C 360（率矩阵） |
| master equation | 主方程 | 离散状态概率质量的演化方程。 | E 409；C 351（主方程） |
| Kolmogorov forward equation | 柯尔莫哥洛夫前向方程 | 本章中的主方程名称。 | E 416；C 355（柯尔莫哥洛夫前向方程） |
| concrete score | 具体得分；离散得分 | 本书用于离散局部概率比的名称，需与连续梯度得分区分。 | E 429；C 366（具体得分），C 366（离散得分） |
| one-hot | 独热；one-hot | 离散状态的向量编码。 | E 415；C 355（独热），C 357（one-hot） |
| pure-jump | 纯跳跃 | 离散状态随机路径。 | E 431；C 368（纯跳跃） |

## 附录 A—D 与符号说明

英文源码：[A_Crash-Course-of-DE.tex](../00_originals/tex_v3_en/A_Crash-Course-of-DE.tex)、[B_Continuity-Equation.tex](../00_originals/tex_v3_en/B_Continuity-Equation.tex)、[C_SDE-and-Ito.tex](../00_originals/tex_v3_en/C_SDE-and-Ito.tex)、[D_Proofs.tex](../00_originals/tex_v3_en/D_Proofs.tex)、[notations.tex](../00_originals/tex_v3_en/notations.tex)。

| 英文术语 | 中文译法与状态 | 语境与维护说明 | 取词位置 |
| --- | --- | --- | --- |
| partial differential equation | 偏微分方程 | 缩写 PDE。 | E 436；C 372（偏微分方程） |
| existence and uniqueness | 存在唯一性；存在性与唯一性 | 解的条件，不按另一本书的定理计数器重编号。 | E 436；C 374（存在唯一性），C 372（存在性与唯一性） |
| Euler-Maruyama | Euler–Maruyama | SDE 的离散方法。 | E 437；C 372（Euler–Maruyama） |
| Itô | Itô | 随机积分与公式的人名。 | E 436；C 372（Itô） |
| quadratic variation | 二次变差 | 随机微积分中的量。 | E 474；C 403（二次变差） |
| Girsanov | Girsanov | 路径测度变换定理的人名。 | E 472；C 401（Girsanov） |
| Radon-Nikodym | Radon–Nikodym | 测度之间的导数。 | E 482；C 411（Radon–Nikodym） |
| Wasserstein gradient flow | Wasserstein 梯度流 | 分布空间中的梯度演化，与样本的速度场区分。 | E 454；C 385（Wasserstein 梯度流） |
| pushforward | 推前 | 映射作用于概率分布。 | E 458；C 389（推前） |
| Lipschitz | Lipschitz | 正则条件名称。 | E 439；C 374（Lipschitz） |

## 后续统一时需注意的用词

- “基于流／流式”“反向／逆时间”等现有变体先按具体句子记录，暂不批量替换。
- 人名、模型名及缩写保持可检索；例如 DDPM、NCSN、PF-ODE、DDIM、DPM-Solver、CFG、CM、CTM。名称中的连字符、加号和阶数不能省略。
- “推断／推理”“得分／评分”“概率路径／样本路径”“条件／边缘”“漂移／扩散”“参数化／训练目标”分别按语义处理。
- 需要继续确认的译名留在本表；术语表的整理不能替代后续对译文条件、公式、图表和内容覆盖的检查。
