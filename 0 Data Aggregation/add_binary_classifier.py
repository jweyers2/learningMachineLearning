import pandas as pd
import numpy as np
import datetime

newPath='../00 Data/Final/binaryFinal.csv'
path='../00 Data/Final/final.csv'
dataframe=pd.read_csv(path)

dataframe['datetime'] = pd.to_datetime(dataframe['datetime'])

# Add new rows for aggregated price and volume data of both auctions for the las 2-1 days, 9-2 days and 31-9 days
# last 24 hours before 11:45 on the day of the last auction
dataframe['price_dayahead_lastDay'] = np.nan
dataframe['consumption_dayahead_lastDay'] = np.nan
dataframe['price_intraday_lastDay'] = np.nan
dataframe['consumption_intraday_lastDay'] = np.nan
# last 24-168 hours before 11:45 on the day of the last auction
dataframe['price_dayahead_increase_lastWeek'] = np.nan
dataframe['consumption_dayahead_increase_lastWeek'] = np.nan
dataframe['price_intraday_increase_lastWeek'] = np.nan
dataframe['consumption_intraday_increase_lastWeek'] = np.nan

for index, row in dataframe.iterrows():
    # skip the first 8 days
    daysToSkip = 8
    rowsToSkip = (96*daysToSkip)
    if index > rowsToSkip-1:
        hour = dataframe.iloc[index]['datetime'].hour
        minute = dataframe.iloc[index]['datetime'].minute
        # go to the index of the last day at 11:30
        lastAuctionDate = pd.to_datetime(dataframe.iloc[index]['datetime'].date()-datetime.timedelta(1))
        indexBeforePrediction = dataframe.loc[(pd.DatetimeIndex(dataframe['datetime']).hour == 11) &
                              (pd.DatetimeIndex(dataframe['datetime']).minute == 30) &
                              (pd.DatetimeIndex(dataframe['datetime']).day == lastAuctionDate.day) &
                              (pd.DatetimeIndex(dataframe['datetime']).month == lastAuctionDate.month) &
                              (pd.DatetimeIndex(dataframe['datetime']).year == lastAuctionDate.year)].index[0]
        indexBeforePrediction = indexBeforePrediction.astype(np.int32)

        lastWeekdf = dataframe[indexBeforePrediction - 671:indexBeforePrediction+1]
        lastWeekdf = lastWeekdf.loc[(pd.DatetimeIndex(lastWeekdf['datetime']).hour == hour)&(pd.DatetimeIndex(lastWeekdf['datetime']).minute == minute)]
        lastDaydf = lastWeekdf.iloc[-1]
        # last 24 hours before 11:45 on the day of the last auction
        dataframe.at[index, 'price_dayahead_lastDay'] = lastDaydf['price_dayahead']
        dataframe.at[index, 'consumption_dayahead_lastDay'] = lastDaydf['consumption_dayahead']
        dataframe.at[index, 'price_intraday_lastDay'] = lastDaydf['price']
        dataframe.at[index, 'consumption_intraday_lastDay'] = lastDaydf['consumption']
        # last 24-168 hours before 11:45 on the day of the last auction
        dataframe.at[index, 'price_dayahead_increase_lastWeek'] = (lastWeekdf.iloc[-1]['price_dayahead']-lastWeekdf.iloc[0]['price_dayahead'])/lastWeekdf.shape[0]
        dataframe.at[index, 'consumption_dayahead_increase_lastWeek'] = (lastWeekdf.iloc[-1]['consumption_dayahead']-lastWeekdf.iloc[0]['consumption_dayahead'])/lastWeekdf.shape[0]
        dataframe.at[index, 'price_intraday_increase_lastWeek'] = (lastWeekdf.iloc[-1]['price']-lastWeekdf.iloc[0]['price'])/lastWeekdf.shape[0]
        dataframe.at[index, 'consumption_intraday_increase_lastWeek'] = (lastWeekdf.iloc[-1]['consumption']-lastWeekdf.iloc[0]['consumption'])/lastWeekdf.shape[0]
        
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
