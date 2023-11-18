import torch
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

data = torch.randn(100, 10)
target = torch.randint(0, 2, (100,))
model = torch.nn.Linear(10, 2)

print(data)
print(target)
print(model)

train_data = DataLoader(
    datasets.MNIST('../data', train=True, download=True,
                   transform=transforms.Compose([
                       transforms.ToTensor(),
                       transforms.Normalize((0.1,), (0.3,))
                   ])),
    batch_size=64, shuffle=True
)

for dt, tgt in train_data:
    dt.send()
    print(dt.shape, tgt.shape)