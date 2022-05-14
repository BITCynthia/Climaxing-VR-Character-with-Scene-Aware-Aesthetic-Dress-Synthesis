# -*- coding: utf-8 -*-
import json


# 读取label
def grabLabel(filename):
    fr = open(filename, "rb")
    return json.load(fr)


# 存储label
def storeLabel(inputLabel, filename):
    with open(filename, 'w') as fw:
        json.dump(inputLabel, fw)
