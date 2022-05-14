import os
from PIL import Image
import shutil
import sys

inputDir = 'output_palette'
output_dirHR = 'output_palette_jpg'

if not os.path.exists(output_dirHR):
    os.makedirs(output_dirHR)


def img2img(dataset_dir, type):
    files = []
    image_list = os.listdir(dataset_dir)
    files = [os.path.join(dataset_dir, _) for _ in image_list]
    for index, bmp in enumerate(files):
        if index > 100000:
            break
        try:
            sys.stdout.write('\r>>Converting image %d/100000 ' % (index))
            sys.stdout.flush()
            im = Image.open(bmp)
            img = os.path.splitext(bmp)[0] + "." + type
            im.save(img)
            shutil.move(img, output_dirHR)
        except IOError as e:
            print('could not read:', bmp)
            print('error:', e)
            print('skip it\n')
    sys.stdout.write('Convert Over!\n')
    sys.stdout.flush()


if __name__ == "__main__":
    current_dir = inputDir
    img2img(current_dir, 'jpg')
