class ARM(nn.Module):
    def __init__(self, net, D=2, num_vals=256):
        super(ARM, self).__init__()

        # 记得注明作者，即使作者就是你 ;)
        print('ARM by JT.')

        # 这里定义网络，见下一段代码。
        self.net = net
        # 每个像素的可能取值数。
        self.num_vals = num_vals
        # 问题的维数，也就是像素数。
        self.D = D

    # 此函数计算 ARM 的输出。
    def f(self, x):
        # 先做因果卷积。
        h = self.net(x.unsqueeze(1))
        # 通道维是取值数，因此调整维度顺序。
        h = h.permute(0, 2, 1)
        # 用 softmax 计算各项概率。
        p = torch.softmax(h, 2)
        return p

    # 前向计算给出图像的对数概率。
    def forward(self, x, reduction='avg'):
        if reduction == 'avg':
            return -(self.log_prob(x).mean())
        elif reduction == 'sum':
            return -(self.log_prob(x).sum())
        else:
            raise ValueError('reduction could be either `avg` or `sum`.')

    # 此函数计算类别分布的对数概率。
    # 详情见单独文件中的完整代码。
    def log_prob(self, x):
        mu_d = self.f(x)
        log_p = log_categorical(x, mu_d, num_classes=self.num_vals, reduction='sum', dim=-1).sum(-1)

        return log_p

    # 此函数实现采样过程。
    def sample(self, batch_size):
        # 首先用零初始化一个张量。
        x_new = torch.zeros((batch_size, self.D))

        # 然后逐个像素采样。
        for d in range(self.D):
            p = self.f(x_new)
            x_new_d = torch.multinomial(p[:, d, :], num_samples=1)
            x_new[:, d] = x_new_d[:,0]

        return x_new
