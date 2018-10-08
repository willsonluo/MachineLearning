# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 17:20:09 2017
@author: onlyyo
最后一步，对于要测试的验证码处理，然后进行预测，输出结果
"""

from split_pic import *
from write_img import *
import os
from cross_svc import cross_validation


def cutPictures2(name):
    im = imgTransfer(name)
    pics = segment(im)
    for pic in pics:
        pic.save(u'J:/数据分析学习/python/机器学习之验证码识别/test_picture/%s.jpeg' % (int(time.time() * 1000000)), 'jpeg')


def load_Predict(name):
    #
    cutPictures2(name)  # 切割图片

    # dirs = u'J:/数据分析学习/python/机器学习之验证码识别/test_picture/'
    dirs = 'yzm_test'
    fs = os.listdir(dirs)  # 获取图片名称
    clf = cross_validation()
    predictValue = []

    for fname in fs:
        fn = dirs + fname
        binpix = getBinaryPix(fn)
        predictValue.append(clf.predict(binpix))

    predictValue = [str(int(i)) for i in predictValue]
    print
    "the picture number is :", "".join(predictValue)


# name = u'J:/数据分析学习/python/机器学习之验证码识别/8473.jpg'
name = r'D:\Pytorch\yzm\yzm_data\1538183308678040.jpg'
load_Predict(name)

