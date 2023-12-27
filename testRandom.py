import torch

# torch.manual_seed(123)

random_int = torch.randint(1, 1001, (1,)).item()

print(random_int)

labels = torch.arange(10, dtype=torch.long, device='cpu')
modified_labels = labels.t().reshape(-1)

print(labels)
print(modified_labels)

distill_data = torch.randn(10, 1, 28, 28, device='cpu', requires_grad=True)
print(distill_data)