# merge the interpolated day-ahead data and the intra-day data to a combined datafile
import pandas as pd
import numpy as np

path_weather= '../00 Data/quarterhourlyIntraDayData.csv'
path_intraday= '../00 Data/merge.csv'
#path_interday='../00 Data/interpolatedDayAhead'
weather_data=pd.read_csv(path_weather)
intraday_data= pd.read_csv(path_intraday)
#interday_data= pd.read_csv(path_interday)

intraday_data.set_index('datetime', inplace=True)
weather_data.set_index('datetime', inplace=True)
#interday_data.set_index('datetime', inplace=True)

def join_dataframes(dataframe1, dataframe2):
    result= dataframe1.join(dataframe2)
    return result

weather_intraday= join_dataframes(weather_data,intraday_data)
#final= join_dataframes(weather_intraday, interday_data)
out_path= '../00 Data/final.csv'
weather_intraday.to_csv(out_path)

