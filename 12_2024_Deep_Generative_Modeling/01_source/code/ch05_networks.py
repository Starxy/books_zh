# 用于参数化编码器和解码器的神经网络示例。

# 编码器输出两倍的值，因为高斯分布需要 L 个均值和 L 个对数方差。
encoder = nn.Sequential(nn.Linear(D, M), nn.LeakyReLU(),
                        nn.Linear(M, M), nn.LeakyReLU(),
                        nn.Linear(M, 2 * L))

# 若使用类别分布，每个像素必须输出 num_vals 个值。
decoder = nn.Sequential(nn.Linear(L, M), nn.LeakyReLU(),
                        nn.Linear(M, M), nn.LeakyReLU(),
                        nn.Linear(M, num_vals * D))
