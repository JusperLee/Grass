import sklearn
import torch
import torch.nn as nn
from torch.autograd import Variable
import torch.nn.functional as F
import numpy as np
import matplotlib.pyplot as plt
import torch.optim
from sklearn import datasets

iris = datasets.load_iris()
x = iris['data']
x = torch.FloatTensor(x)
x = Variable(x)
print(x)