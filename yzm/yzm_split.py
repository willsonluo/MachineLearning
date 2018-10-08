# -*- coding: utf-8 -*-
from PIL import Image, ImageEnhance
from PIL import *
import time
import os
# 图片切割


def segment(im):
    s = 4
    w = 15
    h = 22
    t = 0
    im_new = []
    for i in range(4):
        im1 = im.crop((s + w * i, t, s + w * (i + 1), h))
        im_new.append(im1)
    return im_new


# 图片预处理，二值化，图片增强
def imgTransfer(f_name):
    im = Image.open(f_name)
    im = im.filter(ImageFilter.MedianFilter())
    # enhancer = ImageEnhance.Contrast(im)
    # im = enhancer.enhancer(1)
    im = im.convert('L')
    return im


def cutPictures(img):
    im = imgTransfer(img)
    pics = segment(im)
    for pic in pics:
        pic.save('yzm_test'+os.sep + '%s.jpeg' % (int(time.time() * 1000000)), 'jpeg')


if __name__ == '__main__':
    files_name = [abc for abc in os.listdir('yzm_data')]
    print(files_name)
    for i in range(len(files_name)):
        # print('yzm_data' + os.sep + files_name[i])
        cutPictures('yzm_data' + os.sep + files_name[i])
