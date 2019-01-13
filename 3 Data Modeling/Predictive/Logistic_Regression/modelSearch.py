import sys
sys.path.insert(0, '../../')
from utils import train_test_split_predictive
import pandas as pd
import warnings
warnings.simplefilter("ignore")

from sklearn.model_selection import TimeSeriesSplit
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.decomposition import PCA

#some global variables
useDevDataset = True
searchResultsPath = './searchResults.csv'
if useDevDataset:
    path = '../../../00 Data/Final/binaryDeveloperDatasetScaled.csv'
else:
    path = '../../../00 Data/Final/binaryScaled.csv'

x_train, x_test, y_train, y_test = train_test_split_predictive(path)
x_train_original = x_train
x_test_original = x_test
tscv = TimeSeriesSplit(n_splits=10)
testrunScores = []
totalpred = []
totaltrue = []
totalproba = []
row = []

param_grid = {
    #pca
    'ratio': [0.95, 0.975, None],
    'penalty': ['l1', 'l2'],
    #strongness of regularization
    'solver_l1':['liblinear', 'saga'],
    'solver_l2':['newton-cg', 'lbfgs', 'sag'],
    'c': [1, 10, 20, 50, 100],
}

def train(clf):
    for train_index, test_index in tscv.split(x_train):
        x_train_train, x_train_test = x_train[:train_index.size], x_train[train_index.size:train_index.size + test_index.size]
        y_train_train, y_train_true = y_train[:train_index.size], y_train[train_index.size:train_index.size + test_index.size]

        clf.fit(x_train_train, y_train_train)
        y_pred = clf.predict(x_train_test)
        totalpred.extend(y_pred)
        totaltrue.extend(y_train_true)

        y_proba = clf.predict_proba(x_train_test)
        totalproba.extend(y_proba)
    score = round(accuracy_score(totaltrue, totalpred), 3)
    testrunScores.append(score)
    row.append(sum(testrunScores) / len(testrunScores))
    totalproba2 = [x[1] for x in totalproba]
    row.append(sum(totalproba2)/len(totalproba2))
    print(row)
    search_results.loc[len(search_results)] = row


search_results = pd.DataFrame(columns=['ratio', 'penalty', 'c', 'solver', 'score', 'probability'])

# Grid Search
for ratio in param_grid['ratio']:
    print(ratio)
    x_train = x_train_original
    if ratio is not None:
        pca = PCA(n_components=ratio)
        x_train = pca.fit_transform(x_train)
    for penalty in param_grid['penalty']:
        for c in param_grid['c']:
            if penalty == 'l1':
                for solver in param_grid['solver_l1']:
                    row = [ratio, penalty, c, solver]
                    clf = LogisticRegression(C=c, penalty=penalty, solver=solver)
                    train(clf)
                    testrunScores = []
                    totalpred = []
                    totaltrue = []
                    totalproba = []
            elif penalty == 'l2':
                for solver in param_grid['solver_l2']:
                    row = [ratio, penalty, c, solver]
                    clf = LogisticRegression(C=c, penalty=penalty, solver=solver)
                    train(clf)
                    testrunScores = []
                    totalpred = []
                    totaltrue = []
                    totalproba = []
    print('---------------------------------')


search_results.to_csv(searchResultsPath, index=False, sep=',')

