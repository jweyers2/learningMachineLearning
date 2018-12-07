import pandas as pd

newPath='../00 Data/Final/binaryFinal.csv'
path='../00 Data/Final/final.csv'
dataframe=pd.read_csv(path)

#categorical price premium
dataframe['cat_price_premium'] = (dataframe['price_premium'] > 0).astype(int)
# = 1 if day ahead price > intraday price

#months
dataframe['january'] = (pd.DatetimeIndex(dataframe['datetime']).month == 1).astype(int)
dataframe['february'] = (pd.DatetimeIndex(dataframe['datetime']).month == 2).astype(int)
dataframe['march'] = (pd.DatetimeIndex(dataframe['datetime']).month == 3).astype(int)
dataframe['april'] = (pd.DatetimeIndex(dataframe['datetime']).month == 4).astype(int)
dataframe['may'] = (pd.DatetimeIndex(dataframe['datetime']).month == 5).astype(int)
dataframe['june'] = (pd.DatetimeIndex(dataframe['datetime']).month == 6).astype(int)
dataframe['july'] = (pd.DatetimeIndex(dataframe['datetime']).month == 7).astype(int)
dataframe['august'] = (pd.DatetimeIndex(dataframe['datetime']).month == 8).astype(int)
dataframe['september'] = (pd.DatetimeIndex(dataframe['datetime']).month == 9).astype(int)
dataframe['october'] = (pd.DatetimeIndex(dataframe['datetime']).month == 10).astype(int)
dataframe['november'] = (pd.DatetimeIndex(dataframe['datetime']).month == 11).astype(int)
dataframe['december'] = (pd.DatetimeIndex(dataframe['datetime']).month == 12).astype(int)

#weekdays
dataframe['monday'] = (pd.DatetimeIndex(dataframe['datetime']).weekday == 0).astype(int)
dataframe['tuesday'] = (pd.DatetimeIndex(dataframe['datetime']).weekday == 1).astype(int)
dataframe['wednesday'] = (pd.DatetimeIndex(dataframe['datetime']).weekday == 2).astype(int)
dataframe['thursday'] = (pd.DatetimeIndex(dataframe['datetime']).weekday == 3).astype(int)
dataframe['friday'] = (pd.DatetimeIndex(dataframe['datetime']).weekday == 4).astype(int)
dataframe['saturday'] = (pd.DatetimeIndex(dataframe['datetime']).weekday == 5).astype(int)
dataframe['sunday'] = (pd.DatetimeIndex(dataframe['datetime']).weekday == 6).astype(int)

#hours
for i in range (24):
    hour =  'hour' + str(i)
    dataframe[hour] = (pd.DatetimeIndex(dataframe['datetime']).hour == i).astype(int)

dataframe.to_csv(newPath, index=False)
