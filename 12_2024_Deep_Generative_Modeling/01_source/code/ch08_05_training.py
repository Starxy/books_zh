# 使用两个优化器。
# optimizer_dis 用于判别器的参数。
# optimizer_gen 用于生成器的参数。
for indx_batch, batch in enumerate(training_loader):

    # 判别器
    # 注意，以 'discriminator' 模式调用模型。
    loss_dis = model.forward(batch, mode='discriminator')

    optimizer_dis.zero_grad()
    optimizer_gen.zero_grad()
    loss_dis.backward(retain_graph=True)
    optimizer_dis.step()

    # 生成器
    # 注意，以 'generator' 模式调用模型。
    loss_gen = model.forward(batch, mode='generator')

    optimizer_dis.zero_grad()
    optimizer_gen.zero_grad()
    loss_gen.backward(retain_graph=True)
    optimizer_gen.step()
