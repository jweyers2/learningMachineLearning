# change day ahead dataset from an hourly to quarterhourly resolution
# use interpolation to fill in the missing values
import pandas as pd
import datetime

path ='../../00 Data/hourlyDayAheadData.csv'
df= pd.read_csv(path)
df['datetime']=pd.to_datetime(df['datetime'])
#print(df)

#Fehler korrigieren -->31.10.2016 02:00, 01.11.2016 02:00, 02.11.2016 02:00, 03.11.2016 02:00, 04.11.2016 02:00, 05.11.2016 02:00, 30.10.2017 02:00, 31.10.2017 02:00, 01.11.2017 02:00, 02.11.2017 02:00, 03.11.2017 02:00, 04.11.2017 02:00
df= df.drop_duplicates(subset='datetime',keep='first')


time = pd.Series(pd.date_range(start='01.01.2016 00:00:00', end="31.12.2017 23:45:00",freq='15min'))
#print(time)
time = pd.DataFrame(time)
time.columns= ["datetime"]
time.set_index('datetime',inplace=True)
df.set_index('datetime',inplace=True)


merge=time.join(df)
merge.fillna(method="ffill", inplace=True)

#Save the datastream to a new .csv file
save_path= '../../00 Data/Interpolation_Data/interpolatedDayAhead.csv'
merge.to_csv(save_path)




