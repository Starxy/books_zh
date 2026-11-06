class DDGM(nn.Module):
    def __init__(self, p_dnns, decoder_net, beta, T, D):
        super(DDGM, self).__init__()

        print('DDGM by JT.')

        self.p_dnns = p_dnns # Sequential 模块列表，每个模块定义一个 DNN，为 p(z_i | z_i+1) 作参数化

        self.decoder_net = decoder_net # 对 p(x|z1) 作参数化的最后一个 DNN

        # 其他参数
        self.D = D # 输入的维数，采样时需要

        self.T = T # 步数

        self.beta = torch.FloatTensor([beta]) # 固定的扩散方差

    # 高斯分布的重参数化技巧
    @staticmethod
    def reparameterization(mu, log_var):
        std = torch.exp(0.5*log_var)
        eps = torch.randn_like(std)
        return mu + std * eps

    # 高斯前向扩散的重参数化技巧
    def reparameterization_gaussian_diffusion(self, x, i):
        return torch.sqrt(1. - self.beta) * x + torch.sqrt(self.beta) * torch.randn_like(x)

    def forward(self, x, reduction='avg'):
        # =====
        # 前向扩散
        # 注意，这里只是用高斯随机游走在空间中“漫步”。
        # 把所有 z 保存在列表中
        zs = [self.reparameterization_gaussian_diffusion(x, 0)]

        for i in range(1, self.T):
            zs.append(self.reparameterization_gaussian_diffusion(zs[-1], i))

        # =====
        # 反向扩散
        # 从最后一个 z 开始，逐步走向 x。
        # 在每一步计算均值和方差。
        mus = []
        log_vars = []

        for i in range(len(self.p_dnns) - 1, -1, -1):
            h = self.p_dnns[i](zs[i+1])
            mu_i, log_var_i = torch.chunk(h, 2, dim=1)
            mus.append(mu_i)
            log_vars.append(log_var_i)

        # 最后一步，输出 x 的均值。
        # 注意，假定最后一个分布是 Normal(x | tanh(NN(z_1)), 1)！
        mu_x = self.decoder_net(zs[0])

        # =====ELBO
        # RE
        # 相当于 -MSE(x, mu_x) + const
        RE = log_standard_normal(x - mu_x).sum(-1)

        # KL：要遍历潜变量的所有层次
        KL = (log_normal_diag(zs[-1], torch.sqrt(1. - self.beta) * zs[-1], torch.log(self.beta)) - log_standard_normal(zs[-1])).sum(-1)

        for i in range(len(mus)):
            KL_i = (log_normal_diag(zs[i], torch.sqrt(1. - self.beta) * zs[i], torch.log(self.beta)) - log_normal_diag(zs[i], mus[i], log_vars[i])).sum(-1)

            KL = KL + KL_i

        # 最终的 ELBO
        if reduction == 'sum':
            loss = -(RE - KL).sum()
        else:
            loss = -(RE - KL).mean()

        return loss

    # 采样沿反向扩散路径，在每一步采样。
    def sample(self, batch_size=64):
        z = torch.randn([batch_size, self.D])
        for i in range(len(self.p_dnns) - 1, -1, -1):
            h = self.p_dnns[i](z)
            mu_i, log_var_i = torch.chunk(h, 2, dim=1)
            z = self.reparameterization(torch.tanh(mu_i), log_var_i)

        mu_x = self.decoder_net(z)

        return mu_x

    # 也可以用前向扩散采样来核对。
    # 结果应近似于白噪声。
    def sample_diffusion(self, x):
        zs = [self.reparameterization_gaussian_diffusion(x, 0)]

        for i in range(1, self.T):
            zs.append(self.reparameterization_gaussian_diffusion(zs[-1], i))

        return zs[-1]
