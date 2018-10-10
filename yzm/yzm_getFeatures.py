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
    with open(r'D:\Pytorch\yzm\train_data.txt', 'a+') as f:
        f.write(content)
        f.write('\n')
        f.close()


if __name__ == '__main__':
    word = [2,3,4,5,6,7,8,9,'a','b','c','d','e','f','g','h','i','j','k','m','n','p','q','r','s','t','u','v',
            'w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','P','Q','R','S','T','U',
            'V','W','X','Y','Z']
    path = os.getcwd()
    dirs = os.listdir(r'D:\Pytorch\yzm\yzm_test')
    for i in range(len(word)):
        for f in range(len(dirs)):
            print(dirs[f])
            pixs = getBinaryPix(path + os.sep + "yzm_test" + os.sep + dirs[f]).tolist()
            pixs.append(i)
            pixs = [str(i) for i in pixs]
            content = ','.join(pixs)
            writeFile(content)
