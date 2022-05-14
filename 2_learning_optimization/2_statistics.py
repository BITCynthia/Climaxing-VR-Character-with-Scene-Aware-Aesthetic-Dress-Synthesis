import os
import store_grab as sg
from collections import Counter
import matplotlib.pyplot as plt

datasetDir = 'dataset/collect'
statDir = 'output_stat'

No = 0


def random_color():
    global No
    colors = ['aliceblue', 'antiquewhite', 'aqua', 'aquamarine', 'azure', 'bisque', 'black', 'blanchedalmond', 'beige',
              'blue', 'blueviolet', 'brown', 'burlywood', 'cadetblue', 'chartreuse', 'chocolate', 'coral',
              'cornflowerblue', 'cornsilk', 'crimson', 'cyan', 'darkblue', 'darkcyan', 'darkgoldenrod', 'darkgray',
              'darkgreen', 'darkkhaki', 'darkmagenta', 'darkolivegreen', 'darkorange', 'darkorchid', 'darkred',
              'darksalmon', 'darkseagreen', 'darkslateblue', 'darkslategray', 'darkturquoise', 'darkviolet', 'deeppink',
              'deepskyblue', 'dimgray', 'dodgerblue', 'firebrick', 'floralwhite', 'forestgreen', 'fuchsia', 'gainsboro',
              'ghostwhite', 'gold', 'goldenrod', 'gray', 'green', 'greenyellow', 'honeydew', 'hotpink', 'indianred',
              'indigo', 'ivory', 'khaki', 'lavender', 'lavenderblush', 'lawngreen', 'lemonchiffon', 'lightblue',
              'lightcoral', 'lightcyan', 'lightgoldenrodyellow', 'lightgreen', 'lightgray', 'lightpink', 'lightsalmon',
              'lightseagreen', 'lightskyblue', 'lightslategray', 'lightsteelblue', 'lightyellow', 'lime', 'limegreen',
              'linen', 'magenta', 'maroon', 'mediumaquamarine', 'mediumblue', 'mediumorchid', 'mediumpurple',
              'mediumseagreen', 'mediumslateblue', 'mediumspringgreen', 'mediumturquoise', 'mediumvioletred',
              'midnightblue', 'mintcream', 'mistyrose', 'moccasin', 'navajowhite', 'navy', 'oldlace', 'olive',
              'olivedrab', 'orange', 'orangered', 'orchid', 'palegoldenrod', 'palegreen', 'paleturquoise',
              'palevioletred', 'papayawhip', 'peachpuff', 'peru', 'pink', 'plum', 'powderblue', 'purple', 'red',
              'rosybrown', 'royalblue', 'saddlebrown', 'salmon', 'sandybrown', 'seagreen', 'seashell', 'sienna',
              'silver', 'skyblue', 'slateblue', 'slategray', 'snow', 'springgreen', 'steelblue', 'tan', 'teal',
              'thistle', 'tomato', 'turquoise', 'violet', 'wheat', 'white', 'whitesmoke', 'yellow', 'yellowgreen']

    No = (No + 1) % len(colors)
    return colors[No]


def render(str, stat):
    labels = []
    sizes = []
    explode = []
    colors = []
    for item in stat:
        # if item ==0:
        #    continue
        labels.append(item)
        sizes.append(stat[item])
        explode.append(0)
        colors.append(random_color())
    print(str, stat)
    plt.cla()
    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=False, startangle=50)
    plt.axis('equal')
    plt.title(str)
    plt.savefig(os.path.join(statDir, str + ".jpg"))
    # plt.show()
    return


def clothesAnalysis(clothesList):
    clothType = []
    UpperType = []
    UpperLength = []
    UpperModel = []
    UpperCollar = []
    UpperSleeveLength = []
    UpperShouders = []
    UpperCuff = []
    UpperOpening = []
    UpperMaterial = []
    UpperPattern = []
    TrousersType = []
    TrousersWaist = []
    TrousersLength = []
    TrousersModel = []
    TrousersMaterial = []
    TrousersPattern = []
    SkirtType = []
    SkirtWaist = []
    SkirtLength = []
    SkirtFold = []
    SkirtMaterial = []
    SkirtPattern = []
    for clothes in clothesList:
        for cloth in clothes:
            clothType.append(cloth['clothType'])
            UpperType.append(cloth['UpperType'])
            UpperLength.append(cloth['UpperLength'])
            UpperModel.append(cloth['UpperModel'])
            UpperCollar.append(cloth['UpperCollar'])
            UpperSleeveLength.append(cloth['UpperSleeveLength'])
            UpperShouders.append(cloth['UpperShouders'])

            UpperCuff.append(cloth['UpperCuff'])
            UpperOpening.append(cloth['UpperOpening'])
            UpperMaterial.append(cloth['UpperMaterial'])
            UpperPattern.append(cloth['UpperPattern'])

            TrousersType.append(cloth['TrousersType'])
            TrousersWaist.append(cloth['TrousersWaist'])
            TrousersLength.append(cloth['TrousersLength'])
            TrousersModel.append(cloth['TrousersModel'])
            TrousersMaterial.append(cloth['TrousersMaterial'])
            TrousersPattern.append(cloth['TrousersPattern'])

            SkirtType.append(cloth['SkirtType'])
            SkirtWaist.append(cloth['SkirtWaist'])
            SkirtLength.append(cloth['SkirtLength'])
            SkirtFold.append(cloth['SkirtFold'])
            SkirtMaterial.append(cloth['SkirtMaterial'])
            SkirtPattern.append(cloth['SkirtPattern'])

    render("clothType", Counter(clothType))
    render("UpperType", Counter(UpperType))
    render("UpperLength", Counter(UpperLength))
    render("UpperModel", Counter(UpperModel))
    render("UpperCollar", Counter(UpperCollar))
    render("UpperSleeveLength", Counter(UpperSleeveLength))
    render("UpperShouders", Counter(UpperShouders))
    render("UpperCuff", Counter(UpperCuff))
    render("UpperOpening", Counter(UpperOpening))
    render("UpperMaterial", Counter(UpperMaterial))
    render("UpperPattern", Counter(UpperPattern))
    render("TrousersType", Counter(TrousersType))
    render("TrousersWaist", Counter(TrousersWaist))
    render("TrousersLength", Counter(TrousersLength))
    render("TrousersModel", Counter(TrousersModel))
    render("TrousersMaterial", Counter(TrousersMaterial))
    render("TrousersPattern", Counter(TrousersPattern))
    render("SkirtType", Counter(SkirtType))
    render("SkirtWaist", Counter(SkirtWaist))
    render("SkirtLength", Counter(SkirtLength))
    render("SkirtFold", Counter(SkirtFold))
    render("SkirtMaterial", Counter(SkirtMaterial))
    render("SkirtPattern", Counter(SkirtPattern))

    return


def sceneAnalysis(scenes):
    season = []
    sceneClass = []
    event = []
    for scene in scenes:
        season.append(scene['season'])
        sceneClass.append(scene['sceneClass'])
        event.append(scene['event'])

    render("season", Counter(season))
    render("scene class", Counter(sceneClass))
    render("event", Counter(event))
    return


def figureAnalysis(figures):
    gender = []
    age = []
    height = []
    shape = []
    skinColor = []
    hair = []
    for figure in figures:
        gender.append(figure['gender'])
        age.append(figure['age'])
        height.append(figure['height'])
        shape.append(figure['shape'])
        skinColor.append(figure['skinColor'])
        hair.append(figure['hair'])

    render("gender", Counter(gender))
    render("age", Counter(age))
    render("height", Counter(height))
    render("shape", Counter(shape))
    render("skin", Counter(skinColor))
    render("hair", Counter(hair))

    return


def statistics():
    figures = []
    scenes = []
    clothesList = []

    filenameList = os.listdir(datasetDir)
    for filename in filenameList:
        filepath = os.path.join(datasetDir, filename)
        fileJson = sg.grabLabel(filepath)
        # print(fileJson)

        figures.append(fileJson['figure'])
        scenes.append(fileJson['scene'])
        clothesList.append(fileJson['clothes'])

    figureAnalysis(figures)
    sceneAnalysis(scenes)
    clothesAnalysis(clothesList)
    return


if __name__ == '__main__':
    statistics()
