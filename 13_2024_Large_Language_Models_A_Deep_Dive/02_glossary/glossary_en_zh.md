# 《大语言模型深度解析》中英术语表

按本书正文使用的含义维护。首次出现按实际阅读顺序判断，缩写表和目录中的词项不计作正文引入。

| 英文 | 中文 | 语境或首次引入 |
|---|---|---|
| large language model (LLM) | 大语言模型 | 序；复数 LLMs 仍用同一译名 |
| artificial intelligence (AI) | 人工智能 | 序 |
| pre-training | 预训练 | 序 |
| prompt-based learning | 基于提示的学习 | 序；上下文明确时可简称提示学习 |
| fine-tuning | 微调 | 序；与泛指调优的 tuning 区分 |
| retrieval-augmented generation (RAG) | 检索增强生成 | 序 |
| large language model operations (LLMOps) | 大语言模型运维 | 序 |
| productionizing | 生产部署 | 序 |
| multimodal large language model (MMLLM) | 多模态大语言模型 | 序 |
| bias | 偏见 | 序；伦理和群体公平性，统计估计语境译为偏差 |
| fairness | 公平性 | 序 |
| machine learning | 机器学习 | 推荐语 |
| generative AI | 生成式人工智能 | 推荐语 |
| prompt engineering | 提示工程 | 推荐语 |
| reinforcement learning (RL) | 强化学习 | 前言 |
| computer vision | 计算机视觉 | 前言 |
| robotics | 机器人学 | 前言 |
| speech processing | 语音处理 | 前言 |
| emergent behavior | 涌现行为 | 前言；能力用 emergent ability |
| natural language processing (NLP) | 自然语言处理 | 前言 |
| prompt-based tuning | 基于提示的调优 | 前言 |
| instruction tuning (IT) | 指令调优 | 前言 |
| parameter-efficient fine-tuning (PEFT) | 参数高效微调 | 前言 |
| compute-efficient fine-tuning | 计算高效微调 | 前言 |
| hallucination | 幻觉 | 前言；生成内容中的不实或无依据成分 |
| toxicity | 毒性 | 前言；对文本可能造成伤害的度量语境 |
| inference | 推理 | 模型运行时；自然语言推断和统计推断分别按相应语境处理 |
| reasoning | 推理 | 认知或解题过程；与模型推理易混时写“推理过程/能力” |
| alignment tuning | 对齐调优 | 前言；使模型行为符合预期 |
| reinforcement learning from human feedback (RLHF) | 基于人类反馈的强化学习 | 前言；原书另用 reinforcement learning with human feedback |
| attention mechanism | 注意力机制 | 前言 |
| encoder-decoder | 编码器—解码器 | 前言 |
| autoregressive | 自回归 | 前言 |
| masked language model | 掩码语言模型 | 前言；任务 masked language modeling (MLM) 为掩码语言建模 |
| answer engineering | 答案工程 | 前言；设计提示学习中的输出空间及其到标签的映射 |
| multi-prompting | 多提示 | 前言 |
| adapter | 适配器 | 前言；模型中加入的可训练模块 |
| low-rank adaptation (LoRA) | 低秩适配 | 前言 |
| vector-based random matrix adaptation (VeRA) | 基于向量的随机矩阵适配 | 前言 |
| delta-tuning | 增量调优 | 前言；关注相对预训练模型的参数变化 |
| zero-/few-/multi-shot learning | 零样本／少样本／多样本学习 | 前言；示例数由语境决定 |
| in-context learning (ICL) | 上下文学习 | 前言 |
| chain-of-thought (CoT) | 思维链 | 前言；区分思维链推理和思维链提示 |
| full-parameter tuning | 全参数调优 | 前言 |
| post-training quantization (PTQ) | 训练后量化 | 前言 |
| quantization-aware fine-tuning | 量化感知微调 | 前言 |
| helpful, honest, and harmless (HHH/3H) | 有帮助、诚实且无害 | 原文三词的排列不固定，按所在句处理 |
| constitutional AI | 宪法式人工智能 | 前言；方法名称 |
| direct preference optimization (DPO) | 直接偏好优化 | 前言 |
| neural toxic degeneration | 神经模型的毒性退化 | 前言 |
| dense retrieval | 稠密检索 | 前言；用稠密向量表示检索对象 |
| synthetic data | 合成数据 | 前言 |
| context window | 上下文窗口 | 前言 |
| knowledge transfer | 知识迁移 | 前言 |
| state space model | 状态空间模型 | 前言 |
| prompt | 提示 | 前言；一般性讨论。作为模型输入的英文提示保留字面值 |
| token | 词元 | 语言模型输入或输出序列的基本单位；tokenizer 为词元切分器 |
| norm | 范数 | 符号表 |
| log-likelihood loss | 对数似然损失 | 符号表；目标的符号按各式 |
| logistic sigmoid | 逻辑 S 形函数 | 符号表 |
| dot product | 点积 | 符号表 |
| cross product | 叉积 | 符号表；保留原书将 A、B 写为矩阵的说明 |
| Hadamard product | 哈达玛积 | 符号表；逐元素乘积 |
| Kronecker product | 克罗内克积 | 符号表 |
| safety guardrails | 安全约束 | 1.1；模型对争议性问题的回答限制 |
| generative model | 生成模型 | 1.1 |
| text-to-image model | 文本到图像模型 | 1.1 |
| graphics processing unit (GPU) | 图形处理器 | 1.1；缩写表保留原文 Graphical Processing Unit |
| deep fake | 深度伪造 | 1.1；合成或篡改语音、视频 |
| life history | 生活史 | 1.2；演化生物学语境 |
| knowledge graph | 知识图谱 | 1.2 |
| wetware | 生物湿件 | 1.2；指生物神经系统 |
| natural language understanding (NLU) | 自然语言理解 | 1.3 |
| natural language generation (NLG) | 自然语言生成 | 1.3 |
| expert system | 专家系统 | 1.3.2；与混合专家中的 expert 区分 |
| hidden Markov model (HMM) | 隐马尔可夫模型 | 1.3.2 |
| n-gram model | n 元模型 | 1.3.2；unigram、bigram、trigram 分别译一元、二元、三元模型 |
| language model (LM) | 语言模型 | 1.3.2 |
| pre-trained language model (PLM) | 预训练语言模型 | 1.3.2 |
| dense vector representation | 稠密向量表示 | 1.3.3 |
| recurrent neural network (RNN) | 循环神经网络 | 1.3.3 |
| long short-term memory (LSTM) | 长短期记忆 | 1.3.3 |
| word embedding | 词嵌入 | 1.3.3；与词元嵌入区分 |
| convolutional neural network (CNN) | 卷积神经网络 | 1.3.3 |
| continuous bag-of-words (CBOW) | 连续词袋 | 1.3.4 |
| skip-gram | 跳元模型 | 1.3.4；用中心词预测邻近词 |
| transfer learning | 迁移学习 | 1.3.4 |
| named entity recognition (NER) | 命名实体识别 | 1.4 |
| emergent ability | 涌现能力 | 1.4；预训练或微调未显式教授的能力 |
| end-user prompting | 终端用户提示 | 1.5 |
| adaptive pre-training | 适应性预训练 | 1.5.1；domain-adaptive 为领域适应性预训练 |
| total cost of ownership (TCO) | 总拥有成本 | 1.5.1 |
| tokenization | 词元切分 | 1.5.1.1 |
| self-attention | 自注意力 | 1.5.1.1；首次见“自注意力机制” |
| contextual representation | 上下文表示 | 1.5.1.1 |
| sequence-to-sequence | 序列到序列 | 1.5.1.1 |
| causal decoder architecture | 因果解码器架构 | 1.5.1.1；自回归生成 |
| prefix-decoder architecture | 前缀解码器架构 | 1.5.1.1；前缀双向、生成单向 |
| denoising autoencoding | 去噪自编码 | 1.5.1.1；2.5.2.13 的 DAE 为去噪自编码器 |
| mixture-of-denoisers | 混合去噪器 | 1.5.1.1 |
| reward model | 奖励模型 | 1.5.2.2 |
| quantization | 量化 | 1.5.2.3 |
| encoder / decoder | 编码器／解码器 | 2.1；模型组件 |
| abstractive summarization | 生成式摘要 | 2.1；与抽取式摘要区分 |
| subword | 子词 | 2.1.1 |
| hidden state | 隐藏状态 | 2.1.1 |
| context variable / context vector | 上下文变量／上下文向量 | 2.1.1 |
| categorical cross-entropy | 类别交叉熵 | 2.1.3 |
| key-value pair | 键值对 | 2.2 |
| scaled dot product | 缩放点积 | 2.2 |
| multi-head attention | 多头注意力 | 2.3.1 |
| residual connection | 残差连接 | 2.3.1 |
| layer normalization (LayerNorm / LN) | 层归一化 | 2.3.1；pre-LN、post-LN 为前置、后置层归一化 |
| masked multi-head attention | 掩码多头注意力 | 2.3.2 |
| out-of-vocabulary word | 词表外词 | 2.3.3 |
| byte-pair encoding (BPE) | 字节对编码 | 2.3.3 |
| positional encoding | 位置编码 | 2.3.4；positional embedding 为位置嵌入 |
| rectified linear unit (ReLU) | 整流线性单元 | 2.3.6 |
| covariate shift | 协变量偏移 | 2.3.7；保留原书此处的解释 |
| batch normalization (BatchNorm) | 批归一化 | 2.3.10.1 |
| root mean square layer normalization (RMSNorm) | 均方根归一化 | 2.3.10.1 |
| rotary position embedding (RoPE) | 旋转位置嵌入 | 2.3.10.4 |
| length extrapolation | 长度外推 | 2.3.10.4 |
| full / sparse attention | 全注意力／稀疏注意力 | 2.3.10.5 |
| multi-query attention | 多查询注意力 | 2.3.10.5 |
| cross-attention | 交叉注意力 | 2.3.10.5 |
| adaptive computation time (ACT) | 自适应计算时间 | 2.3.10.5 |
| parallel corpus | 平行语料库 | 2.4.1.1；句子有明确跨语言对应 |
| multilingual corpus | 多语言语料库 | 2.4.1.1；不要求句子级对应 |
| tokenizer | 词元切分器 | 2.4.2.5 |
| pre-training from scratch (PTS) | 从头预训练 | 2.5.1.1 |
| continual pre-training (CPT) | 持续预训练 | 2.5.1.2 |
| simultaneous pre-training (SPT) | 同步预训练 | 2.5.1.3 |
| task adaptive pre-training (TAPT) | 任务适应性预训练 | 2.5.1.4 |
| knowledge inherited pre-training (KIPT) | 知识继承预训练 | 2.5.1.5 |
| self-supervised learning (SSL) | 自监督学习 | 2.5.2 |
| causal language modeling (CLM) | 因果语言建模 | 2.5.2.1 |
| masked language modeling (MLM) | 掩码语言建模 | 2.5.2.2；指训练任务 |
| replaced token detection (RTD) | 替换词元检测 | 2.5.2.3 |
| shuffled token detection (STD) | 打乱词元检测 | 2.5.2.4 |
| random token substitution (RTS) | 随机词元替换 | 2.5.2.5 |
| swapped language modeling (SLM) | 替换式语言建模 | 2.5.2.6 |
| translation language modeling (TLM) | 翻译语言建模 | 2.5.2.7 |
| alternate language modeling (ALM) | 交替语言建模 | 2.5.2.8 |
| sentence boundary objective (SBO) | 句段边界目标 | 2.5.2.9；预测跨词元片段内的遮盖词元 |
| next sentence prediction (NSP) | 下一句预测 | 2.5.2.10 |
| sentence order prediction (SOP) | 句序预测 | 2.5.2.11 |
| mixture of experts (MoE) | 混合专家 | 2.5.3.5；路由器决定词元所使用的专家 |
| greedy search | 贪心搜索 | 2.5.4.2 |
| beam search | 束搜索 | 2.5.4.2 |
| temperature sampling | 温度采样 | 2.5.4.2 |
| nucleus sampling | 核采样 | 2.5.4.2；即 Top-p 采样 |
| data / pipeline / tensor parallelism | 数据／流水线／张量并行 | 2.5.4.3 |
| ablation experiment | 消融实验 | 2.6.2 |
| sentinel token | 哨兵词元 | 2.6.2.3；例如 T5 的 <extra_id_0> |
| perplexity | 困惑度 | 2.6.3.4 |
| expert parallelism (EP) | 专家并行 | 2.6.4.4 |
| forward pass | 前向传播 | 2.7.2 |
| backpropagation | 反向传播 | 2.7.2 |
| fully supervised learning | 全监督学习 | 3.1.1 |
| feature engineering | 特征工程 | 3.1.1 |
| pre-train and fine-tune (PTFT) | 预训练再微调 | 3.1.2 |
| head-based fine-tuning | 基于任务头的微调 | 3.1.2；与基于提示的微调作比较 |
| zero-shot / one-shot / few-shot | 零样本／单样本／少样本 | 3.1.3 |
| cloze prompt | 完形填空式提示 | 3.2；在答案槽位填词元 |
| prefix prompt | 前缀式提示 | 3.2；从提示末尾继续生成 |
| knowledge probing | 知识探查 | 3.2.3；从模型中查询事实知识 |
| prompt template | 提示模板 | 3.3；与填入输入后的实际提示区分 |
| prompt mining | 提示挖掘 | 3.3.3.1 |
| prompt paraphrasing | 提示改写 | 3.3.3.2；以回译得到变体 |
| back-translation | 回译 | 3.3.3.2 |
| trigger token | 触发词元 | 3.3.3.3；离散模板搜索的变量 |
| discrete prompt / continuous prompt | 离散提示／连续提示 | 3.3.3；连续提示也称软提示 |
| soft prompt / hard token | 软提示／硬词元 | 3.3.4；硬词元具有固定的表示 |
| prefix tuning | 前缀调优 | 3.3.4.1；学习连续向量作为前缀 |
| virtual token | 虚拟词元 | 3.3.4.1 |
| prompt-based fine-tuning | 基于提示的微调 | 3.3.5；固定模板，更新模型参数 |
| answer engineering | 答案工程 | 3.4；设计答案形式、空间和映射 |
| answer shape / answer space | 答案形式／答案空间 | 3.4 |
| answer mapping / verbalizer | 答案映射／答案映射器 | 3.4、3.5.3；把答案映射到标签 |
| constrained / unconstrained answer space | 受约束／无约束答案空间 | 3.4.2 |
| multi-prompt inference | 多提示推理 | 3.5 |
| ensembling | 集成 | 3.5.1；汇总多个提示的预测结果 |
| knowledge distillation | 知识蒸馏 | 3.5.1 |
| in-context learning (ICL) | 上下文学习 | 3.5.2 |
| prompt augmentation | 提示扩充 | 3.5.2 |
| demonstration learning | 示例学习 | 3.5.2 |
| prompt decomposition | 提示分解 | 3.5.3 |
| catastrophic forgetting | 灾难性遗忘 | 3.6.3.2 |
| domain adaptation | 领域适配 | 4.2.3 |
| fully fine-tuned / full-parameter fine-tuning | 全参数微调 | 4.3；更新预训练模型的全部参数 |
| series / parallel adapter | 串联／并联适配器 | 4.3.1 |
| bottleneck dimension | 瓶颈维数 | 4.3.1；适配器降维后的特征维数 |
| intrinsic dimension | 内在维度 | 4.3.2 |
| reparameterization | 重参数化 | 4.3.2 |
| low-rank adaptation / low-rank adapter (LoRA) | 低秩适配／低秩适配器 | 4.3.2.1；原书标题采用 adapter |
| Kronecker product | 克罗内克积 | 4.3.2.2 |
| Kronecker adapter (KronA) | 克罗内克适配器 | 4.3.2.2 |
| vector-based random matrix adaptation (VeRA) | 基于向量的随机矩阵适配 | 4.3.2.3 |
| outlier feature | 离群特征 | 4.4.1.1；量化时需保留精度的异常大激活 |
| post-training quantization (PTQ) | 训练后量化 | 4.4.1.1 |
| quantization-aware training (QAT) | 量化感知训练 | 4.4.1.2 |
| double quantization | 二次量化 | 4.4.1.2；量化量化常数 |
| paged optimizer | 分页优化器 | 4.4.1.2 |
| Frobenius norm | Frobenius 范数 | 4.4.1.2 |
| singular value decomposition (SVD) | 奇异值分解 | 4.4.1.2 |
| prompt chaining | 提示链 | 4.5.3；根据先后依赖串联提示 |
| self-consistency | 自一致性 | 4.5.5 |
| tree-of-thoughts (ToT) | 思维树 | 4.5.6 |
| helpfulness / honesty / harmlessness | 有帮助性／诚实性／无害性 | 5.1 |
| red teaming | 红队测试 | 5.1.3；主动诱发不当输出以收集样例 |
| chain-of-hindsight | 后见链 | 5.1.3；以好坏回答给出反馈 |
| jailbreak | 越狱 | 5.1.3.1；对模型安全约束的绕过 |
| operant conditioning | 操作性条件作用 | 5.2 |
| agent / environment | 智能体／环境 | 5.2；强化学习框架 |
| Markov decision process (MDP) | 马尔可夫决策过程 | 5.2 |
| state / action / reward | 状态／动作／奖励 | 5.2 |
| transition function | 转移函数 | 5.2；下一状态的条件分布 |
| policy | 策略 | 5.2；由状态给出动作分布 |
| trajectory / episode | 轨迹／回合 | 5.2；回合通常以终止状态结束 |
| return / discount factor | 回报／折扣因子 | 5.2；折扣后的累计奖励 |
| sensibleness / specificity / interestingness (SSI) | 合理性／具体性／趣味性 | 5.4.1；LaMDA 质量指标 |
| groundedness / informativeness | 有据性／信息性 | 5.4.1；LaMDA 评估指标 |
| policy gradient | 策略梯度 | 5.4.2.1 |
| advantage actor critic | 优势行动者—评论家算法 | 5.4.2.1 |
| trust region policy optimization | 信赖域策略优化 | 5.4.2.1 |
| Bradley–Terry model | Bradley–Terry 模型 | 5.4.2.1、5.5.2.1 |
| proximal policy optimization (PPO) | 近端策略优化 | 5.4.3.1 |
| Kullback–Leibler divergence | Kullback–Leibler 散度 | 5.4.3.1；简称 KL 散度 |
| supervised fine-tuning (SFT) | 监督微调 | 5.4.4.1 |
| personally identifiable information (PII) | 个人身份信息 | 5.4.4.1 |
| reinforcement learning from AI feedback (RLAIF) | 基于人工智能反馈的强化学习 | 5.5.1；由模型提供偏好反馈 |
| partition function | 配分函数 | 5.5.2.1 |
| hallucination | 幻觉 | 6.1；与输入、上下文或事实冲突 |
| sycophancy | 迎合 | 6.1.1；模型附和用户观点 |
| atomic fact | 原子事实 | 6.1.2.1；FActScore 核查单位 |
| factuality | 事实性 | 6.1.2.3；与真实性 truthfulness 按语境区分 |
| parametric knowledge | 参数知识 | 6.1.4；储存在模型参数中的知识 |
| factual-nucleus sampling | 事实性核采样 | 6.1.4.4 |
| social group / protected attribute | 社会群体／受保护属性 | 6.2 |
| group fairness / individual fairness | 群体公平性／个体公平性 | 6.2 |
| representational harm / allocational harm | 表征性伤害／分配性伤害 | 6.2.1、6.2.2 |
| word embedding association test (WEAT) | 词嵌入关联检验 | 6.2.4.1 |
| sentence encoder association test (SEAT) | 句子编码器关联检验 | 6.2.4.1 |
| contextualized embedding association test (CEAT) | 上下文嵌入关联检验 | 6.2.4.1 |
| pseudo-log-likelihood (PLL) | 伪对数似然 | 6.2.4.2 |
| counterfactual data augmentation (CDA) | 反事实数据增强 | 6.2.6.1 |
| counterfactual data substitution (CDS) | 反事实数据替换 | 6.2.6.1 |
| control token / control code | 控制词元／控制码 | 6.2.6.1、6.3.4.2 |
| movement pruning / diff pruning | 移动剪枝／差分剪枝 | 6.2.6.2、6.2.6.3 |
| expected maximum toxicity (EMT) | 期望最大毒性 | 6.3.2 |
| toxicity probability (TP) / toxic fraction (TF) | 毒性概率／有毒比例 | 6.3.2 |
| domain-adapted pre-training (DAPT) | 领域适应性预训练 | 6.3.4.1 |
| plug and play language model (PPLM) | 即插即用语言模型 | 6.3.4.2 |
| self-diagnosis / self-debiasing | 自我诊断／自我去偏 | 6.3.4.2 |
| black-box / white-box probing | 黑箱／白箱探查 | 6.4.2；分别只能观察输出或还可访问模型权重 |
| differential privacy | 差分隐私 | 6.4.2 |
| vector index | 向量索引 | 7.2 |
| text chunking | 文本分块 | 7.3 |
| semantic textual similarity (STS) | 语义文本相似性 | 7.3 |
| modular RAG | 模块化 RAG | 7.4 |
| query rewriting | 查询改写 | 7.4.2.1 |
| reciprocal rank fusion (RRF) | 倒数排名融合 | 7.4.2.1 |
| query-to-document expansion | 查询到文档扩展 | 7.4.2.2 |
| generation-augmented retrieval (GAR) | 生成增强检索 | 7.4.2.2 |
| subquery generation / routing | 生成子查询／路由 | 7.4.2.3、7.4.2.4 |
| reranking | 重排序 | 7.4.3.1 |
| lost in the middle | 遗失在中间 | 7.4.3.1；提示中间位置的信息被遗漏 |
| iterative retrieval / multi-hop question | 迭代检索／多跳问题 | 7.4.3.2 |
| context consolidation | 上下文整合 | 7.4.3.3 |
| context relevance / answer relevance | 上下文相关性／答案相关性 | 7.5.1 |
| answer faithfulness | 答案忠实度 | 7.5.1.2；原书也称 groundedness |
| mean reciprocal rank (MRR) | 平均倒数排名 | 7.5.1.1 |
| normalized discounted cumulative gain (nDCG) | 归一化折损累积增益 | 7.5.1.1 |
| noise robustness / counterfactual robustness | 噪声鲁棒性／反事实鲁棒性 | 7.5.2.1、7.5.2.4 |
| negative rejection | 无答案时拒答 | 7.5.2.2 |
| information integration | 信息整合 | 7.5.2.3；从多份上下文文档综合信息 |
| brevity penalty | 长度惩罚 | 8.3.2；BLEU 对偏短输出的惩罚 |
| longest common subsequence (LCS) | 最长公共子序列 | 8.3.3；允许不连续 |
| word mover's distance (WMD) | 词移动距离 | 8.3.5 |
| sentence mover's distance (SMD) | 句子移动距离 | 8.3.5 |
| analytic quality | 分析质量 | 8.5.2；完成应用相关任务的质量 |
| prefill / decode | 预填充／解码 | 8.5.3；处理输入词元／逐步生成输出词元 |
| inference latency / throughput | 推理延迟／吞吐量 | 8.5.3、8.7.2 |
| vector database | 向量数据库 | 8.6.3 |
| dynamic batching / continuous batching | 动态批处理／连续批处理 | 8.7.2.1 |
| key-value caching | 键值缓存 | 8.7.2.2；缓存此前词元的键和值张量 |
| experiment tracking / model registry | 实验跟踪／模型注册库 | 8.8.1.1 |
| monitoring / observability | 监控／可观测性 | 8.8.1.4 |
| human-in-the-loop | 人在回路中 | 8.8.2.2；人工参与标注、审核或决策 |
| model card | 模型卡 | 8.8.3.1 |
| data provenance | 数据来源 | 8.8.3.2；包含来源与模型使用关系 |
| image captioning | 图像描述生成 | 9.1 |
| visual question answering (VQA) | 视觉问答 | 9.1 |
| modality encoder / modality generator | 模态编码器／模态生成器 | 9.3.1、9.3.7 |
| input projector / output projector | 输入投影器／输出投影器 | 9.3.2、9.3.6 |
| single-stream / cross-stream architecture | 单流／跨流架构 | 9.3.2 |
| contrastive learning | 对比学习 | 9.3.3.1 |
| hard negative | 困难负例 | 9.3.3.2 |
| masked object classification (MOC) | 掩码物体分类 | 9.3.3.4 |
| video-subtitle matching (VSM) | 视频与字幕匹配 | 9.3.3.7 |
| frame order modeling (FOM) | 帧顺序建模 | 9.3.3.8 |
| modality-switching instruction tuning (MosIT) | 模态切换指令调优 | 9.5.3.4 |
| gradient checkpointing | 梯度检查点 | 10.2.3 |
| multi-token prediction / generation | 多词元预测／多词元生成 | 10.2.4 |
| small language model (SLM) | 小型语言模型 | 10.3.1；缩写与第 2 章的替换式语言建模相同 |
| domain-specific language model (DSLM) | 领域专用语言模型 | 10.3.3 |
| multilayer perceptron (MLP) | 多层感知机 | 附录 A |
| mean squared error / mean absolute error | 均方误差／平均绝对误差 | A.4.3 |
| hinge loss | 铰链损失 | 9.3.3.7、A.4.3.5 |
| stochastic gradient descent (SGD) | 随机梯度下降 | A.4.4.1 |
| dropout | 随机失活 | A.4.6.3 |
| episodic / continuing task | 回合式／持续式任务 | B.1.1 |
| state-value / action-value function | 状态价值／动作价值函数 | B.1.3 |
| exploration / exploitation | 探索／利用 | B.2 |
| off-policy / on-policy | 离策略／同策略 | B.3 |
| experience replay | 经验回放 | B.3.2 |
