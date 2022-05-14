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
#from torch.utils.data import Dataset, DataLoader

from sklearn import svm

datasetDir = 'dataset'
modelPath = "model/googlenet.m"


def clothes_dataset(path):
    DIR = os.path.join(datasetDir, path)
    fileList = os.listdir(DIR)

    featureList=[]
    labelList=[]

    for filename in fileList:
        filepath = os.path.join(DIR, filename)
        temp = sg.grabLabel(filepath)

        figureLabel = temp['figure']
        figure = [figureLabel['gender'], figureLabel['age'], figureLabel['height'], figureLabel['shape']]
        sceneLabel = temp['scene']
        scene = [sceneLabel['season'], int(sceneLabel['sceneClass']), sceneLabel['event']]
        label = temp['rate']

        clothesLabel = temp['clothes']
        for cloth in clothesLabel:
            clothes = [cloth['clothType'], cloth['UpperType'], cloth['UpperLength'], cloth['UpperModel'],
                       cloth['UpperCollar'], cloth['UpperSleeveLength'], cloth['UpperShouders'], cloth['UpperCuff'],
                       cloth['UpperOpening'], cloth['UpperMaterial'], cloth['UpperPattern'], cloth['TrousersType'],
                       cloth['TrousersWaist'], cloth['TrousersLength'], cloth['TrousersModel'],
                       cloth['TrousersMaterial'], cloth['TrousersPattern'], cloth['SkirtType'],
                       cloth['SkirtWaist'], cloth['SkirtLength'], cloth['SkirtFold'], cloth['SkirtMaterial'],
                       cloth['SkirtPattern']]

        feature_temp = np.append(np.append(figure, scene), clothes)
        featureList.append(feature_temp)
        labelList.append(label)

    return featureList, labelList

def main():
    train_X,train_Y = clothes_dataset("train")
    test_X,test_Y = clothes_dataset("test")

    model = svm.SVC(kernel='rbf', C=0.5, gamma=10,decision_function_shape='ovr')
    model.fit(train_X, train_Y)

    #y_hat = model.predict(train_X)
    print (model.score(train_X, train_Y))

    #y_hat = model.predict(test_X)
    print (model.score(test_X, test_Y))


    return


if __name__ == '__main__':
    main()
