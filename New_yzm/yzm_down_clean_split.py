# -*- coding:utf-8 -*-
from yzm_class import *
import pandas as pd
import numpy as np


def downloadCleanSplit():
    fetch_num = 100
    url = 'https://app.singlewindow.cn/cas/plat_cas_verifycode_gen'
    for i in range(fetch_num):
        yzm_download(url)
    yzm_file = os.listdir('yzm_download')
    for x in range(len(yzm_file)):
        yzm_clean('yzm_download'+os.sep+yzm_file[x])
        yzm_split('yzm_download'+os.sep+yzm_file[x])
        os.remove('yzm_download'+os.sep+yzm_file[x])


def predict_for_train():
    yzm_word = [abc for abc in os.listdir('yzm_split')]
    for x in range(len(yzm_word)):
        name = yzm_gnb_pred('yzm_split'+os.sep+yzm_word[x])[0]
        os.rename('yzm_split'+os.sep+yzm_word[x],'yzm_split'+os.sep + name +"_"+str(int(time.time()*1000000))+'.jpg')


def train():
    train_folder = 'yzm_train'
    Xdata = yzm_matrix(train_folder)
    ydata = yzm_vector(train_folder)
    print(ydata)
    yzm_gnb(Xdata,ydata)
    yzm_svm(Xdata,ydata)
    yzm_rf(Xdata,ydata)
    ydata_list = ydata.tolist()
    dict = {}
    for key in ydata_list:
        dict[key] = dict.get(key, 0) + 1
    print(dict)


# downloadCleanSplit()
# predict_for_train()
train()