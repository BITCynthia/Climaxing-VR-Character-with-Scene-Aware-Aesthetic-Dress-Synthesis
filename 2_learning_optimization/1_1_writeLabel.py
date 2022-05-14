import os
import store_grab as sg

imgDir = 'label/images'
figureDir = 'label/figure'
seasonDir = 'label/season'
sceneClassDir = 'label/sceneClass'
eventDir = 'label/event'
colorDir = 'label/colorValue'
clothesDir = 'label/clothes'

outputDir = 'dataset/collect'


def clothWrite(name):
    clothesPath = os.path.join(clothesDir, name + '_x.json')
    clothesJson = sg.grabLabel(clothesPath)
    clothes = clothesJson['labelclothes']
    # print(clothes)
    return clothes


def sceneWrite(name):
    seasonpath = os.path.join(seasonDir, name + '_season.json')
    seasonJson = sg.grabLabel(seasonpath)
    season = seasonJson['season']

    sceneClassPath = os.path.join(sceneClassDir, name + '.json')
    sceneClassJson = sg.grabLabel(sceneClassPath)
    sceneClass = sceneClassJson['label']

    eventPath = os.path.join(eventDir, name + '_event.json')
    eventJson = sg.grabLabel(eventPath)
    event = eventJson['event']

    colorPath = os.path.join(colorDir, name + '.json')
    colorJson = sg.grabLabel(colorPath)
    color = colorJson['colorPalette']

    scene = {'season': season, 'sceneClass': sceneClass, 'event': event, 'color': color}
    # print(scene)

    return scene


def figureWrite(name):
    figurepath = os.path.join(figureDir, name + '_figure.json')
    figureJson = sg.grabLabel(figurepath)
    # print(figureJson)
    figure = figureJson['figure']

    return figure


def retrieveNames():
    nameList = []
    filenameList = os.listdir(imgDir)
    for filename in filenameList:
        # print(filename, filename[0:len(filename) - 4])
        nameList.append(filename[0:len(filename) - 4])
    return nameList


def writeLabel():
    nameList = retrieveNames()

    for name in nameList:
        figure = figureWrite(name)
        scene = sceneWrite(name)
        clothes = clothWrite(name)
        label = {'image_id': name, 'figure': figure, 'scene': scene, 'clothes': clothes, 'rate': 1}
        savepath = os.path.join(outputDir, name + '_info.json')
        sg.storeLabel(label, savepath)

    print("Done!")
    return


if __name__ == '__main__':
    writeLabel()
