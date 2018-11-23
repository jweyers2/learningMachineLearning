# merge the interpolated day-ahead data and the intra-day data to a combined datafile
import pandas as pd
import numpy as np
import datetime

path_weather= '../00 Data/Interpolation_Data/interpolated_weatherdata.csv'
path_intraday= '../00 Data/quarterhourlyIntraDayData.csv'
path_interday='../00 Data/Interpolation_Data/interpolatedDayAhead.csv'
path_participants='../00 Data/Interpolation_Data/interpolated_participants.csv'
path_holidays='../00 Data/Interpolation_Data/interpolated_holidays.csv'
weather_data=pd.read_csv(path_weather)
intraday_data= pd.read_csv(path_intraday)
interday_data= pd.read_csv(path_interday)
participants=pd.read_csv(path_participants)
holidays=pd.read_csv(path_holidays)

#Fehler korrigieren --> Siehe Excel
intraday_data['datetime']= pd.to_datetime(intraday_data['datetime'])
intraday_data= intraday_data.drop_duplicates(subset='datetime',keep='first')

#renaming columns in interday_data
interday_data.rename(columns={'consumption': 'consumption_dayahead', 'price': 'price_dayahead'}, inplace=True)

#setting the index of the data to the datetime column
intraday_data.set_index('datetime', inplace=True)
print(intraday_data.shape, "Shape Intradaydata")
weather_data.set_index('datetime', inplace=True)
print(weather_data.shape, "Shape weather")
interday_data.set_index('datetime', inplace=True)
print(interday_data.shape, "Shape Interday")
participants.set_index('datetime', inplace=True)
print(participants.shape, "Shape participants")
holidays.set_index('datetime', inplace=True)
print(participants.shape, "Shape participants")

def join_dataframes(dataframe1, dataframe2):
    result= dataframe1.join(dataframe2)
    return result



weather_intraday= join_dataframes(intraday_data, weather_data)
without_holidays= join_dataframes(weather_intraday, interday_data)
without_participants= join_dataframes(without_holidays, holidays)
final=join_dataframes(without_participants,participants)

#output the final file
out_path= '../00 Data/Final/final.csv'
final.to_csv(out_path)

