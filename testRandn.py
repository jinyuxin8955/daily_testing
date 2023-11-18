import torch
import numpy as np

# 生成一个大小为(3, 4)的随机张量
random_tensor = torch.randn(3, 4)

print(random_tensor)

mean = 2.0  # 均值
std = 0.5  # 方差

random_tensor = torch.normal(mean, std, size=(3, 4))

print(random_tensor)

noise_levels = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
nl = noise_level = np.random.choice(noise_levels)
print(nl)