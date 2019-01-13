import sys
sys.path.insert(0, '../../')
from utils import train_test_split_predictive
import pandas as pd
import numpy

from sklearn.model_selection import TimeSeriesSplit
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score

import warnings
warnings.simplefilter("ignore")
import matplotlib.pyplot as plt
from sklearn.externals import joblib
from sklearn.metrics import confusion_matrix
import seaborn as sn
import datetime

useDevDataset = False
probability = True

# path = ''
if useDevDataset:
    path = '../../../00 Data/Final/binaryDeveloperDatasetScaled.csv'
else:
    path = '../../../00 Data/Final/binaryScaled.csv'
paramSetPath = './bestParamSet.csv'

paramSet = pd.read_csv(paramSetPath, dayfirst=True)
ratio = paramSet.iloc[0]['ratio']
c = paramSet.iloc[0]['c']
kernel = paramSet.iloc[0]['kernel']
gamma = paramSet.iloc[0]['gamma']
degree = paramSet.iloc[0]['degree']

if ratio == 'None':
    ratio = None
X_train, X_test, y_train, y_test = train_test_split_predictive(path, ratio)
dataframe = pd.read_csv(path, dayfirst=True)
#print(int(y_test.size/(96)))
tscv = TimeSeriesSplit(n_splits=int(y_test.size/(96)))
print('Total splits = '+str(tscv.n_splits))
totalpred = []
totaltrue = []
totalprob = []
avg = []
counter = 0
firstIteration = True
for train_index, test_index in tscv.split(X_test):
    # For the first iteration train on the training set and predict the first test set split
    if firstIteration is True:
        firstIteration = False
        print(str(datetime.datetime.now()) + ' | ' + str(counter))
        x_test_train = X_train
        y_test_train = y_train
        x_test_test = X_test[:train_index.size]
        y_test_test = y_test[:train_index.size]
    else:
        # For the iterations 2+ on the training set and some of the test set splits and predict the next test set split
        print(str(datetime.datetime.now()) + ' | ' + str(counter))
        x_test_train, x_test_test = numpy.vstack([X_train, X_test[:train_index.size]]), X_test[train_index.size:train_index.size + test_index.size]
        y_test_train, y_test_test = y_train.append(y_test[:train_index.size]), y_test[train_index.size:train_index.size + test_index.size]
    if gamma != 'None':
        clf = SVC(C=c, kernel=kernel, gamma=gamma, probability=probability)
    elif degree != 'None':
        clf = SVC(C=c, kernel=kernel, degree=degree, probability=probability)
    else:
        clf = SVC(C=c, kernel=kernel, probability=probability)
    clf.fit(x_test_train, y_test_train)
    y_pred = clf.predict(x_test_test)
    totalpred.extend(y_pred)
    totaltrue.extend(y_test_test)
    if probability:
        y_proba = clf.predict_proba(x_test_test)
        totalprob.extend(y_proba[:, 1])
    counter = counter + 1
joblib.dump(clf, './model.pkl')

#ROC Curve
fpr, tpr, _ = roc_curve(totaltrue, totalpred)
score = roc_auc_score(totaltrue, totalpred)
plt.plot(fpr,tpr,label="ROC prediction score ("+str(round(score,2))+")")
if probability == True:
    fpr2, tpr2, _2 = roc_curve(totaltrue, totalprob)
    plt.plot(fpr2, tpr2, label="ROC probability score")
    plt.plot([0, 1],[0,1], 'k--')
plt.axis([0,1,0,1])
plt.xlabel('False positive rate')
plt.ylabel('True positive rate')
plt.legend(loc=4)
plt.savefig('./rocCurve.png')

#Confusion Matrix
conf_matrix = confusion_matrix(totaltrue, totalpred)
accuracy = round(accuracy_score(totaltrue, totalpred),2)
plt.figure(figsize = (5,5))
plt.figtext(.325, .04, "Accuracy = "+str(accuracy))
plt.figtext(.325, 0.9, "Predicted values")
plt.figtext(0.05, 0.55, "Real values", rotation=90)
plt.ylabel('Actual values')
plt.xlabel('Predicted values')
sn.heatmap(conf_matrix, annot=True, fmt='g')
plt.savefig('./confusionMatrix.png')
plt.close()

