import pandas as pd
import numpy as np

newPath='../00 Data/Final/binaryFinal.csv'
path='../00 Data/Final/final.csv'
dataframe=pd.read_csv(path)

dataframe['time'] = pd.to_datetime(dataframe['datetime'])

# Add new rows for aggregated price and volume data of both auctions for the las 2-1 days, 9-2 days and 31-9 days
# average price of the previous 48-24 hours
# intraday
dataframe['price_dayahead_lastDay_hour0'] = np.nan
dataframe['price_dayahead_lastDay_hour1'] = np.nan
dataframe['price_dayahead_lastDay_hour2'] = np.nan
dataframe['price_dayahead_lastDay_hour3'] = np.nan
dataframe['price_dayahead_lastDay_hour4'] = np.nan
dataframe['price_dayahead_lastDay_hour5'] = np.nan
dataframe['price_dayahead_lastDay_hour6'] = np.nan
dataframe['price_dayahead_lastDay_hour7'] = np.nan
dataframe['price_dayahead_lastDay_hour8'] = np.nan
dataframe['price_dayahead_lastDay_hour9'] = np.nan
dataframe['price_dayahead_lastDay_hour10'] = np.nan
dataframe['price_dayahead_lastDay_hour11'] = np.nan
dataframe['price_dayahead_lastDay_hour12'] = np.nan
dataframe['price_dayahead_lastDay_hour13'] = np.nan
dataframe['price_dayahead_lastDay_hour14'] = np.nan
dataframe['price_dayahead_lastDay_hour15'] = np.nan
dataframe['price_dayahead_lastDay_hour16'] = np.nan
dataframe['price_dayahead_lastDay_hour17'] = np.nan
dataframe['price_dayahead_lastDay_hour18'] = np.nan
dataframe['price_dayahead_lastDay_hour19'] = np.nan
dataframe['price_dayahead_lastDay_hour20'] = np.nan
dataframe['price_dayahead_lastDay_hour21'] = np.nan
dataframe['price_dayahead_lastDay_hour22'] = np.nan
dataframe['price_dayahead_lastDay_hour23'] = np.nan
dataframe['consumption_dayahead_lastDay_hour0'] = np.nan
dataframe['consumption_dayahead_lastDay_hour1'] = np.nan
dataframe['consumption_dayahead_lastDay_hour2'] = np.nan
dataframe['consumption_dayahead_lastDay_hour3'] = np.nan
dataframe['consumption_dayahead_lastDay_hour4'] = np.nan
dataframe['consumption_dayahead_lastDay_hour5'] = np.nan
dataframe['consumption_dayahead_lastDay_hour6'] = np.nan
dataframe['consumption_dayahead_lastDay_hour7'] = np.nan
dataframe['consumption_dayahead_lastDay_hour8'] = np.nan
dataframe['consumption_dayahead_lastDay_hour9'] = np.nan
dataframe['consumption_dayahead_lastDay_hour10'] = np.nan
dataframe['consumption_dayahead_lastDay_hour11'] = np.nan
dataframe['consumption_dayahead_lastDay_hour12'] = np.nan
dataframe['consumption_dayahead_lastDay_hour13'] = np.nan
dataframe['consumption_dayahead_lastDay_hour14'] = np.nan
dataframe['consumption_dayahead_lastDay_hour15'] = np.nan
dataframe['consumption_dayahead_lastDay_hour16'] = np.nan
dataframe['consumption_dayahead_lastDay_hour17'] = np.nan
dataframe['consumption_dayahead_lastDay_hour18'] = np.nan
dataframe['consumption_dayahead_lastDay_hour19'] = np.nan
dataframe['consumption_dayahead_lastDay_hour20'] = np.nan
dataframe['consumption_dayahead_lastDay_hour21'] = np.nan
dataframe['consumption_dayahead_lastDay_hour22'] = np.nan
dataframe['consumption_dayahead_lastDay_hour23'] = np.nan
dataframe['price_intraday_lastDay_hour0'] = np.nan
dataframe['price_intraday_lastDay_hour1'] = np.nan
dataframe['price_intraday_lastDay_hour2'] = np.nan
dataframe['price_intraday_lastDay_hour3'] = np.nan
dataframe['price_intraday_lastDay_hour4'] = np.nan
dataframe['price_intraday_lastDay_hour5'] = np.nan
dataframe['price_intraday_lastDay_hour6'] = np.nan
dataframe['price_intraday_lastDay_hour7'] = np.nan
dataframe['price_intraday_lastDay_hour8'] = np.nan
dataframe['price_intraday_lastDay_hour9'] = np.nan
dataframe['price_intraday_lastDay_hour10'] = np.nan
dataframe['price_intraday_lastDay_hour11'] = np.nan
dataframe['price_intraday_lastDay_hour12'] = np.nan
dataframe['price_intraday_lastDay_hour13'] = np.nan
dataframe['price_intraday_lastDay_hour14'] = np.nan
dataframe['price_intraday_lastDay_hour15'] = np.nan
dataframe['price_intraday_lastDay_hour16'] = np.nan
dataframe['price_intraday_lastDay_hour17'] = np.nan
dataframe['price_intraday_lastDay_hour18'] = np.nan
dataframe['price_intraday_lastDay_hour19'] = np.nan
dataframe['price_intraday_lastDay_hour20'] = np.nan
dataframe['price_intraday_lastDay_hour21'] = np.nan
dataframe['price_intraday_lastDay_hour22'] = np.nan
dataframe['price_intraday_lastDay_hour23'] = np.nan
dataframe['consumption_intraday_lastDay_hour0'] = np.nan
dataframe['consumption_intraday_lastDay_hour1'] = np.nan
dataframe['consumption_intraday_lastDay_hour2'] = np.nan
dataframe['consumption_intraday_lastDay_hour3'] = np.nan
dataframe['consumption_intraday_lastDay_hour4'] = np.nan
dataframe['consumption_intraday_lastDay_hour5'] = np.nan
dataframe['consumption_intraday_lastDay_hour6'] = np.nan
dataframe['consumption_intraday_lastDay_hour7'] = np.nan
dataframe['consumption_intraday_lastDay_hour8'] = np.nan
dataframe['consumption_intraday_lastDay_hour9'] = np.nan
dataframe['consumption_intraday_lastDay_hour10'] = np.nan
dataframe['consumption_intraday_lastDay_hour11'] = np.nan
dataframe['consumption_intraday_lastDay_hour12'] = np.nan
dataframe['consumption_intraday_lastDay_hour13'] = np.nan
dataframe['consumption_intraday_lastDay_hour14'] = np.nan
dataframe['consumption_intraday_lastDay_hour15'] = np.nan
dataframe['consumption_intraday_lastDay_hour16'] = np.nan
dataframe['consumption_intraday_lastDay_hour17'] = np.nan
dataframe['consumption_intraday_lastDay_hour18'] = np.nan
dataframe['consumption_intraday_lastDay_hour19'] = np.nan
dataframe['consumption_intraday_lastDay_hour20'] = np.nan
dataframe['consumption_intraday_lastDay_hour21'] = np.nan
dataframe['consumption_intraday_lastDay_hour22'] = np.nan
dataframe['consumption_intraday_lastDay_hour23'] = np.nan

for index, row in dataframe.iterrows():
    # skip the first 2 days
    if index > 191:
        # dayahead
        dataframe.at[index, 'price_dayahead_lastDay_hour0'] = dataframe.iloc[index - 192:index - 188]['price_dayahead'].mean()
        dataframe.at[index, 'price_dayahead_lastDay_hour1'] = dataframe.iloc[index - 188:index - 184]['price_dayahead'].mean()
        dataframe.at[index, 'price_dayahead_lastDay_hour2'] = dataframe.iloc[index - 184:index - 180]['price_dayahead'].mean()
        dataframe.at[index, 'price_dayahead_lastDay_hour3'] = dataframe.iloc[index - 180:index - 176]['price_dayahead'].mean()
        dataframe.at[index, 'price_dayahead_lastDay_hour4'] = dataframe.iloc[index - 176:index - 172]['price_dayahead'].mean()
        dataframe.at[index, 'price_dayahead_lastDay_hour5'] = dataframe.iloc[index - 172:index - 168]['price_dayahead'].mean()
        dataframe.at[index, 'price_dayahead_lastDay_hour6'] = dataframe.iloc[index - 168:index - 164]['price_dayahead'].mean()
        dataframe.at[index, 'price_dayahead_lastDay_hour7'] = dataframe.iloc[index - 164:index - 160]['price_dayahead'].mean()
        dataframe.at[index, 'price_dayahead_lastDay_hour8'] = dataframe.iloc[index - 160:index - 156]['price_dayahead'].mean()
        dataframe.at[index, 'price_dayahead_lastDay_hour9'] = dataframe.iloc[index - 156:index - 152]['price_dayahead'].mean()
        dataframe.at[index, 'price_dayahead_lastDay_hour10'] = dataframe.iloc[index - 152:index - 148]['price_dayahead'].mean()
        dataframe.at[index, 'price_dayahead_lastDay_hour11'] = dataframe.iloc[index - 148:index - 144]['price_dayahead'].mean()
        dataframe.at[index, 'price_dayahead_lastDay_hour12'] = dataframe.iloc[index - 144:index - 140]['price_dayahead'].mean()
        dataframe.at[index, 'price_dayahead_lastDay_hour13'] = dataframe.iloc[index - 140:index - 136]['price_dayahead'].mean()
        dataframe.at[index, 'price_dayahead_lastDay_hour14'] = dataframe.iloc[index - 136:index - 132]['price_dayahead'].mean()
        dataframe.at[index, 'price_dayahead_lastDay_hour15'] = dataframe.iloc[index - 132:index - 128]['price_dayahead'].mean()
        dataframe.at[index, 'price_dayahead_lastDay_hour16'] = dataframe.iloc[index - 128:index - 124]['price_dayahead'].mean()
        dataframe.at[index, 'price_dayahead_lastDay_hour17'] = dataframe.iloc[index - 124:index - 120]['price_dayahead'].mean()
        dataframe.at[index, 'price_dayahead_lastDay_hour18'] = dataframe.iloc[index - 120:index - 116]['price_dayahead'].mean()
        dataframe.at[index, 'price_dayahead_lastDay_hour19'] = dataframe.iloc[index - 116:index - 112]['price_dayahead'].mean()
        dataframe.at[index, 'price_dayahead_lastDay_hour20'] = dataframe.iloc[index - 112:index - 108]['price_dayahead'].mean()
        dataframe.at[index, 'price_dayahead_lastDay_hour21'] = dataframe.iloc[index - 108:index - 104]['price_dayahead'].mean()
        dataframe.at[index, 'price_dayahead_lastDay_hour22'] = dataframe.iloc[index - 104:index - 100]['price_dayahead'].mean()
        dataframe.at[index, 'price_dayahead_lastDay_hour23'] = dataframe.iloc[index - 100:index - 96]['price_dayahead'].mean()
        dataframe.at[index, 'consumption_dayahead_lastDay_hour0'] = dataframe.iloc[index - 192:index - 188]['consumption_dayahead'].mean()
        dataframe.at[index, 'consumption_dayahead_lastDay_hour1'] = dataframe.iloc[index - 188:index - 184]['consumption_dayahead'].mean()
        dataframe.at[index, 'consumption_dayahead_lastDay_hour2'] = dataframe.iloc[index - 184:index - 180]['consumption_dayahead'].mean()
        dataframe.at[index, 'consumption_dayahead_lastDay_hour3'] = dataframe.iloc[index - 180:index - 176]['consumption_dayahead'].mean()
        dataframe.at[index, 'consumption_dayahead_lastDay_hour4'] = dataframe.iloc[index - 176:index - 172]['consumption_dayahead'].mean()
        dataframe.at[index, 'consumption_dayahead_lastDay_hour5'] = dataframe.iloc[index - 172:index - 168]['consumption_dayahead'].mean()
        dataframe.at[index, 'consumption_dayahead_lastDay_hour6'] = dataframe.iloc[index - 168:index - 164]['consumption_dayahead'].mean()
        dataframe.at[index, 'consumption_dayahead_lastDay_hour7'] = dataframe.iloc[index - 164:index - 160]['consumption_dayahead'].mean()
        dataframe.at[index, 'consumption_dayahead_lastDay_hour8'] = dataframe.iloc[index - 160:index - 156]['consumption_dayahead'].mean()
        dataframe.at[index, 'consumption_dayahead_lastDay_hour9'] = dataframe.iloc[index - 156:index - 152]['consumption_dayahead'].mean()
        dataframe.at[index, 'consumption_dayahead_lastDay_hour10'] = dataframe.iloc[index - 152:index - 148]['consumption_dayahead'].mean()
        dataframe.at[index, 'consumption_dayahead_lastDay_hour11'] = dataframe.iloc[index - 148:index - 144]['consumption_dayahead'].mean()
        dataframe.at[index, 'consumption_dayahead_lastDay_hour12'] = dataframe.iloc[index - 144:index - 140]['consumption_dayahead'].mean()
        dataframe.at[index, 'consumption_dayahead_lastDay_hour13'] = dataframe.iloc[index - 140:index - 136]['consumption_dayahead'].mean()
        dataframe.at[index, 'consumption_dayahead_lastDay_hour14'] = dataframe.iloc[index - 136:index - 132]['consumption_dayahead'].mean()
        dataframe.at[index, 'consumption_dayahead_lastDay_hour15'] = dataframe.iloc[index - 132:index - 128]['consumption_dayahead'].mean()
        dataframe.at[index, 'consumption_dayahead_lastDay_hour16'] = dataframe.iloc[index - 128:index - 124]['consumption_dayahead'].mean()
        dataframe.at[index, 'consumption_dayahead_lastDay_hour17'] = dataframe.iloc[index - 124:index - 120]['consumption_dayahead'].mean()
        dataframe.at[index, 'consumption_dayahead_lastDay_hour18'] = dataframe.iloc[index - 120:index - 116]['consumption_dayahead'].mean()
        dataframe.at[index, 'consumption_dayahead_lastDay_hour19'] = dataframe.iloc[index - 116:index - 112]['consumption_dayahead'].mean()
        dataframe.at[index, 'consumption_dayahead_lastDay_hour20'] = dataframe.iloc[index - 112:index - 108]['consumption_dayahead'].mean()
        dataframe.at[index, 'consumption_dayahead_lastDay_hour21'] = dataframe.iloc[index - 108:index - 104]['consumption_dayahead'].mean()
        dataframe.at[index, 'consumption_dayahead_lastDay_hour22'] = dataframe.iloc[index - 104:index - 100]['consumption_dayahead'].mean()
        dataframe.at[index, 'consumption_dayahead_lastDay_hour23'] = dataframe.iloc[index - 100:index - 96]['consumption_dayahead'].mean()
        # intraday
        dataframe.at[index, 'price_intraday_lastDay_hour0'] = dataframe.iloc[index - 97:index - 93]['price'].mean()
        dataframe.at[index, 'price_intraday_lastDay_hour1'] = dataframe.iloc[index - 93:index - 89]['price'].mean()
        dataframe.at[index, 'price_intraday_lastDay_hour2'] = dataframe.iloc[index - 89:index - 85]['price'].mean()
        dataframe.at[index, 'price_intraday_lastDay_hour3'] = dataframe.iloc[index - 85:index - 81]['price'].mean()
        dataframe.at[index, 'price_intraday_lastDay_hour4'] = dataframe.iloc[index - 81:index - 77]['price'].mean()
        dataframe.at[index, 'price_intraday_lastDay_hour5'] = dataframe.iloc[index - 77:index - 73]['price'].mean()
        dataframe.at[index, 'price_intraday_lastDay_hour6'] = dataframe.iloc[index - 73:index - 69]['price'].mean()
        dataframe.at[index, 'price_intraday_lastDay_hour7'] = dataframe.iloc[index - 69:index - 65]['price'].mean()
        dataframe.at[index, 'price_intraday_lastDay_hour8'] = dataframe.iloc[index - 65:index - 61]['price'].mean()
        dataframe.at[index, 'price_intraday_lastDay_hour9'] = dataframe.iloc[index - 61:index - 57]['price'].mean()
        dataframe.at[index, 'price_intraday_lastDay_hour10'] = dataframe.iloc[index - 57:index - 53]['price'].mean()
        dataframe.at[index, 'price_intraday_lastDay_hour11'] = dataframe.iloc[index - 53:index - 49]['price'].mean()
        dataframe.at[index, 'price_intraday_lastDay_hour12'] = dataframe.iloc[index - 49:index - 45]['price'].mean()
        dataframe.at[index, 'price_intraday_lastDay_hour13'] = dataframe.iloc[index - 45:index - 41]['price'].mean()
        dataframe.at[index, 'price_intraday_lastDay_hour14'] = dataframe.iloc[index - 41:index - 37]['price'].mean()
        dataframe.at[index, 'price_intraday_lastDay_hour15'] = dataframe.iloc[index - 37:index - 33]['price'].mean()
        dataframe.at[index, 'price_intraday_lastDay_hour16'] = dataframe.iloc[index - 33:index - 29]['price'].mean()
        dataframe.at[index, 'price_intraday_lastDay_hour17'] = dataframe.iloc[index - 29:index - 25]['price'].mean()
        dataframe.at[index, 'price_intraday_lastDay_hour18'] = dataframe.iloc[index - 25:index - 21]['price'].mean()
        dataframe.at[index, 'price_intraday_lastDay_hour19'] = dataframe.iloc[index - 21:index - 17]['price'].mean()
        dataframe.at[index, 'price_intraday_lastDay_hour20'] = dataframe.iloc[index - 17:index - 13]['price'].mean()
        dataframe.at[index, 'price_intraday_lastDay_hour21'] = dataframe.iloc[index - 13:index - 9]['price'].mean()
        dataframe.at[index, 'price_intraday_lastDay_hour22'] = dataframe.iloc[index - 9:index - 5]['price'].mean()
        dataframe.at[index, 'price_intraday_lastDay_hour23'] = dataframe.iloc[index - 5:index - 1]['price'].mean()
        dataframe.at[index, 'consumption_intraday_lastDay_hour0'] = dataframe.iloc[index - 97:index - 93]['consumption'].mean()
        dataframe.at[index, 'consumption_intraday_lastDay_hour1'] = dataframe.iloc[index - 93:index - 89]['consumption'].mean()
        dataframe.at[index, 'consumption_intraday_lastDay_hour2'] = dataframe.iloc[index - 89:index - 85]['consumption'].mean()
        dataframe.at[index, 'consumption_intraday_lastDay_hour3'] = dataframe.iloc[index - 85:index - 81]['consumption'].mean()
        dataframe.at[index, 'consumption_intraday_lastDay_hour4'] = dataframe.iloc[index - 81:index - 77]['consumption'].mean()
        dataframe.at[index, 'consumption_intraday_lastDay_hour5'] = dataframe.iloc[index - 77:index - 73]['consumption'].mean()
        dataframe.at[index, 'consumption_intraday_lastDay_hour6'] = dataframe.iloc[index - 73:index - 69]['consumption'].mean()
        dataframe.at[index, 'consumption_intraday_lastDay_hour7'] = dataframe.iloc[index - 69:index - 65]['consumption'].mean()
        dataframe.at[index, 'consumption_intraday_lastDay_hour8'] = dataframe.iloc[index - 65:index - 61]['consumption'].mean()
        dataframe.at[index, 'consumption_intraday_lastDay_hour9'] = dataframe.iloc[index - 61:index - 57]['consumption'].mean()
        dataframe.at[index, 'consumption_intraday_lastDay_hour10'] = dataframe.iloc[index - 57:index - 53]['consumption'].mean()
        dataframe.at[index, 'consumption_intraday_lastDay_hour11'] = dataframe.iloc[index - 53:index - 49]['consumption'].mean()
        dataframe.at[index, 'consumption_intraday_lastDay_hour12'] = dataframe.iloc[index - 49:index - 45]['consumption'].mean()
        dataframe.at[index, 'consumption_intraday_lastDay_hour13'] = dataframe.iloc[index - 45:index - 41]['consumption'].mean()
        dataframe.at[index, 'consumption_intraday_lastDay_hour14'] = dataframe.iloc[index - 41:index - 37]['consumption'].mean()
        dataframe.at[index, 'consumption_intraday_lastDay_hour15'] = dataframe.iloc[index - 37:index - 33]['consumption'].mean()
        dataframe.at[index, 'consumption_intraday_lastDay_hour16'] = dataframe.iloc[index - 33:index - 29]['consumption'].mean()
        dataframe.at[index, 'consumption_intraday_lastDay_hour17'] = dataframe.iloc[index - 29:index - 25]['consumption'].mean()
        dataframe.at[index, 'consumption_intraday_lastDay_hour18'] = dataframe.iloc[index - 25:index - 21]['consumption'].mean()
        dataframe.at[index, 'consumption_intraday_lastDay_hour19'] = dataframe.iloc[index - 21:index - 17]['consumption'].mean()
        dataframe.at[index, 'consumption_intraday_lastDay_hour20'] = dataframe.iloc[index - 17:index - 13]['consumption'].mean()
        dataframe.at[index, 'consumption_intraday_lastDay_hour21'] = dataframe.iloc[index - 13:index - 9]['consumption'].mean()
        dataframe.at[index, 'consumption_intraday_lastDay_hour22'] = dataframe.iloc[index - 9:index - 5]['consumption'].mean()
        dataframe.at[index, 'consumption_intraday_lastDay_hour23'] = dataframe.iloc[index - 5:index - 1]['consumption'].mean()



# Drop the first 2 days
dataframe = dataframe.drop(index=range(0,192))

# categorical price premium
dataframe['cat_price_premium'] = (dataframe['price_premium'] > 0).astype(int)
# = 1 if day ahead price > intraday price

# months
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

# weekdays
dataframe['monday'] = (pd.DatetimeIndex(dataframe['datetime']).weekday == 0).astype(int)
dataframe['tuesday'] = (pd.DatetimeIndex(dataframe['datetime']).weekday == 1).astype(int)
dataframe['wednesday'] = (pd.DatetimeIndex(dataframe['datetime']).weekday == 2).astype(int)
dataframe['thursday'] = (pd.DatetimeIndex(dataframe['datetime']).weekday == 3).astype(int)
dataframe['friday'] = (pd.DatetimeIndex(dataframe['datetime']).weekday == 4).astype(int)
dataframe['saturday'] = (pd.DatetimeIndex(dataframe['datetime']).weekday == 5).astype(int)
dataframe['sunday'] = (pd.DatetimeIndex(dataframe['datetime']).weekday == 6).astype(int)

# hours
for i in range (24):
    hour = 'hour' + str(i)
    dataframe[hour] = (pd.DatetimeIndex(dataframe['datetime']).hour == i).astype(int)

dataframe.to_csv(newPath, index=False)
