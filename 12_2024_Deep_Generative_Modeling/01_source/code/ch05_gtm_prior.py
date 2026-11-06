class GTMPrior(nn.Module):
    def __init__(self, L, gtm_net, num_components, u_min=-1., u_max=1.):
        super(GTMPrior, self).__init__()

        self.L = L

        # 二维流形。
        self.u = torch.zeros(num_components**2, 2) # K**2 x 2
        u1 = torch.linspace(u_min, u_max, steps=num_components)
        u2 = torch.linspace(u_min, u_max, steps=num_components)

        k = 0
        for i in range(num_components):
            for j in range(num_components):
                self.u[k,0] = u1[i]
                self.u[k,1] = u2[j]
                k = k + 1

        # GTM 网络将 u 映射到 z。
        self.gtm_net = gtm_net

        # 混合权重。
        self.w = nn.Parameter(torch.zeros(num_components**2, 1, 1))

    def get_params(self):
        # 从 u 到 z。
        h_gtm = self.gtm_net(self.u) # K**2 x 2L
        mean_gtm, logvar_gtm = torch.chunk(h_gtm, 2, dim=1) # K**2 x L 与 K**2 x L
        return mean_gtm, logvar_gtm

    def sample(self, batch_size):
        # 从 u 到 z。
        mean_gtm, logvar_gtm = self.get_params()

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
                z = mean_gtm[[indx]] + eps[[i]] * torch.exp(logvar_gtm[[indx]])
            else:
                z = torch.cat((z, mean_gtm[[indx]] + eps[[i]] * torch.exp(logvar_gtm[[indx]])), 0)
        return z

    def log_prob(self, z):
        # 从 u 到 z。
        mean_gtm, logvar_gtm = self.get_params()

        # 高斯混合的对数概率。
        z = z.unsqueeze(0) # 1 x B x L
        mean_gtm = mean_gtm.unsqueeze(1) # K**2 x 1 x L
        logvar_gtm = logvar_gtm.unsqueeze(1) # K**2 x 1 x L

        w = F.softmax(self.w, dim=0)

        log_p = log_normal_diag(z, mean_gtm, logvar_gtm) + torch.log(w) # K**2 x B x L
        log_prob = torch.logsumexp(log_p, dim=0, keepdim=False) # B x L

        return log_prob
