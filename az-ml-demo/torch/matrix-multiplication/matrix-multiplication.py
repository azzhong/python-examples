import torch

A = torch.tensor([[1,2],[3,4]])
x = torch.tensor([[1],[2]])
B = torch.matmul(A, x)
print(f'A = {A}')
print(f'x = {x}')
print(f'B = {B}')
