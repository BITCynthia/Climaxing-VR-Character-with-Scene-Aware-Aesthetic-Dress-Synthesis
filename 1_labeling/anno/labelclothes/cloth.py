import copy

clothAttributesNames = ['clothType',
                        'UpperType', 'UpperLength', 'UpperModel', 'UpperCollar', 'UpperSleeveLength', 'UpperShouders',
                        'UpperSleeve', 'UpperCuff', 'UpperOpening', 'UpperMaterial', 'UpperPattern',
                        'TrousersType', 'TrousersWaist', 'TrousersLength', 'TrousersModel', 'TrousersMaterial',
                        'TrousersPattern',
                        'SkirtType', 'SkirtWaist', 'SkirtLength', 'SkirtFold', 'SkirtMaterial',
                        'SkirtPattern']

clothAttributes = {'clothType': 0,

                   'UpperType': 0, 'UpperLength': 0, 'UpperModel': 0, 'UpperCollar': 0, 'UpperSleeveLength': 0,
                   'UpperShouders': 0, 'UpperSleeve': 0, 'UpperCuff': 0, 'UpperOpening': 0, 'UpperMaterial': 0,
                   'UpperPattern': 0,

                   'TrousersType': 0, 'TrousersWaist': 0, 'TrousersLength': 0, 'TrousersModel': 0,
                   'TrousersMaterial': 0,
                   'TrousersPattern': 0,

                   'SkirtType': 0, 'SkirtWaist': 0, 'SkirtLength': 0, 'SkirtFold': 0, 'SkirtMaterial': 0,
                   'SkirtPattern': 0}

clothList = []


def clothType(x):
    clothAttributes['clothType'] = x
    return


def UpperType(x):
    clothAttributes['UpperType'] = x
    return


def UpperLength(x):
    clothAttributes['UpperLength'] = x
    return


def UpperModel(x):
    clothAttributes['UpperModel'] = x
    return


def UpperCollar(x):
    clothAttributes['UpperCollar'] = x
    return


def UpperSleeveLength(x):
    clothAttributes['UpperSleeveLength'] = x
    return


def UpperShouders(x):
    clothAttributes['UpperShouders'] = x
    return


def UpperCuff(x):
    clothAttributes['UpperCuff'] = x
    return


def UpperOpening(x):
    clothAttributes['UpperOpening'] = x
    return


def UpperMaterial(x):
    clothAttributes['UpperMaterial'] = x
    return


def UpperPattern(x):
    clothAttributes['UpperPattern'] = x
    return


def TrousersType(x):
    clothAttributes['TrousersType'] = x
    return


def TrousersWaist(x):
    clothAttributes['TrousersWaist'] = x
    return


def TrousersLength(x):
    clothAttributes['TrousersLength'] = x
    return


def TrousersModel(x):
    clothAttributes['TrousersModel'] = x
    return


def TrousersMaterial(x):
    clothAttributes['TrousersMaterial'] = x
    return


def TrousersPattern(x):
    clothAttributes['TrousersPattern'] = x
    return


def SkirtType(x):
    clothAttributes['SkirtType'] = x
    return


def SkirtWaist(x):
    clothAttributes['SkirtWaist'] = x
    return


def SkirtLength(x):
    clothAttributes['SkirtLength'] = x
    return


def SkirtFold(x):
    clothAttributes['SkirtFold'] = x
    return


def SkirtMaterial(x):
    clothAttributes['SkirtMaterial'] = x
    return


def SkirtPattern(x):
    clothAttributes['SkirtPattern'] = x
    return


def NewCloth():
    clothList.append(copy.deepcopy(clothAttributes))
    for name in clothAttributesNames:
        clothAttributes[name] = 0
    return


def NewImage():
    clothList.clear()
    for name in clothAttributesNames:
        clothAttributes[name] = 0
    return
