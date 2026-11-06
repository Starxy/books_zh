class GTMVampPrior(nn.Module):
    def __init__(self, L, D, gtm_net, encoder, num_points, u_min=-10., u_max=10., num_vals=255):
        super(GTMVampPrior, self).__init__()

        self.L = L
        self.D = D
        self.num_vals = num_vals

        self.encoder = encoder

        # 二维流形。
        self.u = torch.zeros(num_points**2, 2) # K**2 x 2
        u1 = torch.linspace(u_min, u_max, steps=num_points)
        u2 = torch.linspace(u_min, u_max, steps=num_points)

        k = 0
        for i in range(num_points):
            for j in range(num_points):
                self.u[k,0] = u1[i]
                self.u[k,1] = u2[j]
                k = k + 1

        # GTM 网络将 u 映射到 x。
        self.gtm_net = gtm_net

        # 混合权重。
        self.w = nn.Parameter(torch.zeros(num_points**2, 1, 1))

    def get_params(self):
        # u 经 gtm_net 映射到 u_x。
        h_gtm = self.gtm_net(self.u) # K x D
        h_gtm = h_gtm * self.num_vals
        # u_x 经编码器得到均值和对数方差。
        mean_vampprior, logvar_vampprior = self.encoder.encode(h_gtm) # (K x L), (K x L)
        return mean_vampprior, logvar_vampprior

    def sample(self, batch_size):
    # u 经编码器得到均值和对数方差。
    mean_vampprior, logvar_vampprior = self.get_params()

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
                z = mean_vampprior[[indx]] + eps[[i]] * torch.exp(logvar_vampprior[[indx]])
            else:
                z = torch.cat((z, mean_vampprior[[indx]] + eps[[i]] * torch.exp(logvar_vampprior[[indx]])), 0)
        return z

    def log_prob(self, z):
        # u 经编码器得到均值和对数方差。
        mean_vampprior, logvar_vampprior = self.get_params()

        # 混合概率。
        w = F.softmax(self.w, dim=0)

        # 高斯混合的对数概率。
        z = z.unsqueeze(0) # 1 x B x L
        mean_vampprior = mean_vampprior.unsqueeze(1) # K x 1 x L
        logvar_vampprior = logvar_vampprior.unsqueeze(1) # K x 1 x L

        log_p = log_normal_diag(z, mean_vampprior, logvar_vampprior) + torch.log(w) # K x B x L
        log_prob = torch.logsumexp(log_p, dim=0, keepdim=False) # B x L

        return log_prob
