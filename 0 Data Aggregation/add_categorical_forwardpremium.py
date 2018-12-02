import pandas as pd

path = '../00 Data/Final/cleanFinal.csv'
dataframe = pd.read_csv(path, dayfirst=True)
dataframe['cat_price_premium'] = (dataframe['price_premium'] > 0).astype(int)
# = 1 if day ahead price > intraday price

dataframe.to_csv(path, index=False)
