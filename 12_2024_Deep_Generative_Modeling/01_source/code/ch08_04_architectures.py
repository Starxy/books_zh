# 先初始化生成器和判别器。
# 生成器
generator_net = nn.Sequential(nn.Linear(L, M), nn.ReLU(),
                              nn.Linear(M, D), nn.Tanh())

generator = Generator(generator_net, z_size=L)

# 判别器
discriminator_net = nn.Sequential(nn.Linear(D, M), nn.ReLU(),
                                  nn.Linear(M, 1), nn.Sigmoid())

discriminator = Discriminator(discriminator_net)

# 最后初始化完整模型。
model = GAN(generator=generator, discriminator=discriminator)
