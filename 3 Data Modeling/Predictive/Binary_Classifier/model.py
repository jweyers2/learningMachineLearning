import sys
sys.path.insert(0, '../../')
from utils import train_test_split_predictive
import pandas as pd
import numpy as np
from sklearn.model_selection import TimeSeriesSplit
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import accuracy_score
useDevDataset = True
useTimeStamps = False

path = ''
if (useDevDataset):
    path = '../../../00 Data/Final/developerDatasetScaled.csv'
else:
    path = '../../../00 Data/Final/scaledFinal.csv'
X_train, X_test, y_train, y_test = train_test_split_predictive(useDevDataset, path)
if not useTimeStamps:
    X_train = X_train.drop(['datetime'], axis=1)
    X_test = X_test.drop(['datetime'], axis=1)
tscv = TimeSeriesSplit(n_splits=10)
testruns = 10
scores = []
runscores = []
for i in range(testruns):
    for train_index, test_index in tscv.split(X_train):
        print("TRAIN:", train_index, "\n", "TEST:", test_index)
        X_train_train, X_train_test = X_train[:train_index.size], X_train[
                                                                  train_index.size:train_index.size + test_index.size]
        y_train_train, y_train_true = y_train[:train_index.size], y_train[
                                                                  train_index.size:train_index.size + test_index.size]
        clf = SGDClassifier(loss="hinge", penalty="l2", max_iter=3)
        clf.fit(X_train_train, y_train_train)
        y_pred = clf.predict(X_train_test)
        score = accuracy_score(y_train_true, y_pred)
        scores.append(score)
    runscores.append(sum(scores)/len(scores))

scoreAvg = sum(runscores)/len(runscores)
print(scoreAvg)

