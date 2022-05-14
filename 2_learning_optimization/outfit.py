import os
import itertools
import store_grab as sg

dir = 'output_clothes'


def outfit(scene, figure):
    path = os.path.join(dir, scene + '_' + figure + '_outfit.json')
    Json = sg.grabLabel(path)
    outfits = Json['ChromosomeMatrix']

    outfits.sort()
    outfits = itertools.groupby(outfits)
    new_outfits = []
    for k, g in outfits:
        new_outfits += k
    new_outfits = list(set(new_outfits))
    print(new_outfits)
    return new_outfits[1]
