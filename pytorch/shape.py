import torch
# float
t1 = torch.tensor(4.)
print(t1)
# vector
t2 = torch.tensor([2., 4, 6, 9])
print(t2)
#  matrix
t3 = torch.tensor([[2., 4], [6, 9]])
print(t3)

# 3 dimensional array

t4 = torch.tensor([
    [[3, 4, 4], [3, 6, 7]],
    [[90, 34, 5], [7, 30, 12]]
])
t5 = t4 = torch.tensor([
    [[11, 12, 13],
     [13, 14, 15]],
    [[15, 16, 17],
     [17, 18, 19.]]])
print(t4)
print(t1.shape)
print(t2.shape)
print(t3.shape)
print(t5.shape)
