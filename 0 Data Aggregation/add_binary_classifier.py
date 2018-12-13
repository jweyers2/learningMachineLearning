import pandas as pd
import numpy as np

newPath='../00 Data/Final/binaryFinal.csv'
path='../00 Data/Final/final.csv'
dataframe=pd.read_csv(path)

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

# dataframe['time'] = pd.to_datetime(dataframe['datetime'])
#
# Add new rows for aggregated price and volume data of both auctions for the las 2-1 days, 9-2 days and 31-9 days
# 48 to 24 hours before the time slot where the price premium has to be predicted
# dataframe['price_dayahead_lastDay_hour0'] = np.nan
# dataframe['price_dayahead_lastDay_hour1'] = np.nan
# dataframe['price_dayahead_lastDay_hour2'] = np.nan
# dataframe['price_dayahead_lastDay_hour3'] = np.nan
# dataframe['price_dayahead_lastDay_hour4'] = np.nan
# dataframe['price_dayahead_lastDay_hour5'] = np.nan
# dataframe['price_dayahead_lastDay_hour6'] = np.nan
# dataframe['price_dayahead_lastDay_hour7'] = np.nan
# dataframe['price_dayahead_lastDay_hour8'] = np.nan
# dataframe['price_dayahead_lastDay_hour9'] = np.nan
# dataframe['price_dayahead_lastDay_hour10'] = np.nan
# dataframe['price_dayahead_lastDay_hour11'] = np.nan
# dataframe['price_dayahead_lastDay_hour12'] = np.nan
# dataframe['price_dayahead_lastDay_hour13'] = np.nan
# dataframe['price_dayahead_lastDay_hour14'] = np.nan
# dataframe['price_dayahead_lastDay_hour15'] = np.nan
# dataframe['price_dayahead_lastDay_hour16'] = np.nan
# dataframe['price_dayahead_lastDay_hour17'] = np.nan
# dataframe['price_dayahead_lastDay_hour18'] = np.nan
# dataframe['price_dayahead_lastDay_hour19'] = np.nan
# dataframe['price_dayahead_lastDay_hour20'] = np.nan
# dataframe['price_dayahead_lastDay_hour21'] = np.nan
# dataframe['price_dayahead_lastDay_hour22'] = np.nan
# dataframe['price_dayahead_lastDay_hour23'] = np.nan
# dataframe['consumption_dayahead_lastDay_hour0'] = np.nan
# dataframe['consumption_dayahead_lastDay_hour1'] = np.nan
# dataframe['consumption_dayahead_lastDay_hour2'] = np.nan
# dataframe['consumption_dayahead_lastDay_hour3'] = np.nan
# dataframe['consumption_dayahead_lastDay_hour4'] = np.nan
# dataframe['consumption_dayahead_lastDay_hour5'] = np.nan
# dataframe['consumption_dayahead_lastDay_hour6'] = np.nan
# dataframe['consumption_dayahead_lastDay_hour7'] = np.nan
# dataframe['consumption_dayahead_lastDay_hour8'] = np.nan
# dataframe['consumption_dayahead_lastDay_hour9'] = np.nan
# dataframe['consumption_dayahead_lastDay_hour10'] = np.nan
# dataframe['consumption_dayahead_lastDay_hour11'] = np.nan
# dataframe['consumption_dayahead_lastDay_hour12'] = np.nan
# dataframe['consumption_dayahead_lastDay_hour13'] = np.nan
# dataframe['consumption_dayahead_lastDay_hour14'] = np.nan
# dataframe['consumption_dayahead_lastDay_hour15'] = np.nan
# dataframe['consumption_dayahead_lastDay_hour16'] = np.nan
# dataframe['consumption_dayahead_lastDay_hour17'] = np.nan
# dataframe['consumption_dayahead_lastDay_hour18'] = np.nan
# dataframe['consumption_dayahead_lastDay_hour19'] = np.nan
# dataframe['consumption_dayahead_lastDay_hour20'] = np.nan
# dataframe['consumption_dayahead_lastDay_hour21'] = np.nan
# dataframe['consumption_dayahead_lastDay_hour22'] = np.nan
# dataframe['consumption_dayahead_lastDay_hour23'] = np.nan
# dataframe['price_intraday_lastDay_hour0'] = np.nan
# dataframe['price_intraday_lastDay_hour1'] = np.nan
# dataframe['price_intraday_lastDay_hour2'] = np.nan
# dataframe['price_intraday_lastDay_hour3'] = np.nan
# dataframe['price_intraday_lastDay_hour4'] = np.nan
# dataframe['price_intraday_lastDay_hour5'] = np.nan
# dataframe['price_intraday_lastDay_hour6'] = np.nan
# dataframe['price_intraday_lastDay_hour7'] = np.nan
# dataframe['price_intraday_lastDay_hour8'] = np.nan
# dataframe['price_intraday_lastDay_hour9'] = np.nan
# dataframe['price_intraday_lastDay_hour10'] = np.nan
# dataframe['price_intraday_lastDay_hour11'] = np.nan
# dataframe['price_intraday_lastDay_hour12'] = np.nan
# dataframe['price_intraday_lastDay_hour13'] = np.nan
# dataframe['price_intraday_lastDay_hour14'] = np.nan
# dataframe['price_intraday_lastDay_hour15'] = np.nan
# dataframe['price_intraday_lastDay_hour16'] = np.nan
# dataframe['price_intraday_lastDay_hour17'] = np.nan
# dataframe['price_intraday_lastDay_hour18'] = np.nan
# dataframe['price_intraday_lastDay_hour19'] = np.nan
# dataframe['price_intraday_lastDay_hour20'] = np.nan
# dataframe['price_intraday_lastDay_hour21'] = np.nan
# dataframe['price_intraday_lastDay_hour22'] = np.nan
# dataframe['price_intraday_lastDay_hour23'] = np.nan
# dataframe['consumption_intraday_lastDay_hour0'] = np.nan
# dataframe['consumption_intraday_lastDay_hour1'] = np.nan
# dataframe['consumption_intraday_lastDay_hour2'] = np.nan
# dataframe['consumption_intraday_lastDay_hour3'] = np.nan
# dataframe['consumption_intraday_lastDay_hour4'] = np.nan
# dataframe['consumption_intraday_lastDay_hour5'] = np.nan
# dataframe['consumption_intraday_lastDay_hour6'] = np.nan
# dataframe['consumption_intraday_lastDay_hour7'] = np.nan
# dataframe['consumption_intraday_lastDay_hour8'] = np.nan
# dataframe['consumption_intraday_lastDay_hour9'] = np.nan
# dataframe['consumption_intraday_lastDay_hour10'] = np.nan
# dataframe['consumption_intraday_lastDay_hour11'] = np.nan
# dataframe['consumption_intraday_lastDay_hour12'] = np.nan
# dataframe['consumption_intraday_lastDay_hour13'] = np.nan
# dataframe['consumption_intraday_lastDay_hour14'] = np.nan
# dataframe['consumption_intraday_lastDay_hour15'] = np.nan
# dataframe['consumption_intraday_lastDay_hour16'] = np.nan
# dataframe['consumption_intraday_lastDay_hour17'] = np.nan
# dataframe['consumption_intraday_lastDay_hour18'] = np.nan
# dataframe['consumption_intraday_lastDay_hour19'] = np.nan
# dataframe['consumption_intraday_lastDay_hour20'] = np.nan
# dataframe['consumption_intraday_lastDay_hour21'] = np.nan
# dataframe['consumption_intraday_lastDay_hour22'] = np.nan
# dataframe['consumption_intraday_lastDay_hour23'] = np.nan
# # 8 to 2 days before the time slot where the price premium has to be predicted
# dataframe['price_dayahead_lastWeek_hour0'] = np.nan
# dataframe['price_dayahead_lastWeek_hour1'] = np.nan
# dataframe['price_dayahead_lastWeek_hour2'] = np.nan
# dataframe['price_dayahead_lastWeek_hour3'] = np.nan
# dataframe['price_dayahead_lastWeek_hour4'] = np.nan
# dataframe['price_dayahead_lastWeek_hour5'] = np.nan
# dataframe['price_dayahead_lastWeek_hour6'] = np.nan
# dataframe['price_dayahead_lastWeek_hour7'] = np.nan
# dataframe['price_dayahead_lastWeek_hour8'] = np.nan
# dataframe['price_dayahead_lastWeek_hour9'] = np.nan
# dataframe['price_dayahead_lastWeek_hour10'] = np.nan
# dataframe['price_dayahead_lastWeek_hour11'] = np.nan
# dataframe['price_dayahead_lastWeek_hour12'] = np.nan
# dataframe['price_dayahead_lastWeek_hour13'] = np.nan
# dataframe['price_dayahead_lastWeek_hour14'] = np.nan
# dataframe['price_dayahead_lastWeek_hour15'] = np.nan
# dataframe['price_dayahead_lastWeek_hour16'] = np.nan
# dataframe['price_dayahead_lastWeek_hour17'] = np.nan
# dataframe['price_dayahead_lastWeek_hour18'] = np.nan
# dataframe['price_dayahead_lastWeek_hour19'] = np.nan
# dataframe['price_dayahead_lastWeek_hour20'] = np.nan
# dataframe['price_dayahead_lastWeek_hour21'] = np.nan
# dataframe['price_dayahead_lastWeek_hour22'] = np.nan
# dataframe['price_dayahead_lastWeek_hour23'] = np.nan
# dataframe['consumption_dayahead_lastWeek_hour0'] = np.nan
# dataframe['consumption_dayahead_lastWeek_hour1'] = np.nan
# dataframe['consumption_dayahead_lastWeek_hour2'] = np.nan
# dataframe['consumption_dayahead_lastWeek_hour3'] = np.nan
# dataframe['consumption_dayahead_lastWeek_hour4'] = np.nan
# dataframe['consumption_dayahead_lastWeek_hour5'] = np.nan
# dataframe['consumption_dayahead_lastWeek_hour6'] = np.nan
# dataframe['consumption_dayahead_lastWeek_hour7'] = np.nan
# dataframe['consumption_dayahead_lastWeek_hour8'] = np.nan
# dataframe['consumption_dayahead_lastWeek_hour9'] = np.nan
# dataframe['consumption_dayahead_lastWeek_hour10'] = np.nan
# dataframe['consumption_dayahead_lastWeek_hour11'] = np.nan
# dataframe['consumption_dayahead_lastWeek_hour12'] = np.nan
# dataframe['consumption_dayahead_lastWeek_hour13'] = np.nan
# dataframe['consumption_dayahead_lastWeek_hour14'] = np.nan
# dataframe['consumption_dayahead_lastWeek_hour15'] = np.nan
# dataframe['consumption_dayahead_lastWeek_hour16'] = np.nan
# dataframe['consumption_dayahead_lastWeek_hour17'] = np.nan
# dataframe['consumption_dayahead_lastWeek_hour18'] = np.nan
# dataframe['consumption_dayahead_lastWeek_hour19'] = np.nan
# dataframe['consumption_dayahead_lastWeek_hour20'] = np.nan
# dataframe['consumption_dayahead_lastWeek_hour21'] = np.nan
# dataframe['consumption_dayahead_lastWeek_hour22'] = np.nan
# dataframe['consumption_dayahead_lastWeek_hour23'] = np.nan
# dataframe['price_intraday_lastWeek_hour0'] = np.nan
# dataframe['price_intraday_lastWeek_hour1'] = np.nan
# dataframe['price_intraday_lastWeek_hour2'] = np.nan
# dataframe['price_intraday_lastWeek_hour3'] = np.nan
# dataframe['price_intraday_lastWeek_hour4'] = np.nan
# dataframe['price_intraday_lastWeek_hour5'] = np.nan
# dataframe['price_intraday_lastWeek_hour6'] = np.nan
# dataframe['price_intraday_lastWeek_hour7'] = np.nan
# dataframe['price_intraday_lastWeek_hour8'] = np.nan
# dataframe['price_intraday_lastWeek_hour9'] = np.nan
# dataframe['price_intraday_lastWeek_hour10'] = np.nan
# dataframe['price_intraday_lastWeek_hour11'] = np.nan
# dataframe['price_intraday_lastWeek_hour12'] = np.nan
# dataframe['price_intraday_lastWeek_hour13'] = np.nan
# dataframe['price_intraday_lastWeek_hour14'] = np.nan
# dataframe['price_intraday_lastWeek_hour15'] = np.nan
# dataframe['price_intraday_lastWeek_hour16'] = np.nan
# dataframe['price_intraday_lastWeek_hour17'] = np.nan
# dataframe['price_intraday_lastWeek_hour18'] = np.nan
# dataframe['price_intraday_lastWeek_hour19'] = np.nan
# dataframe['price_intraday_lastWeek_hour20'] = np.nan
# dataframe['price_intraday_lastWeek_hour21'] = np.nan
# dataframe['price_intraday_lastWeek_hour22'] = np.nan
# dataframe['price_intraday_lastWeek_hour23'] = np.nan
# dataframe['consumption_intraday_lastWeek_hour0'] = np.nan
# dataframe['consumption_intraday_lastWeek_hour1'] = np.nan
# dataframe['consumption_intraday_lastWeek_hour2'] = np.nan
# dataframe['consumption_intraday_lastWeek_hour3'] = np.nan
# dataframe['consumption_intraday_lastWeek_hour4'] = np.nan
# dataframe['consumption_intraday_lastWeek_hour5'] = np.nan
# dataframe['consumption_intraday_lastWeek_hour6'] = np.nan
# dataframe['consumption_intraday_lastWeek_hour7'] = np.nan
# dataframe['consumption_intraday_lastWeek_hour8'] = np.nan
# dataframe['consumption_intraday_lastWeek_hour9'] = np.nan
# dataframe['consumption_intraday_lastWeek_hour10'] = np.nan
# dataframe['consumption_intraday_lastWeek_hour11'] = np.nan
# dataframe['consumption_intraday_lastWeek_hour12'] = np.nan
# dataframe['consumption_intraday_lastWeek_hour13'] = np.nan
# dataframe['consumption_intraday_lastWeek_hour14'] = np.nan
# dataframe['consumption_intraday_lastWeek_hour15'] = np.nan
# dataframe['consumption_intraday_lastWeek_hour16'] = np.nan
# dataframe['consumption_intraday_lastWeek_hour17'] = np.nan
# dataframe['consumption_intraday_lastWeek_hour18'] = np.nan
# dataframe['consumption_intraday_lastWeek_hour19'] = np.nan
# dataframe['consumption_intraday_lastWeek_hour20'] = np.nan
# dataframe['consumption_intraday_lastWeek_hour21'] = np.nan
# dataframe['consumption_intraday_lastWeek_hour22'] = np.nan
# dataframe['consumption_intraday_lastWeek_hour23'] = np.nan
#
# for index, row in dataframe.iterrows():
#     # skip the first 2 days
#     daysToSkip = 8
#     rowsToSkip = (96*daysToSkip)
#     if index > rowsToSkip-1:
#         # 48 to 24 hours before the time slot where the price premium has to be predicted
#         dataframe.at[index, 'price_dayahead_lastDay_hour0'] = dataframe.iloc[index - 192:index - 188]['price_dayahead'].mean()
#         dataframe.at[index, 'price_dayahead_lastDay_hour1'] = dataframe.iloc[index - 188:index - 184]['price_dayahead'].mean()
#         dataframe.at[index, 'price_dayahead_lastDay_hour2'] = dataframe.iloc[index - 184:index - 180]['price_dayahead'].mean()
#         dataframe.at[index, 'price_dayahead_lastDay_hour3'] = dataframe.iloc[index - 180:index - 176]['price_dayahead'].mean()
#         dataframe.at[index, 'price_dayahead_lastDay_hour4'] = dataframe.iloc[index - 176:index - 172]['price_dayahead'].mean()
#         dataframe.at[index, 'price_dayahead_lastDay_hour5'] = dataframe.iloc[index - 172:index - 168]['price_dayahead'].mean()
#         dataframe.at[index, 'price_dayahead_lastDay_hour6'] = dataframe.iloc[index - 168:index - 164]['price_dayahead'].mean()
#         dataframe.at[index, 'price_dayahead_lastDay_hour7'] = dataframe.iloc[index - 164:index - 160]['price_dayahead'].mean()
#         dataframe.at[index, 'price_dayahead_lastDay_hour8'] = dataframe.iloc[index - 160:index - 156]['price_dayahead'].mean()
#         dataframe.at[index, 'price_dayahead_lastDay_hour9'] = dataframe.iloc[index - 156:index - 152]['price_dayahead'].mean()
#         dataframe.at[index, 'price_dayahead_lastDay_hour10'] = dataframe.iloc[index - 152:index - 148]['price_dayahead'].mean()
#         dataframe.at[index, 'price_dayahead_lastDay_hour11'] = dataframe.iloc[index - 148:index - 144]['price_dayahead'].mean()
#         dataframe.at[index, 'price_dayahead_lastDay_hour12'] = dataframe.iloc[index - 144:index - 140]['price_dayahead'].mean()
#         dataframe.at[index, 'price_dayahead_lastDay_hour13'] = dataframe.iloc[index - 140:index - 136]['price_dayahead'].mean()
#         dataframe.at[index, 'price_dayahead_lastDay_hour14'] = dataframe.iloc[index - 136:index - 132]['price_dayahead'].mean()
#         dataframe.at[index, 'price_dayahead_lastDay_hour15'] = dataframe.iloc[index - 132:index - 128]['price_dayahead'].mean()
#         dataframe.at[index, 'price_dayahead_lastDay_hour16'] = dataframe.iloc[index - 128:index - 124]['price_dayahead'].mean()
#         dataframe.at[index, 'price_dayahead_lastDay_hour17'] = dataframe.iloc[index - 124:index - 120]['price_dayahead'].mean()
#         dataframe.at[index, 'price_dayahead_lastDay_hour18'] = dataframe.iloc[index - 120:index - 116]['price_dayahead'].mean()
#         dataframe.at[index, 'price_dayahead_lastDay_hour19'] = dataframe.iloc[index - 116:index - 112]['price_dayahead'].mean()
#         dataframe.at[index, 'price_dayahead_lastDay_hour20'] = dataframe.iloc[index - 112:index - 108]['price_dayahead'].mean()
#         dataframe.at[index, 'price_dayahead_lastDay_hour21'] = dataframe.iloc[index - 108:index - 104]['price_dayahead'].mean()
#         dataframe.at[index, 'price_dayahead_lastDay_hour22'] = dataframe.iloc[index - 104:index - 100]['price_dayahead'].mean()
#         dataframe.at[index, 'price_dayahead_lastDay_hour23'] = dataframe.iloc[index - 100:index - 96]['price_dayahead'].mean()
#         dataframe.at[index, 'consumption_dayahead_lastDay_hour0'] = dataframe.iloc[index - 192:index - 188]['consumption_dayahead'].mean()
#         dataframe.at[index, 'consumption_dayahead_lastDay_hour1'] = dataframe.iloc[index - 188:index - 184]['consumption_dayahead'].mean()
#         dataframe.at[index, 'consumption_dayahead_lastDay_hour2'] = dataframe.iloc[index - 184:index - 180]['consumption_dayahead'].mean()
#         dataframe.at[index, 'consumption_dayahead_lastDay_hour3'] = dataframe.iloc[index - 180:index - 176]['consumption_dayahead'].mean()
#         dataframe.at[index, 'consumption_dayahead_lastDay_hour4'] = dataframe.iloc[index - 176:index - 172]['consumption_dayahead'].mean()
#         dataframe.at[index, 'consumption_dayahead_lastDay_hour5'] = dataframe.iloc[index - 172:index - 168]['consumption_dayahead'].mean()
#         dataframe.at[index, 'consumption_dayahead_lastDay_hour6'] = dataframe.iloc[index - 168:index - 164]['consumption_dayahead'].mean()
#         dataframe.at[index, 'consumption_dayahead_lastDay_hour7'] = dataframe.iloc[index - 164:index - 160]['consumption_dayahead'].mean()
#         dataframe.at[index, 'consumption_dayahead_lastDay_hour8'] = dataframe.iloc[index - 160:index - 156]['consumption_dayahead'].mean()
#         dataframe.at[index, 'consumption_dayahead_lastDay_hour9'] = dataframe.iloc[index - 156:index - 152]['consumption_dayahead'].mean()
#         dataframe.at[index, 'consumption_dayahead_lastDay_hour10'] = dataframe.iloc[index - 152:index - 148]['consumption_dayahead'].mean()
#         dataframe.at[index, 'consumption_dayahead_lastDay_hour11'] = dataframe.iloc[index - 148:index - 144]['consumption_dayahead'].mean()
#         dataframe.at[index, 'consumption_dayahead_lastDay_hour12'] = dataframe.iloc[index - 144:index - 140]['consumption_dayahead'].mean()
#         dataframe.at[index, 'consumption_dayahead_lastDay_hour13'] = dataframe.iloc[index - 140:index - 136]['consumption_dayahead'].mean()
#         dataframe.at[index, 'consumption_dayahead_lastDay_hour14'] = dataframe.iloc[index - 136:index - 132]['consumption_dayahead'].mean()
#         dataframe.at[index, 'consumption_dayahead_lastDay_hour15'] = dataframe.iloc[index - 132:index - 128]['consumption_dayahead'].mean()
#         dataframe.at[index, 'consumption_dayahead_lastDay_hour16'] = dataframe.iloc[index - 128:index - 124]['consumption_dayahead'].mean()
#         dataframe.at[index, 'consumption_dayahead_lastDay_hour17'] = dataframe.iloc[index - 124:index - 120]['consumption_dayahead'].mean()
#         dataframe.at[index, 'consumption_dayahead_lastDay_hour18'] = dataframe.iloc[index - 120:index - 116]['consumption_dayahead'].mean()
#         dataframe.at[index, 'consumption_dayahead_lastDay_hour19'] = dataframe.iloc[index - 116:index - 112]['consumption_dayahead'].mean()
#         dataframe.at[index, 'consumption_dayahead_lastDay_hour20'] = dataframe.iloc[index - 112:index - 108]['consumption_dayahead'].mean()
#         dataframe.at[index, 'consumption_dayahead_lastDay_hour21'] = dataframe.iloc[index - 108:index - 104]['consumption_dayahead'].mean()
#         dataframe.at[index, 'consumption_dayahead_lastDay_hour22'] = dataframe.iloc[index - 104:index - 100]['consumption_dayahead'].mean()
#         dataframe.at[index, 'consumption_dayahead_lastDay_hour23'] = dataframe.iloc[index - 100:index - 96]['consumption_dayahead'].mean()
#         dataframe.at[index, 'price_intraday_lastDay_hour0'] = dataframe.iloc[index - 192:index - 188]['price'].mean()
#         dataframe.at[index, 'price_intraday_lastDay_hour1'] = dataframe.iloc[index - 188:index - 184]['price'].mean()
#         dataframe.at[index, 'price_intraday_lastDay_hour2'] = dataframe.iloc[index - 184:index - 180]['price'].mean()
#         dataframe.at[index, 'price_intraday_lastDay_hour3'] = dataframe.iloc[index - 180:index - 176]['price'].mean()
#         dataframe.at[index, 'price_intraday_lastDay_hour4'] = dataframe.iloc[index - 176:index - 172]['price'].mean()
#         dataframe.at[index, 'price_intraday_lastDay_hour5'] = dataframe.iloc[index - 172:index - 168]['price'].mean()
#         dataframe.at[index, 'price_intraday_lastDay_hour6'] = dataframe.iloc[index - 168:index - 164]['price'].mean()
#         dataframe.at[index, 'price_intraday_lastDay_hour7'] = dataframe.iloc[index - 164:index - 160]['price'].mean()
#         dataframe.at[index, 'price_intraday_lastDay_hour8'] = dataframe.iloc[index - 160:index - 156]['price'].mean()
#         dataframe.at[index, 'price_intraday_lastDay_hour9'] = dataframe.iloc[index - 156:index - 152]['price'].mean()
#         dataframe.at[index, 'price_intraday_lastDay_hour10'] = dataframe.iloc[index - 152:index - 148]['price'].mean()
#         dataframe.at[index, 'price_intraday_lastDay_hour11'] = dataframe.iloc[index - 148:index - 144]['price'].mean()
#         dataframe.at[index, 'price_intraday_lastDay_hour12'] = dataframe.iloc[index - 144:index - 140]['price'].mean()
#         dataframe.at[index, 'price_intraday_lastDay_hour13'] = dataframe.iloc[index - 140:index - 136]['price'].mean()
#         dataframe.at[index, 'price_intraday_lastDay_hour14'] = dataframe.iloc[index - 136:index - 132]['price'].mean()
#         dataframe.at[index, 'price_intraday_lastDay_hour15'] = dataframe.iloc[index - 132:index - 128]['price'].mean()
#         dataframe.at[index, 'price_intraday_lastDay_hour16'] = dataframe.iloc[index - 128:index - 124]['price'].mean()
#         dataframe.at[index, 'price_intraday_lastDay_hour17'] = dataframe.iloc[index - 124:index - 120]['price'].mean()
#         dataframe.at[index, 'price_intraday_lastDay_hour18'] = dataframe.iloc[index - 120:index - 116]['price'].mean()
#         dataframe.at[index, 'price_intraday_lastDay_hour19'] = dataframe.iloc[index - 116:index - 112]['price'].mean()
#         dataframe.at[index, 'price_intraday_lastDay_hour20'] = dataframe.iloc[index - 112:index - 108]['price'].mean()
#         dataframe.at[index, 'price_intraday_lastDay_hour21'] = dataframe.iloc[index - 108:index - 104]['price'].mean()
#         dataframe.at[index, 'price_intraday_lastDay_hour22'] = dataframe.iloc[index - 104:index - 100]['price'].mean()
#         dataframe.at[index, 'price_intraday_lastDay_hour23'] = dataframe.iloc[index - 100:index - 96]['price'].mean()
#         dataframe.at[index, 'consumption_intraday_lastDay_hour0'] = dataframe.iloc[index - 192:index - 188]['consumption'].mean()
#         dataframe.at[index, 'consumption_intraday_lastDay_hour1'] = dataframe.iloc[index - 188:index - 184]['consumption'].mean()
#         dataframe.at[index, 'consumption_intraday_lastDay_hour2'] = dataframe.iloc[index - 184:index - 180]['consumption'].mean()
#         dataframe.at[index, 'consumption_intraday_lastDay_hour3'] = dataframe.iloc[index - 180:index - 176]['consumption'].mean()
#         dataframe.at[index, 'consumption_intraday_lastDay_hour4'] = dataframe.iloc[index - 176:index - 172]['consumption'].mean()
#         dataframe.at[index, 'consumption_intraday_lastDay_hour5'] = dataframe.iloc[index - 172:index - 168]['consumption'].mean()
#         dataframe.at[index, 'consumption_intraday_lastDay_hour6'] = dataframe.iloc[index - 168:index - 164]['consumption'].mean()
#         dataframe.at[index, 'consumption_intraday_lastDay_hour7'] = dataframe.iloc[index - 164:index - 160]['consumption'].mean()
#         dataframe.at[index, 'consumption_intraday_lastDay_hour8'] = dataframe.iloc[index - 160:index - 156]['consumption'].mean()
#         dataframe.at[index, 'consumption_intraday_lastDay_hour9'] = dataframe.iloc[index - 156:index - 152]['consumption'].mean()
#         dataframe.at[index, 'consumption_intraday_lastDay_hour10'] = dataframe.iloc[index - 152:index - 148]['consumption'].mean()
#         dataframe.at[index, 'consumption_intraday_lastDay_hour11'] = dataframe.iloc[index - 148:index - 144]['consumption'].mean()
#         dataframe.at[index, 'consumption_intraday_lastDay_hour12'] = dataframe.iloc[index - 144:index - 140]['consumption'].mean()
#         dataframe.at[index, 'consumption_intraday_lastDay_hour13'] = dataframe.iloc[index - 140:index - 136]['consumption'].mean()
#         dataframe.at[index, 'consumption_intraday_lastDay_hour14'] = dataframe.iloc[index - 136:index - 132]['consumption'].mean()
#         dataframe.at[index, 'consumption_intraday_lastDay_hour15'] = dataframe.iloc[index - 132:index - 128]['consumption'].mean()
#         dataframe.at[index, 'consumption_intraday_lastDay_hour16'] = dataframe.iloc[index - 128:index - 124]['consumption'].mean()
#         dataframe.at[index, 'consumption_intraday_lastDay_hour17'] = dataframe.iloc[index - 124:index - 120]['consumption'].mean()
#         dataframe.at[index, 'consumption_intraday_lastDay_hour18'] = dataframe.iloc[index - 120:index - 116]['consumption'].mean()
#         dataframe.at[index, 'consumption_intraday_lastDay_hour19'] = dataframe.iloc[index - 116:index - 112]['consumption'].mean()
#         dataframe.at[index, 'consumption_intraday_lastDay_hour20'] = dataframe.iloc[index - 112:index - 108]['consumption'].mean()
#         dataframe.at[index, 'consumption_intraday_lastDay_hour21'] = dataframe.iloc[index - 108:index - 104]['consumption'].mean()
#         dataframe.at[index, 'consumption_intraday_lastDay_hour22'] = dataframe.iloc[index - 104:index - 100]['consumption'].mean()
#         dataframe.at[index, 'consumption_intraday_lastDay_hour23'] = dataframe.iloc[index - 100:index - 96]['consumption'].mean()
#         # 8 to 2 days before the time slot where the price premium has to be predicted
#         dataframe.at[index, 'price_dayahead_lastWeek_hour0'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 0]['price_dayahead'].mean()
#         dataframe.at[index, 'price_dayahead_lastWeek_hour1'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 1]['price_dayahead'].mean()
#         dataframe.at[index, 'price_dayahead_lastWeek_hour2'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 2]['price_dayahead'].mean()
#         dataframe.at[index, 'price_dayahead_lastWeek_hour3'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 3]['price_dayahead'].mean()
#         dataframe.at[index, 'price_dayahead_lastWeek_hour4'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 4]['price_dayahead'].mean()
#         dataframe.at[index, 'price_dayahead_lastWeek_hour5'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 5]['price_dayahead'].mean()
#         dataframe.at[index, 'price_dayahead_lastWeek_hour6'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 6]['price_dayahead'].mean()
#         dataframe.at[index, 'price_dayahead_lastWeek_hour7'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 7]['price_dayahead'].mean()
#         dataframe.at[index, 'price_dayahead_lastWeek_hour8'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 8]['price_dayahead'].mean()
#         dataframe.at[index, 'price_dayahead_lastWeek_hour9'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 9]['price_dayahead'].mean()
#         dataframe.at[index, 'price_dayahead_lastWeek_hour10'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 10]['price_dayahead'].mean()
#         dataframe.at[index, 'price_dayahead_lastWeek_hour11'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 11]['price_dayahead'].mean()
#         dataframe.at[index, 'price_dayahead_lastWeek_hour12'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 12]['price_dayahead'].mean()
#         dataframe.at[index, 'price_dayahead_lastWeek_hour13'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 13]['price_dayahead'].mean()
#         dataframe.at[index, 'price_dayahead_lastWeek_hour14'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 14]['price_dayahead'].mean()
#         dataframe.at[index, 'price_dayahead_lastWeek_hour15'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 15]['price_dayahead'].mean()
#         dataframe.at[index, 'price_dayahead_lastWeek_hour16'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 16]['price_dayahead'].mean()
#         dataframe.at[index, 'price_dayahead_lastWeek_hour17'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 17]['price_dayahead'].mean()
#         dataframe.at[index, 'price_dayahead_lastWeek_hour18'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 18]['price_dayahead'].mean()
#         dataframe.at[index, 'price_dayahead_lastWeek_hour19'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 19]['price_dayahead'].mean()
#         dataframe.at[index, 'price_dayahead_lastWeek_hour20'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 20]['price_dayahead'].mean()
#         dataframe.at[index, 'price_dayahead_lastWeek_hour21'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 21]['price_dayahead'].mean()
#         dataframe.at[index, 'price_dayahead_lastWeek_hour22'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 22]['price_dayahead'].mean()
#         dataframe.at[index, 'price_dayahead_lastWeek_hour23'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 23]['price_dayahead'].mean()
#         dataframe.at[index, 'consumption_dayahead_lastWeek_hour0'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 0]['consumption_dayahead'].mean()
#         dataframe.at[index, 'consumption_dayahead_lastWeek_hour1'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 1]['consumption_dayahead'].mean()
#         dataframe.at[index, 'consumption_dayahead_lastWeek_hour2'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 2]['consumption_dayahead'].mean()
#         dataframe.at[index, 'consumption_dayahead_lastWeek_hour3'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 3]['consumption_dayahead'].mean()
#         dataframe.at[index, 'consumption_dayahead_lastWeek_hour4'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 4]['consumption_dayahead'].mean()
#         dataframe.at[index, 'consumption_dayahead_lastWeek_hour5'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 5]['consumption_dayahead'].mean()
#         dataframe.at[index, 'consumption_dayahead_lastWeek_hour6'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 6]['consumption_dayahead'].mean()
#         dataframe.at[index, 'consumption_dayahead_lastWeek_hour7'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 7]['consumption_dayahead'].mean()
#         dataframe.at[index, 'consumption_dayahead_lastWeek_hour8'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 8]['consumption_dayahead'].mean()
#         dataframe.at[index, 'consumption_dayahead_lastWeek_hour9'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 9]['consumption_dayahead'].mean()
#         dataframe.at[index, 'consumption_dayahead_lastWeek_hour10'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 10]['consumption_dayahead'].mean()
#         dataframe.at[index, 'consumption_dayahead_lastWeek_hour11'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 11]['consumption_dayahead'].mean()
#         dataframe.at[index, 'consumption_dayahead_lastWeek_hour12'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 12]['consumption_dayahead'].mean()
#         dataframe.at[index, 'consumption_dayahead_lastWeek_hour13'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 13]['consumption_dayahead'].mean()
#         dataframe.at[index, 'consumption_dayahead_lastWeek_hour14'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 14]['consumption_dayahead'].mean()
#         dataframe.at[index, 'consumption_dayahead_lastWeek_hour15'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 15]['consumption_dayahead'].mean()
#         dataframe.at[index, 'consumption_dayahead_lastWeek_hour16'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 16]['consumption_dayahead'].mean()
#         dataframe.at[index, 'consumption_dayahead_lastWeek_hour17'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 17]['consumption_dayahead'].mean()
#         dataframe.at[index, 'consumption_dayahead_lastWeek_hour18'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 18]['consumption_dayahead'].mean()
#         dataframe.at[index, 'consumption_dayahead_lastWeek_hour19'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 19]['consumption_dayahead'].mean()
#         dataframe.at[index, 'consumption_dayahead_lastWeek_hour20'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 20]['consumption_dayahead'].mean()
#         dataframe.at[index, 'consumption_dayahead_lastWeek_hour21'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 21]['consumption_dayahead'].mean()
#         dataframe.at[index, 'consumption_dayahead_lastWeek_hour22'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 22]['consumption_dayahead'].mean()
#         dataframe.at[index, 'consumption_dayahead_lastWeek_hour23'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 23]['consumption_dayahead'].mean()
#         dataframe.at[index, 'price_intraday_lastWeek_hour0'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 0]['price'].mean()
#         dataframe.at[index, 'price_intraday_lastWeek_hour1'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 1]['price'].mean()
#         dataframe.at[index, 'price_intraday_lastWeek_hour2'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 2]['price'].mean()
#         dataframe.at[index, 'price_intraday_lastWeek_hour3'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 3]['price'].mean()
#         dataframe.at[index, 'price_intraday_lastWeek_hour4'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 4]['price'].mean()
#         dataframe.at[index, 'price_intraday_lastWeek_hour5'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 5]['price'].mean()
#         dataframe.at[index, 'price_intraday_lastWeek_hour6'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 6]['price'].mean()
#         dataframe.at[index, 'price_intraday_lastWeek_hour7'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 7]['price'].mean()
#         dataframe.at[index, 'price_intraday_lastWeek_hour8'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 8]['price'].mean()
#         dataframe.at[index, 'price_intraday_lastWeek_hour9'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 9]['price'].mean()
#         dataframe.at[index, 'price_intraday_lastWeek_hour10'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 10]['price'].mean()
#         dataframe.at[index, 'price_intraday_lastWeek_hour11'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 11]['price'].mean()
#         dataframe.at[index, 'price_intraday_lastWeek_hour12'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 12]['price'].mean()
#         dataframe.at[index, 'price_intraday_lastWeek_hour13'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 13]['price'].mean()
#         dataframe.at[index, 'price_intraday_lastWeek_hour14'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 14]['price'].mean()
#         dataframe.at[index, 'price_intraday_lastWeek_hour15'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 15]['price'].mean()
#         dataframe.at[index, 'price_intraday_lastWeek_hour16'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 16]['price'].mean()
#         dataframe.at[index, 'price_intraday_lastWeek_hour17'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 17]['price'].mean()
#         dataframe.at[index, 'price_intraday_lastWeek_hour18'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 18]['price'].mean()
#         dataframe.at[index, 'price_intraday_lastWeek_hour19'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 19]['price'].mean()
#         dataframe.at[index, 'price_intraday_lastWeek_hour20'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 20]['price'].mean()
#         dataframe.at[index, 'price_intraday_lastWeek_hour21'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 21]['price'].mean()
#         dataframe.at[index, 'price_intraday_lastWeek_hour22'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 22]['price'].mean()
#         dataframe.at[index, 'price_intraday_lastWeek_hour23'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 23]['price'].mean()
#         dataframe.at[index, 'consumption_intraday_lastWeek_hour0'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 0]['consumption'].mean()
#         dataframe.at[index, 'consumption_intraday_lastWeek_hour1'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 1]['consumption'].mean()
#         dataframe.at[index, 'consumption_intraday_lastWeek_hour2'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 2]['consumption'].mean()
#         dataframe.at[index, 'consumption_intraday_lastWeek_hour3'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 3]['consumption'].mean()
#         dataframe.at[index, 'consumption_intraday_lastWeek_hour4'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 4]['consumption'].mean()
#         dataframe.at[index, 'consumption_intraday_lastWeek_hour5'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 5]['consumption'].mean()
#         dataframe.at[index, 'consumption_intraday_lastWeek_hour6'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 6]['consumption'].mean()
#         dataframe.at[index, 'consumption_intraday_lastWeek_hour7'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 7]['consumption'].mean()
#         dataframe.at[index, 'consumption_intraday_lastWeek_hour8'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 8]['consumption'].mean()
#         dataframe.at[index, 'consumption_intraday_lastWeek_hour9'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 9]['consumption'].mean()
#         dataframe.at[index, 'consumption_intraday_lastWeek_hour10'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 10]['consumption'].mean()
#         dataframe.at[index, 'consumption_intraday_lastWeek_hour11'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 11]['consumption'].mean()
#         dataframe.at[index, 'consumption_intraday_lastWeek_hour12'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 12]['consumption'].mean()
#         dataframe.at[index, 'consumption_intraday_lastWeek_hour13'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 13]['consumption'].mean()
#         dataframe.at[index, 'consumption_intraday_lastWeek_hour14'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 14]['consumption'].mean()
#         dataframe.at[index, 'consumption_intraday_lastWeek_hour15'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 15]['consumption'].mean()
#         dataframe.at[index, 'consumption_intraday_lastWeek_hour16'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 16]['consumption'].mean()
#         dataframe.at[index, 'consumption_intraday_lastWeek_hour17'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 17]['consumption'].mean()
#         dataframe.at[index, 'consumption_intraday_lastWeek_hour18'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 18]['consumption'].mean()
#         dataframe.at[index, 'consumption_intraday_lastWeek_hour19'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 19]['consumption'].mean()
#         dataframe.at[index, 'consumption_intraday_lastWeek_hour20'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 20]['consumption'].mean()
#         dataframe.at[index, 'consumption_intraday_lastWeek_hour21'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 21]['consumption'].mean()
#         dataframe.at[index, 'consumption_intraday_lastWeek_hour22'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 22]['consumption'].mean()
#         dataframe.at[index, 'consumption_intraday_lastWeek_hour23'] = dataframe.loc[pd.DatetimeIndex(dataframe.iloc[index - 768:index - 192]['datetime']).hour == 23]['consumption'].mean()
#
#         # Print index to track progress
#         if index % 1000 == 0:
#             print(index)
#
# # Drop the first few rows where no aggregated data columns could be filled
# dataframe = dataframe.drop(index=range(0,rowsToSkip))

dataframe.to_csv(newPath, index=False)
