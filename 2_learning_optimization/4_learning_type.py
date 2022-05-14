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
    total = output.shape[0]

    # _, pred_label = output.max(1)
    # _, tar_label = label.max(1)
    # print (pred_label, tar_label)
    # if output.item() > 0.5:
    #    pred_label = 1
    # else:
    #    pred_label = 0
    # print (output.item(), pred_label)

    pred_label = torch.tensor([1 if x > 0.5 else 0 for x in output.squeeze()])
    label = label.squeeze().cpu()

    num_correct = torch.eq(pred_label, label).sum().data
    # print(num_correct,total,num_correct*10./total)
    return 1.0 * num_correct / total


def train(net, train_data, valid_data, num_epoches, optimizer, criterion):
    if torch.cuda.is_available():
        net = net.cuda()

    prev_time = datetime.now()

    for epoch in range(num_epoches):
        train_loss = 0
        train_acc = 0

        net.train()
        for im, label in train_data:
            if torch.cuda.is_available():
                im = im.cuda()
                label = label.cuda()
            else:
                im = Variable(im)
                label = Variable(label)
            # print("Input: ", im)
            # print("Label: ", label.float())

            optimizer.zero_grad()
            output = net(im)
            # print("Output: ", output)

            loss = criterion(output, label.float())
            loss.backward()
            optimizer.step()
            # print("Loss:   ", loss, loss.data)

            train_loss += loss.item()
            train_acc += get_acc(output, label.long())

        cur_time = datetime.now()
        h, remainder = divmod((cur_time - prev_time).seconds, 3600)
        m, s = divmod(remainder, 60)
        time_str = "Time %02d:%02d:%02d" % (h, m, s)
        if epoch % 50 == 0 and epoch != 0:
            for param_group in optimizer.param_groups:
                param_group['lr'] *= 0.1
                lr = param_group['lr']
            print("adjust lr to " + str(lr))

        if valid_data is not None:
            valid_loss = 0
            valid_acc = 0

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
                loss = criterion(output, label.float())
                valid_loss += loss.item()
                valid_acc += get_acc(output, label.long())
                # print(len(train_data),train_acc,len(valid_data),valid_acc)
                epoch_str = ("Epoch %d. Train Loss: %f, Train Acc: %f, Valid Loss: %f, Valid Acc: %f, " % (
                    epoch, train_loss / len(train_data), train_acc / len(train_data), valid_loss / len(valid_data),
                    valid_acc / len(valid_data)))
        else:
            epoch_str = ("Epoch %d. Train Loss: %f, Train Acc: %f, " % (
                epoch, train_loss / len(train_data), train_acc / len(train_data)))

        prev_time = cur_time
        print(epoch_str + time_str)

    return net


def main():
    train_set = clothes_dataset("train")
    train_loader = DataLoader(train_set, batch_size=16, shuffle=True, num_workers=4)
    test_set = clothes_dataset("test")
    test_loader = DataLoader(test_set, batch_size=16, shuffle=False, num_workers=4)
    print("Train dataset: ", len(train_set))
    print("Test  dataset: ", len(test_set))

    net = net(12, 1)
    optimizer = torch.optim.SGD(net.parameters(), lr=0.0001, momentum=0.9, weight_decay=0.1)
    # criterion = nn.CrossEntropyLoss()
    criterion = nn.BCELoss(reduction='mean')

    # mynet = joblib.load(modelPath)
    net = train(net, train_loader, test_loader, 300, optimizer, criterion)

    joblib.dump(net, modelPath)

    return


if __name__ == '__main__':
    main()
