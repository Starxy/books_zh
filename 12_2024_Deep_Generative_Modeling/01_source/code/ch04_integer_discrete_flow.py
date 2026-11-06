# 整数离散流（IDF）类。
# 实现了两种选项。
# 选项 1：Hoogeboom 等人（2019）的二分耦合层。
# 选项 2：Tomczak（2021）提出的四分耦合层。
# 第二种选项不使用循环，逐步写出，以便看清它的工作方式。
class IDF(nn.Module):
    def __init__(self, netts, num_flows, D=2):
        super(IDF, self).__init__()

        print('IDF by JT.')

        # 选项 1
        if len(netts) == 1:
            self.t = torch.nn.ModuleList([netts[0]() for _ in range(num_flows)])
            self.idf_git = 1

        # 选项 2
        elif len(netts) == 4:
            self.t_a = torch.nn.ModuleList([netts[0]() for _ in range(num_flows)])
            self.t_b = torch.nn.ModuleList([netts[1]() for _ in range(num_flows)])
            self.t_c = torch.nn.ModuleList([netts[2]() for _ in range(num_flows)])
            self.t_d = torch.nn.ModuleList([netts[3]() for _ in range(num_flows)])
            self.idf_git = 4

        else:
            raise ValueError('You can provide either 1 or 4 translation nets.')

        # 流变换（即可逆变换）的次数。
        self.num_flows = num_flows

        # 取整算子
        self.round = RoundStraightThrough.apply

        # 初始化基分布的参数。
        # 这些参数与神经网络的权重一同训练。
        self.mean = nn.Parameter(torch.zeros(1, D)) # 均值
        self.logscale = nn.Parameter(torch.ones(1, D)) # 对数尺度

        # 问题的维数。
        self.D = D

    # 耦合层。
    def coupling(self, x, index, forward=True):

        # 选项 1
        if self.idf_git == 1:
            (xa, xb) = torch.chunk(x, 2, 1)

            if forward:
                yb = xb + self.round(self.t[index](xa))
            else:
                yb = xb - self.round(self.t[index](xa))

            return torch.cat((xa, yb), 1)

        # 选项 2
        elif self.idf_git == 4:
            (xa, xb, xc, xd) = torch.chunk(x, 4, 1)

            if forward:
                ya = xa + self.round(self.t_a[index](torch.cat((xb, xc, xd), 1)))
                yb = xb + self.round(self.t_b[index](torch.cat((ya, xc, xd), 1)))
                yc = xc + self.round(self.t_c[index](torch.cat((ya, yb, xd), 1)))
                yd = xd + self.round(self.t_d[index](torch.cat((ya, yb, yc), 1)))
            else:
                yd = xd - self.round(self.t_d[index](torch.cat((xa, xb, xc), 1)))
                yc = xc - self.round(self.t_c[index](torch.cat((xa, xb, yd), 1)))
                yb = xb - self.round(self.t_b[index](torch.cat((xa, yc, yd), 1)))
                ya = xa - self.round(self.t_a[index](torch.cat((yb, yc, yd), 1)))

            return torch.cat((ya, yb, yc, yd), 1)

    # 与 RealNVP 类似，这里也有置换层。
    def permute(self, x):
        return x.flip(1)

    # IDF 的主要函数，正向计算从 x 到 z。
    def f(self, x):
        z = x
        for i in range(self.num_flows):
            z = self.coupling(z, i, forward=True)
            z = self.permute(z)

        return z

    # 从 z 反求 x。
    def f_inv(self, z):
        x = z
        for i in reversed(range(self.num_flows)):
            x = self.permute(x)
            x = self.coupling(x, i, forward=False)

        return x

    # PyTorch 的 forward 函数，返回对数概率。
    def forward(self, x, reduction='avg'):
        z = self.f(x)
        if reduction == 'sum':
            return -self.log_prior(z).sum()
        else:
            return -self.log_prior(z).mean()

    # 采样函数。
    # 首先从基分布采样。
    # 然后对 z 应用逆变换。
    def sample(self, batchSize, intMax=100):
        # 采样得到 z。
        z = self.prior_sample(batchSize=batchSize, D=self.D, intMax=intMax)
        # x = f^-1(z)
        x = self.f_inv(z)
        return x.view(batchSize, 1, self.D)

    # 计算基分布的对数概率。
    def log_prior(self, x):
        log_p = log_integer_probability(x, self.mean, self.logscale)
        return log_p.sum(1)

    # 从基分布采样得到整数。
    def prior_sample(self, batchSize, D=2):
        # 从逻辑斯蒂分布采样。
        y = torch.rand(batchSize, self.D)
        # 这里利用逻辑斯蒂分布的一个性质。
        # 要从逻辑斯蒂分布采样，先采样 y ~ Uniform[0,1]。
        # 然后计算 log(y / (1.-y))，乘以尺度并加上均值。
        x = torch.exp(self.logscale) * torch.log(y / (1. - y)) + self.mean
        # 最后取整。
        return torch.round(x)
