class HierarchicalVAE(nn.Module):
    def __init__(self, nn_r_1, nn_r_2, nn_delta_1, nn_delta_2, nn_z_1, nn_x, num_vals=256, D=64, L=16, likelihood_type='categorical'):
        super(HierarchicalVAE, self).__init__()

        print('Hierachical VAE by JT.')

        # 自底向上的路径
        self.nn_r_1 = nn_r_1
        self.nn_r_2 = nn_r_2

        self.nn_delta_1 = nn_delta_1
        self.nn_delta_2 = nn_delta_2

        # 自顶向下的路径
        self.nn_z_1 = nn_z_1
        self.nn_x = nn_x


        # 其他参数
        self.D = D # 输入维数

        self.L = L # 第二层潜变量的维数

        self.num_vals = num_vals # 每个像素的取值数

        self.likelihood_type = likelihood_type # 条件似然的类型（类别／伯努利）

    # 如果不记得重参数化技巧，请回顾关于 VAE 的一节。
    def reparameterization(self, mu, log_var):
        std = torch.exp(0.5*log_var)
        eps = torch.randn_like(std)
        return mu + std * eps

    def forward(self, x, reduction='avg'):
        #=====
        # 首先计算自底向上的确定性路径。
        # 为限制方差的调整量，使用 hard-tanh 非线性函数。

        # 自底向上
        # 第 1 步
        r_1 = self.nn_r_1(x)
        r_2 = self.nn_r_2(r_1)

        # 第 2 步
        delta_1 = self.nn_delta_1(r_1)
        delta_mu_1, delta_log_var_1 = torch.chunk(delta_1, 2, dim=1)
        delta_log_var_1 = F.hardtanh(delta_log_var_1, -7., 2.)

        # 第 3 步
        delta_2 = self.nn_delta_2(r_2)
        delta_mu_2, delta_log_var_2 = torch.chunk(delta_2, 2, dim=1)
        delta_log_var_2 = F.hardtanh(delta_log_var_2, -7., 2.)


        # 接着处理自顶向下的路径。

        # 自顶向下
        # 第 4 步
        z_2 = self.reparameterization(delta_mu_2, delta_log_var_2)

        # 第 5 步
        h_1 = self.nn_z_1(z_2)
        mu_1, log_var_1 = torch.chunk(h_1, 2, dim=1)

        # 第 6 步
        z_1 = self.reparameterization(mu_1 + delta_mu_1, log_var_1 + delta_log_var_1)

        # 第 7 步
        h_d = self.nn_x(z_1)

        if self.likelihood_type == 'categorical':
            b = h_d.shape[0]
            d = h_d.shape[1]//self.num_vals
            h_d = h_d.view(b, d, self.num_vals)
            mu_d = torch.softmax(h_d, 2)

        elif self.likelihood_type == 'bernoulli':
            mu_d = torch.sigmoid(h_d)

        #=====ELBO
        # RE
        if self.likelihood_type == 'categorical':
            RE = log_categorical(x, mu_d, num_classes=self.num_vals, reduction='sum', dim=-1).sum(-1)

        elif self.likelihood_type == 'bernoulli':
            RE = log_bernoulli(x, mu_d, reduction='sum', dim=-1)

        # KL
        # Kullback-Leibler 部分需要计算两个散度。
        # 1) KL[q(z_2|z) || p(z_2)]，其中 p(z_2) = N(0,1)
        # 2) KL[q(z_1|z_2, x) || p(z_1|z_2)]
        # 注意，这里用的是两个高斯分布间的 KL 解析式。
        # 若采用其他分布，请改用相应表达式。
        KL_z_2 = 0.5 * (delta_mu_2**2 + torch.exp(delta_log_var_2) - delta_log_var_2 - 1).sum(-1)
        KL_z_1 = 0.5 * (delta_mu_1**2 / torch.exp(log_var_1) + torch.exp(delta_log_var_1) -\
                        delta_log_var_1 - 1).sum(-1)

        KL = KL_z_1 + KL_z_2

        # 最终的 ELBO
        if reduction == 'sum':
            loss = -(RE - KL).sum()
        else:
            loss = -(RE - KL).mean()

        return loss

    # 采样沿自顶向下的路径，无需计算均值和方差的调整量。
    def sample(self, batch_size=64):
        # 第 1 步
        z_2 = torch.randn(batch_size, self.L)
        # 第 2 步
        h_1 = self.nn_z_1(z_2)
        mu_1, log_var_1 = torch.chunk(h_1, 2, dim=1)
        # 第 3 步
        z_1 = self.reparameterization(mu_1, log_var_1)

        # 第 4 步
        h_d = self.nn_x(z_1)

        if self.likelihood_type == 'categorical':
            b = batch_size
            d = h_d.shape[1]//self.num_vals
            h_d = h_d.view(b, d, self.num_vals)
            mu_d = torch.softmax(h_d, 2)
            # 第 5 步
            p = mu_d.view(-1, self.num_vals)
            x_new = torch.multinomial(p, num_samples=1).view(b,d)

        elif self.likelihood_type == 'bernoulli':
            mu_d = torch.sigmoid(h_d)
            # 第 5 步
            x_new = torch.bernoulli(mu_d)
        return x_new
