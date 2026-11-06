class GAN(nn.Module):
    def __init__(self, generator, discriminator, EPS=1.e-5):
        super(GAN, self).__init__()

        print('GAN by JT.')

        # 将生成器和判别器组合起来。
        # 注意，二者都是类的实例！
        self.generator = generator
        self.discriminator = discriminator

        # 为避免数值问题，引入一个很小的 epsilon。
        self.EPS = EPS

    def forward(self, x_real, reduction='avg', mode='discriminator'):
        # 前向传播计算对抗损失。
        # 具体来说，计算生成器部分
        # 或判别器部分。
        if mode == 'generator':
            # 对生成器，先采样生成数据。
            x_fake_gen = self.generator.sample(x_real.shape[0])

            # 然后计算判别器对生成数据的输出。
            # 注意，这里截断输出，以便后续计算在数值上保持稳定。
            d_fake = torch.clamp(self.discriminator(x_fake_gen), self.EPS, 1. - self.EPS)

            # 生成器的损失是 log(1 - D(G(z)))。
            loss = torch.log(1. - d_fake)

        elif mode == 'discriminator':
            # 对判别器，先采样生成数据。
            x_fake_gen = self.generator.sample(x_real.shape[0])

            # 然后计算判别器对生成数据的输出。
            # 注意，截断输出可避免后续的数值问题。
            d_fake = torch.clamp(self.discriminator(x_fake_gen), self.EPS, 1. - self.EPS)

            # 再计算判别器对真实数据的输出。
            # 注意，为了数值稳定性，这里同样截断输出。
            d_real = torch.clamp(self.discriminator(x_real), self.EPS, 1. - self.EPS)

            # 判别器的最终损失是 log(1 - D(G(z))) + log D(x)。
            # 注意，最大化判别器的对抗损失
            # 等价于取负号后再最小化。
            loss = -(torch.log(d_real) + torch.log(1. - d_fake))

        if reduction == 'sum':
            return loss.sum()
        else:
            return loss.mean()

    def sample(self, batch_size=64):
        return self.generator.sample(batch_size=batch_size)
