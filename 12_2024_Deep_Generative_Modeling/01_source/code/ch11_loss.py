class LossFun(nn.Module):
    def __init__(self,):
        super().__init__()

        self.loss = nn.NLLLoss(reduction='none')

    def forward(self, y_model, y_true, reduction='sum'):
        # y_model：B（批量）x T（词元数）x V（取值数）
        # y_true：B x T
        B, T, V = y_model.size()

        y_model = y_model.view(B * T, V)
        y_true = y_true.view(B * T,)

        loss_matrix = self.loss(y_model, y_true)  # B * T

        if reduction == 'sum':
            return torch.sum(loss_matrix)
        elif reduction == 'mean':
            loss_matrix = loss_matrix.view(B, T)
            return torch.mean(torch.sum(loss_matrix, 1))
        else:
            raise ValueError('Reduction could be either `sum` or `mean`.')
