> 状态更新（2026-10-24）：本术语表随已完成的全书中文译稿保留。成品：`00_books/Foundations_of_Large_Language_Models_cn_translated.pdf`（285页）。历史批次说明仅用于追溯。

# 《大语言模型基础》术语表（arXiv v4）

依据用户提供的 TeX 源码建立。各章首次出现写作“中文（English，缩写）”，随后使用统一中文；模型名、代码、引用键、数学变量和语言学示例保留字面形式。

| English | 中文 | 缩写或说明 |
|---|---|---|
| large language model | 大语言模型 | LLM |
| foundation model | 基础模型 |  |
| pre-training | 预训练 |  |
| post-training | 后训练 |  |
| fine-tuning | 微调 |  |
| supervised fine-tuning | 监督微调 | SFT |
| instruction fine-tuning | 指令微调 |  |
| alignment | 对齐 |  |
| human preference | 人类偏好 |  |
| human feedback | 人类反馈 |  |
| reinforcement learning from human feedback | 基于人类反馈的强化学习 | RLHF |
| reinforcement learning from AI feedback | 基于人工智能反馈的强化学习 | RLAIF |
| natural language processing | 自然语言处理 | NLP |
| self-supervised learning | 自监督学习 |  |
| supervised learning | 监督学习 |  |
| unsupervised learning | 无监督学习 |  |
| transfer learning | 迁移学习 |  |
| representation learning | 表示学习 |  |
| contextualized representation | 上下文化表示 |  |
| sequence encoding | 序列编码 |  |
| sequence generation | 序列生成 |  |
| encoder | 编码器 |  |
| decoder | 解码器 |  |
| encoder-only architecture | 仅编码器架构 |  |
| decoder-only architecture | 仅解码器架构 |  |
| encoder-decoder architecture | 编码器—解码器架构 |  |
| language modeling | 语言建模 |  |
| autoregressive language model | 自回归语言模型 |  |
| masked language modeling | 掩码语言建模 | MLM |
| next sentence prediction | 下一句预测 | NSP |
| next-token prediction | 下一词元预测 |  |
| token | 词元 | 保留英文分词示例及特殊词元的字面形式 |
| tokenization | 词元化 |  |
| tokenizer | 词元化器 |  |
| vocabulary | 词表 |  |
| embedding | 嵌入 |  |
| positional encoding | 位置编码 |  |
| positional embedding | 位置嵌入 |  |
| rotary positional embedding | 旋转位置嵌入 | RoPE |
| relative position bias | 相对位置偏置 |  |
| absolute position | 绝对位置 |  |
| extrapolation | 外推 |  |
| interpolation | 插值 |  |
| self-attention | 自注意力 |  |
| cross-attention | 交叉注意力 |  |
| multi-head attention | 多头注意力 | MHA |
| multi-query attention | 多查询注意力 | MQA |
| grouped-query attention | 分组查询注意力 | GQA |
| query | 查询 |  |
| key | 键 |  |
| value | 值 |  |
| key-value cache | 键值缓存 | KV 缓存 |
| feed-forward network | 前馈网络 | FFN |
| residual connection | 残差连接 |  |
| layer normalization | 层归一化 |  |
| activation function | 激活函数 |  |
| attention mask | 注意力掩码 |  |
| causal mask | 因果掩码 |  |
| dropout | 随机失活 | dropout |
| cross-entropy | 交叉熵 |  |
| perplexity | 困惑度 |  |
| loss function | 损失函数 |  |
| objective function | 目标函数 |  |
| maximum likelihood estimation | 最大似然估计 | MLE |
| gradient descent | 梯度下降 |  |
| backpropagation | 反向传播 |  |
| learning rate | 学习率 |  |
| warmup | 预热 |  |
| batch size | 批量大小 |  |
| mini-batch | 小批量 |  |
| epoch | 训练轮次 |  |
| weight decay | 权重衰减 |  |
| data parallelism | 数据并行 |  |
| model parallelism | 模型并行 |  |
| tensor parallelism | 张量并行 |  |
| pipeline parallelism | 流水线并行 |  |
| sequence parallelism | 序列并行 |  |
| mixed precision | 混合精度 |  |
| gradient accumulation | 梯度累积 |  |
| gradient checkpointing | 梯度检查点 |  |
| activation recomputation | 激活重计算 |  |
| scaling law | 缩放定律 |  |
| compute-optimal | 计算最优 |  |
| training corpus | 训练语料 |  |
| data curation | 数据整理 |  |
| deduplication | 去重 |  |
| data contamination | 数据污染 |  |
| long context | 长上下文 |  |
| context window | 上下文窗口 |  |
| retrieval augmentation | 检索增强 |  |
| retrieval-augmented generation | 检索增强生成 | RAG |
| mixture of experts | 混合专家 | MoE |
| router | 路由器 |  |
| load balancing | 负载均衡 |  |
| prompt | 提示 |  |
| prompting | 提示方法 |  |
| prompt engineering | 提示工程 |  |
| in-context learning | 上下文学习 | ICL |
| demonstration | 示例 |  |
| zero-shot learning | 零样本学习 |  |
| few-shot learning | 少样本学习 |  |
| chain of thought | 思维链 | CoT |
| tree of thoughts | 思维树 | ToT |
| graph of thoughts | 思维图 | GoT |
| self-consistency | 自一致性 |  |
| self-reflection | 自我反思 |  |
| hard prompt | 硬提示 |  |
| soft prompt | 软提示 |  |
| prefix tuning | 前缀微调 |  |
| prompt tuning | 提示微调 |  |
| automatic prompt optimization | 自动提示优化 |  |
| context distillation | 上下文蒸馏 |  |
| parameter-efficient fine-tuning | 参数高效微调 | PEFT |
| low-rank adaptation | 低秩适配 | LoRA |
| adapter | 适配器 |  |
| reward model | 奖励模型 | RM |
| reward function | 奖励函数 |  |
| reward hacking | 奖励投机 |  |
| policy | 策略 |  |
| policy gradient | 策略梯度 |  |
| reference policy | 参考策略 |  |
| proximal policy optimization | 近端策略优化 | PPO |
| direct preference optimization | 直接偏好优化 | DPO |
| group relative policy optimization | 组相对策略优化 | GRPO |
| advantage | 优势 |  |
| value function | 价值函数 |  |
| return | 回报 |  |
| Kullback-Leibler divergence | KL 散度 | KL divergence |
| importance sampling | 重要性采样 |  |
| rejection sampling | 拒绝采样 |  |
| inference | 推理 | 结合语境写“模型推理”“推理阶段效率”等；易混处括注 inference |
| reasoning | 推理 | 结合语境写“推理能力”“推理模型”“推理词元”等；易混处括注 reasoning |
| inference-time scaling | 推理时扩展 |  |
| test-time compute | 测试时计算量 |  |
| decoding | 解码 |  |
| greedy search | 贪心搜索 |  |
| beam search | 束搜索 |  |
| sampling | 采样 |  |
| temperature | 温度 |  |
| top-k sampling | top-k 采样 |  |
| top-p sampling | top-p 采样 | nucleus sampling 亦称核采样 |
| speculative decoding | 推测解码 |  |
| draft model | 草稿模型 |  |
| target model | 目标模型 |  |
| prefill | 预填充 |  |
| throughput | 吞吐量 |  |
| latency | 时延 |  |
| continuous batching | 连续批处理 |  |
| quantization | 量化 |  |
| pruning | 剪枝 |  |
| knowledge distillation | 知识蒸馏 |  |
| best-of-N | N 次采样择优 | best-of-N |
| verifier | 验证器 |  |
| outcome reward model | 结果奖励模型 | ORM |
| process reward model | 过程奖励模型 | PRM |
| process supervision | 过程监督 |  |
| outcome supervision | 结果监督 |  |
| Monte Carlo tree search | 蒙特卡洛树搜索 | MCTS |
| search tree | 搜索树 |  |
| rollout | 轨迹采样 | 依语境也可写为“展开” |
| reasoning trajectory | 推理轨迹 |  |
| long chain of thought | 长思维链 |  |
| hallucination | 幻觉 |  |
| catastrophic forgetting | 灾难性遗忘 |  |
| emergent ability | 涌现能力 |  |
| benchmark | 基准 |  |
| evaluation | 评测 |  |
| ablation study | 消融实验 |  |
| ground truth | 真实值 | 标注任务可写“标准答案” |
| completion | 补全文本 | 依语境可简称“补全” |
| logit | 未归一化分数 | 首现写 logit |
| log-likelihood | 对数似然 |  |
| entropy | 熵 |  |
| distribution shift | 分布偏移 |  |
| distribution | 分布 |  |
| hidden state | 隐状态 |  |
| downstream task | 下游任务 |  |

用户于2026-10-23指定：inference 与 reasoning 统一译“推理”，通常靠语境区分；特殊歧义处使用“xx推理（inference）”或“xx推理（reasoning）”。

进一步依据全书索引术语补充：

| English | 中文 | 缩写或说明 |
|---|---|---|
| $k$-nearest neighbors | $k$ 近邻 | $k$-NN |
| $k$-NN language modeling | $k$ 近邻语言建模 | $k$-NN LM |
| agent | 智能体 |  |
| automated machine learning | 自动化机器学习 | AutoML |
| neural architecture search | 神经架构搜索 | NAS |
| Bradley-Terry model | Bradley–Terry 模型 |  |
| Plackett-Luce model | Plackett–Luce 模型 |  |
| gated linear unit | 门控线性单元 | GLU |
| gaussian error linear unit | 高斯误差线性单元 | GeLU |
| rectified linear unit | 修正线性单元 | ReLU |
| attention with linear biases | 带线性偏置的注意力 | ALiBi |
| NTK-aware scaled RoPE | 感知神经正切核的缩放 RoPE | NTK-aware scaled RoPE |
| inference engine | 推理引擎 |  |
| scheduler | 调度器 |  |
| request-level scheduling | 请求级调度 |  |
| iteration-level scheduling | 迭代级调度 |  |
| parallel scaling | 并行扩展 |  |
| sequential scaling | 序列扩展 |  |
| speculative execution | 推测执行 |  |
| performance function | 性能函数 |  |
| surrogate objective | 替代目标 |  |
| ratio function | 比率函数 |  |
| trust region | 信赖域 |  |
| overoptimization problem | 过度优化问题 |  |
| cumulative reward | 累积奖励 |  |
| state-value function | 状态价值函数 |  |
| action-value function | 动作价值函数 | Q-value function |
| advantage actor-critic | 优势演员—评论家 | A2C |
| temporal difference | 时序差分 | TD |
| offline reinforcement learning | 离线强化学习 |  |
| on-policy distillation | 同策略蒸馏 | OPD |
| off-policy distillation | 异策略蒸馏 | 与“离线蒸馏”依上下文区分 |
| outcome-based approaches | 基于结果的方法 |  |
| process-based approaches | 基于过程的方法 |  |
| Monte Carlo rollout | 蒙特卡洛轨迹采样 |  |
| latent reasoning | 潜空间推理 |  |
| implicit reasoning | 隐式推理 |  |
| continuous thought | 连续思维 |  |
| chain of continuous thought | 连续思维链 | COCONUT |
| deliberate-then-generate | 先思考后生成 | DTG |
| calculation annotation | 计算标注 |  |
| reasoning trace | 推理轨迹 | CoT trace 译“思维链轨迹” |
| causal language modeling | 因果语言建模 |  |
| permuted language modeling | 排列语言建模 |  |
| prefix language modeling | 前缀语言建模 |  |
| translation language modeling | 翻译语言建模 |  |
| cross-lingual language model | 跨语言语言模型 | XLM |
| multilingual BERT | 多语言 BERT | mBERT |
| the curse of multilinguality | 多语言诅咒 |  |
| token masking | 词元掩码 |  |
| span masking | 片段掩码 |  |
| token deletion | 词元删除 |  |
| document rotation | 文档旋转 |  |
| sentence reordering | 句子重排 |  |
| relation extraction | 关系抽取 |  |
| text completion | 文本补全 |  |
| text transformation | 文本转换 |  |
| external memory | 外部记忆 |  |
| internal memory | 内部记忆 |  |
| irreducible error | 不可约误差 |  |
| chain-of-thought prompting | 思维链提示 | CoT prompting |
| zero-shot CoT | 零样本思维链 |  |
| few-shot CoT prompting | 少样本思维链提示 |  |
| one-shot CoT prompting | 单样本思维链提示 |  |
| automatic prompt design | 自动提示设计 |  |
| prompt embedding | 提示嵌入 |  |
| prompt search space | 提示搜索空间 |  |
| problem decomposition | 问题分解 |  |
| sub-problem generation | 子问题生成 |  |
| sub-problem solving | 子问题求解 |  |
| least-to-most prompting | 由简到繁提示 |  |
| input inversion | 输入反演 |  |
| label mapping | 标签映射 |  |
| compositional generalization | 组合泛化 |  |
| formal linguistic competence | 形式语言能力 |  |
| instruction alignment | 指令对齐 |  |
| human preference alignment | 人类偏好对齐 |  |
| superficial alignment hypothesis | 表层对齐假说 |  |
| self-instruct | 自指令 | Self-Instruct 方法名保留 |
| self-training | 自训练 |  |
| single-round prediction | 单轮预测 |  |
| weak-to-strong generalization | 弱到强泛化 |  |
| weak performance | 弱模型性能 |  |
| weak-to-strong performance | 弱到强性能 |  |
| strong ceiling performance | 强模型性能上限 |  |
| performance gap recovered | 性能差距弥合比例 | PGR |
| sample efficient | 样本高效 |  |
| best-of-N sampling | N 次采样择优 | BoN sampling |

首批译校及后三章补充：

| English | 中文 | 缩写或说明 |
|---|---|---|
| one-hot representation | 独热表示 |  |
| denoising autoencoder | 去噪自编码器 |  |
| sentinel token | 哨兵词元 |  |
| fertility modeling | 繁衍率建模 |  |
| discriminative training | 判别式训练 |  |
| segment embedding | 片段嵌入 |  |
| pre-norm | 前置归一化 |  |
| post-norm | 后置归一化 |  |
| hidden size | 隐层维度 |  |
| depth-adaptive model | 深度自适应模型 |  |
| length-adaptive model | 长度自适应模型 |  |
| cross-lingual transfer learning | 跨语言迁移学习 |  |
| code-switching | 语码转换 |  |
| capacity interference | 容量干扰 |  |
| experience replay | 经验回放 |  |
| elastic weight consolidation | 弹性权重巩固 |  |
| generative adversarial network | 生成对抗网络 | GAN |
| sequence labeling | 序列标注 |  |
| span prediction | 片段预测 |  |
| deduction | 演绎推理 |  |
| induction | 归纳推理 |  |
| abduction | 溯因推理 |  |
| premise | 前提 |  |
| logical form | 逻辑形式 |  |
| generative verifier | 生成式验证器 |  |
| formal verification | 形式化验证 |  |
| formal symbolic system | 形式符号系统 |  |
| grokking | 顿悟 | grokking 现象 |
| memorization | 记忆 | 指记住训练实例；与 reasoning 比较 |
| planning | 规划 |  |
| agentic planning | 智能体规划 |  |
| logical entailment | 逻辑蕴含 |  |
| reasoning token | 推理词元 |  |
| reasoning model | 推理模型 |  |
| reasoning capability | 推理能力 |  |
| self-refinement | 自我改进 |  |
| teacher forcing | 教师强制 |  |
| data leakage | 数据泄漏 |  |
| exposure bias | 暴露偏差 |  |
| order of growth | 增长阶 |  |
| time to first token | 首词元时延 | TTFT |
| time per output token | 每输出词元耗时 | TPOT |
| inter-token latency | 词元间时延 | ITL |
| chunked prefilling | 分块预填充 |  |
| prefix caching | 前缀缓存 |  |
| output ensembling | 输出集成 |  |
| thinking path | 思维路径 | reasoning path 可依语境写“推理路径” |
| critic | 评论家 |  |
| actor | 演员 | 与 critic 配对的强化学习术语 |
| policy optimization | 策略优化 |  |

第2、3章译校补录：

| English | 中文 | 缩写或说明 |
|---|---|---|
| internal covariate shift | 内部协变量偏移 |  |
| root mean square layer normalization | 均方根层归一化 |  |
| micro-batch | 微批次 |  |
| collective operation | 集合操作 |  |
| all-reduce | 全归约 |  |
| tile-based parallel algorithm | 分块并行算法 |  |
| attention sink | 注意力汇聚点 |  |
| datastore | 数据存储库 |  |
| vector store | 向量存储库 |  |
| forced decoding | 强制解码 |  |
| memory capacity | 记忆容量 |  |
| compressive Transformer | 压缩式 Transformer |  |
| continuous-space attention | 连续空间注意力 |  |
| needle-in-a-haystack | 大海捞针 |  |
| passkey retrieval | 口令检索 |  |
| copy memory task | 复制记忆任务 |  |
| double descent | 双下降 |  |
| prompt template | 提示模板 |  |
| system prompt | 系统提示 |  |
| one-shot learning | 单样本学习 |  |
| named entity recognition | 命名实体识别 |  |
| information extraction | 信息抽取 |  |
| model ensembling | 模型集成 |  |
| prompt ensembling | 提示集成 |  |
| hypothesis selection | 假设选择 |  |
| minimum Bayes risk search | 最小贝叶斯风险搜索 |  |
| prompt optimization | 提示优化 |  |
| performance estimation | 性能估计 |  |
| pseudo embedding | 伪嵌入 |  |
| summary token | 摘要词元 |  |
| multi-hop question answering | 多跳问答 |  |
| compositionality | 组合性 |  |
| meta-learning | 元学习 |  |

第4至6章译校补录：

| English | 中文 | 缩写或说明 |
|---|---|---|
| reward shaping | 奖励塑形 | 第4章 |
| pairwise comparison | 成对比较 | 第4章 |
| pairwise ranking | 成对排序 | 第4章 |
| listwise ranking | 列表式排序 | 第4章 |
| pointwise supervision | 逐点监督 | 第4章 |
| learning-to-rank | 排序学习 | 第4章 |
| underdetermination | 欠定性 | 第4章 |
| aspect-based sentiment analysis | 基于方面的情感分析 | 第4章 |
| hinge loss | 合页损失 | 第4章 |
| reward gaming | 奖励取巧 | 第4章 |
| oracle reward model | 理想奖励模型 | 第4章 |
| model cascading | 模型级联 | 第4章 |
| dynamics | 环境动态 | 第4章 |
| baseline | 基线 | 第4章 |
| trajectory | 轨迹 | 第4章 |
| discount factor | 折扣因子 | 第4章 |
| Markov decision process | 马尔可夫决策过程 | 第4章 |
| Q-value function | Q 价值函数 | 第4章 |
| dense reward | 稠密奖励 | 第4章 |
| sparse reward | 稀疏奖励 | 第4章 |
| curriculum learning | 课程学习 | 第4章 |
| intrinsic motivation | 内在动机 | 第4章 |
| hindsight experience replay | 事后经验回放 | 第4章 |
| instruction following | 指令遵循 | 第4章 |
| multi-round prediction | 多轮预测 | 第4章 |
| online reinforcement learning | 在线强化学习 | 第4章 |
| reranking | 重排序 | 第4章 |
| ensemble learning | 集成学习 | 第4章 |
| maximum a posteriori decoding | 最大后验解码 | 第5章 |
| minimum Bayes risk decoding | 最小贝叶斯风险解码 | 第5章 |
| request latency | 请求时延 | 第5章 |
| repetition penalty | 重复惩罚 | 第5章 |
| length penalty | 长度惩罚 | 第5章 |
| diversity penalty | 多样性惩罚 | 第5章 |
| constraint-based penalty | 基于约束的惩罚 | 第5章 |
| key-value datastore | 键值数据存储 | 第5章 |
| least recently used caching | 最近最少使用缓存 | 第5章 |
| prefilling-decoding disaggregation | 预填充与解码分离 | 第5章 |
| priority-based scheduling | 基于优先级的调度 | 第5章 |
| memory-compute trade-off | 内存与计算之间的权衡 | 第5章 |
| context scaling | 上下文扩展 | 第5章 |
| search scaling | 搜索扩展 | 第5章 |
| solution-level search | 解答级搜索 | 第5章 |
| solution-level verification | 解答级验证 | 第5章 |
| step-level search | 步骤级搜索 | 第5章 |
| step-level verification | 步骤级验证 | 第5章 |
| critique-refine cycle | 评议—改进循环 | 第5章 |
| verification model | 验证模型 | 第5章 |
| evaluation model | 评估模型 | 第5章 |
| credit assignment problem | 信用分配问题 | 第6章 |
| telescoping sum | 裂项相消求和 | 第6章 |
| functional linguistic competence | 功能语言能力 | 第6章 |
| mechanistic interpretability | 机制可解释性 | 第6章 |
| natural language auto-encoder | 自然语言自编码器 | 第6章 |
| activation verbalizer | 激活语言化器 | 第6章 |
| activation reconstructor | 激活重构器 | 第6章 |
| consensus | 共识 | 第6章 |
| verifier hallucination | 验证器幻觉 | 第6章 |
