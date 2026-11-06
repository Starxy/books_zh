class NeuralCompressor(nn.Module):
    def __init__(self, encoder, decoder, entropy_coding, quantizer, beta=1., detaching=False):
        super(NeuralCompressor, self).__init__()

        print('Neural Compressor by JT.')

        # 我们
        self.encoder = encoder
        self.decoder = decoder
        self.entropy_coding = entropy_coding
        self.quantizer = quantizer

        # beta 决定相对于重建质量，我们对压缩的侧重程度。
        self.beta = beta

        # 可以将码率的输入从计算图分离，分别学习码率和失真。
        self.detaching = detaching

    def forward(self, x, reduction='avg'):
        # 编码
        # 未量化的值
        z = self.encoder(x)
        # 量化
        quantizer_out = self.quantizer(z)

        # 解码
        x_rec = self.decoder(quantizer_out[2])

        # 失真（例如 MSE）
        Distortion = torch.mean(torch.pow(x - x_rec, 2), 1)

        # 码率：这里使用熵编码。
        Rate = torch.mean(self.entropy_coding(quantizer_out[0], quantizer_out[2]), 1)

        # 目标
        objective = Distortion + self.beta * Rate

        if reduction == 'sum':
            return objective.sum(), Distortion.sum(), Rate.sum()
        else:
            return objective.mean(), Distortion.mean(), Rate.mean()
