# change day ahead dataset from an hourly to quarterhourly resolution
# use interpolation to fill in the missing values
import pandas as pd
import datetime

path ='../00 Data/hourlyDayAheadData.csv'
df= pd.read_csv(path)
dataframe_0=pd.read_csv(path)

#Convert the datetime column of the dataframe from strings to timestamps
def convertion(dataframe):
    date = pd.to_datetime(dataframe["datetime"])
    new_date= add_15_minutes(date)
    return new_date

#Add to every timestamp 15 minutes
def add_15_minutes(date):
    new_date = []
    for i in date:
        new_datetime = i + datetime.timedelta(minutes=15)
        new_date.append(new_datetime)
    return new_date

#Create a new dataframe, which can be appended to the old one
def create_new_dataframe(date):
    new_dataframe = pd.DataFrame(df)
    index = df.columns.get_loc("datetime")
    valueOfColumn = df.iloc[0:, index]
    del new_dataframe["datetime"]
    new_dataframe.insert(index, "datetime",date)
    return new_dataframe

#Sort the whole datastream with a timestamp
def sort(dataframe):
    new=dataframe.iloc[pd.to_datetime(dataframe.datetime).sort_values().index]
    return new


#First dataframe with 15 minutes
date_15= convertion(df)
dataframe_15=create_new_dataframe(date_15)
dataframe_1= dataframe_0.append([dataframe_15], ignore_index=True)

#second dataframe with 30 minutes
date_30= convertion(dataframe_15)
dataframe_30= create_new_dataframe(date_30)
dataframe_2= dataframe_1.append(dataframe_30, ignore_index=True)

#third dataframe with 45 minutes
date_45= convertion(dataframe_30)
dataframe_45= create_new_dataframe(date_45)

interpolated_dataframe= dataframe_2.append(dataframe_45, ignore_index=True)

sorted_interpolated_dataframe= sort(interpolated_dataframe)

#Save the datastream to a new .csv file
save_path= '../00 Data/interpolatedDayAhead.csv'
sorted_interpolated_dataframe.to_csv(save_path, index=False)




