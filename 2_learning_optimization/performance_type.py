import sys

sys.path.append("...")

import os
import torch
import joblib
import numpy as np
import store_grab as sg
from torch import nn
from datetime import datetime
from torch.autograd import Variable
from torch.utils.data import Dataset, DataLoader

datasetDir = 'dataset'
modelPath = "model/netType.m"


class clothes_dataset(Dataset):
    def __init__(self, path):
        self.sample = []

        DIR = os.path.join(datasetDir, path)
        fileList = os.listdir(DIR)
        for filename in fileList:
            filepath = os.path.join(DIR, filename)
            temp = sg.grabLabel(filepath)

            figureLabel = temp['figure']
            figure = [figureLabel['gender'], figureLabel['age'], figureLabel['height'], figureLabel['shape']]
            sceneLabel = temp['scene']
            scene = [sceneLabel['season'], int(sceneLabel['sceneClass']), sceneLabel['event']]
            label = temp['rate']

            clothesLabel = temp['clothes']
            clothes = []
            for cloth in clothesLabel:
                clothes.append([cloth['clothType']])
            for i in range(5 - len(clothes)):
                clothes.append([0])

            feature_temp = np.append(np.append(figure, scene), clothes)
            # print(len(feature_temp))
            feature = torch.from_numpy(np.array([[[feature_temp]]]))
            label = torch.from_numpy(np.array([label]))

            self.sample.append((feature, label))

    def __len__(self):
        return len(self.sample)

    def __getitem__(self, idx):
        return self.sample[idx]


class net(nn.Module):
    def __init__(self, featureDim, num_class):
        super(net, self).__init__()

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


def get_acc(output, label):
    print("=====================")
    total = output.shape[0]
    label = label.squeeze().cpu()
    P = label.sum().data  # 正样本
    N = total - P  # 负样本

    pred_label = torch.tensor([1 if x > 0.5 else 0 for x in output.squeeze()])

    num_correct = torch.eq(pred_label, label).sum().data  # TP+TN
    F = total - num_correct

    TP = (pred_label & label).sum().data
    FP = P - TP

    TN = num_correct - TP
    FN = N - TN

    print(total)
    print(P, N)
    print(TP, TN, num_correct)
    print(FP, FN, F)

    return 1.0 * num_correct / total, 1.0 * TP / P, 1.0 * TP / (TP + FN)


def test(net, valid_data):
    if torch.cuda.is_available():
        net = net.cuda()

    if valid_data is not None:
        net = net.eval()

        for im, label in valid_data:
            if torch.cuda.is_available():
                with torch.no_grad():
                    im = im.cuda()
                    label = label.cuda()
            else:
                with torch.no_grad():
                    im = Variable(im)
                    label = Variable(label)

            output = net(im)
            # valid_acc += get_acc(output, label.long())
            valid_acc, pre, recall = get_acc(output, label.long())
            print(valid_acc, pre, recall)

    return


def main():
    test_set = clothes_dataset("test")
    test_loader = DataLoader(test_set, batch_size=720, shuffle=False, num_workers=4)
    print("Test  dataset: ", len(test_set))

    mynet = joblib.load(modelPath)
    test(mynet, test_loader)

    return


if __name__ == '__main__':
    main()
