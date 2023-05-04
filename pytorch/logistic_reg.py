# Imports
import torch
import torchvision
from torchvision.datasets import MNIST

dataset = MNIST(root='data/', download=True)
len(dataset)

test_dataset = MNIST(root='data/', train=False)
len(test_dataset)
print(test_dataset[0])
import matplotlib.pyplot as plt
%matplotlib inline

image, label = dataset[0]
plt.imshow(image, cmap='gray')
print('Label:', label)