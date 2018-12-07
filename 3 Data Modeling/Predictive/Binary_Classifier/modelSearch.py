import sys
sys.path.insert(0, '../../')
from utils import train_test_split_predictive
import pandas as pd
from sklearn.model_selection import TimeSeriesSplit
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve
useDevDataset = True
import warnings
warnings.simplefilter("ignore")
from sklearn.decomposition import PCA

searchResultsPath = './searchResults.csv'
path = ''
if (useDevDataset):
    path = '../../../00 Data/Final/binaryDeveloperDatasetScaled.csv'
else:
    path = '../../../00 Data/Final/binaryScaled.csv'
X_train, X_test, y_train, y_test = train_test_split_predictive(path)
X_train_original = X_train
tscv = TimeSeriesSplit(n_splits=5)
scores = []
testruns = 5
testrunScores = []
param_grid = [
    # pca variance ratio
    [0.75, 0.8, 0.85, 0.9, 0.95, None],
    # loss
    ['hinge', 'log', 'modified_huber', 'squared_hinge', 'perceptron'],
    # penalty
    ['l2', 'elasticnet'],
    # n_splits
    [50, 100, 150],
    # tol
    [0.001, 0.003, 0.005, 0.007, 0.01]
]
search_results = pd.DataFrame(columns=['ratio', 'loss', 'penalty', 'n_splits', 'tol', 'score'])
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
                            score = roc_auc_score(y_train_true, y_pred)
                            scores.append(score)
                        testrunScores.append(sum(scores) / len(scores))
                        scores = []
                    row = [ratio, loss, penalty, n, tol, sum(testrunScores) / len(testrunScores)]
                    testrunScores = []
                    search_results.loc[len(search_results)] = row
        print(loss)
    print(ratio)


search_results.to_csv(searchResultsPath, index=False, sep=',')

