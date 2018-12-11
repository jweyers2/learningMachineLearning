import pandas as pd
import numpy as np
import statistics

path = '../00 Data/Final/cleanFinal.csv'
df= pd.read_csv(path,sep=',')
df['datetime']= pd.to_datetime(df['datetime'])
df.set_index('datetime', inplace=True)

intraday_price= df['price']
dayahead_price= df['price_dayahead']

mean_interday= dayahead_price.mean()
mean_intra=intraday_price.mean()
var_interday= np.var(dayahead_price)
var_intraday= np.var(intraday_price)
stdev_interday= statistics.stdev(dayahead_price)
stdev_intraday= statistics.stdev(intraday_price)
print('Mean of Intraday-Price: ', mean_intra)
print('Mean of Interday-Price: ', mean_interday)
print('Variance of Intraday-Price: ', var_intraday)
print('Variance of Interday-Price: ', var_interday)
print('Standard Deviation of Intraday-Price: ', stdev_intraday)
print('Standard Deviation of Interday-Price: ', stdev_interday)

#Difference in dayahead and intraday (mean, std, volatility): Interday - Intraday
print('Difference in mean: ', mean_interday-mean_intra)
print('Difference in variance: ', var_interday-var_intraday)
print('Difference in standard deviation: ', stdev_interday-stdev_intraday)


