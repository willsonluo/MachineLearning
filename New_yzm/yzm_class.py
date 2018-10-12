# -*- coding: utf-8 -*-
"""
@Time: 2018 Oct 11
@Author: Willson Luo
"""
from PIL import Image
import os
import requests
import time
import cv2
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.externals import joblib

def yzm_download(down_url):
  #  url = 'https://app.singlewindow.cn/cas/plat_cas_verifycode_gen'
    res = requests.get(down_url, stream=True)
    with open('yzm_download'+os.sep+str(int(time.time() * 1000000))+'.jpg', 'wb') as f:
        for chunk in res.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                f.flush()
    #    f.close()
    return


def yzm_clean(yzm_file):
    img = cv2.imread(yzm_file, 0)  # 直接读为灰度图像
    ret, thresh1 = cv2.threshold(img, 30, 255, cv2.THRESH_BINARY)
    cv2.imwrite(yzm_file, thresh1)
    return


def yzm_split(yzm_file):
    img = Image.open(yzm_file)
    im = img.convert("L")
    split_lines = [4, 18, 32, 46, 60]
    y_min = 1
    y_max = 23
    for x_min, x_max in zip(split_lines[:-1], split_lines[1:]):
        im.crop([x_min, y_min, x_max, y_max]).save(
                'yzm_split' + os.sep + str('zz_')+str(int(time.time() * 1000000))+'.jpg',
                'jpeg')  # (str(c)+'.jpg')
    return


def yzm_binary(yzm_file):
    im = Image.open(yzm_file)
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


def yzm_matrix(yzm_folder):
    samples_list = []
    samples_filename = os.listdir(yzm_folder)
    for i in range(len(samples_filename)):
        samples_list.append(yzm_binary(yzm_folder + os.sep + samples_filename[i]))
    samples = np.array(samples_list)
    print(samples.shape)
    return samples


def yzm_vector(yzm_folder):
    vector_list = []
    vector_filename = os.listdir(yzm_folder)
    for i in range(len(vector_filename)):
        vector_list.append(vector_filename[i].split("_")[0])
    vectors = np.array(vector_list)
    print(vectors.shape)
    return vectors


def yzm_gnb(yzm_Xdata,yzm_ydata):
    Xtrain, Xtest, ytrain, ytest = train_test_split(yzm_Xdata,yzm_ydata,
                                                    test_size=0.3)  # random_state=1)
    model = GaussianNB()
    model.fit(Xtrain,ytrain)
    y_model = model.predict(Xtest)
    score = accuracy_score(ytest, y_model)
    print("Gaussian Naive Bayes Accuracy is:",score)
    joblib.dump(model, "GNB_train_model.m")
    return


def yzm_svm(yzm_Xdata,yzm_ydata):
    Xtrain, Xtest, ytrain, ytest = train_test_split(yzm_Xdata,yzm_ydata,
                                                    test_size=0.3)  # random_state=1)
    clf = svm.SVC()
    clf.fit(Xtrain, ytrain)
    y_model = clf.predict(Xtest)
    score = accuracy_score(ytest, y_model)
    print("Support Vector Machine Accuracy is:",score)
    joblib.dump(clf, "SVM_train_model.m")
    return


def yzm_rf(yzm_Xdata,yzm_ydata):
    Xtrain, Xtest, ytrain, ytest = train_test_split(yzm_Xdata,yzm_ydata,
                                                    test_size=0.3)  # random_state=1)
    model = RandomForestClassifier(n_estimators=1000)
    model.fit(yzm_Xdata, yzm_ydata)
    y_model = model.predict(Xtest)
    score = accuracy_score(ytest, y_model)
    print("Radon Forest Accuracy is:",score)
    joblib.dump(model, "RF_train_model.m")
    return


def yzm_gnb_pred(yzm_file):
    X_tmp = []
    img_orig = yzm_binary(yzm_file)
    X_tmp.append(img_orig)
    X_pred = np.array(X_tmp)
    gnb_model = joblib.load("GNB_train_model.m")
    return gnb_model.predict(X_pred)

def yzm_rf_pred(yzm_file):
    X_tmp = []
    img_orig = yzm_binary(yzm_file)
    X_tmp.append(img_orig)
    X_pred = np.array(X_tmp)
    gnb_model = joblib.load("RF_train_model.m")
    return gnb_model.predict(X_pred)


def yzm_svm_pred(yzm_file):
    X_tmp = []
    img_orig = yzm_binary(yzm_file)
    X_tmp.append(img_orig)
    X_pred = np.array(X_tmp)
    svm_model = joblib.load("SVM_train_model.m")
    return svm_model.predict(X_pred)