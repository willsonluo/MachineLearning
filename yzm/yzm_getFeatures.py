# -*- coding: utf-8 -*-
from PIL import Image
import numpy as np
import os


def getBinaryPix(im):
    im = Image.open(im)
    img = np.array(im)
    rows, cols = img.shape
    for i in range(rows):
        for j in range(cols):
            if (img[i, j] <= 128):
                img[i, j] = 0
            else:
                img[i, j] = 1
    binpix = np.ravel(img)
    return binpix


def getfiles(dirs):
    fs = []
    for fr in os.listdir(dirs):
        f = dirs + fr
        if f.rfind(u'.DS_Store') == -1:
            fs.append(f)
    return fs


def writeFile(content):
    with open(r'D:\Pytorch\yzm\yzm_training\train_data.txt', 'a+') as f:
        f.write(content)
        f.write('\n')
        f.close()


if __name__ == '__main__':
    path = os.getcwd()
    dirs = os.listdir(r'D:\Pytorch\yzm\yzm_test')
    for i in range(9):
        for f in range(len(dirs)):
            print(dirs[f])
            pixs = getBinaryPix(path + os.sep + "yzm_test" + os.sep + dirs[f]).tolist()
            pixs.append(i)
            pixs = [str(i) for i in pixs]
            content = ','.join(pixs)
            writeFile(content)
