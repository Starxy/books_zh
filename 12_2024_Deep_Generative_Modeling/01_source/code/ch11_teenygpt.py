class teenyGPT(nn.Module):
    def __init__(self, num_tokens, num_token_vals, num_emb, num_neurons, num_heads=2, dropout_prob=0.1, num_blocks=10, device='cpu'):
        super().__init__()

        # 记得总要署上作者的名字，哪怕作者就是你自己 ;)
        print('teenyGPT by JT.')

        # 超参数
        self.device = device
        self.num_tokens = num_tokens
        self.num_token_vals = num_token_vals
        self.num_emb = num_emb
        self.num_blocks = num_blocks

        # 嵌入层
        self.embedding = torch.nn.Embedding(num_token_vals, num_emb)

        # 位置嵌入
        self.positional_embedding = nn.Embedding(num_tokens, num_emb)

        # Transformer 块
        self.transformer_blocks = nn.ModuleList()
        for _ in range(num_blocks):
            self.transformer_blocks.append(TransformerBlock(num_emb=num_emb, num_neurons=num_neurons, num_heads=num_heads))

        # 输出层（logits + softmax）
        self.logits = nn.Sequential(nn.Linear(num_emb, num_token_vals))

        # dropout 层
        self.dropout = nn.Dropout(dropout_prob)

        # 损失函数
        self.loss_fun = LossFun()

    def transformer_forward(self, x, causal=True, temperature=1.0):
        # x：B（批量）x T（词元数）
        # 词元嵌入
        x = self.embedding(x)  # B x T x D
        # 位置嵌入
        pos = torch.arange(0, x.shape[1], dtype=torch.long).unsqueeze(0).to(self.device)
        pos_emb = self.positional_embedding(pos)
        # 对输入嵌入应用 dropout
        x = self.dropout(x + pos_emb)

        # Transformer 块
        for i in range(self.num_blocks):
            x = self.transformer_blocks[i](x)

        # 输出 logits
        out = self.logits(x)

        return F.log_softmax(out/temperature, 2)

    @torch.no_grad()
    def sample(self, batch_size=4, temperature=1.0):
        x_seq = np.asarray([[self.num_token_vals - 1] for i in range(batch_size)])

        # 对后续词元采样
        for i in range(self.num_tokens-1):
            xx = torch.tensor(x_seq, dtype=torch.long, device=self.device)
            # 处理 x 并计算 log_softmax
            x_log_probs = self.transformer_forward(xx, temperature=temperature)
            # 采样第 i 个词元
            x_i_sample = torch.multinomial(torch.exp(x_log_probs[:,i]), 1).to(self.device)
            # 用新样本更新批量
            x_seq = np.concatenate((x_seq, x_i_sample.to('cpu').detach().numpy()), 1)

        return x_seq

    @torch.no_grad()
    def top1_rec(self, x, causal=True):
        x_prob = torch.exp(self.transformer_forward(x, causal=True))[:,:-1,:].contiguous()
        _, x_rec_max = torch.max(x_prob, dim=2)
        return torch.sum(torch.mean((x_rec_max.float() == x[:,1:].float().to(device)).float(), 1).float())

    def forward(self, x, causal=True, temperature=1.0, reduction='mean'):
        # 获取对数概率
        log_prob = self.transformer_forward(x, causal=causal, temperature=temperature)

        return self.loss_fun(log_prob[:,:-1].contiguous(), x[:,1:].contiguous(), reduction=reduction)
