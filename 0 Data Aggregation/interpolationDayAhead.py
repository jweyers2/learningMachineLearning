# change day ahead dataset from an hourly to quarterhourly resolution
# use interpolation to fill in the missing values
import pandas as pd
import datetime

path ='../00 Data/hourlyDayAheadData.csv'
df= pd.read_csv(path)


#Convert the datetime column of the dataframe from strings to timestamps
#Add to every timestamp 15 minutes
def add_15_minutes(dataframe, x):
    dbf= pd.to_datetime(dataframe["datetime"])
    new_date = []
    for i in dbf:
        new_datetime = i + datetime.timedelta(minutes=x)
        new_date.append(new_datetime)
    return new_date

#Create a new dataframe, which can be appended to the old one
def create_new_dataframe(date):
    new_dataframe= pd.read_csv(path)
    del new_dataframe["datetime"]
    new_dataframe["datetime"]=date
    return new_dataframe

#Sort the whole datastream with a timestamp
def sort(dataframe):
    new=dataframe.iloc[pd.to_datetime(dataframe.datetime).sort_values().index]
    return new


#First dataframe with 15 minutes
date_15= add_15_minutes(df,15)
#print(date_15)
dataframe_15=create_new_dataframe(date_15)

#second dataframe with 30 minutes
date_30= add_15_minutes(df,30)
#print(date_30)
dataframe_30= create_new_dataframe(date_30)

#third dataframe with 45 minutes
date_45= add_15_minutes(df,45)
#print(date_45)
dataframe_45= create_new_dataframe(date_45)
interpolated_dataframe= pd.concat([df,dataframe_15,dataframe_30,dataframe_45], ignore_index=True, sort=True)

sorted_interpolated_dataframe= sort(interpolated_dataframe)
print(sorted_interpolated_dataframe)


#Save the datastream to a new .csv file
save_path= '../00 Data/interpolatedDayAhead.csv'
sorted_interpolated_dataframe.to_csv(save_path, index=False)




