import torch
from torchvision import datasets, transforms

# 假设你有一个名为 tensor 的形状为 [10, 1, 28, 28] 的张量
tensor = torch.rand(10, 1, 28, 28)

# 定义归一化的转换
normalize = transforms.Normalize(mean=[0.5], std=[0.5])

# 创建转换器，组合归一化和转换为张量的操作
transform = transforms.Compose([
    transforms.ToTensor(),
    normalize
])

# 将 tensor 转换为可用于处理的 Tensor 数据集
dataset = torch.utils.data.TensorDataset(tensor)

# 对数据集应用转换
dataset.transform = transform

# 创建一个 DataLoader，如果需要
data_loader = torch.utils.data.DataLoader(dataset, batch_size=1, shuffle=False)

# 创建一个示例 MNIST 风格的数据集
mnist_style_dataset = []

# 遍历处理后的数据集，构建 MNIST 风格数据
for i, (data,) in enumerate(data_loader):
    mnist_style_dataset.append((data.squeeze(), torch.tensor([i])))  # 假设标签为索引 i

# 保存数据集
torch.save(mnist_style_dataset, 'mnist_style_dataset.pth')

loaded_dataset = torch.load('mnist_style_dataset.pth')
print(loaded_dataset)

# 创建 DataLoader
data_loader = torch.utils.data.DataLoader(loaded_dataset, batch_size=10, shuffle=False)

# 示例的前向传播
for images, label in data_loader:
    # 假设模型是一个可直接进行前向传播的示例模型
    # outputs = model(images)
    # 在这里你可以使用输出进行后续处理或分析
    # 例如，打印输出结果等
    print(images)
