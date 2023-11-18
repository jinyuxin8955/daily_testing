from torchvision import datasets, transforms
import torch
from torch.utils.data import DataLoader, Subset

mnist_trainset = datasets.MNIST('../data', train=True, download=True,
                                transform=transforms.Compose([
                                    transforms.ToTensor(),
                                    transforms.Normalize((0.5,), (0.5,))
                                ]))

totalLen = len(mnist_trainset)

class Person:
    def __init__(self):
        self.data = []

persons = [Person() for _ in range(10)]

print(totalLen)

client_num = 10

subset_size = totalLen // client_num
for i in range(client_num):
    start_idx = i * subset_size
    end_idx = (i + 1) * subset_size
    indices = list(range(start_idx, end_idx))
    subset = torch.utils.data.Subset(mnist_trainset, indices)
    persons[i].data = DataLoader(subset, batch_size=64, shuffle=True)

print(persons[9].data)

