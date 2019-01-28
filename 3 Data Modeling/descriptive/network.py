from math import sqrt
import pandas as pd
import numpy as np
from numpy import concatenate
from matplotlib import pyplot
from pandas import read_csv
from pandas import DataFrame
from pandas import concat
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import StratifiedKFold
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score
import matplotlib.pyplot as plt
import seaborn as sns
from keras.constraints import maxnorm



path='../../00 Data/Final/binaryFinal.csv'
out_path='../../00 Data/Final/prediction.csv'
dataframe=pd.read_csv(path)
print("Länge:", len(dataframe))
dataframe.drop(['datetime'], axis=1, inplace=True)
dataframe.drop(['price_premium', 'price_dayahead', 'consumption_dayahead', 'price', 'consumption'],
               axis=1, inplace=True)
cols = list(dataframe)
cols.insert(0, cols.pop(cols.index('cat_price_premium')))
dataframe = dataframe.ix[:, cols]
values= dataframe.values
# fix random seed for reproducibility
seed = 7
np.random.seed(seed)

# convert series to supervised learning
def series_to_supervised(data, n_in=1, n_out=1, dropnan=True):
    n_vars = 1 if type(data) is list else data.shape[1]
    df = DataFrame(data)
    cols, names = list(), list()
    # input sequence (t-n, ... t-1)
    for i in range(n_in, 0, -1):
        cols.append(df.shift(i))
        names += [('var%d(t-%d)' % (j + 1, i)) for j in range(n_vars)]
    # forecast sequence (t, t+1, ... t+n)
    for i in range(0, n_out):
        cols.append(df.shift(-i))
        if i == 0:
            names += [('var%d(t)' % (j + 1)) for j in range(n_vars)]
        else:
            names += [('var%d(t+%d)' % (j + 1, i)) for j in range(n_vars)]
    # put it all together
    agg = concat(cols, axis=1)
    agg.columns = names
    # drop rows with NaN values
    if dropnan:
        agg.dropna(inplace=True)
    return agg



# ensure all data is float
values = values.astype('float32')
# normalize features
scaler = MinMaxScaler(feature_range=(0 ,1))
scaled = scaler.fit_transform(values)
# frame as supervised learning
reframed = series_to_supervised(scaled, 1, 1)
# drop columns we don't want to predict
reframed.drop(reframed.columns[list(range(68,134))], axis=1, inplace=True)
reframed.drop(reframed.columns[0], axis=1, inplace=True)
print(reframed.head())
print(type(reframed))

reframed_values= reframed.values

# split into input (X) and output (Y) variables
X = reframed_values[:,0:65]
Y = reframed_values[:,66]
print(X)
print(Y)

X = np.reshape(X, (X.shape[0], 1, X.shape[1]))
#Y = np.reshape(Y, (Y.shape[0], 1, Y.shape[1]))

# define 10-fold cross validation test harness
kfold = StratifiedKFold(n_splits=10, shuffle=True, random_state=seed)
cvscores = []

"""
# split into train and test sets
values = reframed.values
n_train_hours = 48586
train = values[:n_train_hours, :]
test = values[n_train_hours:, :]
# split into input and outputs
train_X, train_y = train[:, :-1], train[:, -1]
test_X, test_y = test[:, :-1], test[:, -1]
# reshape input to be 3D [samples, timesteps, features]
train_X = train_X.reshape((train_X.shape[0], 1, train_X.shape[1]))
test_X = test_X.reshape((test_X.shape[0], 1, test_X.shape[1]))
print(train_X.shape, train_y.shape, test_X.shape, test_y.shape)
print(train_y)
"""
y_pred_list= []
y_true_list=[]
y_proba=[]
for train, test in kfold.split(X, Y):
    # design network
    model = Sequential()
    model.add(LSTM(100,input_dim=65))
    model.add(Dense(100, kernel_initializer='normal', activation='relu', kernel_constraint=maxnorm(3)))
    model.add(Dropout(0.3))
    model.add(Dense(150, kernel_initializer='normal', activation='relu', kernel_constraint=maxnorm(3)))
    model.add(Dropout(0.3))
    model.add(Dense(1, activation='sigmoid'))
    model.compile(loss='binary_crossentropy', optimizer='Adamax',metrics=['accuracy'])
    # fit network
    model.fit(X[train], Y[train], epochs=19, batch_size=85, verbose=2,shuffle=False)
    # evaluate the model
    scores = model.evaluate(X[test], Y[test], verbose=0)
    print("%s: %.2f%%" % (model.metrics_names[1], scores[1] * 100))
    cvscores.append(scores[1] * 100)
    y_pred = model.predict(X[test])
    y_probabilities= model.predict_proba(X[test])
    y_pred_list.append(list(y_pred))
    y_true_list.append(list(Y[test]))
    y_proba.append(y_probabilities)
    """
    cm = confusion_matrix(Y[test], y_pred)
    print("True Positives: ", cm[0][0])
    print("True Negatives: ", cm[0][1])
    print("False Positives: ",cm[1][0])
    print("False Negatives: ",cm[1][1])
    print(cm)
    """
print("%.2f%% (+/- %.2f%%)" % (np.mean(cvscores), np.std(cvscores)))

#cm = confusion_matrix(y_true_list, y_pred_list)
print(y_true_list)
flat_y_true_list = [x for sublist in y_true_list for x in sublist]
print(y_pred_list)
flat_y_pred_list = [x for sublist in y_pred_list for x in sublist]
final_y_pred_list=[]

flat_y_proba_list = [x for sublist in y_proba for x in sublist]

for values in flat_y_pred_list:
    if values > 0.5:
        final_y_pred_list.append(1)
    else:
        final_y_pred_list.append(0)

print(len(final_y_pred_list))
print(len(flat_y_true_list))

#cm = confusion_matrix(flat_y_true_list, final_y_pred_list)
# Confusion Matrix:
#confusion_matrix = confusion_matrix(flat_y_true_list, final_y_pred_list)
#print(confusion_matrix)
#(cm=confusion_matrix, normalize=False, target_names=['No Purchase', 'Purchase'], title="Confusion Matrix")

conf_matrix = confusion_matrix(flat_y_true_list, final_y_pred_list)
accuracy= accuracy_score(flat_y_true_list, final_y_pred_list)
print("Accuracy: ", round(accuracy,2)*100,'%')
plt.figure(figsize = (5,5))
plt.figtext(.325, .04, "Accuracy = "+str(accuracy))
plt.figtext(.325, 0.9, "Predicted values")
plt.figtext(0.05, 0.55, "Real values", rotation=90)
plt.ylabel('Actual values')
plt.xlabel('Predicted values')
sns.heatmap(conf_matrix, annot=True, fmt='g')
plt.savefig('./confusionMatrix.png')
plt.close()

fpr, tpr, _ = roc_curve(flat_y_true_list, final_y_pred_list)
score = roc_auc_score(flat_y_true_list, final_y_pred_list)
plt.plot(fpr,tpr,label="ROC prediction score ("+str(round(score,2))+")")
fpr2, tpr2, _2 = roc_curve(flat_y_true_list, flat_y_proba_list)
plt.plot(fpr2, tpr2, label="ROC probability score")
plt.plot([0, 1],[0,1], 'k--')
plt.axis([0,1,0,1])
plt.xlabel('False positive rate')
plt.ylabel('True positive rate')
plt.legend(loc=4)
plt.savefig('./rocCurve.png')

"""
# plot history
pyplot.plot(history.history['loss'], label='train')
pyplot.plot(history.history['val_loss'], label='test')
pyplot.legend()
pyplot.show()

# make a prediction
yhat = model.predict(test_X)
test_X = test_X.reshape((test_X.shape[0], test_X.shape[2]))
# invert scaling for forecast
inv_yhat = concatenate((yhat, test_X[:, 1:]), axis=1)
print(inv_yhat)
inv_yhat = scaler.inverse_transform(inv_yhat)
inv_yhat = inv_yhat[:,0]
# invert scaling for actual
test_y = test_y.reshape((len(test_y), 1))
inv_y = concatenate((test_y, test_X[:, 1:]), axis=1)
inv_y = scaler.inverse_transform(inv_y)
inv_y = inv_y[:,0]

def mean_absolute_percentage_error(y_true, y_pred):
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100

# calculate RMSE
rmse = sqrt(mean_squared_error(inv_y, inv_yhat))
print('Test RMSE: %.3f' % rmse)
mae = sqrt(mean_absolute_error(inv_y, inv_yhat))
print('Test MAE: %.3f' % mae)


pyplot.plot(inv_y, color= "r" )
pyplot.plot(inv_yhat, color= "b")
pyplot.show()

treshold=[]
for values in inv_yhat:
    if (values <= 0.5):
        treshold.append(0)
    else:
        treshold.append(1)

print(len(treshold))
print(len(inv_y))
y_true=inv_y.tolist()
y_pred=treshold

confusion= confusion_matrix(y_true,y_pred)

print(confusion)
ax= plt.subplot()
sns.heatmap(confusion, annot=True, ax = ax); #annot=True to annotate cells
# labels, title and ticks
ax.set_xlabel('Predicted labels');ax.set_ylabel('True labels');
ax.set_title('Confusion Matrix');
#ax.xaxis.set_ticklabels(['business', 'health']); ax.yaxis.set_ticklabels(['health', 'business']);
plt.show()
accuracy= accuracy_score(y_true,y_pred)

print("Accuracy: ", accuracy*100,'%')

roc = roc_auc_score(y_true, y_pred)
print("ROC:", roc)
#plot_roc_curve(y_true, y_pred)
fpr, tpr, _ = roc_curve(y_true, y_pred)
score = roc_auc_score(y_true, y_pred)


plt.plot(fpr,tpr,label="ROC prediction score ("+str(round(score,2))+")")
fpr2, tpr2, _2 = roc_curve(y_true, y_pred)
plt.plot(fpr2, tpr2, label="ROC probability score")
plt.plot([0, 1],[0,1], 'k--')
plt.axis([0,1,0,1])
plt.xlabel('False positive rate')
plt.ylabel('True positive rate')
plt.title("ROC Curve")
plt.legend(loc=4)
plt.show()
"""