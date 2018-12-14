import sys
sys.path.insert(0, '../../')
from utils import train_test_split_predictive
import pandas as pd
import numpy
from sklearn.model_selection import TimeSeriesSplit
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score
useDevDataset = False
import warnings
warnings.simplefilter("ignore")
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.externals import joblib
from sklearn.metrics import confusion_matrix
import seaborn as sn

path = ''
if useDevDataset:
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
threshold = paramSet.iloc[0]['threshold']
X_train, X_test, y_train, y_test = train_test_split_predictive(path, ratio)
dataframe = pd.read_csv(path, dayfirst=True)
# if ratio != 'None':
#     pca = PCA(n_components=float(ratio))
#     X_train = pca.fit_transform(X_train)
tscv = TimeSeriesSplit(n_splits=int(y_test.size/(96)))
# tscv = TimeSeriesSplit(n_splits=int(25))
totalpred = []
totaltrue = []
totalprob = []
threshold_predictions = []
testruns = 10

# Do a run with the test set using the best performing model
for t in range(testruns):
    firstIteration = True
    for train_index, test_index in tscv.split(X_test):
        # For the first iteration train on the training set and predict the first test set split
        if firstIteration is True:
            X_test_train = X_train
            y_test_train = y_train
            X_test_test = X_test[:train_index.size]
            y_test_test = y_test[:train_index.size]
            firstIteration = False
            clf = SGDClassifier(loss=loss, penalty=penalty, max_iter=n, tol=tol)
            clf.fit(X_test_train, y_test_train)
            y_pred = clf.predict(X_test_test)
            totalpred.extend(y_pred)
            totaltrue.extend(y_test_test)
            # If the loss function is 'log' then use the given threshold from the csv
            if loss == 'log':
                y_proba = clf.predict_proba(X_test_test)
                totalprob.extend(y_proba[:, 1])
                for pred in y_proba[:, 1]:
                    if pred >= threshold:
                        threshold_predictions.append(1)
                    else:
                        threshold_predictions.append(0)
        # For the iterations 2+ on the training set and some of the test set splits and predict the next test set split
        X_test_train, X_test_test = numpy.vstack([X_train, X_test[:train_index.size]]), X_test[train_index.size:train_index.size + test_index.size]
        y_test_train, y_test_test = y_train.append(y_test[:train_index.size]), y_test[train_index.size:train_index.size + test_index.size]
        clf = SGDClassifier(loss=loss, penalty=penalty, max_iter=n, tol=tol)
        clf.fit(X_test_train, y_test_train)
        y_pred = clf.predict(X_test_test)
        totalpred.extend(y_pred)
        totaltrue.extend(y_test_test)
        # If the loss function is 'log' then use the given threshold from the csv
        if loss == 'log':
            y_proba = clf.predict_proba(X_test_test)
            totalprob.extend(y_proba[:, 1])
            for pred in y_proba[:, 1]:
                if pred >= threshold:
                    threshold_predictions.append(1)
                else:
                    threshold_predictions.append(0)
    print(t)


if loss == 'log':
    totalpred = threshold_predictions
fpr, tpr, _ = roc_curve(totaltrue, totalpred)
score = roc_auc_score(totaltrue, totalpred)


plt.plot(fpr,tpr,label="ROC prediction score ("+str(round(score,2))+")")
if loss == 'log':
    fpr2, tpr2, _2 = roc_curve(totaltrue, totalprob)
    plt.plot(fpr2, tpr2, label="ROC probability score")
plt.plot([0, 1],[0,1], 'k--')
plt.axis([0,1,0,1])
plt.xlabel('False positive rate')
plt.ylabel('True positive rate')
plt.legend(loc=4)
plt.savefig('./rocCurve.png')
clf = SGDClassifier(loss=loss, penalty=penalty, max_iter=n, tol=tol)
joblib.dump(clf, './model.pkl')

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

