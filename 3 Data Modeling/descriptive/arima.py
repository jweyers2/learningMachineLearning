import pandas as pd
import arima_utils as utils
import matplotlib.pyplot as plt

path = '../../00 Data/Final/cleanFinal.csv'

df = pd.read_csv(path,sep=',')
df['datetime']= pd.to_datetime(df['datetime'])
df.set_index('datetime', inplace=True)




def main():
    # utils.stationaryTest(df)
    # utils.printPACFACF(df['price_premium'])
    predictions,results = utils.arima(df['price_premium'], df[
        ['dailyTempAvg(Celsius)', 'numberIcyDays', 'numberFreezingDays', 'monthlyRainVolume(mm)', 'numberRainyDays',
         'dailySunnyHoursAvg', 'monthlyWindSpeedAvg(km/h)', 'holidayBefore', 'holidayAfter', 'isHoliday',
         'participants']])
    # predictions,results = utils.arima(df['price_premium'])
    print(results.summary())
    print(results.maparams())
    plt.plot(df['price_premium'], color='blue')
    plt.plot(predictions, color='red')
    plt.show()

if __name__ == '__main__':
    main()