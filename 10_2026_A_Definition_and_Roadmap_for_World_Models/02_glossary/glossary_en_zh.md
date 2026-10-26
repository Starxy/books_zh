# 《世界模型的定义与发展路线图》术语表

底本为用户提供的 arXiv:2607.06401v1 TeX 压缩包。节号指本文中文译本，与英文正文顺序一致。模型、算法与评测名称保留原名；下表按本篇论文的语境使用，不覆盖其他书籍的术语约定。

专业术语和文中命名的概念在正文首次出现时保留英文括注；带缩写者同时给出全称与缩写，后续沿用中文或缩写。按语境判断首次出现，不对普通词义机械套用专业词条。

| 英文 | 中文 | 语境与位置 |
|---|---|---|
| world model | 世界模型 | 第1、2节；本文按作者定义与物理世界模型互换 |
| physical world model | 物理世界模型 | 第2.1节；有限计算资源下的物理状态转移压缩建模 |
| physical AI | 物理人工智能 | 摘要、第6节 |
| Inverted Pyramid Workflow | 倒金字塔工作流 | 第1节；保留原文命名及英文括注 |
| Physical AGI | 物理通用人工智能；物理AGI | 第8节 |
| World Action Model (WAM) | 世界行动模型 | 第2.5、3.4、4.3节；跨架构功能范式 |
| World-Actor-Model | 世界—行动者模型 | 第4.2节原文对DreamZero的写法；保留与World Action Model的拼写差异 |
| renderer | 渲染器 | 第2.4节；观测生成角色 |
| simulator | 模拟器 | 第2.4节；状态转移角色 |
| planner | 规划器 | 第2.4节；行动选择角色 |
| representation | 表征 | 学习得到的编码或内部结构；一般不与“表现”混用 |
| representational substrate | 表征基础 | 第2.5节；观测层、潜在空间或结构化基础 |
| latent state / variable | 潜在状态／潜在变量 | 全文；不译为已直接观测的物理状态 |
| latent-space dynamics | 潜在空间动力学 | 第3.2节 |
| observation-level | 观测层 | 第3.1节；直接预测像素、体素、视频词元 |
| omnimodal / omnimodality | 全模态／全模态性 | 第2.1、3.4节；区别于一般多模态 |
| multimodal / multimodality | 多模态／多模态性 | 第7.1节等 |
| multidimensional asynchronicity | 多维异步性 | 第2.1节；各维采样频率不同 |
| locality | 局部性 | 第2.1节；感知范围受限 |
| Omnimodal workscope | 全模态的作用范围 | 第2.1节；原文三项主要性质中的第一项 |
| self-consistency | 自洽性 | 第2.1节；增加模态或数据通道时仍可继续运行和演化 |
| partially observable Markov decision process (POMDP) | 部分可观测马尔可夫决策过程 | 第2.1节首次出现时列全称与缩写 |
| object permanence | 物体恒存性 | 第1节；物体离开视野后仍持续存在 |
| affordance | 可供性 | 第3.2、3.3、7.2节；物体或部件所支持的行动可能 |
| physical grounding | 物理依据；与物理世界的关联 | 依句法区分；不一律译为抽象的“落地” |
| action grounding | 与行动的关联；以行动为依据 | 第3.4节；想象未来与可执行行动相连 |
| epistemic reasoning | 认识性推理 | 第2.1节；关于知识、信念及其形成与更新 |
| epistemic uncertainty | 认识不确定性 | 第4.2、4.3、6.6节；因模型知识不足产生的不确定性 |
| epistemic value | 认识价值 | 第2.4节；通过观测减少不确定性的价值 |
| instrumental value | 工具价值 | 第2.4节；实现外部目标的价值 |
| belief state / distribution | 信念状态／信念分布 | POMDP语境；不是未经条件化的物理状态 |
| Bayesian filtering | 贝叶斯滤波 | 第2.4节；序贯更新信念 |
| transition kernel | 转移核 | 第2.2节；条件状态转移分布 |
| action-conditioned | 以行动为条件的；行动条件 | 动力学、预测、交互或推演的条件变量 |
| token / tokenizer | 词元／分词器 | 第4.1节；含视频与行动等非文本词元 |
| next-token prediction | 下一词元预测 | 第4.1节 |
| masked autoencoding | 掩码自编码 | 第4.1节 |
| tube masking | 管状掩码 | 第4.1节；视频时空图块掩蔽 |
| nuisance factor / variance | 无关干扰因素／无关变化 | 第1、3、4节；与任务或决策无关的外观变化 |
| photometric | 光度的 | 像素观测中的光照、外观等变化 |
| model-based reinforcement learning (MBRL) | 基于模型的强化学习 | 第4.2节 |
| model-free | 无模型 | 第4.2节；强化学习方法 |
| model exploitation | 模型利用；模型误差利用 | 第4.2节；正常使用模型与规划器钻模型误差分别表达 |
| background planning | 后台规划 | 第4.2节；训练阶段使用想象经验 |
| decision-time planning | 决策时规划 | 第4.2节；部署决策时查询模型 |
| rollout | 推演 | 模型递归展开的状态、观测或信念序列 |
| imagination | 想象 | 第4节；模型内部的假想未来计算 |
| recurrent state-space model (RSSM) | 循环状态空间模型 | 第3.2、4.3节 |
| actor / critic | 演员／评论家 | 强化学习网络；第4节 |
| Actor / Evaluator | 行动者／评估器 | 第8节三位一体架构；物理执行与任务评价角色 |
| amortized policy | 将规划计算摊入参数的策略；摊销式策略 | 第4.2节；训练承担计算、部署反应式行动 |
| model predictive control (MPC) | 模型预测控制 | 第4.2节 |
| receding-horizon planning | 滚动时域规划 | 第5.1节；每次执行部分行动后重规划 |
| cross-entropy method (CEM) | 交叉熵方法 | 第4.2节；无导数轨迹优化采样器 |
| Monte Carlo tree search (MCTS) | 蒙特卡洛树搜索 | 第4.2节 |
| value equivalence | 价值等价 | 第4.2节；保持规划所需价值量 |
| compounding error | 误差累积 | 第4、6节；预测递归反馈造成偏离 |
| objective mismatch | 目标不匹配 | 第4.2节；预测似然与下游控制回报不同 |
| optimism–pessimism bias | 乐观—悲观偏差 | 第4.2节；规划对模型不确定性的态度 |
| replay buffer | 经验回放缓冲区 | 第4.2节 |
| off-policy | 离策略 | 策略优化、解释语境；不等同于“离线” |
| intrinsic reward | 内在奖励 | 第4.2节；好奇心或信息增益驱动探索 |
| embodiment | 机器人本体；身体形态 | 机器人身体、形态与控制接口；cross-embodiment译“跨本体”，形容词embodied译“具身” |
| body schema | 身体图式 | 第5.1节；内部身体能力表征 |
| proprioception | 本体感觉 | 第4、6、7节；身体内部状态感知 |
| object-centric | 以物体为中心的；物体中心 | 第3.3节 |
| object slot | 物体槽位 | 第3.3、7.2节 |
| occupancy / occupancy grid | 占据／占据栅格 | 第3.3、7.2节；空间是否被占用的表示 |
| bird's-eye view (BEV) | 鸟瞰图 | 第3.3节 |
| 3D Gaussian Splatting | 三维高斯泼溅 | 第2.5、3.3节 |
| radiance field | 辐射场 | 第3.3、7.2节 |
| novel-view synthesis | 新视角合成 | 第2.5、3.3节 |
| Chain-of-Imagination (CoI) | 想象链 | 第4.4节；行动—后果的时空推理过程 |
| chain-of-thought (CoT) | 思维链 | 第4.4节 |
| physics-informed learning | 物理信息驱动学习 | 第4.5节；物理结构作为学习约束或归纳偏置 |
| physics-informed neural network (PINN) | 物理信息神经网络 | 第4.5节 |
| soft / hard constraint | 软约束／硬约束 | 第4.5节；损失惩罚与架构内置分别处理 |
| counterfactual reasoning / inference | 反事实推理／反事实推断 | 第4.6节；reasoning与统计推断inference按语境区分 |
| structural causal model (SCM) | 结构因果模型 | 第4.6节 |
| exogenous / endogenous variable | 外生／内生变量 | 第4.6节 |
| abduction–action–prediction | 溯因—行动—预测 | 第4.6节；保留同一潜在背景再干预 |
| identifiability | 可识别性 | 第4.6节；观测与结构假设能否确定反事实量 |
| causal credit assignment | 因果信用分配 | 第4.6节 |
| hierarchical planning | 层级规划 | 第4.7节 |
| working / episodic memory | 工作记忆／情景记忆 | 第4.7节 |
| sim-to-real / sim2real gap | 仿真到现实／仿真到现实差距 | 第4.2、6.4节 |
| domain randomization | 域随机化 | 第6.4节 |
| system identification | 系统辨识 | 第6.4节 |
| out-of-distribution (OOD) | 分布外 | 第4、6节 |
| fidelity / precision | 保真度／精度 | 第6.2节；感知质量与物理可执行程度区分 |
| foundation-scale interactive simulator | 基础模型规模的交互模拟器 | 第7.3节；不是传统固定物理引擎的同义词 |
| Unified Physical Representation | 统一物理表征 | 第7.2节；发展路线中的第二阶段 |
| Trinity Architecture | 三位一体架构 | 第8节；世界模型、智能体与评估器组成的认知循环 |
| curriculum learning | 课程学习 | 第7、8节；逐步增加模态或任务难度 |
| federated world model | 联邦世界模型 | 第6.6节 |
| non-IID | 非独立同分布 | 第6.6节；原文英文展开错误另有译注 |
| automation bias | 自动化偏差 | 第6.6节；人过度依赖模型输出 |
| embodied carbon / operational carbon | 隐含碳排放／运行碳排放 | 第6.6节；制造等生命周期排放与使用阶段排放区分 |
