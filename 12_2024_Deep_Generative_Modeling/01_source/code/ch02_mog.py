class MoG(nn.Module):
    def __init__(self, D, K, uniform=False):
        super(MoG, self).__init__()

        print('MoG by JT.')

        # 超参数
        self.uniform = uniform
        self.D = D  # 输入的维数
        self.K = K  # 分量数

        # 参数
        self.mu = nn.Parameter(torch.randn(1, self.K, self.D) * 0.25 + 0.5)
        self.log_var = nn.Parameter(-3. * torch.ones(1, self.K, self.D))

        if self.uniform:
            self.w = torch.zeros(1, self.K)
            self.w.requires_grad = False
        else:
            self.w = nn.Parameter(torch.zeros(1, self.K))

        # 其他
        self.PI = torch.from_numpy(np.asarray(np.pi))

    def log_diag_normal(self, x, mu, log_var, reduction='sum', dim=1):
        log_p = -0.5 * torch.log(2. * self.PI) - 0.5 * log_var - 0.5 * torch.exp(-log_var) * (x.unsqueeze(1) - mu)**2.
        return log_p

    def forward(self, x, reduction='mean'):
        # 计算各分量
        log_pi = torch.log(F.softmax(self.w, 1))  # B x K，softmax 将 R^K 映射到 [0,1]^K，且 sum(pi) = 1
        log_N = torch.sum(self.log_diag_normal(x, self.mu, self.log_var), 2)  # B x K，K 个分量的对角高斯对数密度

        # =====损失：负对数似然
        NLL_loss = -torch.logsumexp(log_pi + log_N, 1)  # B

        # 最终损失
        if reduction == 'sum':
            return NLL_loss.sum()
        elif reduction == 'mean':
            return NLL_loss.mean()
        else:
            raise ValueError('Either `sum` or `mean`.')

    def sample(self, batch_size=64):
        # 初始化空张量
        x_sample = torch.empty(batch_size, self.D)

        # 对分量采样
        pi = F.softmax(self.w, 1)  # B x K，softmax 将 R^K 映射到 [0,1]^K，且 sum(pi) = 1

        indices = torch.multinomial(pi, batch_size, replacement=True).squeeze()

        for n in range(batch_size):
            indx = indices[n]  # 选取第 n 个分量
            x_sample[n] = self.mu[0,indx] + torch.exp(0.5*self.log_var[0,indx]) * torch.randn(self.D)

        return x_sample

    def log_prob(self, x, reduction='mean'):
        with torch.no_grad():
            # 计算各分量
            log_pi = torch.log(F.softmax(self.w, 1))  # B x K，softmax 将 R^K 映射到 [0,1]^K，且 sum(pi) = 1
            log_N = torch.sum(self.log_diag_normal(x, self.mu, self.log_var), 2)  # B x K，K 个分量的对角高斯对数密度

            # 对数概率
            log_prob = torch.logsumexp(log_pi + log_N, 1)  # B

            if reduction == 'sum':
                return log_prob.sum()
            elif reduction == 'mean':
                return log_prob.mean()
            else:
                raise ValueError('Either `sum` or `mean`.')
