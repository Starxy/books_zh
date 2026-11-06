class MultiHeadSelfAttention(nn.Module):
    def __init__(self, num_emb, num_heads=8):
        super().__init__()

        # 超参数
        self.D = num_emb
        self.H = num_heads

        # 自注意力权重
        self.w_k = nn.Linear(self.D, self.D * self.H)
        self.w_q = nn.Linear(self.D, self.D * self.H)
        self.w_v = nn.Linear(self.D, self.D * self.H)

        # 合并多个头所用的权重
        self.w_c = nn.Linear(self.D * self.H, self.D)

    def forward(self, x, causal=True):
        # x 的维度：批量大小 B × 词元数 T × 嵌入维数 D
        B, T, D = x.size()

        # 键、查询和值
        k = self.w_k(x).view(B, T, self.H, D) # B x T x H x D
        q = self.w_q(x).view(B, T, self.H, D) # B x T x H x D
        v = self.w_v(x).view(B, T, self.H, D) # B x T x H x D

        k = k.transpose(1, 2).contiguous().view(B * self.H, T, D) # B*H x T x D
        q = q.transpose(1, 2).contiguous().view(B * self.H, T, D) # B*H x T x D
        v = v.transpose(1, 2).contiguous().view(B * self.H, T, D) # B*H x T x D

        k = k / (D**0.25) # 缩放
        q = q / (D**0.25) # 缩放

        # kq
        kq = torch.bmm(q, k.transpose(1, 2)) # B*H x T x T

        # 启用因果掩码时
        if causal:
            mask = torch.triu_indices(T, T, offset=1)
            kq[..., mask[0], mask[1]] = float('-inf')

        # softmax
        skq = F.softmax(kq, dim=2)

        # 自注意力
        sa = torch.bmm(skq, v) # B*H x T x D
        sa = sa.view(B, self.H, T, D) # B x H x T x D
        sa = sa.transpose(1, 2) # B x T x H x D
        sa = sa.contiguous().view(B, T, D * self.H) # B x T x D*H


        out = self.w_c(sa) # B x T x D

        return out
