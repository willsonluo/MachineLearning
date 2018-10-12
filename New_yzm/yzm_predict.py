# -*- coding:utf-8 -*-
"""
@Time: 2018 Oct 11
@Author: Willson Luo
"""
import requests
import time
import os
import cv2
from PIL import Image
from yzm_class import *
import numpy as np


def downloadCleanSplit():
    fetch_num = 100
    url = 'https://app.singlewindow.cn/cas/plat_cas_verifycode_gen'
    for i in range(fetch_num):
        yzm_download(url)


def predict():
    yzm_file = os.listdir('yzm_download')
    for i in range(len(yzm_file)):
        yzm_clean('yzm_download'+os.sep+yzm_file[i])
        yzm_split('yzm_download'+os.sep+yzm_file[i])
        yzm_word = [abc for abc in os.listdir('yzm_split')]
        words = ''
        for x in range(len(yzm_word)):
            words += yzm_rf_pred('yzm_split'+os.sep+yzm_word[x])[0]
            os.remove('yzm_split'+os.sep+yzm_word[x])
        os.rename('yzm_download'+os.sep+yzm_file[i], 'yzm_download'+os.sep+ words +"_"+str(int(time.time()*1000000))+'.jpg')
        print(words)

downloadCleanSplit()    #下载10个验证码
predict()  # 预测验证码