import torch

x = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
x_flat = x.view(-1)

print(x, x_flat)

tensor1 = torch.tensor([[1, 2], [3, 4]])
tensor2 = torch.tensor([[5, 6]])

# 在维度0上拼接
concatenated_tensor = torch.cat((tensor1, tensor2), dim=0)
print("Concatenated tensor along dimension 0:")
print(concatenated_tensor)
