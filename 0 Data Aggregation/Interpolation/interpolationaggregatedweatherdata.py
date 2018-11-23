import pandas as pd
import datetime

#load csv-file and put it into a dataframe
path="../../00 Data/aggregatedWeatherData.csv"
dataframe= pd.read_csv(path)

#function to add 23:45 hours so that the bfill method will work fine
def addhours(data):
    dataframe["datetime"]=pd.to_datetime(dataframe["datetime"])
    index = dataframe.columns.get_loc("datetime")
    valueOfColumn = dataframe.iloc[0:, index]
    newtime=[]
    del dataframe["datetime"]
    for i in valueOfColumn:
        i= i+ datetime.timedelta(hours=23, minutes=45)
        newtime.append(i)
    dataframe.insert(index, "datetime", newtime)
    return dataframe

#run the function and create the new dataframe with new timestamps
dataframe=addhours(dataframe)


#dataframe["datetime"]= pd.to_datetime(dataframe["datetime"])
#create new series with time column from 01.01.2016 00:00:00 to 31.12.2017 23:45:00 in 15 minute steps
time = pd.Series(pd.date_range(start='01.01.2016 00:00:00', end="31.12.2017 23:45:00",freq='15min'))
#Convert the Series to a dataframe to have access to .set_index
time = pd.DataFrame(time)
#Rename the only column of the dataframe datetime and set it as the index of the dataframe time
time.columns= ["datetime"]
time.set_index('datetime',inplace=True)
#set the index of the dataframe as datetime
dataframe.set_index('datetime',inplace=True)
#Create a join of the time and the dataframe dataframe on the column datetime
merge=time.join(dataframe)
#Fill all the NANs with the
merge.fillna(method="bfill", inplace=True)
#Save merged dataframes in csv-file
save_path= '../../00 Data/Interpolation_Data/interpolated_weatherdata.csv'
merge.to_csv(save_path)


