import pandas as pd
from sklearn.preprocessing import StandardScaler

# Use the StandardScaler because price data has some strong outliers
scaler = StandardScaler()
path = '../00 Data/Final/cleanFinal.csv'
dataframe = pd.read_csv(path, dayfirst=True)
numpyMatrix = dataframe.drop(['datetime', 'cat_price_premium', 'isHoliday'], axis=1).values
X_scaled = scaler.fit_transform(numpyMatrix)
print(list(dataframe))
df_scaled = pd.DataFrame(X_scaled)
df_scaled.columns = ['price', 'consumption', 'dailyTempAvg(Celsius)', 'numberFreezingDays', 'numberIcyDays', 'monthlyRainVolume(mm)', 'numberRainyDays', 'dailySunnyHoursAvg', 'monthlyWindSpeedAvg(km/h)', 'price_dayahead', 'consumption_dayahead', 'holidayBefore', 'holidayAfter', 'participants', 'price_premium']
df_scaled['datetime'] = dataframe['datetime']
df_scaled['cat_price_premium'] = dataframe['cat_price_premium']
df_scaled['isHoliday'] = dataframe['isHoliday']
# Rearrange column order
df_scaled = df_scaled[['datetime', 'price', 'consumption', 'dailyTempAvg(Celsius)', 'numberFreezingDays', 'numberIcyDays', 'monthlyRainVolume(mm)', 'numberRainyDays', 'dailySunnyHoursAvg', 'monthlyWindSpeedAvg(km/h)', 'price_dayahead', 'consumption_dayahead', 'holidayBefore', 'holidayAfter', 'isHoliday', 'participants', 'price_premium', 'cat_price_premium']]
df_scaled.to_csv('../00 Data/Final/scaledFinal.csv', index=False, sep=',')
