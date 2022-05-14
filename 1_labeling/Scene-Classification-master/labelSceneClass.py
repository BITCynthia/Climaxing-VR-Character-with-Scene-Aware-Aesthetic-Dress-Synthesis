# import the necessary packages
import csv
import json
import os
import random

import cv2 as cv
import keras.backend as K
import numpy as np
from keras.applications.inception_resnet_v2 import preprocess_input

from config import best_model
from model import build_model

if __name__ == '__main__':
    model = build_model()
    model_weights_path = os.path.join('models', best_model)
    model.load_weights(model_weights_path)

    with open('scene_classes.csv', encoding='utf-8') as file:
        reader = csv.reader(file)
        scene_classes_list = list(reader)

    scene_classes_dict = dict()
    for item in scene_classes_list:
        scene_classes_dict[int(item[0])] = item[1]

    test_path = 'data/test_a/'
    test_images = [f for f in os.listdir(test_path) if
                   os.path.isfile(os.path.join(test_path, f)) and f.endswith('.jpg')]

    for image_name in test_images:
        filename = os.path.join(test_path, image_name)
        print('Start processing image: {}'.format(filename))
        image = cv.imread(filename)
        rgb_img = cv.cvtColor(image, cv.COLOR_BGR2RGB)
        rgb_img = np.expand_dims(rgb_img, 0).astype(np.float32)
        rgb_img = preprocess_input(rgb_img)
        preds = model.predict(rgb_img)
        prob = np.max(preds)
        class_id = np.argmax(preds)
        print(scene_classes_dict[class_id])
        result = {'image_id': image_name, 'label': str(class_id), 'prob': '{:.4}'.format(prob)}

        # print(result)
        resultJson = image_name[0:len(image_name) - 4] + '.json'
        resultFile = os.path.join('sceneClass', resultJson)
        with open(resultFile, 'w') as file:
            json.dump(result, file)

    K.clear_session()
