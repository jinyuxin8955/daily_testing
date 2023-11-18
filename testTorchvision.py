import torch
import torchvision.transforms as transforms
import torchvision.datasets as datasets
from PIL import Image
from torch.utils.tensorboard import SummaryWriter

# 读取图像
image = Image.open('image.jpg')

# 定义一些转换    transforms.Compose 创建转换序列
transform = transforms.Compose([
    transforms.Resize((256, 256)),        # 调整图像大小
    transforms.ToTensor()                 # 将图像转换为 PyTorch 张量
])

# 应用转换
transformed_image = transform(image)

print(transformed_image.shape)
print(transformed_image.dtype)

train_dataset = datasets.CIFAR10(root='./data', train=True, transform=transform, download=True )
tests_dataset = datasets.CIFAR10(root='./data', train=False,transform=transform, download=False)

print(len(train_dataset), len(tests_dataset))
sample, label = train_dataset[0]
print(sample, label)
print(tests_dataset[100])

writer = SummaryWriter('LOGS/008log')
for i in range(10):
    img, target = tests_dataset[i]
    writer.add_image('test_set', img, i)
writer.close()

