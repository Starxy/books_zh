class Decoder(nn.Module):
    def __init__(self, decoder_net, distribution='categorical', num_vals=None):
        super(Decoder, self).__init__()

        # 解码器网络。
        self.decoder = decoder_net
        # 解码器所用的分布，默认用前面讨论的类别分布。
        self.distribution = distribution
        # 可能的取值数。类别分布需要这个量。
        self.num_vals=num_vals

    # 这个函数计算似然函数 p(x|z) 的参数。
    def decode(self, z):
        # 先应用解码器网络。
        h_d = self.decoder(z)

        # 这个例子只用类别分布……
        if self.distribution == 'categorical':
            # 记录形状，即批大小
            b = h_d.shape[0]
            # 以及 x 的维数。
            d = h_d.shape[1]//self.num_vals
            # 然后重排为（批大小，维数，取值数）。
            h_d = h_d.view(b, d, self.num_vals)
            # 用 softmax 得到概率。
            mu_d = torch.softmax(h_d, 2)
            return [mu_d]
        # ……不过我们也给出了伯努利分布。够贴心吧？
        elif self.distribution == 'bernoulli':
            # 对于伯努利分布，x_d 取 0 或 1，只需输出一个概率，
            # 因为 p(x_d=1|z) = \theta 且 p(x_d=0|z) = 1 - \theta。
            mu_d = torch.sigmoid(h_d)
            return [mu_d]

        else:
            raise ValueError('Only: ‘categorical‘, ‘bernoulli‘')

    # 这个函数实现从解码器采样。
    def sample(self, z):
        outs = self.decode(z)

        if self.distribution == 'categorical':
            # 取出解码器输出
            mu_d = outs[0]
            # 并记录形状，重排时会用到。
            b = mu_d.shape[0]
            m = mu_d.shape[1]
            # 重排形状。
            mu_d = mu_d.view(mu_d.shape[0], -1, self.num_vals)
            p = mu_d.view(-1, self.num_vals)
            # 最后用 PyTorch 内置函数从类别分布采样。
            x_new = torch.multinomial(p, num_samples=1).view(b,m)

        elif self.distribution == 'bernoulli':
            # 对伯努利分布，无需重排。
            mu_d = outs[0]
            # 可以直接用 PyTorch 内置的采样函数。
            x_new = torch.bernoulli(mu_d)

        else:
            raise ValueError('Only: ‘categorical‘, ‘bernoulli‘')

        return x_new

    # 这个函数计算条件对数似然。
    def log_prob(self, x, z):
        outs = self.decode(z)

        if self.distribution == 'categorical':
            mu_d = outs[0]
            log_p = log_categorical(x, mu_d, num_classes=self.num_vals, reduction='sum', dim=-1).sum(-1)

        elif self.distribution == 'bernoulli':
            mu_d = outs[0]
            log_p = log_bernoulli(x, mu_d, reduction='sum', dim=-1)

        else:
            raise ValueError('Only: ‘categorical‘, ‘bernoulli‘')

        return log_p

    # 前向传播可以计算对数概率或采样。
    def forward(self, z, x=None, type='log_prob'):
        assert type in ['decoder', 'log_prob'], 'Type could be either decode or log_prob'
        if type == 'log_prob':
            return self.log_prob(x, z)
        else:
            return self.sample(z)
