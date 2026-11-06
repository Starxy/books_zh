# 编码器是一个神经网络，接收图像并输出相应的码。
class Encoder(nn.Module):
    def __init__(self, encoder_net):
        super(Encoder, self).__init__()

        self.encoder = encoder_net

    def encode(self, x):
        h_e = self.encoder(x)
        return h_e

    def forward(self, x):
        return self.encode(x)

# 解码器是一个神经网络，接收量化后的码并返回图像。
class Decoder(nn.Module):
    def __init__(self, decoder_net):
        super(Decoder, self).__init__()

        self.decoder = decoder_net

    def decode(self, z):
        h_d = self.decoder(z)
        return h_d

    def forward(self, z, x=None):
        x_rec = self.decode(z)
        return x_rec
