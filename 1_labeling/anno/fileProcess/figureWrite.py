import os
import fileProcess.store_grab as sg
import labelFigure.figureAttr as figureAttr


def save(outputDir, filename):
    label = {'image_id': filename[0:len(filename) - 4], 'figure': figureAttr.figureAttributes}

    Json = filename[0:len(filename) - 4] + "_figure.json"
    savepath = os.path.join(outputDir, Json)
    sg.storeLabel(label, savepath)
    return
