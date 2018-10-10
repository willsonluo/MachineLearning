# -*- coding: utf-8 -*-
from PIL import Image
import numpy as np
import os
import time
from sklearn.svm import SVC
from sklearn.model_selection import  train_test_split
from sklearn.naive_bayes import GaussianNB  # 1.选择模型类  Gaussian Native Bayes 高斯朴素贝叶斯
from sklearn.metrics import accuracy_score  ## 用accuracy_score工具验证模型预测结果的准确率
from sklearn.manifold import Isomap  ## Isomap(Isometric Feature Mapping)是流行学习的一种
import matplotlib.pyplot as plt
from sklearn.model_selection import GridSearchCV
import numpy as np
#from sklearn.model_selection import cross_validate as cs
from sklearn.cross_validation import cross_val_score as cs

#def load_data():
#    dataset = np.loadtxt(r'D:\Pytorch\yzm\yzm_training\train_data.txt', delimiter=',')
#    print(dataset)
#    return dataset


def cross_validation(X,y):
#    dataset = load_data()
#    print(dataset)
#    row, col = dataset.shape
#    X = dataset[:, :col - 1]
#    y = dataset[:, -1]
    clf = SVC(kernel='rbf', C=1000)
    clf.fit(X, y)
    scores = cs(clf, X, y, cv=5, scoring=None)
    print("Accuracy: %0.2f (+- %0.2f)" % (scores.mean(), scores.std()))
    return clf



# print "fit time:",round(time.time()-t0,3),"s"


def searchBestParameter(X,y):
    parameters = {'kernel': ('linear', 'poly', 'rbf', 'sigmoid'), 'C': [1, 100]}
#    dataset = load_data()
#    row, col = dataset.shape
#    X = dataset[:, :col - 1]
#    Y = dataset[:, -1]
    svr = SVC()
    clf = GridSearchCV(svr, parameters)
    clf.fit(X, y)
    print
    clf.best_params_
# searchBestParameter()
# print("fit time:", round(time.time() - t0, 3), "s")


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


def get_vectors(samples_folder):
    vector_list = []
    vector_filename = os.listdir(samples_folder)
    for i in range(len(vector_filename)):
        vector_list.append(vector_filename[i].split("_")[0])
    vectors = np.array(vector_list)
    # print(vector_list)
    print(vectors.shape)
    return vectors


def get_samples(samples_folder):
    samples_list = []
    samples_filename = os.listdir(samples_folder)
    for i in range(len(samples_filename)):
        samples_list.append(getBinaryPix(samples_folder+os.sep+samples_filename[i]))
    samples = np.array(samples_list)
    print(samples.shape)
    return samples
        #print(samples_list)
#        with open(r'D:\MachineLearning\yzm\train_data.txt', 'a+') as f:
#            sample = [str(x) for x  in samples_list]
#
#            f.write(samples)
#            f.write('\n')

def GNB(Xtrain,ytrain):
    model = GaussianNB()  # 2.初始化模型
    model.fit(Xtrain, ytrain)  # 3.用模型拟合数据
    y_model = model.predict(Xtest)  # 4.对新数据进行预测
    score = accuracy_score(ytest, y_model)
    print(score)


def randomForest(Xtrain,ytrain):
    model = RandomForestClassifier(n_estimators=1000)
    model.fit(Xtrain, ytrain)
    ypred = model.predict(Xtest)
    score = accuracy_score(ytest, y_model)
    print(score)


if __name__ == '__main__':
    t0 = time.time()
    X = get_samples("yzm_threshold")
    y = get_vectors("yzm_threshold")
    searchBestParameter(X, y)
    cross_validation(X, y)
#    Xtrain, Xtest, ytrain, ytest = train_test_split(X_data, y_data, test_size=0.3) #random_state=1)
#    GNB(Xtrain, ytrain)

#    word = [2,3,4,5,6,7,8,9,'a','b','c','d','e','f','g','h','i','j','k','m','n','p','q','r','s','t','u','v',
#            'w','x','y','z','A','B','C','D','E','F','G','H','J','K','L','M','N','P','Q','R','S','T','U',
#            'V','W','X','Y','Z']
#    path = os.getcwd()
#    dirs = os.listdir(r'D:\Pytorch\yzm\yzm_test')
#    for i in range(len(word)):
#        for f in range(len(dirs)):
#            print(dirs[f])
#            pixs = getBinaryPix(path + os.sep + "yzm_test" + os.sep + dirs[f]).tolist()
#            pixs.append(i)
#            pixs = [str(i) for i in pixs]
#            content = ','.join(pixs)
#            writeFile(content)
