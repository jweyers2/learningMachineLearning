import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import autocorrelation_plot

path = '../00 Data/Final/final.csv'
dataframe = pd.read_csv(path, dayfirst=True)

dataframe['datetime'] = pd.to_datetime(dataframe['datetime'])
datetime = dataframe['datetime']

price = dataframe['price']
price_dayahead = dataframe['price_dayahead']
price_premium = dataframe['price_premium']
cat_price_premium = dataframe['cat_price_premium']
participants = dataframe['participants']
intraday_consumption = dataframe['consumption']
dayahead_consumption = dataframe['consumption_dayahead']
dailyTempAvg = dataframe['dailyTempAvg(Celsius)']
dailyTempMax = dataframe['dailyTempMax(Celsius)']
dailyTempMin = dataframe['dailyTempMin(Celsius)']
numberFreezingDays = dataframe['numberFreezingDays']
numberIcyDays = dataframe['numberIcyDays']
monthlyRainVolume = dataframe['monthlyRainVolume(mm)']
numberRainyDays = dataframe['numberRainyDays']
dailySunnyHoursAvg = dataframe['dailySunnyHoursAvg']
monthlyWindSpeedAvg = dataframe['monthlyWindSpeedAvg(km/h)']

# intraday price autocorrelation
plt.figure()
autocorrelation_plot(price)
plt.savefig('../00 Data/Figures/price_intraday_autocorrelation.png')
plt.close()

# day ahead price autocorrelation
plt.figure()
autocorrelation_plot(price_dayahead)
plt.savefig('../00 Data/Figures/price_dayahead_autocorrelation.png')
plt.close()

# price premium autocorrelation
plt.figure()
autocorrelation_plot(price_premium)
plt.savefig('../00 Data/Figures/price_premium_autocorrelation.png')
plt.close()

# categorical price premium autocorrelation
plt.figure()
autocorrelation_plot(cat_price_premium)
plt.savefig('../00 Data/Figures/price_premium_cat_autocorrelation.png')
plt.close()

# intraday price
plt.plot(datetime, price)
plt.setp(plt.xticks()[1], rotation=90, ha='left')
plt.ylabel('Price (€/MWh)')
plt.title('Intraday auction price history')
plt.gcf().subplots_adjust(bottom=0.15)

plt.savefig('../00 Data/Figures/price_intraday.png')
plt.close()

# day ahead price
plt.plot(datetime, price_dayahead)
plt.setp(plt.xticks()[1], rotation=90, ha='left')
plt.ylabel('Price (€/MWh)')
plt.title('Day-ahead auction price history')
plt.gcf().subplots_adjust(bottom=0.15)

plt.savefig('../00 Data/Figures/price_dayahead.png')
plt.close()

# price comparison
plt.plot(datetime, price, alpha=0.5, color='b', label='Intraday auction')
plt.plot(datetime, price_dayahead, alpha=0.5, color='r', label='Day-ahead auction')
plt.setp(plt.xticks()[1], rotation=90, ha='left')
axes = plt.gca()
axes.set_ylim([-150, 200])
plt.ylabel('Price (€/MWh)')
plt.title('Price comparison')
plt.legend(loc=0)
plt.gcf().subplots_adjust(bottom=0.15)

plt.savefig('../00 Data/Figures/prices.png')
plt.close()

# participants
plt.plot(datetime, participants)
plt.setp(plt.xticks()[1], rotation=90, ha='left')
plt.ylabel('Number of market participants')
plt.title('Market participation history')
plt.gcf().subplots_adjust(bottom=0.15)

plt.savefig('../00 Data/Figures/participants.png')
plt.close()

# intraday consumption
plt.plot(datetime, intraday_consumption)
plt.setp(plt.xticks()[1], rotation=90, ha='left')
plt.ylabel('Consumption (MWh)')
plt.title('Intraday auction energy consumption in 15 minute time frames')
plt.gcf().subplots_adjust(bottom=0.15)

plt.savefig('../00 Data/Figures/consumption_intraday.png')
plt.close()

# day ahead consumption
plt.plot(datetime, dayahead_consumption)
plt.setp(plt.xticks()[1], rotation=90, ha='left')
plt.ylabel('Consumption (MWh)')
plt.title('Day-ahead auction energy consumption in 15 minute time frames')
plt.gcf().subplots_adjust(bottom=0.15)

plt.savefig('../00 Data/Figures/consumption_dayahead.png')
plt.close()

# price comparison
plt.plot(datetime, intraday_consumption, alpha=0.5, color='b', label='Intraday auction')
plt.plot(datetime, dayahead_consumption, alpha=0.5, color='r', label='Day-ahead auction')
plt.setp(plt.xticks()[1], rotation=90, ha='left')
axes = plt.gca()
axes.set_ylim([0, 25000])
plt.ylabel('Consumption (MWh)')
plt.title('Energy consumption comparison in 15 minute time frames')
plt.legend(loc=0)
plt.gcf().subplots_adjust(bottom=0.15)

plt.savefig('../00 Data/Figures/consumption.png')
plt.close()

# temperature
plt.plot(datetime, dailyTempAvg, alpha=0.5, color='m', label='Average temperature')
plt.plot(datetime, dailyTempMax, alpha=0.5, color='r', label='Maximum temperature')
plt.plot(datetime, dailyTempMin, alpha=0.5, color='b', label='Minimum temperature')
plt.setp(plt.xticks()[1], rotation=90, ha='left')
axes = plt.gca()
axes.set_ylim([-5, 25])
plt.ylabel('Temperature (°C)')
plt.title('Temperature of an average day per month')
plt.legend(loc=0)
plt.gcf().subplots_adjust(bottom=0.15)

plt.savefig('../00 Data/Figures/temperature.png')
plt.close()

# cold days
plt.plot(datetime, numberFreezingDays, alpha=0.5, color='b', label='Minimum daily temperature below 0 °C')
plt.plot(datetime, numberIcyDays, alpha=0.5, color='c', label='Maximum daily temperature below 0 °C')
plt.setp(plt.xticks()[1], rotation=90, ha='left')
axes = plt.gca()
axes.set_ylim([0, 29])
plt.ylabel('Number of days per month')
plt.title('Number of cold days per month')
plt.legend(loc=0)
plt.gcf().subplots_adjust(bottom=0.15)

plt.savefig('../00 Data/Figures/cold_days.png')
plt.close()

# rain volume
plt.plot(datetime, monthlyRainVolume)
plt.setp(plt.xticks()[1], rotation=90, ha='left')
plt.ylabel('Rain volume (mm)')
plt.title('Monthly rain volume')
plt.gcf().subplots_adjust(bottom=0.15)

plt.savefig('../00 Data/Figures/rain_volume.png')
plt.close()

# rainy days count
plt.plot(datetime, numberRainyDays)
plt.setp(plt.xticks()[1], rotation=90, ha='left')
plt.ylabel('Number of rainy days')
plt.title('Number of rainy days per month')
plt.gcf().subplots_adjust(bottom=0.15)

plt.savefig('../00 Data/Figures/rainy_day_count.png')
plt.close()

# sunny hours
plt.plot(datetime, dailySunnyHoursAvg)
plt.setp(plt.xticks()[1], rotation=90, ha='left')
plt.ylabel('Number of sunny hours')
plt.title('Amount of sunny hours on an average day per month')
plt.gcf().subplots_adjust(bottom=0.15)

plt.savefig('../00 Data/Figures/sunny_hours.png')
plt.close()

# sunny hours
plt.plot(datetime, monthlyWindSpeedAvg)
plt.setp(plt.xticks()[1], rotation=90, ha='left')
plt.ylabel('Wind speed (km/h)')
plt.title('Average wind speed per month')
plt.gcf().subplots_adjust(bottom=0.15)

plt.savefig('../00 Data/Figures/wind_speed.png')
plt.close()

# normal plots
# https://stackoverflow.com/questions/17430105/autofmt-xdate-deletes-x-axis-labels-of-all-subplots
