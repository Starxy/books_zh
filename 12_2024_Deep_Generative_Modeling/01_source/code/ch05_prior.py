# 这里的先验很简单，是标准高斯分布。
# 原本可以用 PyTorch 内置的分布。这里单独实现，有两个理由。
# （i）要把先验看作 VAE 的一个重要组成部分。
# （ii）我们可以实现可学习的先验，如基于流的先验、VampPrior 或混合分布。
class Prior(nn.Module):
    def __init__(self, L):
        super(Prior, self).__init__()
        self.L = L

    def sample(self, batch_size):
        z = torch.randn((batch_size, self.L))
        return z

    def log_prob(self, z):
        return log_standard_normal(z)
