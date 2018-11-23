import pandas as pd
import datetime
import statistics

#load csv-file and put it into a dataframe
path="../../00 Data//marketParticipants.csv"
dataframe= pd.read_csv(path)

def calc_append_med(data):
    median=data["participants"][-2:]
    median=statistics.median(median)
    date='2017-11-01'
    data=[[date,median]]
    dataframe2=pd.DataFrame(data,columns=['date','participants'])
    return dataframe2

df2=calc_append_med(dataframe)
#insert median into 01.11.2017 00:00:00
dataframe=dataframe.append(df2,ignore_index=True)


#dataframe["datetime"]= pd.to_datetime(dataframe["datetime"])
#create new series with time column from 01.01.2016 00:00:00 to 31.12.2017 23:45:00 in 15 minute steps
time = pd.Series(pd.date_range(start='01.01.2016 00:00:00', end="31.12.2017 23:45:00",freq='15min'))

#Convert the Series to a dataframe to have access to .set_index
time = pd.DataFrame(time)

#Rename the only column of the dataframe datetime and set it as the index of the dataframe time
dataframe.rename(columns={'date': 'datetime'}, inplace=True)
time.columns= ["datetime"]
time.set_index('datetime',inplace=True)

#set the index of the dataframe as datetime
dataframe.set_index('datetime',inplace=True)

#Create a join of the time and the dataframe dataframe on the column datetime
merge=time.join(dataframe)
#Fill all the NANs with the
merge.fillna(method="ffill", inplace=True)
#Save merged dataframes in csv-file
save_path= '../../00 Data/Interpolation_Data/interpolated_participants.csv'
merge.to_csv(save_path)
