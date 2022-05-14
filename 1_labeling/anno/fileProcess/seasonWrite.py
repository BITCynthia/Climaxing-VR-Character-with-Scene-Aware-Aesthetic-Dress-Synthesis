import os
import fileProcess.store_grab as sg
import labelScene.seasonAttr as seasonAttr


def save(outputDir, filename):
    label = {'image_id': filename[0:len(filename) - 4], 'season': seasonAttr.season['season']}

    Json = filename[0:len(filename) - 4] + "_season.json"
    savepath = os.path.join(outputDir, Json)
    sg.storeLabel(label, savepath)
    return
