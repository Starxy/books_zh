class MoGPrior(nn.Module):
    def __init__(self, L, num_components):
        super(MoGPrior, self).__init__()

        self.L = L
        self.num_components = num_components

        # 参数。
        self.means = nn.Parameter(torch.randn(num_components, self.L)*multiplier)
        self.logvars = nn.Parameter(torch.randn(num_components, self.L))

        # 混合权重。
        self.w = nn.Parameter(torch.zeros(num_components, 1, 1))

    def get_params(self):
        return self.means, self.logvars

    def sample(self, batch_size):
        # 均值和对数方差。
        means, logvars = self.get_params()

        # 混合概率。
        w = F.softmax(self.w, dim=0)
        w = w.squeeze()

        # 选取分量。
        indexes = torch.multinomial(w, batch_size, replacement=True)

        # 均值和对数方差。
        eps = torch.randn(batch_size, self.L)
        for i in range(batch_size):
            indx = indexes[i]
            if i == 0:
                z = means[[indx]] + eps[[i]] * torch.exp(logvars[[indx]])
            else:
                z = torch.cat((z, means[[indx]] + eps[[i]] * torch.exp(logvars[[indx]])), 0)
        return z

    def log_prob(self, z):
        # 均值和对数方差。
        means, logvars = self.get_params()

        # 混合概率。
        w = F.softmax(self.w, dim=0)

        # 高斯混合的对数概率。
        z = z.unsqueeze(0) # 1 x B x L
        means = means.unsqueeze(1) # K x 1 x L
        logvars = logvars.unsqueeze(1) # K x 1 x L

        log_p = log_normal_diag(z, means, logvars) + torch.log(w) # K x B x L
        log_prob = torch.logsumexp(log_p, dim=0, keepdim=False) # B x L

        return log_prob
