import sys
sys.path.insert(0, '../../')
from utils import train_test_split_predictive
import pandas as pd
from sklearn.model_selection import TimeSeriesSplit
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import roc_auc_score
from sklearn.metrics import accuracy_score
import random
useDevDataset = True
useGridSearch = True
randomSearchCount = 50
import warnings
warnings.simplefilter("ignore")
from sklearn.decomposition import PCA

searchResultsPath = './searchResults.csv'
path = ''
if useDevDataset:
    path = '../../../00 Data/Final/binaryDeveloperDatasetScaled.csv'
else:
    path = '../../../00 Data/Final/binaryScaled.csv'
X_train, X_test, y_train, y_test = train_test_split_predictive(path)
X_train_original = X_train
tscv = TimeSeriesSplit(n_splits=10)
testruns = 5
testrunScores = []
totalpred = []
totaltrue = []
param_grid = [
    # pca variance ratio
    [0.95, 0.975, None],
    # loss
    ['hinge', 'log', 'modified_huber', 'squared_hinge', 'perceptron'],
    # penalty
    ['l2', 'elasticnet','none','l1'],
    # n_splits
    [50, 100, 150],
    # tol
    [0.001, 0.003, 0.005, 0.007, 0.01]
]
search_results = pd.DataFrame(columns=['ratio', 'loss', 'penalty', 'n_splits', 'tol', 'score'])
# Grid Search
if useGridSearch is True:
    for ratio in param_grid[0]:
        X_train = X_train_original
        if ratio is not None:
            pca = PCA(n_components=ratio)
            X_train = pca.fit_transform(X_train)
        for loss in param_grid[1]:
            for penalty in param_grid[2]:
                for n in param_grid[3]:
                    for tol in param_grid[4]:
                        for t in range(testruns):
                            for train_index, test_index in tscv.split(X_train):
                                # print("TRAIN:", train_index, "\n", "TEST:", test_index)
                                X_train_train, X_train_test = X_train[:train_index.size], X_train[
                                                                                          train_index.size:train_index.size + test_index.size]
                                y_train_train, y_train_true = y_train[:train_index.size], y_train[
                                                                                          train_index.size:train_index.size + test_index.size]
                                clf = SGDClassifier(loss=loss, penalty=penalty, max_iter=n, tol=tol)
                                clf.fit(X_train_train, y_train_train)
                                y_pred = clf.predict(X_train_test)
                                totalpred.extend(y_pred)
                                totaltrue.extend(y_train_true)
                            #score = roc_auc_score(totaltrue, totalpred)
                            score = round(accuracy_score(totaltrue, totalpred), 2)
                            testrunScores.append(score)
                            totalpred = []
                            totaltrue = []
                        row = [ratio, loss, penalty, n, tol, sum(testrunScores) / len(testrunScores)]
                        testrunScores = []
                        search_results.loc[len(search_results)] = row
            print(loss)
        print(ratio)
# Random Search
else:
    for c in range(randomSearchCount):
        ratio = random.choice(param_grid[0])
        loss = random.choice(param_grid[1])
        penalty = random.choice(param_grid[2])
        n = random.choice(param_grid[3])
        tol = random.choice(param_grid[4])
        X_train = X_train_original
        if ratio is not None:
            pca = PCA(n_components=ratio)
            X_train = pca.fit_transform(X_train)
        for t in range(testruns):
            for train_index, test_index in tscv.split(X_train):
                # print("TRAIN:", train_index, "\n", "TEST:", test_index)
                X_train_train, X_train_test = X_train[:train_index.size], X_train[
                                                                          train_index.size:train_index.size + test_index.size]
                y_train_train, y_train_true = y_train[:train_index.size], y_train[
                                                                          train_index.size:train_index.size + test_index.size]
                clf = SGDClassifier(loss=loss, penalty=penalty, max_iter=n, tol=tol)
                clf.fit(X_train_train, y_train_train)
                y_pred = clf.predict(X_train_test)
                totalpred.extend(y_pred)
                totaltrue.extend(y_train_true)
            #score = roc_auc_score(totaltrue, totalpred)
            score = round(accuracy_score(totaltrue, totalpred), 2)
            testrunScores.append(score)
            totalpred = []
            totaltrue = []
        row = [ratio, loss, penalty, n, tol, sum(testrunScores) / len(testrunScores)]
        testrunScores = []
        search_results.loc[len(search_results)] = row
        print(c)


search_results.to_csv(searchResultsPath, index=False, sep=',')

