import os
import fileProcess.store_grab as sg
import labelScene.eventAttr as eventAttr


def save(outputDir, filename):
    label = {'image_id': filename[0:len(filename) - 4], 'event': eventAttr.event['event']}

    Json = filename[0:len(filename) - 4] + "_event.json"
    savepath = os.path.join(outputDir, Json)
    sg.storeLabel(label, savepath)
    return
