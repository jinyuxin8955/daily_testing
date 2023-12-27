import torch
from torch.optim.lr_scheduler import StepLR
import torch.nn as nn
import itertools

initial_lr = 0.1

class model(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = nn.Conv2d(in_channels=3, out_channels=3, kernel_size=3)

    def forward(self, x):
        x = self.conv(x)
        return x

net_1 = model()

optimizer_1 = torch.optim.Adam(net_1.parameters(), lr=initial_lr)
scheduler_1 = StepLR(optimizer_1, 3, 0.1)

print(optimizer_1.defaults['lr'])

for epoch in range(10):
    # train
    optimizer_1.zero_grad()
    optimizer_1.step()

    print("%f" % optimizer_1.param_groups[0]['lr'])
    scheduler_1.step()