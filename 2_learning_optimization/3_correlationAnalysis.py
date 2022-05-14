import os
import numpy as np
import pandas as pd
import seaborn as sns
import store_grab as sg
import matplotlib.pyplot as plt

pd.set_option('display.width', 1000)
pd.set_option('display.max_columns', None)

datasetDir = 'dataset/collect'
figPath = 'model/correlation.png'
correlationPath = 'model/correlation.txt'

Names = ['clothType', 'UpperType', 'UpperLength', 'UpperModel', 'UpperCollar', 'UpperSleeveLength', 'UpperShouders',
         'UpperCuff', 'UpperOpening', 'UpperMaterial', 'UpperPattern', 'TrousersType', 'TrousersWaist',
         'TrousersLength', 'TrousersModel', 'TrousersMaterial', 'TrousersPattern', 'SkirtType', 'SkirtWaist',
         'SkirtLength', 'SkirtFold', 'SkirtMaterial', 'SkirtPattern']


def save(cor1):
    f = open(correlationPath, 'a')
    f.write(str(cor1))
    f.write("\n")
    f.close()
    return


def dataLoad():
    clothesList = []
    filenameList = os.listdir(datasetDir)
    for filename in filenameList:
        filepath = os.path.join(datasetDir, filename)
        fileJson = sg.grabLabel(filepath)
        clothesList.append(fileJson['clothes'])

    clothAttr = []
    clothArray = []
    for clothes in clothesList:
        for cloth in clothes:
            clothAttr.clear()
            clothAttr.append(cloth['clothType'])
            clothAttr.append(cloth['UpperType'])
            clothAttr.append(cloth['UpperLength'])
            clothAttr.append(cloth['UpperModel'])
            clothAttr.append(cloth['UpperCollar'])
            clothAttr.append(cloth['UpperSleeveLength'])
            clothAttr.append(cloth['UpperShouders'])

            clothAttr.append(cloth['UpperCuff'])
            clothAttr.append(cloth['UpperOpening'])
            clothAttr.append(cloth['UpperMaterial'])
            clothAttr.append(cloth['UpperPattern'])

            clothAttr.append(cloth['TrousersType'])
            clothAttr.append(cloth['TrousersWaist'])
            clothAttr.append(cloth['TrousersLength'])
            clothAttr.append(cloth['TrousersModel'])
            clothAttr.append(cloth['TrousersMaterial'])
            clothAttr.append(cloth['TrousersPattern'])

            clothAttr.append(cloth['SkirtType'])
            clothAttr.append(cloth['SkirtWaist'])
            clothAttr.append(cloth['SkirtLength'])
            clothAttr.append(cloth['SkirtFold'])
            clothAttr.append(cloth['SkirtMaterial'])
            clothAttr.append(cloth['SkirtPattern'])
            # print(clothAttr)
            clothArray.append(clothAttr.copy())
    # print(clothArray)
    clothArray = np.array(clothArray)
    return clothArray


def correlationAnalysis():
    print("Loading data...")
    dataset = dataLoad()

    print("Creating dictionary...")
    data_dict = {}
    for i in range(len(Names)):
        data_dict[Names[i]] = dataset[:, i]

    print("Analysis correlation...")
    unstrtf_df = pd.DataFrame(data_dict)
    cor1 = unstrtf_df.corr()
    # print(cor1)

    print("Rendering...")
    plt.figure(figsize=(10, 10))
    sns.heatmap(cor1, annot=False, center=0, vmax=1, vmin=-1, square=True, linewidths=.5, yticklabels=True,
                cmap="Blues")
    plt.savefig(figPath)
    plt.show()

    print("Saving correlation...")
    save(cor1)

    return


if __name__ == '__main__':
    correlationAnalysis()
