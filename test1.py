#!/usr/bin/python
# -*- coding: utf8 -*-

from sklearn import linear_model
from sklearn.metrics import auc_score
import numpy as np

trainfile = open('train.csv')
header = trainfile.next().rstrip().split(',')

y_train = []
X_train_A = []
X_train_B = []

for line in trainfile:
    splitted = line.rstrip().split(',')
    label = int(splitted[0])
    A_features = [float(item) for item in splitted[1:12]]
    B_features = [float(item) for item in splitted[12:]]
    y_train.append(label)
    X_train_A.append(A_features)
    X_train_B.append(B_features)
trainfile.close()

y_train = np.array(y_train)
X_train_A = np.array(X_train_A)
X_train_B = np.array(X_train_B)

def transform_features(x):
    return np.log(1+x)

X_train = transform_features(X_train_A) - transform_features(X_train_B)
model = linear_model.LogisticRegression(fit_intercept=False)
model.fit(X_train,y_train)
p_train = model.predict_proba(X_train)
p_train = p_train[:,1:2]

testfile = open('test.csv')
testfile.next()

X_test_A = []
X_test_B = []
for line in testfile:
    splitted = line.rstrip().split(',')
    A_features = [float(item) for item in splitted[0:11]]
    B_features = [float(item) for item in splitted[11:]]
    X_test_A.append(A_features)
    X_test_B.append(B_features)
testfile.close()

X_test_A = np.array(X_test_A)
X_test_B = np.array(X_test_B)

X_test = transform_features(X_test_A) - transform_features(X_test_B)
p_test = model.predict_proba(X_test)
p_test = p_test[:,1:2]

predfile = open('predictions.csv','w')

print >>predfile,','.join(header)
for line in np.concatenate((p_test,X_test_A,X_test_B),axis=1):
    print >>predfile, ','.join([str(item) for item in line])

predfile.close()