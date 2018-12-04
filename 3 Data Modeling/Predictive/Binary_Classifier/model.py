import pandas as pd
import numpy as np
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
print(1)

