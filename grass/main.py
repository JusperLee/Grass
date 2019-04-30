import sklearn
import torch
import torch.nn as nn
from torch.autograd import Variable
import torch.nn.functional as F
import numpy as np
import matplotlib.pyplot as plt
import torch.optim
import loading
from pylab import mpl
from sklearn.metrics import accuracy_score

x,y = loading.load_data('train.csv')
x1,y1=loading.load_data('test.csv')
x = torch.FloatTensor(x)
y = torch.LongTensor(y)
x = Variable(x)
y = Variable(y)

x1 = torch.FloatTensor(x1)
y1 = torch.LongTensor(y1)
x1 = Variable(x1)
y1 = Variable(y1)
class Net(nn.Module):
    def __init__(self,n_feature,n_hidden,n_out):
        super(Net,self).__init__()
        self.hidden = nn.Linear(n_feature,n_hidden)
        self.out = nn.Linear(n_hidden,n_out)

    def forward(self, x):
        x = F.sigmoid(self.hidden(x))
        x = self.out(x)
        out = F.log_softmax(x,dim=1)
        return out


net = Net(n_feature=5,n_hidden=10,n_out=5)

optimizer = torch.optim.SGD(net.parameters(),lr=0.03)
epochs = 10000

px=[]
py=[]
for i in range(epochs):
    predict = net(x)
    predict1 = np.argmax(net(x1).data.numpy(),axis=1)
    loss = F.nll_loss(predict,y)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    print(i,"loss:%.5f"%loss.data.item())
    print(i,"acc:%.5f"%accuracy_score(y1, predict1))
    px.append(i)
    py.append(loss.data.item())
    if i==epochs-1:
        plt.cla
        plt.title("Loss curve of the training process")
        plt.xlabel("Iterations")
        plt.ylabel("Loss")
        plt.plot(px,py,"r-",lw=1)
        plt.text(0,0,"Loss = %.4f" % loss.data.item(),fontdict={"size":20,'color':'red'})
        plt.savefig("result.png")
        plt.show()
torch.save(net,"result.pkl")