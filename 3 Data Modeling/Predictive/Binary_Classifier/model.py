import sys
sys.path.insert(0, '../../')
from utils import train_test_split_predictive
import pandas as pd
from sklearn.model_selection import TimeSeriesSplit
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score
useDevDataset = True
import warnings
warnings.simplefilter("ignore")
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.externals import joblib

path = ''
if (useDevDataset):
    path = '../../../00 Data/Final/binaryDeveloperDatasetScaled.csv'
else:
    path = '../../../00 Data/Final/binaryScaled.csv'
paramSetPath = './bestParamSet.csv'
paramSet = pd.read_csv(paramSetPath, dayfirst=True)
loss = paramSet.iloc[0]['loss']
penalty = paramSet.iloc[0]['penalty']
n = paramSet.iloc[0]['n_splits']
tol = paramSet.iloc[0]['tol']
ratio = paramSet.iloc[0]['ratio']
X_train, X_test, y_train, y_test = train_test_split_predictive(path)
if ratio != 'None':
    pca = PCA(n_components=ratio)
    X_train = pca.fit_transform(X_train)
tscv = TimeSeriesSplit(n_splits=5)
totalpred = []
totaltrue = []
testruns = 25
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

score = roc_auc_score(totaltrue, totalpred)
fpr, tpr, _ = roc_curve(totaltrue, totalpred)
plt.plot(fpr,tpr,label="data 1")
plt.plot([0, 1],[0,1], 'k--')
plt.axis([0,1,0,1])
plt.xlabel('False positive rate')
plt.ylabel('True positive rate')
plt.legend(loc=4)

plt.savefig('./rocCurve.png')
clf = SGDClassifier(loss=loss, penalty=penalty, max_iter=n, tol=tol)
joblib.dump(clf, './model.pkl')