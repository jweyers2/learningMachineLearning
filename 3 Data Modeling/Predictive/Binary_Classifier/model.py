import sys
sys.path.insert(0, '../../')
from utils import train_test_split_predictive
import pandas as pd
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
# Idea: Train 1 model with the best parameter set. Additionally, train a fine-tuned model with the best parameter set
# that supports probability prediction. Then compare both and save/document the best one
# Set the parameters for model 1
loss = paramSet.iloc[0]['loss']
penalty = paramSet.iloc[0]['penalty']
n = paramSet.iloc[0]['n_splits']
tol = paramSet.iloc[0]['tol']
ratio = paramSet.iloc[0]['ratio']
# Import the parameters for the fine tuned model
loss_proba_model = loss
penalty_proba_model = penalty
n_proba_model = n
tol_proba_model = tol
ratio_proba_model = ratio
X_train, X_test, y_train, y_test = train_test_split_predictive(path)
X_train_original = X_train
if ratio != 'None':
    pca = PCA(n_components=ratio)
    X_train = pca.fit_transform(X_train)
# tscv = TimeSeriesSplit(n_splits=int(y_train.size/5))
tscv = TimeSeriesSplit(n_splits=int(100))
totalpred = []
totaltrue = []
totalprob = []
testruns = 10
# Dummy value 1, will be overwritten
threshold = 1
for t in range(testruns):
    for train_index, test_index in tscv.split(X_train):
        X_train_train, X_train_test = X_train[:train_index.size], X_train[
                                                                  train_index.size:train_index.size + test_index.size]
        y_train_train, y_train_true = y_train[:train_index.size], y_train[
                                                                  train_index.size:train_index.size + test_index.size]
        clf = SGDClassifier(loss=loss, penalty=penalty, max_iter=n, tol=tol)
        clf.fit(X_train_train, y_train_train)
        y_pred = clf.predict(X_train_test)
        totalpred.extend(y_pred)
        totaltrue.extend(y_train_true)
        if loss == 'log':
            y_proba = clf.predict_proba(X_train_test)
            totalprob.extend(y_proba[:, 1])
print('Model 1 finished')
score = roc_auc_score(totaltrue, totalpred)
fpr, tpr, _ = roc_curve(totaltrue, totalpred)
# If the best param set already supports probability prediction, set the threshold here
if loss == 'log':
    threshold = tpr[1]
# If the first parameter set does not support probability prediction, use the second one calculate the threshold
else:
    X_train = X_train_original
    # Import the parameters for model 2
    loss2 = paramSet.iloc[1]['loss']
    penalty2 = paramSet.iloc[1]['penalty']
    n2 = paramSet.iloc[1]['n_splits']
    tol2 = paramSet.iloc[1]['tol']
    ratio2 = paramSet.iloc[1]['ratio']
    if ratio2 != 'None':
        pca = PCA(n_components=ratio2)
        X_train = pca.fit_transform(X_train)
    totalpred2 = []
    totaltrue2 = []
    totalprob2 = []
    for t in range(testruns):
        for train_index, test_index in tscv.split(X_train):
            X_train_train, X_train_test = X_train[:train_index.size], X_train[
                                                                      train_index.size:train_index.size + test_index.size]
            y_train_train, y_train_true = y_train[:train_index.size], y_train[
                                                                      train_index.size:train_index.size + test_index.size]
            clf = SGDClassifier(loss=loss2, penalty=penalty2, max_iter=n2, tol=tol2)
            clf.fit(X_train_train, y_train_train)
            y_pred2 = clf.predict(X_train_test)
            totalpred2.extend(y_pred2)
            totaltrue2.extend(y_train_true)
            y_proba2 = clf.predict_proba(X_train_test)
            totalprob2.extend(y_proba2[:, 1])
    fpr2, tpr2, _2 = roc_curve(totaltrue, totalpred)
    # Set the threshold
    threshold = tpr2[1]
    # Use the parameters from model 2 for the fine tuned model, to support probability prediction
    loss_proba_model = loss2
    penalty_proba_model = penalty2
    n_proba_model = n2
    tol_proba_model = tol2
    ratio_proba_model = ratio2
    print('Model 2 finished')

# Train a fine tuned model
X_train = X_train_original
if ratio_proba_model != 'None':
    pca = PCA(n_components=ratio_proba_model)
    X_train = pca.fit_transform(X_train)
totalpred3 = []
totaltrue3 = []
totalprob3 = []
threshold_predictions = []
for t in range(testruns):
    for train_index, test_index in tscv.split(X_train):
        X_train_train, X_train_test = X_train[:train_index.size], X_train[
                                                                  train_index.size:train_index.size + test_index.size]
        y_train_train, y_train_true = y_train[:train_index.size], y_train[
                                                                  train_index.size:train_index.size + test_index.size]
        clf = SGDClassifier(loss=loss_proba_model, penalty=penalty_proba_model, max_iter=n_proba_model, tol=tol_proba_model)
        clf.fit(X_train_train, y_train_train)
        y_pred3 = clf.predict(X_train_test)
        totalpred3.extend(y_pred3)
        totaltrue3.extend(y_train_true)
        y_proba3 = clf.predict_proba(X_train_test)
        totalprob3.extend(y_proba3[:, 1])
        for pred in y_proba3[:, 1]:
            if pred >= threshold:
                threshold_predictions.append(1)
            else:
                threshold_predictions.append(0)

# Compare the fined tuned model to the previous one
score_tuned = roc_auc_score(totaltrue3, threshold_predictions)
if score_tuned > score:
    # Document the third model since it's better
    totaltrue = totaltrue3
    totalpred = threshold_predictions
    totalprob = totalprob3
    loss = loss_proba_model
    penalty = penalty_proba_model
    n = n_proba_model
    ratio = ratio_proba_model
    tol = tol_proba_model
    fpr, tpr, _ = roc_curve(totaltrue, totalpred)
    score = score_tuned

plt.plot(fpr,tpr,label="ROC prediction score ("+str(round(score,2))+")")
if loss == 'log':
    fpr, tpr, _ = roc_curve(totaltrue, totalprob)
    plt.plot(fpr, tpr, label="ROC probability score")
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

