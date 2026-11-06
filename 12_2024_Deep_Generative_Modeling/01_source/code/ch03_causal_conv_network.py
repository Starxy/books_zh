# 网络示例。注意，第一层设置 A=True，其余层都设置 A=False。
# 到这里我们应该已经知道为什么了 :)
M = 256

net = nn.Sequential(
    CausalConv1d(in_channels=1, out_channels=MM, dilation=1, kernel_size=kernel, A=True, bias=True),
    nn.LeakyReLU(),
    CausalConv1d(in_channels=MM, out_channels=MM, dilation=1, kernel_size=kernel, A=False, bias=True),
    nn.LeakyReLU(),
    CausalConv1d(in_channels=MM, out_channels=MM, dilation=1, kernel_size=kernel, A=False, bias=True),
    nn.LeakyReLU(),
    CausalConv1d(in_channels=MM, out_channels=num_vals, dilation=1, kernel_size=kernel, A=False, bias=True))
