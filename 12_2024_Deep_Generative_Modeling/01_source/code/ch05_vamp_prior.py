class VampPrior(nn.Module):
    def __init__(self, L, D, num_vals, encoder, num_components, data=None):
        super(VampPrior, self).__init__()

        self.L = L
        self.D = D
        self.num_vals = num_vals

        self.encoder = encoder

        # 伪输入。
        u = torch.rand(num_components, D) * self.num_vals
        self.u = nn.Parameter(u)

        # 混合权重。
        self.w = nn.Parameter(torch.zeros(self.u.shape[0], 1, 1)) # K x 1 x 1

    def get_params(self):
        # u 经编码器得到均值和对数方差。
        mean_vampprior, logvar_vampprior = self.encoder.encode(self.u) # (K x L), (K x L)
        return mean_vampprior, logvar_vampprior

    def sample(self, batch_size):
        # u 经编码器得到均值和对数方差。
        mean_vampprior, logvar_vampprior = self.get_params()

        # 混合概率。
        w = F.softmax(self.w, dim=0) # K x 1 x 1
        w = w.squeeze()

        # 选取分量。
        indexes = torch.multinomial(w, batch_size, replacement=True)

        # 均值和对数方差。
        eps = torch.randn(batch_size, self.L)
        for i in range(batch_size):
            indx = indexes[i]
            if i == 0:
                z = mean_vampprior[[indx]] + eps[[i]] * torch.exp(logvar_vampprior[[indx]])
            else:
                z = torch.cat((z, mean_vampprior[[indx]] + eps[[i]] * torch.exp(logvar_vampprior[[indx]])), 0)
        return z

    def log_prob(self, z):
        # u 经编码器得到均值和对数方差。
        mean_vampprior, logvar_vampprior = self.get_params() # (K x L) 与 (K x L)

        # 混合概率。
        w = F.softmax(self.w, dim=0) # K x 1 x 1

        # 高斯混合的对数概率。
        z = z.unsqueeze(0) # 1 x B x L
        mean_vampprior = mean_vampprior.unsqueeze(1) # K x 1 x L
        logvar_vampprior = logvar_vampprior.unsqueeze(1) # K x 1 x L

        log_p = log_normal_diag(z, mean_vampprior, logvar_vampprior) + torch.log(w) # K x B x L
        log_prob = torch.logsumexp(log_p, dim=0, keepdim=False) # B x L

        return log_prob
