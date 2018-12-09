import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
#ACF and PACF plots:
from statsmodels.tsa.stattools import acf, pacf

path = '../../00 Data/Final/cleanFinal.csv'

df = pd.read_csv(path,sep=',')
df['datetime']= pd.to_datetime(df['datetime'])
df.set_index('datetime', inplace=True)
price_premium= df['price_premium']
pp_log= np.log(price_premium)

lag_acf = acf(np.diff(math.log(price_premium)))
#acf(log(price_premium))
lag_pacf = pacf(price_premium, nlags=20, method='ols')

#Plot ACF:
plt.subplot(121)
plt.plot(lag_acf)
plt.axhline(y=0,linestyle='--',color='gray')
plt.axhline(y=-1.96/np.sqrt(len(pp_log)),linestyle='--',color='gray')
plt.axhline(y=1.96/np.sqrt(len(pp_log)),linestyle='--',color='gray')
plt.title('Autocorrelation Function')

#Plot PACF:
plt.subplot(122)
plt.plot(lag_pacf)
plt.axhline(y=0,linestyle='--',color='gray')
plt.axhline(y=-1.96/np.sqrt(len(pp_log)),linestyle='--',color='gray')
plt.axhline(y=1.96/np.sqrt(len(pp_log)),linestyle='--',color='gray')
plt.title('Partial Autocorrelation Function')
plt.tight_layout()