class FlowMatching(nn.Module):
    def __init__(self, vnet, sigma, D, T, stochastic_euler=False, prob_path="icfm"):
        super(FlowMatching, self).__init__()

        print('Flow Matching by JT.')

        self.vnet = vnet
        self.time_embedding = nn.Sequential(nn.Linear(1, D), nn.Tanh())

        # 其他参数
        self.D = D
        self.T = T
        self.sigma = sigma
        self.stochastic_euler = stochastic_euler

        assert prob_path in ["icfm", "fm"], f"Error: The probability path could be either Independent CFM (icfm) or Lipman's Flow Matching (fm) but {prob_path} was provided."
        self.prob_path = prob_path

        self.PI = torch.from_numpy(np.asarray(np.pi))

    def log_p_base(self, x, reduction='sum', dim=1):
        log_p = -0.5 * torch.log(2. * self.PI) - 0.5 * x**2.
        if reduction == 'mean':
            return torch.mean(log_p, dim)
        elif reduction == 'sum':
            return torch.sum(log_p, dim)
        else:
            return log_p

    def sample_base(self, x_1):
        # 高斯基分布
        if self.prob_path == "icfm":
            return torch.randn_like(x_1)
        elif self.prob_path == "fm":
            return torch.randn_like(x_1)
        else:
            return None

    def sample_p_t(self, x_0, x_1, t):
        if self.prob_path == "icfm":
            mu_t = (1. - t) * x_0 + t * x_1
            sigma_t = self.sigma
        elif self.prob_path == "fm":
            mu_t = t * x_1
            sigma_t = t * self.sigma - t + 1.

        x = mu_t + sigma_t * torch.randn_like(x_1)

        return x

    def conditional_vector_field(self, x, x_0, x_1, t):
        if self.prob_path == "icfm":
            u_t = x_1 - x_0
        elif self.prob_path == "fm":
            u_t = (x_1 - (1. - self.sigma) * x) / (1. - (1. - self.sigma) * t)

        return u_t

    def forward(self, x_1, reduction='mean'):
        # =====流匹配
        # =====
        # z ~ q(z)，例如 q(z) = q(x_0) q(x_1)，q(x_0) 为基分布，q(x_1) 为经验分布
        # t ~ Uniform(0, 1)
        x_0 = self.sample_base(x_1)  # 从基分布采样（例如 Normal(0,I)）
        t = torch.rand(size=(x_1.shape[0], 1))

        # =====
        # 从 p(x|z) 采样
        x = self.sample_p_t(x_0, x_1, t)  # 采样独立随机变量

        # =====
        # 反推插值，即计算向量场 v(x, t)
        t_embd = self.time_embedding(t)
        v = self.vnet(x + t_embd)

        # =====
        # 条件向量场
        u_t = self.conditional_vector_field(x, x_0, x_1, t)

        # =====损失：流匹配
        FM_loss = torch.pow(v - u_t, 2).mean(-1)

        # 最终损失
        if reduction == 'sum':
            loss = FM_loss.sum()
        else:
            loss = FM_loss.mean()

        return loss

    def sample(self, batch_size=64):
        # 欧拉法
        # 先采样 x_0
        x_t = self.sample_base(torch.empty(batch_size, self.D))

        # 然后逐步推进到 x_1（数据）
        ts = torch.linspace(0., 1., self.T)
        delta_t = ts[1] - ts[0]

        for t in ts[1:]:
            t_embedding = self.time_embedding(torch.Tensor([t]))
            x_t = x_t + self.vnet(x_t + t_embedding) * delta_t
            # 随机欧拉法
            if self.stochastic_euler:
                x_t = x_t + torch.randn_like(x_t) * delta_t

        x_final = torch.tanh(x_t)
        return x_final

    def log_prob(self, x_1, reduction='mean'):
        # 反向欧拉法（见 Lipman 论文的附录 C）
        ts = torch.linspace(1., 0., self.T)
        delta_t = ts[1] - ts[0]

        for t in ts:
            if t == 1.:
                x_t = x_1 * 1.
                f_t = 0.
            else:

                t_embedding = self.time_embedding(torch.Tensor([t]))
                x_t = x_t - self.vnet(x_t + t_embedding) * delta_t

                # 计算 f_t
                # 用 Hutchinson 迹估计量和自动求导近似散度
                self.vnet.eval()  # 将向量场网络设为评估模式

                x = torch.FloatTensor(x_t.data)  # 复制原始数据（无需求梯度）
                x.requires_grad = True
                e = torch.randn_like(x)  # epsilon ~ Normal(0, I)
                e_grad = torch.autograd.grad(self.vnet(x).sum(), x, create_graph=True)[0]
                e_grad_e = e_grad * e
                f_t = e_grad_e.view(x.shape[0], -1).sum(dim=1)

                self.vnet.eval()  # 将向量场网络切回训练模式

        log_p_1 = self.log_p_base(x_t, reduction='sum') - f_t

        if reduction == "mean":
            return log_p_1.mean()
        elif reduction == "sum":
            return log_p_1.sum()
