import sys
sys.path.insert(0, '../../')
from utils import train_test_split_predictive
import pandas as pd
from sklearn.model_selection import TimeSeriesSplit
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import random
useDevDataset = True
useGridSearch = False
randomSearchCount = 150
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
    # max_depth
    [None,3,5,7,10],
    # min_samples_split
    [2,50,100,150],
    # max_leaf_nodes
    [None,15,10,5,3,2],
    # min_impurity_decrease
    [0.0,0.15,0.25,0.3,0.35],

]
search_results = pd.DataFrame(columns=['ratio','max_depth', 'min_samples_split', 'max_leaf_nodes', 'min_impurity_decrease', 'score'])
# # Grid Search
# if useGridSearch is True:
#     for ratio in param_grid[0]:
#         X_train = X_train_original
#         if ratio is not None:
#             pca = PCA(n_components=ratio)
#             X_train = pca.fit_transform(X_train)
#         for loss in param_grid[1]:
#             for penalty in param_grid[2]:
#                 for n in param_grid[3]:
#                     for tol in param_grid[4]:
#                         for t in range(testruns):
#                             for train_index, test_index in tscv.split(X_train):
#                                 # print("TRAIN:", train_index, "\n", "TEST:", test_index)
#                                 X_train_train, X_train_test = X_train[:train_index.size], X_train[
#                                                                                           train_index.size:train_index.size + test_index.size]
#                                 y_train_train, y_train_true = y_train[:train_index.size], y_train[
#                                                                                           train_index.size:train_index.size + test_index.size]
#                                 clf = SGDClassifier(loss=loss, penalty=penalty, max_iter=n, tol=tol)
#                                 clf.fit(X_train_train, y_train_train)
#                                 y_pred = clf.predict(X_train_test)
#                                 totalpred.extend(y_pred)
#                                 totaltrue.extend(y_train_true)
#                             score = round(accuracy_score(totaltrue, totalpred), 2)
#                             testrunScores.append(score)
#                             totalpred = []
#                             totaltrue = []
#                         row = [ratio, loss, penalty, n, tol, sum(testrunScores) / len(testrunScores)]
#                         testrunScores = []
#                         search_results.loc[len(search_results)] = row
#             print(loss)
#         print(ratio)
# Random Search
# else:
for c in range(randomSearchCount):
    ratio = random.choice(param_grid[0])
    max_depth = random.choice(param_grid[1])
    min_samples_split = random.choice(param_grid[2])
    max_leaf_nodes = random.choice(param_grid[3])
    min_impurity_decrease = random.choice(param_grid[4])
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
            clf = RandomForestClassifier(n_estimators=100, criterion='gini', max_depth=max_depth, min_samples_split=min_samples_split, max_leaf_nodes=max_leaf_nodes, min_impurity_decrease=min_impurity_decrease)
            clf.fit(X_train_train, y_train_train)
            y_pred = clf.predict(X_train_test)
            totalpred.extend(y_pred)
            totaltrue.extend(y_train_true)
        score = round(accuracy_score(totaltrue, totalpred), 2)
        testrunScores.append(score)
        totalpred = []
        totaltrue = []
    row = [ratio, max_depth, min_samples_split, max_leaf_nodes, min_impurity_decrease, sum(testrunScores) / len(testrunScores)]
    testrunScores = []
    search_results.loc[len(search_results)] = row
    print(c)


search_results.to_csv(searchResultsPath, index=False, sep=',')

