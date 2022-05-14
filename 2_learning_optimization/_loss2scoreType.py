import sys

sys.path.append("...")

import torch
import joblib
import numpy as np
from torch import nn
from torch.autograd import Variable

modelPath = "model/googlenetType.m"

'''
class googlenet(nn.Module):
    def __init__(self, featureDim, num_class):
        super(googlenet, self).__init__()

        self.fc1 = nn.Linear(featureDim, 256)
        self.fc2 = nn.Linear(256, 128)
        self.fc3 = nn.Linear(128, num_class)
        self.relu = nn.ReLU()
        self.dropout = nn.Dropout()

    def forward(self, x):
        x = x.float()
        x = x.view(x.shape[0], -1)

        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        x = self.relu(x)
        x = self.fc3(x)
        x = torch.sigmoid(x)
        return x
'''


def calcprobability(net, criterion, feature):
    target = torch.from_numpy(np.array([1.0]))

    if torch.cuda.is_available():
        net = net.cuda()
        with torch.no_grad():
            feature = feature.cuda()
            target = target.cuda()
    else:
        with torch.no_grad():
            feature = Variable(feature)
            target = Variable(target)
    net = net.eval()

    output = net(feature)
    loss = criterion(output, target.float())
    # print(output.item(), target.item(), loss.item())
    return output.item()


def rating(chromosomeMatrix_i, figure, scene):
    net = joblib.load(modelPath)
    criterion = nn.BCELoss(reduction='mean')

    feature_temp = np.append(np.append(figure, scene), chromosomeMatrix_i)
    feature = torch.from_numpy(np.array([[[feature_temp]]]))
    score = calcprobability(net, criterion, feature)

    return score


'''
chromosome = [1, 8, 4, 4, 8]
figure = [0, 1, 2, 2]
scene = [4, 46, 4]
score = rating(chromosome, figure, scene)
print(score)
'''
