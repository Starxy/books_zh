# 可逆变换的次数
num_flows = 8

# 这个变量决定采用哪一种方案。
# 选项 1（取 1）：Hoogeboom 等人（2019）提出的经典耦合层。
# 选项 2（取 4）：Tomczak（2021）提出的通用可逆变换，分成四部分。
idf_git = 1

if idf_git == 1:
    nett = lambda: nn.Sequential(
                        nn.Linear(D//2, M), nn.LeakyReLU(),
                        nn.Linear(M, M), nn.LeakyReLU(),
                        nn.Linear(M, D//2))
    netts = [nett]

elif idf_git == 4:
    nett_a = lambda: nn.Sequential(
                        nn.Linear(3 * (D//4), M), nn.LeakyReLU(),
                        nn.Linear(M, M), nn.LeakyReLU(),
                        nn.Linear(M, D//4))

    nett_b = lambda: nn.Sequential(
                        nn.Linear(3 * (D//4), M), nn.LeakyReLU(),
                        nn.Linear(M, M), nn.LeakyReLU(),
                        nn.Linear(M, D//4))

    nett_c = lambda: nn.Sequential(
                        nn.Linear(3 * (D//4), M), nn.LeakyReLU(),
                        nn.Linear(M, M), nn.LeakyReLU(),
                        nn.Linear(M, D//4))

    nett_d = lambda: nn.Sequential(
                        nn.Linear(3 * (D//4), M), nn.LeakyReLU(),
                        nn.Linear(M, M), nn.LeakyReLU(),
                        nn.Linear(M, D//4))

    netts = [nett_a, nett_b, nett_c, nett_d]

# 初始化 IDF
model = IDF(netts, num_flows, D=D)
# 打印模型摘要（类似 Keras）。
print(summary(model, torch.zeros(1, 64), show_input=False, show_hierarchical=False))
