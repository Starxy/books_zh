class ScoreMatching(nn.Module):
    def __init__(self, snet, alpha, sigma, eta, D, T):
        super(ScoreMatching, self).__init__()

        print('Score Matching by JT.')

        self.snet = snet

        # 其他超参数
        self.D = D

        self.sigma = sigma

        self.T = T

        self.alpha = alpha

        self.eta = eta

    def sample_base(self, x_1):
        # 在 [-1, 1]**D 上均匀分布
        return 2. * torch.rand_like(x_1) - 1.

    def langevin_dynamics(self, x):
        for t in range(self.T):
            x = x + self.alpha * self.snet(x) + self.eta * torch.randn_like(x)
        return x

    def forward(self, x, reduction='mean'):
        # =====得分匹配
        # 采样噪声
        epsilon = torch.randn_like(x)

        # =====
        # 计算加噪数据
        tilde_x = x + self.sigma * epsilon

        # =====
        # 计算得分模型的输出
        s = self.snet(tilde_x)

        # =====损失：得分匹配损失
        SM_loss = (1. / (2. * self.sigma)) * ((s + epsilon)**2.).sum(-1)  # 为使朗之万动力学保持原形式，取 \tilde{s} = sigma * s，舍去 \tilde{s} = -sigma * s 的负号。

        # 最终损失
        if reduction == 'sum':
            loss = SM_loss.sum()
        else:
            loss = SM_loss.mean()

        return loss

    def sample(self, batch_size=64):
        # 采样 x_0
        x = self.sample_base(torch.empty(batch_size, self.D))

        # 运行朗之万动力学
        x = self.langevin_dynamics(x)

        x = torch.tanh(x)
        return x
