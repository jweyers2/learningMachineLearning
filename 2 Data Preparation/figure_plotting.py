import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pylab

path='../00 Data/Final/cleanFinal.csv'
dataframe=pd.read_csv(path, dayfirst=True)

dataframe['datetime']=pd.to_datetime(dataframe['datetime'])
datetime=dataframe['datetime']

price= dataframe['price']
price_dayahead= dataframe['price_dayahead']
price_premium= dataframe['price_premium']
participants= dataframe['participants']
month= dataframe['month']
intraday_consumption= dataframe['consumption']
dailyTempAvg=dataframe['dailyTempAvg(Celsius)']
dailyTempMax=dataframe['dailyTempMax(Celsius)']
dailyTempMin=dataframe['dailyTempMin(Celsius)']
numberFreezingDays=dataframe['numberFreezingDays']
numberIcyDays=dataframe['numberIcyDays']
monthlyRainVolume=dataframe['monthlyRainVolume(mm)']
numberRainyDays=dataframe['numberRainyDays']
dailySunnyHoursAvg= dataframe['dailySunnyHoursAvg']
monthlyWindSpeedAvg=dataframe['monthlyWindSpeedAvg(km/h)']
consumption_dayahead=dataframe['consumption_dayahead']

#normal plots
plt.plot(datetime,consumption_dayahead)
plt.setp(plt.xticks()[1], rotation=90, ha='left')

plt.savefig('../00 Data/Figures/consumption_dayahead.png')

#normal plots
#https://stackoverflow.com/questions/17430105/autofmt-xdate-deletes-x-axis-labels-of-all-subplots

