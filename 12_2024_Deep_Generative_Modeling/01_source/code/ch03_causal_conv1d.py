class CausalConv1d(nn.Module):
    def __init__(self, in_channels, out_channels, kernel_size, dilation, A=False, **kwargs):
        super(CausalConv1d, self).__init__()

        # 基本思路是使用 PyTorch 内置的 Conv1D。要选择合适的填充，以保证卷积是因果的。最后去掉输出末尾不需要的元素！CausalConv1D 仍是卷积，所以必须指定卷积核大小、膨胀率，以及采用 A 型（A=True）还是 B 型（A=False）。调整膨胀率可以扩大记忆范围。

        # 属性
        self.kernel_size = kernel_size
        self.dilation = dilation
        self.A = A # 选择 A 型（A=True）或 B 型（A=False）
        self.padding = (kernel_size - 1) * dilation + A * 1

        # 在前向计算中自行填充！
        self.conv1d = torch.nn.Conv1d(in_channels, out_channels,
                                     kernel_size, stride=1,
                                     padding=0,
                                     dilation=dilation,**kwargs)

    def forward(self, x):
        # 只在左侧填充！这种实现更高效。
        x = torch.nn.functional.pad(x, (self.padding, 0))
        conv1d_out = self.conv1d(x)
        if self.A:
            # 记住，不能依赖当前分量，因此去掉最后一个元素。
            return conv1d_out[:, :, : -1]
        else:
            return conv1d_out
