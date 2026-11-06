class Quantizer(nn.Module):
    def __init__(self, input_dim, codebook_dim, temp=1.e7):
        super(Quantizer, self).__init__()
        # softmax 的温度
        self.temp = temp

        # 输入和码本的维数
        self.input_dim = input_dim
        self.codebook_dim = codebook_dim

        # 码本层（一个码本）
        # 均匀初始化为可学习的参数
        self.codebook = nn.Parameter(torch.FloatTensor(1, self.codebook_dim,).uniform_(-1/self.codebook_dim, 1/self.codebook_dim))

    # 将码本索引（独热表示）转换为码本中的值。
    def indices2codebook(self, indices_onehot):
        return torch.matmul(indices_onehot, self.codebook.t()).squeeze()

    # 将整数转换为独热表示。
    def indices_to_onehot(self, inputs_shape, indices):
        indices_hard = torch.zeros(inputs_shape[0], inputs_shape[1], self.codebook_dim)
        indices_hard.scatter_(2, indices, 1)

    # 前向函数：
    # 先计算输入值和码本值之间的距离。
    # 再计算编码值在码本中的索引，包括可微的软索引和不可微的硬索引。
    # 量化器返回索引和量化后的码（编码器的输出）。
    # 最后解码器将量化后的码映射到观测空间，即对它解码。
    def forward(self, inputs):
        # inputs 是一个 B x M 的浮点数矩阵。
        inputs_shape = inputs.shape
        # 重复输入
        inputs_repeat = inputs.unsqueeze(2).repeat(1, 1, self.codebook_dim)
        # 计算输入值和码本值之间的距离。
        distances = torch.exp(-torch.sqrt(torch.pow(inputs_repeat - self.codebook.unsqueeze(1), 2)))

        # 硬索引，不可微
        indices = torch.argmax(distances, dim=2).unsqueeze(2)
        indices_hard = self.indices_to_onehot(inputs_shape=inputs_shape, indices=indices)

        # 软索引，可微
        indices_soft = torch.softmax(self.temp * distances, -1)

        # 量化值，这里用软索引，以便反向传播。




        quantized = self.indices2codebook(indices_onehot=indices_soft)

        return (indices_soft, indices_hard, quantized)
