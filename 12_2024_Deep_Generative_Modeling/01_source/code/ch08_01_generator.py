class Generator(nn.Module):
    def __init__(self, generator_net, z_size):
        super(Generator, self).__init__()

        # 初始化生成器神经网络。
        self.generator_net = generator_net
        # 还需要知道潜变量的维数。
        self.z_size = z_size

    def generate(self, z):
        # 对给定的 z 生成样本，只需将其输入神经网络。
        return self.generator_net(z)

    def sample(self, batch_size=16):
        # 采样时先抽取潜变量。
        z = torch.randn(batch_size, self.z_size)
        return self.generate(z)

    def forward(self, z=None):
        if z is None:
            return self.sample()
        else:
            return self.generate(z)
