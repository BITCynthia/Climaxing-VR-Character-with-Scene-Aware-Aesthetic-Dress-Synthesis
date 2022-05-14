import os
import store_grab as sg

figureDir = 'input/figures/figures'
scenesDir = 'input/scenes'


def input(scenename, figurename):
    figurePath = os.path.join(figureDir, figurename + '_figure.json')
    figureJson = sg.grabLabel(figurePath)
    figureLabel = figureJson['figure']
    figure = [figureLabel['gender'], figureLabel['age'], figureLabel['height'], figureLabel['shape']]

    seasonPath = os.path.join(os.path.join(scenesDir, 'season'), scenename + '_season.json')
    seasonJson = sg.grabLabel(seasonPath)
    season = seasonJson['season']
    sceneclassPath = os.path.join(os.path.join(scenesDir, 'sceneClass'), scenename + '.json')
    sceneclassJson = sg.grabLabel(sceneclassPath)
    sceneclass = sceneclassJson['label']
    eventPath = os.path.join(os.path.join(scenesDir, 'event'), scenename + '_event.json')
    eventJson = sg.grabLabel(eventPath)
    event = eventJson['event']
    scene = [season, int(sceneclass), event]
    return figure, scene


if __name__ == '__main__':
    sceneIDList = ['autumn_art-photo', 'autumn_business3', 'spring_routine_garden', 'spring_trip',
                   'summer_party_ceremony', 'summer_sport', 'winter_routine']
    figureIDList = ['Daniel_male_blackSkin_blackHair', 'David_male_whiteSkin_YellowHair',
                    'Dylan_male_yellowSkin_blackHair',
                    'Lily_female_yellowSkin_balckHair', 'Lisa_female_blackSkin_brownHair',
                    'Luce_female_whiteSkin_YellowHair',
                    'boy']
    sceneNo = 1
    figureNo = 1

    figure, scene = input(sceneIDList[sceneNo], figureIDList[figureNo])

    print(figure, scene)
