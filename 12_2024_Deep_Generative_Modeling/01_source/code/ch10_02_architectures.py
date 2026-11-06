# 编码器
e_net = nn.Sequential(
            nn.Linear(D, M*2), nn.BatchNorm1d(M*2), nn.ReLU(),
            nn.Linear(M*2, M), nn.BatchNorm1d(M), nn.ReLU(),
            nn.Linear(M, M//2), nn.BatchNorm1d(M//2), nn.ReLU(),
            nn.Linear(M//2, C))

encoder = Encoder(encoder_net=e_net)

# 解码器
d_net = nn.Sequential(
            nn.Linear(C, M//2), nn.BatchNorm1d(M//2), nn.ReLU(),
            nn.Linear(M//2, M), nn.BatchNorm1d(M), nn.ReLU(),
            nn.Linear(M, M*2), nn.BatchNorm1d(M*2), nn.ReLU(),
            nn.Linear(M*2, D))

decoder = Decoder(decoder_net=d_net)
