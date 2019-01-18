import pandas as pd
# import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import datetime as dt
from pandas.plotting import autocorrelation_plot

binarypath = '../00 Data/Final/binaryFinal.csv'
binaryDataframe = pd.read_csv(binarypath, dayfirst=True)
path = '../00 Data/Final/final.csv'
dataframe = pd.read_csv(path, dayfirst=True)

dataframe['datetime'] = pd.to_datetime(dataframe['datetime'])
datetime = dataframe['datetime']

onlyNew = True

price = dataframe['price']
price_dayahead = dataframe['price_dayahead']
price_premium = dataframe['price_premium']
cat_price_premium = binaryDataframe['cat_price_premium']
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

output = '../00 Data/FiguresPresentation/'
resolution = 600
plt.style.use('dark_background')
color = '#39BFB9'

if onlyNew == False:
    # intraday price autocorrelation
    plt.figure()
    autocorrelation_plot(price, color=color)
    outputPath = output + 'price_intraday_autocorrelation.png'
    plt.savefig(outputPath, transparent=True, dpi=resolution)
    plt.close()

    # day ahead price autocorrelation
    plt.figure()
    autocorrelation_plot(price_dayahead, color=color)
    outputPath = output + 'price_dayahead_autocorrelation.png'
    plt.savefig(outputPath, transparent=True, dpi=resolution)
    plt.close()

    # price premium autocorrelation
    plt.figure()
    autocorrelation_plot(price_premium, color=color)
    outputPath = output + 'price_premium_autocorrelation.png'
    plt.savefig(outputPath, transparent=True, dpi=resolution)
    plt.close()

    # categorical price premium autocorrelation
    plt.figure()
    autocorrelation_plot(cat_price_premium, color=color)
    outputPath = output + 'price_premium_cat_autocorrelation.png'
    plt.savefig(outputPath, transparent=True, dpi=resolution)
    plt.close()

    # intraday price
    plt.plot(datetime, price, color=color)
    plt.setp(plt.xticks()[1], rotation=90, ha='left')
    plt.ylabel('Price (€/MWh)')
    plt.title('Intraday auction price history')
    plt.gcf().subplots_adjust(bottom=0.15)
    outputPath = output + 'price_intraday.png'
    plt.savefig(outputPath, transparent=True, dpi=resolution)
    plt.close()

    # day ahead price
    plt.plot(datetime, price_dayahead, color=color)
    plt.setp(plt.xticks()[1], rotation=90, ha='left')
    plt.ylabel('Price (?/MWh)')
    plt.title('Day-ahead auction price history')
    plt.gcf().subplots_adjust(bottom=0.15)
    outputPath = output + 'price_dayahead.png'
    plt.savefig(outputPath, transparent=True, dpi=resolution)
    plt.close()

    # price comparison
    plt.plot(datetime, price, alpha=0.5, color='b', label='Intraday auction')
    plt.plot(datetime, price_dayahead, alpha=0.5, color='r', label='Day-ahead auction')
    plt.setp(plt.xticks()[1], rotation=90, ha='left')
    axes = plt.gca()
    axes.set_ylim([-150, 200])
    plt.ylabel('Price (?/MWh)')
    plt.title('Price comparison')
    plt.legend(loc=0)
    plt.gcf().subplots_adjust(bottom=0.15)
    outputPath = output + 'prices.png'
    plt.savefig(outputPath, transparent=True, dpi=resolution)
    plt.close()

    # participants
    plt.plot(datetime, participants, color=color)
    plt.setp(plt.xticks()[1], rotation=90, ha='left')
    plt.ylabel('Number of market participants')
    plt.title('Market participation history')
    plt.gcf().subplots_adjust(bottom=0.15)
    outputPath = output + 'participants.png'
    plt.savefig(outputPath, transparent=True, dpi=resolution)
    plt.close()

    # intraday consumption
    plt.plot(datetime, intraday_consumption, color=color)
    plt.setp(plt.xticks()[1], rotation=90, ha='left')
    plt.ylabel('Consumption (MWh)')
    plt.title('Intraday auction energy consumption in 15 minute time frames')
    plt.gcf().subplots_adjust(bottom=0.15)
    outputPath = output + 'consumption_intraday.png'
    plt.savefig(outputPath, transparent=True, dpi=resolution)
    plt.close()

    # day ahead consumption
    plt.plot(datetime, dayahead_consumption, color=color)
    plt.setp(plt.xticks()[1], rotation=90, ha='left')
    plt.ylabel('Consumption (MWh)')
    plt.title('Day-ahead auction energy consumption in 15 minute time frames')
    plt.gcf().subplots_adjust(bottom=0.15)
    outputPath = output + 'consumption_dayahead.png'
    plt.savefig(outputPath, transparent=True, dpi=resolution)
    plt.close()

    # consumption comparison
    plt.plot(datetime, intraday_consumption, alpha=0.5, color='b', label='Intraday auction')
    plt.plot(datetime, dayahead_consumption, alpha=0.5, color='r', label='Day-ahead auction')
    plt.setp(plt.xticks()[1], rotation=90, ha='left')
    axes = plt.gca()
    axes.set_ylim([0, 25000])
    plt.ylabel('Consumption (MWh)')
    plt.title('Energy consumption comparison in 15 minute time frames')
    plt.legend(loc=0)
    plt.gcf().subplots_adjust(bottom=0.15)
    outputPath = output + 'consumption.png'
    plt.savefig(outputPath, transparent=True, dpi=resolution)
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
    outputPath = output + 'temperature.png'
    plt.savefig(outputPath, transparent=True, dpi=resolution)
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
    outputPath = output + 'cold_days.png'
    plt.savefig(outputPath, transparent=True, dpi=resolution)
    plt.close()

    # rain volume
    plt.plot(datetime, monthlyRainVolume, color=color)
    plt.setp(plt.xticks()[1], rotation=90, ha='left')
    plt.ylabel('Rain volume (mm)')
    plt.title('Monthly rain volume')
    plt.gcf().subplots_adjust(bottom=0.15)
    outputPath = output + 'rain_volume.png'
    plt.savefig(outputPath, transparent=True, dpi=resolution)
    plt.close()

    # rainy days count
    plt.plot(datetime, numberRainyDays, color=color)
    plt.setp(plt.xticks()[1], rotation=90, ha='left')
    plt.ylabel('Number of rainy days')
    plt.title('Number of rainy days per month')
    plt.gcf().subplots_adjust(bottom=0.15)
    outputPath = output + 'rainy_day_count.png'
    plt.savefig(outputPath, transparent=True, dpi=resolution)
    plt.close()

    # sunny hours
    plt.plot(datetime, dailySunnyHoursAvg, color=color)
    plt.setp(plt.xticks()[1], rotation=90, ha='left')
    plt.ylabel('Number of sunny hours')
    plt.title('Amount of sunny hours on an average day per month')
    plt.gcf().subplots_adjust(bottom=0.15)
    outputPath = output + 'sunny_hours.png'
    plt.savefig(outputPath, transparent=True, dpi=resolution)
    plt.close()

    # sunny hours
    plt.plot(datetime, monthlyWindSpeedAvg, color=color)
    plt.setp(plt.xticks()[1], rotation=90, ha='left')
    plt.ylabel('Wind speed (km/h)')
    plt.title('Average wind speed per month')
    plt.gcf().subplots_adjust(bottom=0.15)
    outputPath = output + 'wind_speed.png'
    plt.savefig(outputPath, transparent=True, dpi=resolution)
    plt.close()

    # day ahead consumption in points
    plt.plot(datetime, dayahead_consumption, 'o', markersize=0.5, color=color)
    plt.setp(plt.xticks()[1], rotation=90, ha='left')
    plt.ylabel('Consumption (MWh)')
    plt.title('Day-ahead auction energy consumption in 15 minute time frames')
    plt.gcf().subplots_adjust(bottom=0.15)
    outputPath = output + 'consumption_dayahead_points.png'
    plt.savefig(outputPath, transparent=True, dpi=resolution)
    plt.close()

    # intraday consumption with points
    plt.plot(datetime, intraday_consumption, 'o', markersize=0.5, color=color)
    plt.setp(plt.xticks()[1], rotation=90, ha='left')
    plt.ylabel('Consumption (MWh)')
    plt.title('Intraday auction energy consumption in 15 minute time frames')
    plt.gcf().subplots_adjust(bottom=0.15)
    outputPath = output + 'consumption_intraday_points.png'
    plt.savefig(outputPath, transparent=True, dpi=resolution)
    plt.close()

    # intraday price autocorrelation
    plt.figure()
    autocorrelation_plot(price, color=color)
    outputPath = output + 'price_intraday_autocorrelation.png'
    plt.savefig(outputPath, transparent=True, dpi=resolution)
    plt.close()

#Price comparison over one day
plt.plot(datetime[0:95], price[0:95], alpha=0.5, color='#6D9EEB', label='Intraday auction')
plt.plot(datetime[0:95], price_dayahead[0:95], alpha=0.5, color='#F35B69', label='Day-ahead auction')
plt.setp(plt.xticks()[1], rotation=90, ha='left')
axes = plt.gca()
axes.set_ylim([-150, 200])
plt.ylabel('Price (Euro/MWh)')
plt.title('Price comparison over one day')
plt.legend(loc=0)
plt.gcf().subplots_adjust(bottom=0.15)
plt.ylim([0, 50])
outputPath = output + 'pricesOneDay.png'
plt.savefig(outputPath, transparent=True, dpi=resolution)
plt.close()


# normal plots
# https://stackoverflow.com/questions/17430105/autofmt-xdate-deletes-x-axis-labels-of-all-subplots
