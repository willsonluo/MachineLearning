# -*- coding: utf-8 -*-
from PIL import Image,ImageFilter
import cv2
import time
import os


def clean(image_clean):
    img = cv2.imread(image_clean, 0)  # 直接读为灰度图像
    ret, thresh1 = cv2.threshold(img, 30, 255, cv2.THRESH_BINARY)
    cv2.imwrite(image_clean, thresh1)


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


# 图片预处理，二值化
def imgTransfer(f_name):
    im = Image.open(f_name)
    im = im.filter(ImageFilter.MedianFilter())
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
        clean('yzm_data' + os.sep + files_name[i])
        # print('yzm_data' + os.sep + files_name[i])
        cutPictures('yzm_data' + os.sep + files_name[i])
