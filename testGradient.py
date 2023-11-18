import torch
import torch.nn as nn
import torch.optim as optim

# 定义神经网络模型
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc = nn.Linear(10, 1)

    def forward(self, x):
        return self.fc(x)

# 创建模型实例
model = Net()

# 定义损失函数和优化器
criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

# 输入数据
input_data = torch.randn(1, 10)

# 前向传播
output = model(input_data)

# 计算损失
target = torch.randn(1, 1)
loss = criterion(output, target)

# 反向传播
optimizer.zero_grad()
loss.backward()

# 获取梯度
gradients = []
for param in model.parameters():
    gradients.append(param.grad)


# 打印梯度
for grad in gradients:
    print(grad, "====")

print(gradients)

gradients2 = []
for param1, param2 in zip(gradients, gradients):
    param = param1 + param2
    gradients2.append(param)
print(gradients2)

my_list = [1, 2, 3, 4, 5]
print(my_list)
my_list.clear()
print(my_list)  # 输出: []

gr = []
for i in range(10):
    gr.append(gradients)

gd = []
for param in zip(*gr):
    sums = sum(param)
    gd.append(sums)

print(gd)