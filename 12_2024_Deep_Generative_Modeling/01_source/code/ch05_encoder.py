class Encoder(nn.Module):
    def __init__(self, encoder_net):
        super(Encoder, self).__init__()

        # 初始化编码器网络。
        self.encoder = encoder_net

    # 高斯分布的重参数化技巧。
    @staticmethod
    def reparameterization(mu, log_var):
        # 使用下面的公式。
        # z = mu + std * epsilon
        # epsilon ~ Normal(0,1)

        # 先从对数方差求标准差。
        std = torch.exp(0.5*log_var)

        # 再从 Normal(0,1) 采样 epsilon。
        eps = torch.randn_like(std)

        # 返回最终结果。
        return mu + std * eps

    # 这个函数返回编码器网络的输出，即高斯分布的参数。
    def encode(self, x):
        # 先算出编码器网络的输出，大小为 2M。
        h_e = self.encoder(x)
        # 再把输出拆成均值和对数方差。
        mu_e, log_var_e = torch.chunk(h_e, 2, dim=1)
        return mu_e, log_var_e

    # 采样过程。
    def sample(self, x=None, mu_e=None, log_var_e=None):
        # 若未提供均值和对数方差，须先求出这两个量。
        if (mu_e is None) and (log_var_e is None):
            mu_e, log_var_e = self.encode(x)
        # 或直接求最终样本。
        else:
            # 此时可以直接应用重参数化技巧。
            if (mu_e is None) or (log_var_e is None):
                raise ValueError('mu and log-var can‘t be None!')
        z = self.reparameterization(mu_e, log_var_e)
        return z

    # 这个函数计算稍后求 ELBO 时要用到的对数概率。
    def log_prob(self, x=None, mu_e=None, log_var_e=None, z=None):
        # 如果只提供 x，就可以算出相应的样本。
        if x is not None:
            mu_e, log_var_e = self.encode(x)
            z = self.sample(mu_e=mu_e, log_var_e=log_var_e)
        else:
            # 否则应提供均值、对数方差和 z。
            if (mu_e is None) or (log_var_e is None) or (z is None):
                raise ValueError('mu, log-var, z can‘t be None')

        return log_normal_diag(z, mu_e, log_var_e)

    # PyTorch 前向传播可以计算对数概率（默认）或采样。
    def forward(self, x, type='log_prob'):
        assert type in ['encode', 'log_prob'], 'Type could be either encode or log_prob'
        if type == 'log_prob':
            return self.log_prob(x)
        else:
            return self.sample(x)
