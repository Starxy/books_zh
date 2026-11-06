# 《大语言模型高效推理》中英术语

页序以用户提供的第二版为准。位置标出正文首次使用处或集中说明处，封面和目录另行排印。英文模型名、框架名、方法名和 API 按原样保留。

| 英文 | 中文 | 义项与原文位置 |
|---|---|---|
| large language model (LLM) | 大语言模型 | §1.1 |
| inference | 推理 | §1.1，运行参数固定的模型 |
| loss function | 损失函数 | §1.1 |
| forward pass / backward pass | 前向传播／反向传播 | §1.1 |
| throughput / latency | 吞吐量／时延 | §1.1 |
| token | 词元 | §1.1；tokenizer 为词元切分器 |
| prompt | 提示 | §1.1；指输入文本或词元序列，prompt caching 对应提示缓存 |
| key-value cache (KV cache) | 键值缓存（KV 缓存） | §1.1 首现，§3.2 定义 |
| autoregressive generation | 自回归生成 | §1.1 |
| prefill / decode | 预填充／解码 | §1.2；处理输入序列／逐步生成输出词元 |
| stop token / end-of-sequence token (EOS) | 停止词元／序列结束词元 | §1.2、Q8.1；字面标识符照录 |
| compute-bound | 受计算能力限制 | §1.2 |
| memory-bandwidth-bound / memory-bound | 受访存带宽限制 | §1.2、§1.5；memory-constrained 在显存容量语境为“受显存容量限制” |
| Tensor Core | 张量核心 | §1.2；硬件单元 |
| iron triangle | 铁三角 | §1.3；时延、吞吐量、成本 |
| Time to First Token (TTFT) | 首词元时延 | §1.3 表、Q1.2 |
| Time Per Output Token (TPOT) | 每输出词元耗时 | §1.3 表、Q1.2；书中按连续输出词元之间的时间说明 |
| batch size / batching | 批大小／批处理 | §1.1、§1.3；也可按句意写“组批” |
| quantization | 量化 | §1.3 表或 Q1.2；第 4 章详述 |
| speculative decoding | 推测解码 | §1.3 表；第 5 章详述 |
| High Bandwidth Memory (HBM) | 高带宽存储器 | §1.4；显卡片外显存 |
| Floating Point Operation (FLOP) | 浮点运算 | §1.4；FLOP/s 表示速率，INT8 吞吐量保留原书用量并注意与 TOPS 区分 |
| Roofline model | 屋顶线模型 | §1.5 |
| arithmetic intensity / operational intensity | 算术强度／运算强度 | §1.5、Q2.4；单位 FLOP/byte |
| continuous batching | 连续批处理 | Q1.2、§8.2.2 |
| Service Level Objective (SLO) | 服务级别目标 | Q1.2、§8.4 |
| prefix caching | 前缀缓存 | Q1.2、§6.3 |
| goodput | 有效吞吐量 | Q1.4、Q8.5、§13.2；原书以满足全部 SLO 的请求占比表示，按原书定义译出 |
| tail latency | 尾部时延 | Q1.4 |
| bandwidth wall | 带宽墙 | Q1.5 |
| Grouped Query Attention (GQA) | 分组查询注意力 | Q1.5、§3.4 |
| Multi-head Latent Attention (MLA) | 多头潜在注意力 | Q1.5、§3.4 |
| Streaming Multiprocessor (SM) | 流式多处理器 | §2.1 |
| shared memory / register / L2 cache | 共享内存／寄存器／二级缓存 | §2.1、§2.3 |
| mixed precision | 混合精度 | §2.2 |
| Brain Float 16 (BF16) | 16 位脑浮点格式 | §2.2 表、Q2.3、附录 C；后续用 BF16 |
| static random-access memory (SRAM) | 静态随机存取存储器 | §2.3 |
| video random-access memory (VRAM) | 显存 | §2.3 表 |
| unified memory | 统一内存 | §2.4 |
| vector neural network instructions (VNNI) | 向量神经网络指令 | §2.4 |
| Tera-Operations Per Second (TOPS) | 每秒万亿次运算 | §2.4 |
| photonic computing | 光子计算 | §2.5、§14.3 |
| tensor parallelism | 张量并行 | Q2.1、§9.2 |
| all-reduce / all-gather / all-to-all | 全归约／全收集／全互换 | Q2.1、§9.2、§9.4；集合通信操作 |
| attention head / query / key / value | 注意力头／查询／键／值 | §1.2、§3.1 |
| Feed-Forward Network (FFN) | 前馈网络 | §3.1 |
| Multi-Head Attention (MHA) | 多头注意力 | §3.4 |
| Multi-Query Attention (MQA) | 多查询注意力 | §3.4 |
| General Matrix Multiplication (GEMM) | 通用矩阵乘法 | §3.3 |
| General Matrix-Vector Multiply (GEMV) | 通用矩阵–向量乘法 | §3.3 |
| Rotary Positional Embeddings (RoPE) | 旋转位置嵌入 | §3.5 |
| NTK-aware scaling | NTK 感知缩放 | §3.5、Q10.4；NTK 为神经切线核 |
| disaggregated prefill and decode | 预填充与解码分离 | Q3.5、§8.3；disaggregated serving 为分离式服务 |
| activation / activation outlier | 激活值／激活离群值 | §4.3.2、§4.5 |
| Post-Training Quantization (PTQ) | 训练后量化 | §4.3、§4.4 |
| Hessian matrix | 海森矩阵 | §4.3.1、附录 C |
| Activation-Aware Weight Quantization (AWQ) | 激活感知权重量化 | §4.3.2 |
| Additive Quantization of Language Models (AQLM) | 语言模型加性量化 | §4.3.3 |
| Quantization-Aware Training (QAT) | 量化感知训练 | §4.4 |
| straight-through estimator (STE) | 直通估计器 | §4.4 |
| calibration dataset / quantization scale | 校准数据集／量化尺度 | §4.3–4.5 |
| weight-only quantization / weight-and-activation quantization | 仅权重量化／权重与激活量化 | Q4.2 |
| draft model / target model | 草稿模型／目标模型 | §5.1；draft token 为草稿词元 |
| rejection sampling / acceptance rate | 拒绝采样／接受率 | §5.1、Q5.2 |
| tree-based speculative decoding / tree mask | 基于树的推测解码／树形掩码 | §5.2 |
| self-distillation / dynamic draft tree | 自蒸馏／动态草稿树 | §5.3–5.4 |
| residual distribution | 残余分布 | Q5.1；拒绝草稿词元后用于校正采样 |
| total variation distance (TV) | 总变差距离 | Q5.1 |
| Extrapolation Algorithm for Greater Language-model Efficiency (EAGLE) | 提高语言模型效率的外推算法 | §5.4、Q5.5，正文后续用 EAGLE |
| PagedAttention / copy-on-write (CoW) | PagedAttention／写时复制 | §6.2 |
| virtual memory / block table | 虚拟内存／块表 | §6.2 |
| attention sink | 注意力汇聚点 | §6.4，现象称“注意力汇聚” |
| sliding window | 滑动窗口 | §6.4 |
| cache eviction | 缓存淘汰 | Q6.4 |
| Least Recently Used (LRU) | 最近最少使用 | Q6.4；优先淘汰最久未访问的块 |
| kernel / kernel fusion | 内核／内核融合 | §2.2、§7.1；指 GPU 计算内核 |
| tiling | 分块 | §2.3、§7.2；也用于矩阵分块 |
| IO-aware exact attention | I/O 感知的精确注意力 | §7.2 |
| online softmax | 在线 softmax | §7.2 首现，§7.3 详述 |
| Warpgroup Matrix Multiply Accumulate (WGMMA) | 线程束组矩阵乘累加 | §7.2、Q7.4 |
| domain-specific language (DSL) / warp | 领域专用语言／线程束 | §7.4 |
| Tensor Memory Accelerator (TMA) / ping-pong pipelining | 张量内存加速器／乒乓流水线 | Q7.4 |
| static batching / chunked prefill | 静态批处理／分块预填充 | §8.2.1、§8.2.3 |
| prefill piracy | 预填充抢占 | §8.2.3、Q8.2；区别于调度器主动抢占请求 |
| KV cache migration / remote direct memory access (RDMA) | KV 缓存迁移／远程直接内存访问 | §8.3 |
| preemption / admission control | 抢占／准入控制 | Q6.4、§8.4 |
| first in, first out (FIFO) | 先入先出 | §8.4 |
| Mixture of Experts (MoE) | 混合专家 | Q8.3、§9.4 |
| Model FLOP Utilization (MFU) | 模型浮点运算利用率 | Q8.5、§13.2；实际模型 FLOP/s 占理论峰值的比例 |
| total cost of ownership (TCO) | 总拥有成本 | Q8.5 |
| column parallelism / row parallelism | 列并行／行并行 | §9.2 |
| pipeline parallelism / pipeline bubble | 流水线并行／流水线气泡 | §9.3 |
| micro-batching | 微批处理 | §9.3 |
| expert parallelism / expert routing | 专家并行／专家路由 | §9.4 |
| expert offloading | 专家卸载 | §9.4；向 CPU 内存或 NVMe 迁出权重 |
| Ring Attention | 环形注意力 | §10.3 |
| context compression | 上下文压缩 | §10.4 |
| perplexity | 困惑度 | §10.4 |
| State Space Model (SSM) | 状态空间模型 | Q3.3 首现，§10.5 详述 |
| retrieval-augmented generation (RAG) | 检索增强生成 | Q10.5 |
| on-device inference / edge inference | 端侧推理／边缘推理 | 第 11 章 |
| neural architecture search (NAS) | 神经架构搜索 | §11.4 |
| hardware-aware NAS / supernet | 硬件感知神经架构搜索／超网络 | §11.4 |
| early exit | 提前退出 | §11.4、§14.4 |
| inference-time compute scaling | 推理时计算扩展 | §12.1 |
| chain-of-thought (CoT) | 思维链 | §12.2 |
| Process Reward Model (PRM) / Outcome Reward Model (ORM) | 过程奖励模型／结果奖励模型 | §12.3、Q12.2 |
| Best-of-N / beam search | N 选一／束搜索 | §12.3 |
| Monte Carlo Tree Search (MCTS) | 蒙特卡洛树搜索 | §12.3 |
| Group Relative Policy Optimization (GRPO) | 群组相对策略优化 | §12.4 |
| Proximal Policy Optimization (PPO) | 近端策略优化 | Q12.4 |
| observability | 可观测性 | §13.1–13.3 |
| percentile | 百分位数 | Q1.4、§13.2；p99 即第 99 百分位数 |
| cold start | 冷启动 | §13.3 |
| diffusion-based language model | 扩散式语言模型 | §14.1 |
| multi-token prediction (MTP) | 多词元预测 | §14.2 |
| neuromorphic computing | 神经形态计算 | §14.3 |
| Mixture of Depths | 混合深度 | §14.4 |
| conditional computation | 条件计算 | §14.4 |
