class HybridIDF(nn.Module):
    def __init__(self, netts, classnet, num_flows, alpha=1., D=2):
        super(HybridIDF, self).__init__()

        print('HybridIDF by JT.')

        # 这里采用前面讨论的两种选项：耦合层或推广的可逆变换。
        # 这些层构成变换 f。
        # 注意新增的 beta 变量。这是 van den Berg 等人（2020）采用的 Rezero 技巧。
        if len(netts) == 1:
            self.t = torch.nn.ModuleList([netts[0]() for _ in range(num_flows)])
            self.idf_git = 1
            self.beta = nn.Parameter(torch.zeros(len(self.t)))

        elif len(netts) == 4:
            self.t_a = torch.nn.ModuleList([netts[0]() for _ in range(num_flows)])
            self.t_b = torch.nn.ModuleList([netts[1]() for _ in range(num_flows)])
            self.t_c = torch.nn.ModuleList([netts[2]() for _ in range(num_flows)])
            self.t_d = torch.nn.ModuleList([netts[3]() for _ in range(num_flows)])
            self.idf_git = 4
            self.beta = nn.Parameter(torch.zeros(len(self.t_a)))

        else:
            raise ValueError('You can provide either 1 or 4 translation nets.')

        # 接在 z 后的分类网络层。
        self.classnet = classnet

        # 流变换（即 f）的次数。
        self.num_flows = num_flows

        # 取整算子。
        self.round = RoundStraightThrough.apply

        # 基分布 pi 的均值和对数尺度。
        self.mean = nn.Parameter(torch.zeros(1, D))
        self.logscale = nn.Parameter(torch.ones(1, D))

        # 输入的维数。
        self.D = D

        # Python 中使用 "lambda" 会有歧义，所以代码用 alpha 表示前面公式里的 lambda（这下一点也不乱了，对吧？！）。
        self.alpha = alpha

        # 这里用 PyTorch 内置的损失函数作教学演示。也可以用类别分布的对数概率。
        self.nll = nn.NLLLoss(reduction='none') # 输入必须是 log-softmax 的结果！

    # 前面介绍过的耦合层。
    # 注意这里用了 Rezero 技巧！
    def coupling(self, x, index, forward=True):

        if self.idf_git == 1:
            (xa, xb) = torch.chunk(x, 2, 1)

            if forward:
                yb = xb + self.beta[index] * self.round(self.t[index](xa))
            else:
                yb = xb - self.beta[index] * self.round(self.t[index](xa))

            return torch.cat((xa, yb), 1)

        elif self.idf_git == 4:
            (xa, xb, xc, xd) = torch.chunk(x, 4, 1)

            if forward:
                ya = xa + self.beta[index] * self.round(self.t_a[index](torch.cat((xb, xc, xd), 1)))
                yb = xb + self.beta[index] * self.round(self.t_b[index](torch.cat((ya, xc, xd), 1)))
                yc = xc + self.beta[index] * self.round(self.t_c[index](torch.cat((ya, yb, xd), 1)))
                yd = xd + self.beta[index] * self.round(self.t_d[index](torch.cat((ya, yb, yc), 1)))
            else:
                yd = xd - self.beta[index] * self.round(self.t_d[index](torch.cat((xa, xb, xc), 1)))
                yc = xc - self.beta[index] * self.round(self.t_c[index](torch.cat((xa, xb, yd), 1)))
                yb = xb - self.beta[index] * self.round(self.t_b[index](torch.cat((xa, yc, yd), 1)))
                ya = xa - self.beta[index] * self.round(self.t_a[index](torch.cat((yb, yc, yd), 1)))

            return torch.cat((ya, yb, yc, yd), 1)

    # 置换层。
    def permute(self, x):
        return x.flip(1)

    # 流变换的正向计算……
    def f(self, x):
        z = x
        for i in range(self.num_flows):
            z = self.coupling(z, i, forward=True)
            z = self.permute(z)

        return z
    # ……以及逆向计算。
    def f_inv(self, z):
        x = z
        for i in reversed(range(self.num_flows)):
            x = self.permute(x)
            x = self.coupling(x, i, forward=False)

        return x

    # 新增的分类函数。先预测各项概率，再选择概率最高的类别。
    def classify(self, x):
        z = self.f(x)
        y_pred = self.classnet(z) # 输出各类别的概率，即 softmax 的结果。
        return torch.argmax(y_pred, dim=1)

    # 计算分类损失的辅助函数。分类损失为 p(y|x) 的负对数似然。
    # 注意先应用可逆变换 f。
    def class_loss(self, x, y):
        z = self.f(x)
        y_pred = self.classnet(z) # 输出各类别的概率，即 softmax 的结果。
        return self.nll(torch.log(y_pred), y)

    def sample(self, batchSize):
        # 采样得到 z。
        z = self.prior_sample(batchSize=batchSize, D=self.D)
        # x = f^-1(z)
        x = self.f_inv(z)
        return x.view(batchSize, 1, self.D)

    # 基分布（即先验）的对数概率。
    def log_prior(self, x):
        log_p = log_integer_probability(x, self.mean, self.logscale)
        return log_p.sum(1)

    # 从基分布采样。
    def prior_sample(self, batchSize, D=2):
        # 从逻辑斯蒂分布采样。
        y = torch.rand(batchSize, self.D)
        x = torch.exp(self.logscale) * torch.log(y / (1. - y)) + self.mean
        # 再取整。
        return torch.round(x)

    # 前向计算。现在用的是混合模型的目标函数！
    def forward(self, x, y, reduction='avg'):
        z = self.f(x)
        y_pred = self.classnet(z) # 输出各类别的概率，即 softmax 的结果。

        idf_loss = -self.log_prior(z)
        class_loss = self.nll(torch.log(y_pred), y) # 记得对 softmax 的输出取对数！

        if reduction == 'sum':
            return (class_loss + self.alpha * idf_loss).sum()
        else:
            return (class_loss + self.alpha * idf_loss).mean()
