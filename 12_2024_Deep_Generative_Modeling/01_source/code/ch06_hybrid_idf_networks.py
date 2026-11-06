# 可逆变换的次数
num_flows = 2

# 这里只展示采用选项 1 的 IDF。
nett = lambda: nn.Sequential(nn.Linear(D // 2, M), nn.LeakyReLU(),
                             nn.Linear(M, M), nn.LeakyReLU(),
                             nn.Linear(M, D // 2))
netts = [nett]

# 再定义一个三层分类器。
classnet = nn.Sequential(nn.Linear(D, M), nn.LeakyReLU(),
                         nn.Linear(M, M), nn.LeakyReLU(),
                         nn.Linear(M, K),
                         nn.Softmax(dim=1))

# 初始化 HybridIDF
model = HybridIDF(netts, classnet, num_flows, D=D, alpha=alpha)
