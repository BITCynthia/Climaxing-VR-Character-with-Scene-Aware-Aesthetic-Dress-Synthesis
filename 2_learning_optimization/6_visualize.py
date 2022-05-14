import os
import itertools
import numpy as np
import store_grab as sg

np.set_printoptions(threshold=np.inf)

dir = 'output_clothes'
name = ''

Names = ['clothType', 'UpperType', 'UpperLength', 'UpperModel', 'UpperCollar', 'UpperSleeveLength', 'UpperShouders',
         'UpperCuff', 'UpperOpening', 'UpperMaterial', 'UpperPattern', 'TrousersType', 'TrousersWaist',
         'TrousersLength', 'TrousersModel', 'TrousersMaterial', 'TrousersPattern', 'SkirtType', 'SkirtWaist',
         'SkirtLength', 'SkirtFold', 'SkirtMaterial', 'SkirtPattern']
dict = {'clothType': ["上衣", "裤子", "半身裙", "连衣裙", "连体裤"],
        'UpperType': ["运动装", "冲锋衣", "羽绒服", "衬衫", "毛衣", "卫衣", "呢大衣", "皮衣", "夹克衫", "背心", "皮草", "旗袍", "打底", "泳衣", "T恤",
                      "其他"],
        'UpperLength': ["超短", "短", "适中", "中长", "超长"],
        'UpperModel': ["紧身", "收腰", "直筒", "宽松", "其他"],
        'UpperCollar': ["毛领", "Polo领", "小v领", "大V领", "圆领", "翻领", "高领", "连帽领", "无领", "U领", "其他"],
        'UpperSleeveLength': ["无袖", "短袖", "中袖", "七分袖", "长袖", "吊带", "其他"],
        'UpperShouders': ["直筒", "泡泡袖", "无袖", "其他"],
        'UpperCuff': ["收口", "灯笼袖", "其他"],
        'UpperOpening': ["套头", "纽扣", "拉链", "敞开", "其他"],
        'UpperMaterial': ["针织", "皮制", "亚麻", "羊毛", "棉质", "其他"],
        'UpperPattern': ["纯色", "纹理", "图案", "其他"],

        'TrousersType': ["西裤", "牛仔", "休闲裤", "运动裤", "短裤", "丝袜", "喇叭裤", "背带裤", "泳裤", "其他"],
        'TrousersWaist': ["高腰", "正常", "低腰", "无"],
        'TrousersLength': ["短", "及膝", "及小腿", "及踝"],
        'TrousersModel': ["紧身", "直筒", "宽松"],
        'TrousersMaterial': ["雪纺", "皮制", "亚麻", "羊毛", "棉质", "其他"],
        'TrousersPattern': ["纯色", "纹理", "图案", "其他"],

        'SkirtType': ["吊带", "背带", "包臀", "A版", "直筒", "蓬蓬裙", "其他"],
        'SkirtWaist': ["高腰", "正常", "低腰", "无"],
        'SkirtLength': ["短", "及膝", "及小腿", "及踝", "拖地", "其他"],
        'SkirtFold': ["有", "无"],
        'SkirtMaterial': ["雪纺", "皮制", "亚麻", "羊毛", "棉质", "其他"],
        'SkirtPattern': ["纯色", "纹理", "图案", "其他"]}

sceneIDList = ['autumn_art-photo', 'autumn_business3', 'spring_routine_garden', 'spring_trip',
               'summer_party_ceremony', 'summer_sport', 'winter_routine']
figureIDList = ['Daniel_male_blackSkin_blackHair', 'David_male_whiteSkin_YellowHair',
                'Dylan_male_yellowSkin_blackHair',
                'Lily_female_yellowSkin_balckHair', 'Lisa_female_blackSkin_brownHair',
                'Luce_female_whiteSkin_YellowHair',
                'boy']


def visualize():
    sceneNo = 3
    figureNo = 6
    num = 1
    name = sceneIDList[sceneNo] + '_' + figureIDList[figureNo]
    #name = figureIDList[figureNo] + '_' + sceneIDList[sceneNo]
    print("scene: ", sceneIDList[sceneNo])
    print("figure: ", figureIDList[figureNo])

    path = os.path.join(dir, name + '_detail' + str(num) + '.json')
    json = sg.grabLabel(path)
    # results = json['ChromosomeMatrixList']
    # result = results[99]
    results = json['ChromosomeMatrix']

    # print(np.array(results))
    results.sort()
    results = itertools.groupby(results)
    new_results = []
    for k, g in results:
        print(k)
        new_results.append(k)

    kid = 0
    for cloth in new_results:
        kid += 1
        print("------------", kid, "------------")
        for i in range(len(cloth)):
            if cloth[i] == 0:
                if i == 17 and (cloth[0] == 3 or cloth[0] == 4):
                    attIndex = int(cloth[i])
                else:
                    continue
            else:
                attIndex = int(cloth[i]) - 1
            if attIndex >= len(dict[Names[i]]):
                continue
            print(Names[i], " : ", dict[Names[i]][attIndex])

    return


if __name__ == '__main__':
    visualize()
