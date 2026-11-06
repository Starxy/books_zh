class RealNVP(nn.Module):
    def __init__(self, nets, nett, num_flows, prior, D=2, dequantization=True):
        super(RealNVP, self).__init__()

        # 好吧，给自己宣传一下总没坏处。
        print('RealNVP by JT.')

        # 离散数据需要去量化。此属性用于训练时对整数数据去量化。
        self.dequantization = dequantization

        # 先验对象（这里用 torch.distribution 的多元正态分布）。
        self.prior = prior
        # 平移网络的模块列表
        self.t = torch.nn.ModuleList([nett() for _ in range(num_flows)])
        # 缩放网络的模块列表
        self.s = torch.nn.ModuleList([nets() for _ in range(num_flows)])
        # 变换次数，公式中记作 K。
        self.num_flows = num_flows

        # 输入的维数，用于采样。
        self.D = D

    # 耦合层是 RealNVP 模型的核心。
    def coupling(self, x, index, forward=True):
        # x 是输入。第一次变换接收图像，以后接收上一次变换的输出。
        # index 指定变换的索引。
        # forward 指定从 x 到 y（forward=True）还是从 y 到 x（forward=False）。

        # 把输入分成两部分 x_a、x_b。
        (xa, xb) = torch.chunk(x, 2, 1)

        # 计算 s(xa)，暂时先不取 exp！
        s = self.s[index](xa)
        # 计算 t(xa)。
        t = self.t[index](xa)

        # 计算正向过程（x -> z）或逆向过程（z -> x）。
        # 注意这里用到了 exp！
        if forward:
            # yb = f^{-1}(x)
            yb = (xb - t) * torch.exp(-s)
        else:
            # xb = f(y)
            yb = torch.exp(s) * xb + t

        # 返回输出 y = [ya, yb]，同时返回 s 以计算雅可比行列式的对数。
        return torch.cat((xa, yb), 1), s

    # 置换层的一种实现
    def permute(self, x):
        # 只需把顺序反转。
        return x.flip(1)

    def f(self, x):
        # 计算通过各耦合层和置换层的完整正向过程。
        # 初始化雅可比行列式的对数。
        log_det_J, z = x.new_zeros(x.shape[0]), x
        # 遍历所有层。
        for i in range(self.num_flows):
            # 先做耦合，
            z, s = self.coupling(z, i, forward=True)
            # 再做置换。
            z = self.permute(z)
            # 把每个变换的雅可比行列式的对数相加，得到整串变换的结果。
            # 因此，只需累加各层的贡献。
            log_det_J = log_det_J - s.sum(dim=1)
        # 同时返回 z 和雅可比行列式的对数，因为还要用 z 计算正态分布的对数密度。
        return z, log_det_J

    def f_inv(self, z):
        # 逆向过程，从 z 到 x。
        # 按相反顺序应用所有变换。
        x = z
        for i in reversed(range(self.num_flows)):
            x = self.permute(x)
            x, _ = self.coupling(x, i, forward=False)
        # 这个函数用于采样，只需返回 x。
        return x

    def forward(self, x, reduction='avg'):
        # 这是 PyTorch 所需的函数。
        # 先进行从 x 到 z 的正向计算，同时得到雅可比行列式的对数。
        z, log_det_J = self.f(x)
        # 输出可以取和或平均。
        # 两种情况都计算学习目标 self.prior.log_prob(z) + log_det_J。
        # 留意负号！默认求解的是最小化问题，
        # 但这里想要最大似然估计。因此利用下式。
        # max F(x) <=> min -F(x)
        if reduction == 'sum':
            return -(self.prior.log_prob(z) + log_det_J).sum()
        else:
            return -(self.prior.log_prob(z) + log_det_J).mean()

    def sample(self, batchSize):
        # 首先从先验采样，z ~ p(z) = Normal(z|0,1)。
        z = self.prior.sample((batchSize, self.D))
        z = z[:, 0, :]
        # 接着从 z 变换到 x。
        x = self.f_inv(z)
        return x.view(-1, self.D)
