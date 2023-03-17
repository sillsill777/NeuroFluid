import torch
from torch.utils.data import Dataset, DataLoader
from torchvision import datasets
import matplotlib.pyplot as plt
from torchvision.transforms import ToTensor

train_data=datasets.FashionMNIST(root='./tmp_data',train=True,download=True,transform=ToTensor())
labels_map = {
    0: "T-Shirt",
    1: "Trouser",
    2: "Pullover",
    3: "Dress",
    4: "Coat",
    5: "Sandal",
    6: "Shirt",
    7: "Sneaker",
    8: "Bag",
    9: "Ankle Boot",
}

dataload=DataLoader(train_data,batch_size=128,shuffle=True)
a=list(iter(dataload))
print(a[0][0].shape,a[0][1].shape)
print(a[-1][0].shape,a[-1][1].shape)

print(len(dataload))
