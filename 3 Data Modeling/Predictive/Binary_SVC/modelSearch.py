import sys
sys.path.insert(0, '../../')
from utils import train_test_split_predictive
import pandas as pd
import warnings
warnings.simplefilter("ignore")

from sklearn.model_selection import TimeSeriesSplit
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.decomposition import PCA

#some global variables
useDevDataset = True
probability = False
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
row = []

param_grid = {
    #pca
    'ratio': [0.95, 0.975, None],
    #softness of margin classification
    'c': [1, 20, 100],
    'kernel': ['linear', 'poly', 'rbf', 'sigmoid'],
    # auto = 1/n_features, scaled = 1/(n_features*X.std())
    'gamma': ['auto', 'scale', 0.01, 0.05, 0.1],
    'degree': [1, 2, 3, 4, 5, 6]
}

def train(clf):
    for train_index, test_index in tscv.split(x_train):
        x_train_train, x_train_test = x_train[:train_index.size], x_train[train_index.size:train_index.size + test_index.size]
        y_train_train, y_train_true = y_train[:train_index.size], y_train[train_index.size:train_index.size + test_index.size]

        clf.fit(x_train_train, y_train_train)
        y_pred = clf.predict(x_train_test)
        totalpred.extend(y_pred)
        totaltrue.extend(y_train_true)
    score = round(accuracy_score(totaltrue, totalpred), 3)
    testrunScores.append(score)
    row.append(sum(testrunScores) / len(testrunScores))
    print(row)
    search_results.loc[len(search_results)] = row


search_results = pd.DataFrame(columns=['ratio', 'c', 'kernel', 'gamma', 'degree', 'score'])
degree = ''
gamma = ''

# Grid Search
for ratio in param_grid['ratio']:
    print(ratio)
    x_train = x_train_original
    if ratio is not None:
        pca = PCA(n_components=ratio)
        x_train = pca.fit_transform(x_train)
    for c in param_grid['c']:
        for kernel in param_grid['kernel']:
            if kernel == 'poly':
                for degree in param_grid['degree']:
                    row = [ratio, c, kernel, '', degree]
                    clf = SVC(C=c, kernel=kernel, degree=degree, probability=probability)
                    train(clf)
                    testrunScores = []
                    totalpred = []
                    totaltrue = []
            elif kernel == 'rbf':
                for gamma in param_grid['gamma']:
                    row = [ratio, c, kernel, gamma, '']
                    clf = SVC(C=c, kernel=kernel, gamma=gamma, probability=probability)
                    train(clf)
                    testrunScores = []
                    totalpred = []
                    totaltrue = []
            else:
                row = [ratio, c, kernel, '', '']
                clf = SVC(C=c, kernel=kernel, probability=probability)
                train(clf)
                testrunScores = []
                totalpred = []
                totaltrue = []
    print('---------------------------------')


search_results.to_csv(searchResultsPath, index=False, sep=',')

