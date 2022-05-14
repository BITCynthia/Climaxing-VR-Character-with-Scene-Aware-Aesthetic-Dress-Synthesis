import os
import fileProcess.store_grab as sg
import labelclothes.cloth as cloth


def savel(outputDir, filename):
    label = {'image_id': filename[0:len(filename) - 4], 'labelclothes': cloth.clothList}

    Json = filename[0:len(filename) - 4] + "_x.json"
    savepath = os.path.join(outputDir, Json)
    if os.path.exists(savepath):
        Json = Json[0:len(Json) - 4] + "_x" + ".json"
        savepath = os.path.join(outputDir, Json)
    sg.storeLabel(label, savepath)
    return


def saver(outputDir, filename):
    label = {'image_id': filename[0:len(filename) - 4] + '_r', 'labelclothes': cloth.clothList}

    Json = filename[0:len(filename) - 4] + "_r.json"
    savepath = os.path.join(outputDir, Json)
    if os.path.exists(savepath):
        Json = filename[0:len(filename) - 4] + "_r" + "_r" + ".json"
        savepath = os.path.join(outputDir, Json)

    sg.storeLabel(label, savepath)
    return
