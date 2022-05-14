import os
import time
import random
import store_grab as sg

outputDir = 'dataset/generate'


def randomFigure():
    figure = {
        "gender": random.randint(0, 1),
        "age": random.randint(1, 3),
        "height": random.randint(1, 3),
        "shape": random.randint(1, 3),
        "skinColor": random.randint(1, 3),
        "hair": random.randint(1, 4)
    }
    return figure


def randomScene():
    scene = {
        "season": random.randint(1, 4),
        "sceneClass": str(random.randint(0, 70)),
        "event": random.randint(1, 7),
        "color": [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
    }
    return scene


def randomClothes():
    clothes = []
    # 衣服
    clothes.append(
        {
            "clothType": random.randint(1, 16),
            "UpperType": random.randint(1, 16),
            "UpperLength": random.randint(1, 5),
            "UpperModel": random.randint(1, 5),
            "UpperCollar": random.randint(1, 11),
            "UpperSleeveLength": random.randint(1, 7),
            "UpperShouders": random.randint(1, 4),
            "UpperCuff": random.randint(1, 3),
            "UpperOpening": random.randint(1, 5),
            "UpperMaterial": random.randint(1, 6),
            "UpperPattern": random.randint(1, 4),

            "TrousersType": 0,
            "TrousersWaist": 0,
            "TrousersLength": 0,
            "TrousersModel": 0,
            "TrousersMaterial": 0,
            "TrousersPattern": 0,

            "SkirtType": 0,
            "SkirtWaist": 0,
            "SkirtLength": 0,
            "SkirtFold": 0,
            "SkirtMaterial": 0,
            "SkirtPattern": 0
        }
    )

    num = random.randint(1, 2)
    for i in range(num):
        TorS = random.randint(0, 1)
        if TorS == 0:
            clothes.append(
                {
                    "clothType": 0,
                    "UpperType": 0,
                    "UpperLength": 0,
                    "UpperModel": 0,
                    "UpperCollar": 0,
                    "UpperSleeveLength": 0,
                    "UpperShouders": 0,
                    "UpperCuff": 0,
                    "UpperOpening": 0,
                    "UpperMaterial": 0,
                    "UpperPattern": 0,

                    "TrousersType": random.randint(1, 10),
                    "TrousersWaist": random.randint(1, 3),
                    "TrousersLength": random.randint(1, 4),
                    "TrousersModel": random.randint(1, 3),
                    "TrousersMaterial": random.randint(1, 6),
                    "TrousersPattern": random.randint(1, 4),

                    "SkirtType": 0,
                    "SkirtWaist": 0,
                    "SkirtLength": 0,
                    "SkirtFold": 0,
                    "SkirtMaterial": 0,
                    "SkirtPattern": 0
                }
            )
        else:
            clothes.append(
                {
                    "clothType": 0,
                    "UpperType": 0,
                    "UpperLength": 0,
                    "UpperModel": 0,
                    "UpperCollar": 0,
                    "UpperSleeveLength": 0,
                    "UpperShouders": 0,
                    "UpperCuff": 0,
                    "UpperOpening": 0,
                    "UpperMaterial": 0,
                    "UpperPattern": 0,

                    "TrousersType": 0,
                    "TrousersWaist": 0,
                    "TrousersLength": 0,
                    "TrousersModel": 0,
                    "TrousersMaterial": 0,
                    "TrousersPattern": 0,

                    "SkirtType": random.randint(1, 7),
                    "SkirtWaist": random.randint(0, 3),
                    "SkirtLength": random.randint(1, 6),
                    "SkirtFold": random.randint(1, 2),
                    "SkirtMaterial": random.randint(1, 7),
                    "SkirtPattern": random.randint(1, 4)
                }
            )

    return clothes


def randomLabel():
    time_start = time.time()
    for i in range(1200):
        figure = randomFigure()
        scene = randomScene()
        clothes = randomClothes()

        label = {'image_id': i, 'figure': figure, 'scene': scene, 'clothes': clothes, 'rate': 0}
        savepath = os.path.join(outputDir, str(i) + '_info.json')
        sg.storeLabel(label, savepath)
    time_end = time.time()

    print('each cost', (time_end - time_start)/1200)
    print("Done!")
    return


if __name__ == '__main__':
    randomLabel()
