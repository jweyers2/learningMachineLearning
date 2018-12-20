import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


"""
TIMESERIES IS STATIONARY
sources:
https://machinelearningmastery.com/time-series-data-stationary-python/
https://machinelearningmastery.com/time-series-forecast-case-study-python-monthly-armed-robberies-boston/
"""
def stationaryTest(ts):
    from statsmodels.tsa.stattools import adfuller

    # Determing rolling statistics
    rolmean = ts.rolling(12).mean()
    rolstd = ts.rolling(12).std()

    # Plot rolling statistics:
    orig = plt.plot(ts, color='blue', label='Original')
    mean = plt.plot(rolmean, color='red', label='Rolling Mean')
    std = plt.plot(rolstd, color='black', label='Rolling Std')
    plt.legend(loc='best')
    plt.title('Rolling Mean & Standard Deviation')
    # plt.show(block=False)
    plt.show()

    result = adfuller(ts.values)
    print('ADF Statistic: %f' % result[0])
    print('p-value: %f' % result[1])
    print('Critical Values:')
    for key, value in result[4].items():
        print('\t%s: %.3f' % (key, value))

    return result


"""
PACF / ACF
RIGHT VALUES FOR P <--ACF / Q <--PACF
HOW TO DETERMINE THE ACF THRESHOLDS:
https://stats.stackexchange.com/questions/185425/how-to-determine-the-critical-values-of-acf
http://sfb649.wiwi.hu-berlin.de/fedc_homepage/xplore/tutorials/xegbohtmlnode39.html
https://sccn.ucsd.edu/wiki/Chapter_3.6._Model_Validation
"""

def printPACFACF(price_premium):
    from statsmodels.tsa.stattools import acf, pacf
    ACF_PLOT_RANGE = 6000
    pp_log = price_premium.values
    lag_acf = acf(pp_log, nlags=ACF_PLOT_RANGE)
    lag_pacf = pacf(pp_log, nlags=20, method='ols')
    # Plot ACF:
    plt.subplot(121)
    plt.plot(lag_acf)
    plt.axhline(y=0, linestyle='--', color='gray')
    x = pd.Series(range(ACF_PLOT_RANGE))
    y_ = (-1.96 / np.sqrt(len(pp_log)-x))
    y = (1.96 / np.sqrt(len(pp_log)-x))
    plt.plot(x.values, y_.values, linestyle='--', color='gray')
    plt.plot(x.values,y.values, linestyle='--', color='gray')
    plt.title('Autocorrelation Function')

    # Plot PACF:
    plt.subplot(122)
    plt.plot(lag_pacf)
    plt.axhline(y=0, linestyle='--', color='gray')
    plt.axhline(y=-1.96 / np.sqrt(len(pp_log)), linestyle='--', color='gray')
    plt.axhline(y=1.96 / np.sqrt(len(pp_log)), linestyle='--', color='gray')
    plt.title('Partial Autocorrelation Function')
    plt.tight_layout()
    plt.show()


    from statsmodels.graphics.tsaplots import plot_acf
    plot_acf(pp_log)
    plt.show()


"""
Decomposition
"""
def decompose(timeseries):
    from statsmodels.tsa.seasonal import seasonal_decompose
    decomposition_ts_saisonal_1 = seasonal_decompose(timeseries, freq=96)
    # decomposition_ts_saisonal_2 = seasonal_decompose(timeseries, freq=672)

    # Seasonal
    seasonal_1 = decomposition_ts_saisonal_1.seasonal
    # seasonal_2 = decomposition_ts_saisonal_2.seasonal
    seasonal_1.fillna(inplace=True, value=seasonal_1.mean())
    # seasonal_2.fillna(inplace=True, value=seasonal_2.mean())
    detrend_ts = decomposition_ts_saisonal_1.resid
    # detrend_ts = detrend_ts - seasonal_2

    # Subtract the seasonal to make TS stationary
    # detrend_ts = timeseries - seasonal
    detrend_ts.fillna(value=detrend_ts.mean(), inplace=True)

    # Plot
    fig, axs = plt.subplots(1, 3, figsize=(9, 3), sharey=True)
    axs[0].plot(timeseries, label='Original')
    plt.legend(loc='best')
    axs[1].plot(seasonal_1,label='Seasonality')
    plt.legend(loc='best')
    axs[2].plot(detrend_ts, label='residual')
    plt.legend(loc='best')
    fig.autofmt_xdate()

    plt.show()

    # return (detrend_ts, seasonal_1,seasonal_2)
    return (detrend_ts, seasonal_1)

"""
TODO: PACF / ACF --> STRUCTURED DETERMINATION OF P , Q (D IS = 0 )
sources partially by: https://www.analyticsvidhya.com/blog/2016/02/time-series-forecasting-codes-python/
ASSUMPTION FOR FURTHER MODELING -> TIMESERIES STATIONARY (DICKEY-FULLER-TEST)
"""
def arima(ts,exVar=None):
    from statsmodels.tsa.arima_model import ARIMA
    TRAIN_RATIO = 0.7
    date_index = ts.index
    from sklearn.metrics import mean_absolute_error
    from sklearn.model_selection import TimeSeriesSplit
    tscv = TimeSeriesSplit(n_splits=2)
    errors = []
    for train, test in tscv.split(ts.values):
        p = 1
        d = 0
        q = 1
        if exVar is None:
            model = ARIMA(ts.iloc[train], dates=np.asanyarray(ts.index[train]), order=(p, d, q))
        else:
            model = ARIMA(ts.iloc[train], dates=np.asanyarray(ts.index[train]), exog=exVar.iloc[train, :],
                          order=(p, d, q))
        results_AR = model.fit(disp=-1)
        if exVar is None:
            predictions = results_AR.predict(start=ts.index[test[0]].to_pydatetime(),end=ts.index[test[-1]].to_pydatetime(), dynamic=True)
            # predictions = results_AR.forecast(steps=1000)
        else:
           predictions = results_AR.predict(start=ts.index[test[0]].to_pydatetime(),end=ts.index[test[-1]].to_pydatetime(),exog=exVar.iloc[train,:],dynamic=True)

        errors.append(mean_absolute_error(ts.iloc[test],predictions))

    print("MAE:" + str(np.mean(errors)))
    predictions = pd.Series(predictions)
    import datetime as dt
    # predictions.index = pd.date_range(dt.datetime(year=2018,month=1,day=1,hour=0,minute=0), periods=1000).tolist()
    predictions.index = date_index[test]
    return predictions,results_AR



