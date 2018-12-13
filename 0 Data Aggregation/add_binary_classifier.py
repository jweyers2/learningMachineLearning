import pandas as pd
import numpy as np
import datetime

newPath='../00 Data/Final/binaryFinal.csv'
path='../00 Data/Final/final.csv'
dataframe=pd.read_csv(path)

dataframe['datetime'] = pd.to_datetime(dataframe['datetime'])

# Add new rows for aggregated price and volume data of both auctions for the las 2-1 days, 9-2 days and 31-9 days
# last 24 hours before 11:45 on the day of the last auction
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
# last 24-168 hours before 11:45 on the day of the last auction
dataframe['price_dayahead_lastWeek_hour0'] = np.nan
dataframe['price_dayahead_lastWeek_hour1'] = np.nan
dataframe['price_dayahead_lastWeek_hour2'] = np.nan
dataframe['price_dayahead_lastWeek_hour3'] = np.nan
dataframe['price_dayahead_lastWeek_hour4'] = np.nan
dataframe['price_dayahead_lastWeek_hour5'] = np.nan
dataframe['price_dayahead_lastWeek_hour6'] = np.nan
dataframe['price_dayahead_lastWeek_hour7'] = np.nan
dataframe['price_dayahead_lastWeek_hour8'] = np.nan
dataframe['price_dayahead_lastWeek_hour9'] = np.nan
dataframe['price_dayahead_lastWeek_hour10'] = np.nan
dataframe['price_dayahead_lastWeek_hour11'] = np.nan
dataframe['price_dayahead_lastWeek_hour12'] = np.nan
dataframe['price_dayahead_lastWeek_hour13'] = np.nan
dataframe['price_dayahead_lastWeek_hour14'] = np.nan
dataframe['price_dayahead_lastWeek_hour15'] = np.nan
dataframe['price_dayahead_lastWeek_hour16'] = np.nan
dataframe['price_dayahead_lastWeek_hour17'] = np.nan
dataframe['price_dayahead_lastWeek_hour18'] = np.nan
dataframe['price_dayahead_lastWeek_hour19'] = np.nan
dataframe['price_dayahead_lastWeek_hour20'] = np.nan
dataframe['price_dayahead_lastWeek_hour21'] = np.nan
dataframe['price_dayahead_lastWeek_hour22'] = np.nan
dataframe['price_dayahead_lastWeek_hour23'] = np.nan
dataframe['consumption_dayahead_lastWeek_hour0'] = np.nan
dataframe['consumption_dayahead_lastWeek_hour1'] = np.nan
dataframe['consumption_dayahead_lastWeek_hour2'] = np.nan
dataframe['consumption_dayahead_lastWeek_hour3'] = np.nan
dataframe['consumption_dayahead_lastWeek_hour4'] = np.nan
dataframe['consumption_dayahead_lastWeek_hour5'] = np.nan
dataframe['consumption_dayahead_lastWeek_hour6'] = np.nan
dataframe['consumption_dayahead_lastWeek_hour7'] = np.nan
dataframe['consumption_dayahead_lastWeek_hour8'] = np.nan
dataframe['consumption_dayahead_lastWeek_hour9'] = np.nan
dataframe['consumption_dayahead_lastWeek_hour10'] = np.nan
dataframe['consumption_dayahead_lastWeek_hour11'] = np.nan
dataframe['consumption_dayahead_lastWeek_hour12'] = np.nan
dataframe['consumption_dayahead_lastWeek_hour13'] = np.nan
dataframe['consumption_dayahead_lastWeek_hour14'] = np.nan
dataframe['consumption_dayahead_lastWeek_hour15'] = np.nan
dataframe['consumption_dayahead_lastWeek_hour16'] = np.nan
dataframe['consumption_dayahead_lastWeek_hour17'] = np.nan
dataframe['consumption_dayahead_lastWeek_hour18'] = np.nan
dataframe['consumption_dayahead_lastWeek_hour19'] = np.nan
dataframe['consumption_dayahead_lastWeek_hour20'] = np.nan
dataframe['consumption_dayahead_lastWeek_hour21'] = np.nan
dataframe['consumption_dayahead_lastWeek_hour22'] = np.nan
dataframe['consumption_dayahead_lastWeek_hour23'] = np.nan
dataframe['price_intraday_lastWeek_hour0'] = np.nan
dataframe['price_intraday_lastWeek_hour1'] = np.nan
dataframe['price_intraday_lastWeek_hour2'] = np.nan
dataframe['price_intraday_lastWeek_hour3'] = np.nan
dataframe['price_intraday_lastWeek_hour4'] = np.nan
dataframe['price_intraday_lastWeek_hour5'] = np.nan
dataframe['price_intraday_lastWeek_hour6'] = np.nan
dataframe['price_intraday_lastWeek_hour7'] = np.nan
dataframe['price_intraday_lastWeek_hour8'] = np.nan
dataframe['price_intraday_lastWeek_hour9'] = np.nan
dataframe['price_intraday_lastWeek_hour10'] = np.nan
dataframe['price_intraday_lastWeek_hour11'] = np.nan
dataframe['price_intraday_lastWeek_hour12'] = np.nan
dataframe['price_intraday_lastWeek_hour13'] = np.nan
dataframe['price_intraday_lastWeek_hour14'] = np.nan
dataframe['price_intraday_lastWeek_hour15'] = np.nan
dataframe['price_intraday_lastWeek_hour16'] = np.nan
dataframe['price_intraday_lastWeek_hour17'] = np.nan
dataframe['price_intraday_lastWeek_hour18'] = np.nan
dataframe['price_intraday_lastWeek_hour19'] = np.nan
dataframe['price_intraday_lastWeek_hour20'] = np.nan
dataframe['price_intraday_lastWeek_hour21'] = np.nan
dataframe['price_intraday_lastWeek_hour22'] = np.nan
dataframe['price_intraday_lastWeek_hour23'] = np.nan
dataframe['consumption_intraday_lastWeek_hour0'] = np.nan
dataframe['consumption_intraday_lastWeek_hour1'] = np.nan
dataframe['consumption_intraday_lastWeek_hour2'] = np.nan
dataframe['consumption_intraday_lastWeek_hour3'] = np.nan
dataframe['consumption_intraday_lastWeek_hour4'] = np.nan
dataframe['consumption_intraday_lastWeek_hour5'] = np.nan
dataframe['consumption_intraday_lastWeek_hour6'] = np.nan
dataframe['consumption_intraday_lastWeek_hour7'] = np.nan
dataframe['consumption_intraday_lastWeek_hour8'] = np.nan
dataframe['consumption_intraday_lastWeek_hour9'] = np.nan
dataframe['consumption_intraday_lastWeek_hour10'] = np.nan
dataframe['consumption_intraday_lastWeek_hour11'] = np.nan
dataframe['consumption_intraday_lastWeek_hour12'] = np.nan
dataframe['consumption_intraday_lastWeek_hour13'] = np.nan
dataframe['consumption_intraday_lastWeek_hour14'] = np.nan
dataframe['consumption_intraday_lastWeek_hour15'] = np.nan
dataframe['consumption_intraday_lastWeek_hour16'] = np.nan
dataframe['consumption_intraday_lastWeek_hour17'] = np.nan
dataframe['consumption_intraday_lastWeek_hour18'] = np.nan
dataframe['consumption_intraday_lastWeek_hour19'] = np.nan
dataframe['consumption_intraday_lastWeek_hour20'] = np.nan
dataframe['consumption_intraday_lastWeek_hour21'] = np.nan
dataframe['consumption_intraday_lastWeek_hour22'] = np.nan
dataframe['consumption_intraday_lastWeek_hour23'] = np.nan

for index, row in dataframe.iterrows():
    # skip the first 8 days
    daysToSkip = 8
    rowsToSkip = (96*daysToSkip)
    if index > rowsToSkip-1:
        # go to the index of the last day at 11:30
        lastAuctionDate = pd.to_datetime(dataframe.iloc[index]['datetime'].date()-datetime.timedelta(1))
        indexBeforePrediction = dataframe.loc[(pd.DatetimeIndex(dataframe['datetime']).hour == 11) &
                              (pd.DatetimeIndex(dataframe['datetime']).minute == 30) &
                              (pd.DatetimeIndex(dataframe['datetime']).day == lastAuctionDate.day) &
                              (pd.DatetimeIndex(dataframe['datetime']).month == lastAuctionDate.month) &
                              (pd.DatetimeIndex(dataframe['datetime']).year == lastAuctionDate.year)].index[0]
        indexBeforePrediction = indexBeforePrediction.astype(np.int32)

        lastDaydf = dataframe[indexBeforePrediction-95:indexBeforePrediction+1]
        lastWeekdf = dataframe[indexBeforePrediction - 671:indexBeforePrediction - 95]
        # last 24 hours before 11:45 on the day of the last auction
        dataframe.at[index, 'price_dayahead_lastDay_hour0'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 0]['price_dayahead'].mean()
        dataframe.at[index, 'price_dayahead_lastDay_hour1'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 1]['price_dayahead'].mean()
        dataframe.at[index, 'price_dayahead_lastDay_hour2'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 2]['price_dayahead'].mean()
        dataframe.at[index, 'price_dayahead_lastDay_hour3'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 3]['price_dayahead'].mean()
        dataframe.at[index, 'price_dayahead_lastDay_hour4'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 4]['price_dayahead'].mean()
        dataframe.at[index, 'price_dayahead_lastDay_hour5'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 5]['price_dayahead'].mean()
        dataframe.at[index, 'price_dayahead_lastDay_hour6'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 6]['price_dayahead'].mean()
        dataframe.at[index, 'price_dayahead_lastDay_hour7'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 7]['price_dayahead'].mean()
        dataframe.at[index, 'price_dayahead_lastDay_hour8'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 8]['price_dayahead'].mean()
        dataframe.at[index, 'price_dayahead_lastDay_hour9'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 9]['price_dayahead'].mean()
        dataframe.at[index, 'price_dayahead_lastDay_hour10'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 10]['price_dayahead'].mean()
        dataframe.at[index, 'price_dayahead_lastDay_hour11'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 11]['price_dayahead'].mean()
        dataframe.at[index, 'price_dayahead_lastDay_hour12'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 12]['price_dayahead'].mean()
        dataframe.at[index, 'price_dayahead_lastDay_hour13'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 13]['price_dayahead'].mean()
        dataframe.at[index, 'price_dayahead_lastDay_hour14'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 14]['price_dayahead'].mean()
        dataframe.at[index, 'price_dayahead_lastDay_hour15'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 15]['price_dayahead'].mean()
        dataframe.at[index, 'price_dayahead_lastDay_hour16'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 16]['price_dayahead'].mean()
        dataframe.at[index, 'price_dayahead_lastDay_hour17'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 17]['price_dayahead'].mean()
        dataframe.at[index, 'price_dayahead_lastDay_hour18'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 18]['price_dayahead'].mean()
        dataframe.at[index, 'price_dayahead_lastDay_hour19'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 19]['price_dayahead'].mean()
        dataframe.at[index, 'price_dayahead_lastDay_hour20'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 20]['price_dayahead'].mean()
        dataframe.at[index, 'price_dayahead_lastDay_hour21'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 21]['price_dayahead'].mean()
        dataframe.at[index, 'price_dayahead_lastDay_hour22'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 22]['price_dayahead'].mean()
        dataframe.at[index, 'price_dayahead_lastDay_hour23'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 23]['price_dayahead'].mean()
        dataframe.at[index, 'consumption_dayahead_lastDay_hour0'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 0]['consumption_dayahead'].mean()
        dataframe.at[index, 'consumption_dayahead_lastDay_hour1'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 1]['consumption_dayahead'].mean()
        dataframe.at[index, 'consumption_dayahead_lastDay_hour2'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 2]['consumption_dayahead'].mean()
        dataframe.at[index, 'consumption_dayahead_lastDay_hour3'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 3]['consumption_dayahead'].mean()
        dataframe.at[index, 'consumption_dayahead_lastDay_hour4'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 4]['consumption_dayahead'].mean()
        dataframe.at[index, 'consumption_dayahead_lastDay_hour5'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 5]['consumption_dayahead'].mean()
        dataframe.at[index, 'consumption_dayahead_lastDay_hour6'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 6]['consumption_dayahead'].mean()
        dataframe.at[index, 'consumption_dayahead_lastDay_hour7'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 7]['consumption_dayahead'].mean()
        dataframe.at[index, 'consumption_dayahead_lastDay_hour8'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 8]['consumption_dayahead'].mean()
        dataframe.at[index, 'consumption_dayahead_lastDay_hour9'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 9]['consumption_dayahead'].mean()
        dataframe.at[index, 'consumption_dayahead_lastDay_hour10'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 10]['consumption_dayahead'].mean()
        dataframe.at[index, 'consumption_dayahead_lastDay_hour11'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 11]['consumption_dayahead'].mean()
        dataframe.at[index, 'consumption_dayahead_lastDay_hour12'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 12]['consumption_dayahead'].mean()
        dataframe.at[index, 'consumption_dayahead_lastDay_hour13'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 13]['consumption_dayahead'].mean()
        dataframe.at[index, 'consumption_dayahead_lastDay_hour14'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 14]['consumption_dayahead'].mean()
        dataframe.at[index, 'consumption_dayahead_lastDay_hour15'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 15]['consumption_dayahead'].mean()
        dataframe.at[index, 'consumption_dayahead_lastDay_hour16'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 16]['consumption_dayahead'].mean()
        dataframe.at[index, 'consumption_dayahead_lastDay_hour17'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 17]['consumption_dayahead'].mean()
        dataframe.at[index, 'consumption_dayahead_lastDay_hour18'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 18]['consumption_dayahead'].mean()
        dataframe.at[index, 'consumption_dayahead_lastDay_hour19'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 19]['consumption_dayahead'].mean()
        dataframe.at[index, 'consumption_dayahead_lastDay_hour20'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 20]['consumption_dayahead'].mean()
        dataframe.at[index, 'consumption_dayahead_lastDay_hour21'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 21]['consumption_dayahead'].mean()
        dataframe.at[index, 'consumption_dayahead_lastDay_hour22'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 22]['consumption_dayahead'].mean()
        dataframe.at[index, 'consumption_dayahead_lastDay_hour23'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 23]['consumption_dayahead'].mean()
        dataframe.at[index, 'price_intraday_lastDay_hour0'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 0]['price'].mean()
        dataframe.at[index, 'price_intraday_lastDay_hour1'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 1]['price'].mean()
        dataframe.at[index, 'price_intraday_lastDay_hour2'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 2]['price'].mean()
        dataframe.at[index, 'price_intraday_lastDay_hour3'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 3]['price'].mean()
        dataframe.at[index, 'price_intraday_lastDay_hour4'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 4]['price'].mean()
        dataframe.at[index, 'price_intraday_lastDay_hour5'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 5]['price'].mean()
        dataframe.at[index, 'price_intraday_lastDay_hour6'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 6]['price'].mean()
        dataframe.at[index, 'price_intraday_lastDay_hour7'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 7]['price'].mean()
        dataframe.at[index, 'price_intraday_lastDay_hour8'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 8]['price'].mean()
        dataframe.at[index, 'price_intraday_lastDay_hour9'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 9]['price'].mean()
        dataframe.at[index, 'price_intraday_lastDay_hour10'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 10]['price'].mean()
        dataframe.at[index, 'price_intraday_lastDay_hour11'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 11]['price'].mean()
        dataframe.at[index, 'price_intraday_lastDay_hour12'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 12]['price'].mean()
        dataframe.at[index, 'price_intraday_lastDay_hour13'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 13]['price'].mean()
        dataframe.at[index, 'price_intraday_lastDay_hour14'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 14]['price'].mean()
        dataframe.at[index, 'price_intraday_lastDay_hour15'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 15]['price'].mean()
        dataframe.at[index, 'price_intraday_lastDay_hour16'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 16]['price'].mean()
        dataframe.at[index, 'price_intraday_lastDay_hour17'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 17]['price'].mean()
        dataframe.at[index, 'price_intraday_lastDay_hour18'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 18]['price'].mean()
        dataframe.at[index, 'price_intraday_lastDay_hour19'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 19]['price'].mean()
        dataframe.at[index, 'price_intraday_lastDay_hour20'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 20]['price'].mean()
        dataframe.at[index, 'price_intraday_lastDay_hour21'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 21]['price'].mean()
        dataframe.at[index, 'price_intraday_lastDay_hour22'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 22]['price'].mean()
        dataframe.at[index, 'price_intraday_lastDay_hour23'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 23]['price'].mean()
        dataframe.at[index, 'consumption_intraday_lastDay_hour0'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 0]['consumption'].mean()
        dataframe.at[index, 'consumption_intraday_lastDay_hour1'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 1]['consumption'].mean()
        dataframe.at[index, 'consumption_intraday_lastDay_hour2'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 2]['consumption'].mean()
        dataframe.at[index, 'consumption_intraday_lastDay_hour3'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 3]['consumption'].mean()
        dataframe.at[index, 'consumption_intraday_lastDay_hour4'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 4]['consumption'].mean()
        dataframe.at[index, 'consumption_intraday_lastDay_hour5'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 5]['consumption'].mean()
        dataframe.at[index, 'consumption_intraday_lastDay_hour6'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 6]['consumption'].mean()
        dataframe.at[index, 'consumption_intraday_lastDay_hour7'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 7]['consumption'].mean()
        dataframe.at[index, 'consumption_intraday_lastDay_hour8'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 8]['consumption'].mean()
        dataframe.at[index, 'consumption_intraday_lastDay_hour9'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 9]['consumption'].mean()
        dataframe.at[index, 'consumption_intraday_lastDay_hour10'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 10]['consumption'].mean()
        dataframe.at[index, 'consumption_intraday_lastDay_hour11'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 11]['consumption'].mean()
        dataframe.at[index, 'consumption_intraday_lastDay_hour12'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 12]['consumption'].mean()
        dataframe.at[index, 'consumption_intraday_lastDay_hour13'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 13]['consumption'].mean()
        dataframe.at[index, 'consumption_intraday_lastDay_hour14'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 14]['consumption'].mean()
        dataframe.at[index, 'consumption_intraday_lastDay_hour15'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 15]['consumption'].mean()
        dataframe.at[index, 'consumption_intraday_lastDay_hour16'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 16]['consumption'].mean()
        dataframe.at[index, 'consumption_intraday_lastDay_hour17'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 17]['consumption'].mean()
        dataframe.at[index, 'consumption_intraday_lastDay_hour18'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 18]['consumption'].mean()
        dataframe.at[index, 'consumption_intraday_lastDay_hour19'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 19]['consumption'].mean()
        dataframe.at[index, 'consumption_intraday_lastDay_hour20'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 20]['consumption'].mean()
        dataframe.at[index, 'consumption_intraday_lastDay_hour21'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 21]['consumption'].mean()
        dataframe.at[index, 'consumption_intraday_lastDay_hour22'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 22]['consumption'].mean()
        dataframe.at[index, 'consumption_intraday_lastDay_hour23'] = lastDaydf.loc[pd.DatetimeIndex(lastDaydf['datetime']).hour == 23]['consumption'].mean()
        # last 24-168 hours before 11:45 on the day of the last auction
        dataframe.at[index, 'price_dayahead_lastWeek_hour0'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 0]['price_dayahead'].mean()
        dataframe.at[index, 'price_dayahead_lastWeek_hour1'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 1]['price_dayahead'].mean()
        dataframe.at[index, 'price_dayahead_lastWeek_hour2'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 2]['price_dayahead'].mean()
        dataframe.at[index, 'price_dayahead_lastWeek_hour3'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 3]['price_dayahead'].mean()
        dataframe.at[index, 'price_dayahead_lastWeek_hour4'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 4]['price_dayahead'].mean()
        dataframe.at[index, 'price_dayahead_lastWeek_hour5'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 5]['price_dayahead'].mean()
        dataframe.at[index, 'price_dayahead_lastWeek_hour6'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 6]['price_dayahead'].mean()
        dataframe.at[index, 'price_dayahead_lastWeek_hour7'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 7]['price_dayahead'].mean()
        dataframe.at[index, 'price_dayahead_lastWeek_hour8'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 8]['price_dayahead'].mean()
        dataframe.at[index, 'price_dayahead_lastWeek_hour9'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 9]['price_dayahead'].mean()
        dataframe.at[index, 'price_dayahead_lastWeek_hour10'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 10]['price_dayahead'].mean()
        dataframe.at[index, 'price_dayahead_lastWeek_hour11'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 11]['price_dayahead'].mean()
        dataframe.at[index, 'price_dayahead_lastWeek_hour12'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 12]['price_dayahead'].mean()
        dataframe.at[index, 'price_dayahead_lastWeek_hour13'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 13]['price_dayahead'].mean()
        dataframe.at[index, 'price_dayahead_lastWeek_hour14'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 14]['price_dayahead'].mean()
        dataframe.at[index, 'price_dayahead_lastWeek_hour15'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 15]['price_dayahead'].mean()
        dataframe.at[index, 'price_dayahead_lastWeek_hour16'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 16]['price_dayahead'].mean()
        dataframe.at[index, 'price_dayahead_lastWeek_hour17'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 17]['price_dayahead'].mean()
        dataframe.at[index, 'price_dayahead_lastWeek_hour18'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 18]['price_dayahead'].mean()
        dataframe.at[index, 'price_dayahead_lastWeek_hour19'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 19]['price_dayahead'].mean()
        dataframe.at[index, 'price_dayahead_lastWeek_hour20'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 20]['price_dayahead'].mean()
        dataframe.at[index, 'price_dayahead_lastWeek_hour21'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 21]['price_dayahead'].mean()
        dataframe.at[index, 'price_dayahead_lastWeek_hour22'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 22]['price_dayahead'].mean()
        dataframe.at[index, 'price_dayahead_lastWeek_hour23'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 23]['price_dayahead'].mean()
        dataframe.at[index, 'consumption_dayahead_lastWeek_hour0'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 0]['consumption_dayahead'].mean()
        dataframe.at[index, 'consumption_dayahead_lastWeek_hour1'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 1]['consumption_dayahead'].mean()
        dataframe.at[index, 'consumption_dayahead_lastWeek_hour2'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 2]['consumption_dayahead'].mean()
        dataframe.at[index, 'consumption_dayahead_lastWeek_hour3'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 3]['consumption_dayahead'].mean()
        dataframe.at[index, 'consumption_dayahead_lastWeek_hour4'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 4]['consumption_dayahead'].mean()
        dataframe.at[index, 'consumption_dayahead_lastWeek_hour5'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 5]['consumption_dayahead'].mean()
        dataframe.at[index, 'consumption_dayahead_lastWeek_hour6'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 6]['consumption_dayahead'].mean()
        dataframe.at[index, 'consumption_dayahead_lastWeek_hour7'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 7]['consumption_dayahead'].mean()
        dataframe.at[index, 'consumption_dayahead_lastWeek_hour8'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 8]['consumption_dayahead'].mean()
        dataframe.at[index, 'consumption_dayahead_lastWeek_hour9'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 9]['consumption_dayahead'].mean()
        dataframe.at[index, 'consumption_dayahead_lastWeek_hour10'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 10]['consumption_dayahead'].mean()
        dataframe.at[index, 'consumption_dayahead_lastWeek_hour11'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 11]['consumption_dayahead'].mean()
        dataframe.at[index, 'consumption_dayahead_lastWeek_hour12'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 12]['consumption_dayahead'].mean()
        dataframe.at[index, 'consumption_dayahead_lastWeek_hour13'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 13]['consumption_dayahead'].mean()
        dataframe.at[index, 'consumption_dayahead_lastWeek_hour14'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 14]['consumption_dayahead'].mean()
        dataframe.at[index, 'consumption_dayahead_lastWeek_hour15'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 15]['consumption_dayahead'].mean()
        dataframe.at[index, 'consumption_dayahead_lastWeek_hour16'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 16]['consumption_dayahead'].mean()
        dataframe.at[index, 'consumption_dayahead_lastWeek_hour17'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 17]['consumption_dayahead'].mean()
        dataframe.at[index, 'consumption_dayahead_lastWeek_hour18'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 18]['consumption_dayahead'].mean()
        dataframe.at[index, 'consumption_dayahead_lastWeek_hour19'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 19]['consumption_dayahead'].mean()
        dataframe.at[index, 'consumption_dayahead_lastWeek_hour20'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 20]['consumption_dayahead'].mean()
        dataframe.at[index, 'consumption_dayahead_lastWeek_hour21'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 21]['consumption_dayahead'].mean()
        dataframe.at[index, 'consumption_dayahead_lastWeek_hour22'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 22]['consumption_dayahead'].mean()
        dataframe.at[index, 'consumption_dayahead_lastWeek_hour23'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 23]['consumption_dayahead'].mean()
        dataframe.at[index, 'price_intraday_lastWeek_hour0'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 0]['price'].mean()
        dataframe.at[index, 'price_intraday_lastWeek_hour1'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 1]['price'].mean()
        dataframe.at[index, 'price_intraday_lastWeek_hour2'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 2]['price'].mean()
        dataframe.at[index, 'price_intraday_lastWeek_hour3'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 3]['price'].mean()
        dataframe.at[index, 'price_intraday_lastWeek_hour4'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 4]['price'].mean()
        dataframe.at[index, 'price_intraday_lastWeek_hour5'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 5]['price'].mean()
        dataframe.at[index, 'price_intraday_lastWeek_hour6'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 6]['price'].mean()
        dataframe.at[index, 'price_intraday_lastWeek_hour7'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 7]['price'].mean()
        dataframe.at[index, 'price_intraday_lastWeek_hour8'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 8]['price'].mean()
        dataframe.at[index, 'price_intraday_lastWeek_hour9'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 9]['price'].mean()
        dataframe.at[index, 'price_intraday_lastWeek_hour10'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 10]['price'].mean()
        dataframe.at[index, 'price_intraday_lastWeek_hour11'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 11]['price'].mean()
        dataframe.at[index, 'price_intraday_lastWeek_hour12'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 12]['price'].mean()
        dataframe.at[index, 'price_intraday_lastWeek_hour13'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 13]['price'].mean()
        dataframe.at[index, 'price_intraday_lastWeek_hour14'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 14]['price'].mean()
        dataframe.at[index, 'price_intraday_lastWeek_hour15'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 15]['price'].mean()
        dataframe.at[index, 'price_intraday_lastWeek_hour16'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 16]['price'].mean()
        dataframe.at[index, 'price_intraday_lastWeek_hour17'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 17]['price'].mean()
        dataframe.at[index, 'price_intraday_lastWeek_hour18'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 18]['price'].mean()
        dataframe.at[index, 'price_intraday_lastWeek_hour19'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 19]['price'].mean()
        dataframe.at[index, 'price_intraday_lastWeek_hour20'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 20]['price'].mean()
        dataframe.at[index, 'price_intraday_lastWeek_hour21'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 21]['price'].mean()
        dataframe.at[index, 'price_intraday_lastWeek_hour22'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 22]['price'].mean()
        dataframe.at[index, 'price_intraday_lastWeek_hour23'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 23]['price'].mean()
        dataframe.at[index, 'consumption_intraday_lastWeek_hour0'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 0]['consumption'].mean()
        dataframe.at[index, 'consumption_intraday_lastWeek_hour1'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 1]['consumption'].mean()
        dataframe.at[index, 'consumption_intraday_lastWeek_hour2'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 2]['consumption'].mean()
        dataframe.at[index, 'consumption_intraday_lastWeek_hour3'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 3]['consumption'].mean()
        dataframe.at[index, 'consumption_intraday_lastWeek_hour4'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 4]['consumption'].mean()
        dataframe.at[index, 'consumption_intraday_lastWeek_hour5'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 5]['consumption'].mean()
        dataframe.at[index, 'consumption_intraday_lastWeek_hour6'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 6]['consumption'].mean()
        dataframe.at[index, 'consumption_intraday_lastWeek_hour7'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 7]['consumption'].mean()
        dataframe.at[index, 'consumption_intraday_lastWeek_hour8'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 8]['consumption'].mean()
        dataframe.at[index, 'consumption_intraday_lastWeek_hour9'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 9]['consumption'].mean()
        dataframe.at[index, 'consumption_intraday_lastWeek_hour10'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 10]['consumption'].mean()
        dataframe.at[index, 'consumption_intraday_lastWeek_hour11'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 11]['consumption'].mean()
        dataframe.at[index, 'consumption_intraday_lastWeek_hour12'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 12]['consumption'].mean()
        dataframe.at[index, 'consumption_intraday_lastWeek_hour13'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 13]['consumption'].mean()
        dataframe.at[index, 'consumption_intraday_lastWeek_hour14'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 14]['consumption'].mean()
        dataframe.at[index, 'consumption_intraday_lastWeek_hour15'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 15]['consumption'].mean()
        dataframe.at[index, 'consumption_intraday_lastWeek_hour16'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 16]['consumption'].mean()
        dataframe.at[index, 'consumption_intraday_lastWeek_hour17'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 17]['consumption'].mean()
        dataframe.at[index, 'consumption_intraday_lastWeek_hour18'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 18]['consumption'].mean()
        dataframe.at[index, 'consumption_intraday_lastWeek_hour19'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 19]['consumption'].mean()
        dataframe.at[index, 'consumption_intraday_lastWeek_hour20'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 20]['consumption'].mean()
        dataframe.at[index, 'consumption_intraday_lastWeek_hour21'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 21]['consumption'].mean()
        dataframe.at[index, 'consumption_intraday_lastWeek_hour22'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 22]['consumption'].mean()
        dataframe.at[index, 'consumption_intraday_lastWeek_hour23'] = lastWeekdf.loc[pd.DatetimeIndex(lastWeekdf['datetime']).hour == 23]['consumption'].mean()
        
        # Print index to track progress
        if index % 1000 == 0:
            print(index)

# Drop the first few rows where no aggregated data columns could be filled
dataframe = dataframe.drop(index=range(0,rowsToSkip))


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
