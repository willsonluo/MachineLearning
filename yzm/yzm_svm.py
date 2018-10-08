# -*- coding: utf-8 -*-
from sklearn.svm import SVC
# from sklearn import grid_search
from sklearn.model_selection import GridSearchCV
import numpy as np
from sklearn.model_selection import cross_validate as cs
# from sklearn.metrics import cross_validation as cs
# from sklearn.externals import joblib
# from yzm_predict import loadPredict
# import warnings
import time


def load_data():
    dataset = np.loadtxt(r'D:\Pytorch\yzm\yzm_training\train_data.txt', delimiter=',')
    print(dataset)
    return dataset


def cross_validation():
    dataset = load_data()
    print(dataset)
    row, col = dataset.shape
    X = dataset[:, :col - 1]
    y = dataset[:, -1]
    clf = SVC(kernel='rbf', C=1000)
    clf.fit(X, Y)
    scores = cs.cross_val_score(clf, X, y, cv=5, score_func=None)
    print("Accuracy: %0.2f (+- %0.2f)" % (scores.mean(), scores.std()))
    return clf


t0 = time.time()
cross_validation()
# print "fit time:",round(time.time()-t0,3),"s"


def searchBestParameter():
    parameters = {'kernel': ('linear', 'poly', 'rbf', 'sigmoid'), 'C': [1, 100]}
    dataset = load_data()
    row, col = dataset.shape
    X = dataset[:, :col - 1]
    Y = dataset[:, -1]
    svr = SVC()
    clf = GridSearchCV(svr, parameters)
    clf.fit(X, Y)
    print
    clf.best_params_
# searchBestParameter()
print("fit time:", round(time.time() - t0, 3), "s")
