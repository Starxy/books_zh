class TransformerBlock(nn.Module):
    def __init__(self, num_emb, num_neurons, num_heads=4):
        super().__init__()

        # 超参数
        self.D = num_emb
        self.H = num_heads
        self.neurons = num_neurons

        # 各组件
        self.msha = MultiHeadSelfAttention(num_emb=self.D, num_heads=self.H)
        self.layer_norm1 = nn.LayerNorm(self.D)
        self.layer_norm2 = nn.LayerNorm(self.D)

        self.mlp = nn.Sequential(nn.Linear(self.D, self.neurons * self.D),
                                 nn.GELU(),
                                 nn.Linear(self.neurons * self.D, self.D))

    def forward(self, x, causal=True):
        # 多头自注意力
        x_attn = self.msha(x, causal)
        # 层归一化
        x = self.layer_norm1(x_attn + x)
        # MLP
        x_mlp = self.mlp(x)
        # 层归一化
        x = self.layer_norm2(x_mlp + x)

        return x
