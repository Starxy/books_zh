class EBM(nn.Module):
    def __init__(self, energy_net, alpha, sigma, ld_steps, D):
        super(EBM, self).__init__()

        print('EBM by JT.')

        # EBM 使用的神经网络
        self.energy_net = energy_net

        # 分类损失
        self.nll = nn.NLLLoss(reduction='none')  # 需要输入 log-softmax！

        # 超参数
        self.D = D

        self.sigma = sigma

        self.alpha = torch.FloatTensor([alpha])

        self.ld_steps = ld_steps

    def classify(self, x):
        f_xy = self.energy_net(x)
        y_pred = torch.softmax(f_xy, 1)
        return torch.argmax(y_pred, dim=1)

    def class_loss(self, f_xy, y):
        # 计算分类用的 logits
        y_pred = torch.softmax(f_xy, 1)

        return self.nll(torch.log(y_pred), y)

    def gen_loss(self, x, f_xy):
        # 用朗之万动力学采样
        x_sample = self.sample(x=None, batch_size=x.shape[0])

        # 计算 f(x_sample)[y]
        f_x_sample_y = self.energy_net(x_sample)

        return -(torch.logsumexp(f_xy, 1) - torch.logsumexp(f_x_sample_y, 1))

    def forward(self, x, y, reduction='avg'):
        # =====
        # 在网络中前向计算
        # 计算 f(x)[y]
        f_xy = self.energy_net(x)

        # =====
        # 判别部分
        # 计算判别损失，即交叉熵
        L_clf = self.class_loss(f_xy, y)

        # =====
        # 生成部分
        # 计算生成损失 E(x) - E(x_sample)
        L_gen = self.gen_loss(x, f_xy)

        # =====
        # 最终目标
        if reduction == 'sum':
            loss = (L_clf + L_gen).sum()
        else:
            loss = (L_clf + L_gen).mean()

        return loss

    def energy_gradient(self, x):
        self.energy_net.eval()

        # 复制原始数据，此时不要求梯度
        x_i = torch.FloatTensor(x.data)
        x_i.requires_grad = True  # 必须设置，否则自动微分不起作用

        # 计算梯度
        x_i_grad = torch.autograd.grad(torch.logsumexp(self.energy_net(x_i), 1).sum(), [x_i], retain_graph=True)[0]

        self.energy_net.train()

        return x_i_grad

    def langevin_dynamics_step(self, x_old, alpha):
        # 计算关于 x_old 的梯度
        grad_energy = self.energy_gradient(x_old)
        # 采样 eta ~ Normal(0, alpha)
        epsilon = torch.randn_like(grad_energy) * self.sigma

        # 新样本
        x_new = x_old + alpha * grad_energy + epsilon

        return x_new

    def sample(self, batch_size=64, x=None):
        # 1）从均匀分布采样
        x_sample = 2. * torch.rand([batch_size, self.D]) - 1.

        # 2）运行朗之万动力学
        for i in range(self.ld_steps):
            x_sample = self.langevin_dynamics_step(x_sample, alpha=self.alpha)

        return x_sample
