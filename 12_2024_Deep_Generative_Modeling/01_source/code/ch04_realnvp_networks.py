# 流变换的次数
num_flows = 8

# 一次变换（一个流）使用的神经网络。
nets = lambda: nn.Sequential(nn.Linear(D//2, M), nn.LeakyReLU(),
                             nn.Linear(M, M), nn.LeakyReLU(),
                             nn.Linear(M, D//2), nn.Tanh())

nett = lambda: nn.Sequential(nn.Linear(D//2, M), nn.LeakyReLU(),
                             nn.Linear(M, M), nn.LeakyReLU(),
                             nn.Linear(M, D//2))

# 先验可以使用 PyTorch 内置的分布。
prior = torch.distributions.MultivariateNormal(torch.zeros(D), torch.eye(D))

# 初始化 RealNVP。注意，这里需要对数据作均匀去量化。
model = RealNVP(nets, nett, num_flows, prior, D=D, dequantization=True)
