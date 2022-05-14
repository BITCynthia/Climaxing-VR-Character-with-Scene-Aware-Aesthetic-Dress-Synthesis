import os
import time
import random
import _input as input
import numpy as np
import store_grab as sg
import _loss2scoreType as ls
import torch
from torch import nn

np.set_printoptions(threshold=np.inf)

outputDir = 'output_clothes'

chromosomeLength = 5  # 染色体长度
scope = [0, 5]

chromosomeNum = 100  # 初始化染色体数量
crossoverMutationNum = 20  # 参与交叉变异的染色体数量
cp = 0.8  # 染色体复制的比例(每代中保留适应度较高的染色体直接成为下一代)

iteratorNum = 50  # 代数
adaptability = []  # 适应度矩阵(下标：染色体编号、值：该染色体的适应度)
selectionProbability = []

adaptabilityList = []
selectionProbabilityList = []
ChromosomeMatrixList = []


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


def maxN(chromosomeNum_cp):
    matrix = []
    for i in range(len(adaptability)):
        matrix.append([i, adaptability[i]])

    for i in range(len(matrix) - 1):
        for j in range(i + 1, len(matrix)):
            if matrix[i][1] < matrix[j][1]:
                temp = matrix[j]
                matrix[j] = matrix[i]
                matrix[i] = temp
    # print(np.array(matrix))

    maxIndexArray = []
    for i in range(chromosomeNum_cp):
        maxIndexArray.append(matrix[i][0])

    return maxIndexArray


def copy(chromosomeMatrix, newChromosomeMatrix):
    # 寻找适应度最高的chromosomeNum * cp条染色体
    chromosomeIndexArr = maxN(int(len(chromosomeMatrix) * cp))
    # print(chromosomeIndexArr)

    for index in chromosomeIndexArr:
        # print("这里index常常溢出", index, len(chromosomeMatrix))
        chromosome = chromosomeMatrix[index].copy()
        newChromosomeMatrix.append(chromosome)
    return newChromosomeMatrix.copy()


def mutation(newChromosomeMatrix):
    # 随机选一个染色体
    chromosomeIndex = random.randint(0, len(newChromosomeMatrix) - 1)

    # 选择染色体要变异的位置
    mutateIndex = random.randint(0, chromosomeLength - 1)

    # 变异后的值
    mutateValue = random.randint(scope[0], scope[1])

    # print("这里chromosomeIndex常常溢出", chromosomeIndex, len(newChromosomeMatrix))
    # print("这里mutateIndex    常常溢出", mutateIndex, chromosomeLength)
    newChromosomeMatrix[chromosomeIndex][mutateIndex] = mutateValue

    return newChromosomeMatrix


def RWS():
    sum = 0
    rand = random.random()

    for i in range(len(selectionProbability)):
        sum += selectionProbability[i]
        if sum >= rand:
            return i
    return len(selectionProbability) - 1


def cross(chromosomeMatrix):
    newChromosomeMatrix = []
    for i in range(crossoverMutationNum):
        chromosomeFather = chromosomeMatrix[RWS()]
        chromosomeMother = chromosomeMatrix[RWS()]
        while chromosomeFather[0] != chromosomeMother[0]:
            chromosomeFather = chromosomeMatrix[RWS()]
            chromosomeMother = chromosomeMatrix[RWS()]

        # 选择要染色体交叉的位置
        crossIndex = random.randint(0, chromosomeLength - 1)
        newChromosome = np.append(chromosomeFather[0:crossIndex].copy(),
                                  chromosomeMother[crossIndex:chromosomeLength].copy())
        newChromosomeMatrix.append(newChromosome)
    return newChromosomeMatrix


def createGeneration(chromosomeMatrix):
    newChromosomeMatrix = cross(chromosomeMatrix)
    newChromosomeMatrix = mutation(newChromosomeMatrix.copy())
    newChromosomeMatrix = copy(chromosomeMatrix.copy(), newChromosomeMatrix.copy())
    ChromosomeMatrixList.append(newChromosomeMatrix)
    return newChromosomeMatrix


def calSelectionProbability(chromosomeMatrix):
    sumAdaptability = 0
    for i in range(len(chromosomeMatrix)):
        sumAdaptability += adaptability[i]

    for i in range(len(chromosomeMatrix)):
        selectionProbability.append(adaptability[i] / sumAdaptability)

    selectionProbabilityList.append(selectionProbability)
    return


def calAdaptability(chromosomeMatrix, figure, scene):
    adaptability.clear()
    for chromosomeMatrix_i in chromosomeMatrix:
        fitness = ls.rating(chromosomeMatrix_i, figure, scene)
        adaptability.append(fitness)
    adaptabilityList.append(adaptability)
    return


def initialGeneration():
    chromosomeMatrix = []
    for i in range(chromosomeNum):
        chromosomeMatrix_i = []
        for j in range(chromosomeLength):
            chromosomeMatrix_i.append(random.randint(scope[0], scope[1]))
        chromosomeMatrix.append(chromosomeMatrix_i)
    return chromosomeMatrix


def geneAlgorithm(figure, scene):
    print(" 1.Generating the primary population...")
    chromosomeMatrix = initialGeneration()
    print("  ", len(chromosomeMatrix), "chromosomes: ", chromosomeMatrix)

    print(" 2.Iteratoring...")
    for i in range(iteratorNum):
        # print("  2.1 Calculating fitness of each chromosome of the " + str(i + 1) + "-th generation...")
        calAdaptability(chromosomeMatrix.copy(), figure, scene)
        #print("    ", "fitness: ", adaptability)

        # print("  2.2 Calculating the probability of natural selection...")
        calSelectionProbability(chromosomeMatrix.copy())
        # print("    ", "probability", selectionProbability)

        # print("  2.3 Generating a new generation of chromosomes...")
        chromosomeMatrix = createGeneration(chromosomeMatrix.copy())
        #print("    chromosomes ", chromosomeMatrix)
        # print(chromosomeMatrix)
    return chromosomeMatrix


def optimize():
    sceneIDList = ['autumn_art-photo', 'autumn_business3', 'spring_routine_garden', 'spring_trip',
                   'summer_party_ceremony', 'summer_sport', 'winter_routine']
    figureIDList = ['Daniel_male_blackSkin_blackHair', 'David_male_whiteSkin_YellowHair',
                    'Dylan_male_yellowSkin_blackHair',
                    'Lily_female_yellowSkin_balckHair', 'Lisa_female_blackSkin_brownHair',
                    'Luce_female_whiteSkin_YellowHair',
                    'boy']
    sceneNo = 4
    figureNo = 5

    print("I.Inputting...")
    figure, scene = input.input(sceneIDList[sceneNo], figureIDList[figureNo])

    time_start = time.time()
    print("II.Optimizating...")
    clothSequence = geneAlgorithm(figure, scene)
    time_end = time.time()

    print("III.Outfit:")
    print(np.array(clothSequence))

    print("IV.Saving results...")
    # for optimization
    value = {'figure': figure, 'scene': scene, 'ChromosomeMatrixList': np.array(ChromosomeMatrixList).tolist(),
             'adaptabilityList': adaptabilityList, 'selectionProbabilityList': selectionProbabilityList}
    sg.storeLabel(value, os.path.join(outputDir, '_optimization.json'))
    # for user study
    # value = {'sceneID': sceneIDList[sceneNo], 'figureID': figureIDList[figureNo],
    #         'ChromosomeMatrix': np.array(clothSequence).tolist()}
    # sg.storeLabel(value,
    #              os.path.join(outputDir, sceneIDList[sceneNo] + '_' + figureIDList[figureNo] + '_outfit.json'))

    print('totally cost', time_end - time_start)
    return


if __name__ == '__main__':
    optimize()
