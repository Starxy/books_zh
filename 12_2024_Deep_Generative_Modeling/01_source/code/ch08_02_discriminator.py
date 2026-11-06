class Discriminator(nn.Module):
    def __init__(self, discriminator_net):
        super(Discriminator, self).__init__()
        # 初始化判别器神经网络。
        self.discriminator_net = discriminator_net

    def forward(self, x):
        # 前向传播只需调用神经网络。
        return self.discriminator_net(x)
