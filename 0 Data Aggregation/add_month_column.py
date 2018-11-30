import pandas as pd
import numpy as np

path='../00 Data/Final/cleanFinal.csv'
dataframe=pd.read_csv(path)

dataframe['month'] = pd.DatetimeIndex(dataframe['datetime']).month

dataframe.to_csv(path,index=False)

