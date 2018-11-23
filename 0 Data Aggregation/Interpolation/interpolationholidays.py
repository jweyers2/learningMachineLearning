import pandas as pd
import numpy as np
import datetime

#load csv-file and put it into a dataframe
path="../../00 Data//holidays.csv"
dataframe= pd.read_csv(path)

#dataframe["datetime"]= pd.to_datetime(dataframe["datetime"])
#create new series with time column from 01.01.2016 00:00:00 to 31.12.2017 23:45:00 in 15 minute steps
time = pd.Series(pd.date_range(start='01.01.2016 00:00:00', end="31.12.2017 23:45:00",freq='15min'))

#Convert the Series to a dataframe to have access to .set_index
time = pd.DataFrame(time)
dataframe= pd.DataFrame(dataframe)

dataframe.rename(columns={'date':'datetime'}, inplace=True)
time.rename(columns={0:'datetime'}, inplace=True)
dataframe.datetime= pd.to_datetime(dataframe.datetime)

dataframe.set_index('datetime')
time.set_index('datetime')

merge= time.merge(dataframe, on='datetime', how='left')

#Fill all the NANs with the
merge.fillna(method="ffill", inplace=True)
#Save merged dataframes in csv-file
save_path= '../../00 Data/Interpolation_Data/interpolated_holidays.csv'
merge.to_csv(save_path,index=False)