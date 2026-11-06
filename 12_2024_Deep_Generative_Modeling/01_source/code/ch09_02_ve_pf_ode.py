class SBGM(nn.Module):
    def __init__(self, snet, sigma, D, T):
        super(SBGM, self).__init__()

        print("SBGM by JT.")

        # sigma 参数
        self.sigma = torch.Tensor([sigma])

        # 定义基分布（协方差矩阵为对角矩阵的多元高斯分布）
        var = (1./(2.* torch.log(self.sigma))) * (self.sigma**2 - 1.)
        self.base = torch.distributions.multivariate_normal.MultivariateNormal(torch.zeros(D), var * torch.eye(D))

        # 得分模型
        self.snet = snet

        # 时间嵌入（单个线性层）
        self.time_embedding = nn.Sequential(nn.Linear(1, D), nn.Tanh())

        # 其他超参数
        self.D = D

        self.T = T

        self.EPS = 1.e-5

    def sigma_fun(self, t):
        # sigma 函数（依赖于 t），它是分布的标准差
        return torch.sqrt((1./(2. * torch.log(self.sigma))) * (self.sigma**(2.*t) - 1.))

    def log_p_base(self, x):
        # 基分布 p_1(x) 的对数概率
        log_p = self.base.log_prob(x)
        return log_p

    def sample_base(self, x_0):
        # 从基分布采样
        return self.base.rsample(sample_shape=torch.Size([x_0.shape[0]]))

    def sample_p_t(self, x_0, x_1, t):
        # 从 p_0t(x_t|x_0) 采样
        # x_0 ~ 数据，x_1 ~ 噪声
        x = x_0 + self.sigma_fun(t) * x_1

        return x

    def lambda_t(self, t):
        # 损失权重
        return self.sigma_fun(t)**2

    def diffusion_coeff(self, t):
        # SDE 中的扩散系数
        return self.sigma**t

    def forward(self, x_0, reduction='mean'):
        # =====
        # x_1 ~ 基分布
        x_1 = torch.randn_like(x_0)
        # t ~ Uniform(0, 1)
        t = torch.rand(size=(x_0.shape[0], 1)) * (1. - self.EPS) + self.EPS

        # =====
        # 从 p_0t(x|x_0) 采样
        x_t = self.sample_p_t(x_0, x_1, t)

        # =====
        # 反推噪声
        # 注意：这里采用对应关系 eps_theta(x,t) = -sigma*t score_theta(x,t)
        t_embd = self.time_embedding(t)
        x_pred = -self.sigma_fun(t) * self.snet(x_t + t_embd)

        # =====损失：得分匹配
        # 注意：x_pred 是预测的噪声，x_1 是噪声，因此对应于噪声匹配
        # （也就是 Ho 等人在基于扩散的模型中使用的损失）
        SM_loss = 0.5 * self.lambda_t(t) * torch.pow(x_pred + x_1, 2).mean(-1)

        if reduction == 'sum':
            loss = SM_loss.sum()
        else:
            loss = SM_loss.mean()

        return loss

    def sample(self, batch_size=64):
        # 1) 采样 x_0 ~ Normal(0,1/(2log sigma) * (sigma**2 - 1))
        x_t = self.sample_base(torch.empty(batch_size, self.D))

        # 应用欧拉法
        # 注意：x_0 是数据，x_1 是噪声
        # 因此必须用反向欧拉法！于是出现了减号。
        ts = torch.linspace(1., self.EPS, self.T)
        delta_t = ts[0] - ts[1]

        for t in ts[1:]:
            tt = torch.Tensor([t])
            u = 0.5 * self.diffusion_coeff(tt) * self.snet(x_t + self.time_embedding(tt))
            x_t = x_t - delta_t * u

        x_t = torch.tanh(x_t)
        return x_t

    def log_prob_proxy(self, x_0, reduction="mean"):
        # 计算对数似然的代理量（见 Song 等人，2021）
        # 注意：为简化实现和加快计算，每个时间步只取一个样本。
        # 若要得到更好的估计，应采样更多噪声。
        ts = torch.linspace(self.EPS, 1., self.T)

        for t in ts:
            # 采样噪声
            x_1 = torch.randn_like(x_0)
            # 从 p_0t(x_t|x_0) 采样
            x_t = self.sample_p_t(x_0, x_1, t)
            # 预测噪声
            t_embd = self.time_embedding(torch.Tensor([t]))
            x_pred = -self.snet(x_t + t_embd) * self.sigma_fun(t)
            # 损失（代理量）
            if t == self.EPS:
                proxy = 0.5 * self.lambda_t(t) * torch.pow(x_pred + x_1, 2).mean(-1)
            else:
                proxy = proxy + 0.5 * self.lambda_t(t) * torch.pow(x_pred + x_1, 2).mean(-1)

        if reduction == "mean":
            return proxy.mean()
        elif reduction == "sum":
            return proxy.sum()
