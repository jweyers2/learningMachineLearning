import pandas as pd
import matplotlib.pyplot as plt

path = '../../00 Data/Final/cleanFinal.csv'

df = pd.read_csv(path,sep=',')
df['datetime']= pd.to_datetime(df['datetime'])
df.set_index('datetime', inplace=True)

"""
First Run at 1% Level: -3,4 --> stationary : IS THAT CORRECT?? -> validate!!!
sources by https://machinelearningmastery.com/time-series-data-stationary-python/
https://machinelearningmastery.com/time-series-forecast-case-study-python-monthly-armed-robberies-boston/
"""
def stationaryTest(df):
    from statsmodels.tsa.stattools import adfuller

    # Determing rolling statistics
    rolmean = df['price_premium'].rolling(12).mean()
    rolstd = df['price_premium'].rolling(12).std()

    # Plot rolling statistics:
    orig = plt.plot(df['price_premium'], color='blue', label='Original')
    mean = plt.plot(rolmean, color='red', label='Rolling Mean')
    std = plt.plot(rolstd, color='black', label='Rolling Std')
    plt.legend(loc='best')
    plt.title('Rolling Mean & Standard Deviation')
    # plt.show(block=False)
    plt.show()

    result = adfuller(df['price_premium'].values)
    print('ADF Statistic: %f' % result[0])
    print('p-value: %f' % result[1])
    print('Critical Values:')
    for key, value in result[4].items():
        print('\t%s: %.3f' % (key, value))

    return result

# stationaryTest(df)

"""
TODO: PACF / ACF --> STRUCTURED DETERMINATION OF P , Q (D IS = 0 )
sources partially by: https://www.analyticsvidhya.com/blog/2016/02/time-series-forecasting-codes-python/
ASSUMPTION FOR FURTHER MODELING -> TIMESERIES STATIONARY (DICKEY-FULLER-TEST)
"""
def arima(df):
    from statsmodels.tsa.arima_model import ARIMA
    import datetime
    f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
    model = ARIMA(df['price_premium'].values,order=(2, 1, 0))
    results_AR = model.fit(disp=-1)
    # plt.plot(df['price_premium'].values,color='b')

    ax1.plot(results_AR.fittedvalues, color='red')
    ax2.plot(results_AR.predict(start = datetime.datetime(year=2016, month=1, day = 1, hour = 0,minute=0), end = datetime.datetime(year=2017, month=12, day = 31, hour = 23,minute=45), dynamic=True), color='green')
    plt.show()

arima(df)