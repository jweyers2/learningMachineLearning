import pandas as pd
import numpy as np
from sklearn.model_selection import TimeSeriesSplit
import sys
sys.path.insert(0, '../../')
from utils import train_test_split_predictive
useDevDataset = True

path = ''
if (useDevDataset):
    path = '../../../00 Data/Final/developerDatasetScaled.csv'
else:
    path = '../../../00 Data/Final/scaledFinal.csv'
X_train, X_test, y_train, y_test = train_test_split_predictive(useDevDataset, path)
tscv = TimeSeriesSplit(n_splits=5)
for train_index, test_index in tscv.split(X_train):
    print("TRAIN:", train_index, "\n", "TEST:", test_index)
    X_train_train, X_train_test = X_train[:train_index.size], X_train[train_index.size:train_index.size+test_index.size]
    y_train_train, y_train_test = y_train[:train_index.size], y_train[train_index.size:train_index.size+test_index.size]
print(1)

