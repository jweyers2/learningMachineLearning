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
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import GridSearchCV
from keras.optimizers import SGD
from keras.constraints import maxnorm

path='../../00 Data/Final/binaryFinal.csv'
dataframe=pd.read_csv(path)
print("Länge:", len(dataframe))
dataframe.drop(['datetime'], axis=1, inplace=True)
cols = list(dataframe)
cols.insert(0, cols.pop(cols.index('cat_price_premium')))
dataframe = dataframe.ix[:, cols]
values= dataframe.values

# Function to create model, required for KerasClassifier
def create_model(activation='relu'):
    model = Sequential()
    model.add(LSTM(100, input_dim=71))
    model.add(Dense(100, kernel_initializer='normal', activation=activation))
    model.add(Dense(200, kernel_initializer='normal', activation=activation))
    model.add(Dense(1, activation='sigmoid'))
    optimizer = SGD(lr=0.1, momentum=0.0)
    model.compile(loss='binary_crossentropy', optimizer='Adamax', metrics=['accuracy'])
    return model

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
print(reframed)

reframed.drop(reframed.columns[list(range(73,144))], axis=1, inplace=True)
print(reframed.head())
print(type(reframed))
reframed_values= reframed.values

# split into input (X) and output (Y) variables
X = reframed_values[:,0:71]
Y = reframed_values[:,72]

X = np.reshape(X, (X.shape[0], 1, X.shape[1]))

# create model
model = KerasClassifier(build_fn=create_model, epochs=100, batch_size=10, verbose=0)
# define the grid search parameters
activation = ['softmax', 'softplus', 'softsign', 'relu', 'tanh', 'sigmoid', 'hard_sigmoid', 'linear']
param_grid = dict(activation=activation)
grid = GridSearchCV(estimator=model, param_grid=param_grid, n_jobs=-1, cv=10)
grid_result = grid.fit(X, Y)
# summarize results
print("Best: %f using %s" % (grid_result.best_score_, grid_result.best_params_))
means = grid_result.cv_results_['mean_test_score']
stds = grid_result.cv_results_['std_test_score']
params = grid_result.cv_results_['params']
for mean, stdev, param in zip(means, stds, params):
    print("%f (%f) with: %r" % (mean, stdev, param))