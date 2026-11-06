# 要让 torch.round（取整算子）可用于反向传播，前向计算时取整，反向传播时则按原输入传递梯度。这就是 STE。
class RoundStraightThrough(torch.autograd.Function):

    def __init__(self):
        super().__init__()

    @staticmethod
    def forward(ctx, input):
        rounded = torch.round(input, out=None)
        return rounded

    @staticmethod
    def backward(ctx, grad_output):
        grad_input = grad_output.clone()
        return grad_input
