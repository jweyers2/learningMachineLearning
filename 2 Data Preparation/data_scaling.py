import pandas as pd
from sklearn.preprocessing import StandardScaler

# Use the StandardScaler because price data has some strong outliers
scaler = StandardScaler()
path = '../00 Data/Final/cleanFinal.csv'
dataframe = pd.read_csv(path, dayfirst=True)
numpyMatrix = dataframe.drop(['datetime', 'isHoliday'], axis=1).values
X_scaled = scaler.fit_transform(numpyMatrix)
print(list(dataframe))
df_scaled = pd.DataFrame(X_scaled)
df_scaled.columns = ['price', 'consumption', 'dailyTempAvg(Celsius)', 'numberFreezingDays', 'numberIcyDays', 'monthlyRainVolume(mm)', 'numberRainyDays', 'dailySunnyHoursAvg', 'monthlyWindSpeedAvg(km/h)', 'price_dayahead', 'consumption_dayahead', 'holidayBefore', 'holidayAfter', 'participants', 'price_premium']
df_scaled['datetime'] = dataframe['datetime']
df_scaled['isHoliday'] = dataframe['isHoliday']
# Rearrange column order
df_scaled = df_scaled[['datetime', 'price', 'consumption', 'dailyTempAvg(Celsius)', 'numberFreezingDays', 'numberIcyDays', 'monthlyRainVolume(mm)', 'numberRainyDays', 'dailySunnyHoursAvg', 'monthlyWindSpeedAvg(km/h)', 'price_dayahead', 'consumption_dayahead', 'holidayBefore', 'holidayAfter', 'isHoliday', 'participants', 'price_premium']]
df_scaled.to_csv('../00 Data/Final/scaledFinal.csv', index=False, sep=',')

path = '../00 Data/Final/binaryCleanFinal.csv'
dataframe = pd.read_csv(path, dayfirst=True)
numpyMatrix = dataframe.drop(['cat_price_premium', 'isHoliday', 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'hour0', 'hour1', 'hour2', 'hour3', 'hour4', 'hour5', 'hour6', 'hour7', 'hour8', 'hour9', 'hour10', 'hour11', 'hour12', 'hour13', 'hour14', 'hour15', 'hour16', 'hour17', 'hour18', 'hour19', 'hour20', 'hour21', 'hour22', 'hour23'], axis=1).values
print(list(dataframe))
# numpyMatrix = dataframe.drop(['cat_price_premium', 'isHoliday'], axis=1).values
X_scaled = scaler.fit_transform(numpyMatrix)
print(list(dataframe))
df_scaled = pd.DataFrame(X_scaled)
df_scaled.columns = ['price', 'consumption', 'dailyTempAvg(Celsius)', 'numberFreezingDays', 'numberIcyDays', 'monthlyRainVolume(mm)', 'numberRainyDays', 'dailySunnyHoursAvg', 'monthlyWindSpeedAvg(km/h)', 'price_dayahead', 'consumption_dayahead', 'holidayBefore', 'holidayAfter', 'participants', 'price_premium']
df_scaled['cat_price_premium'] = dataframe['cat_price_premium']
df_scaled['isHoliday'] = dataframe['isHoliday']
df_scaled['january'] = dataframe['january']
df_scaled['february'] = dataframe['february']
df_scaled['march'] = dataframe['march']
df_scaled['april'] = dataframe['april']
df_scaled['may'] = dataframe['may']
df_scaled['june'] = dataframe['june']
df_scaled['july'] = dataframe['july']
df_scaled['august'] = dataframe['august']
df_scaled['september'] = dataframe['september']
df_scaled['october'] = dataframe['october']
df_scaled['november'] = dataframe['november']
df_scaled['december'] = dataframe['december']
df_scaled['monday'] = dataframe['monday']
df_scaled['tuesday'] = dataframe['tuesday']
df_scaled['wednesday'] = dataframe['wednesday']
df_scaled['thursday'] = dataframe['thursday']
df_scaled['friday'] = dataframe['friday']
df_scaled['saturday'] = dataframe['saturday']
df_scaled['sunday'] = dataframe['sunday']
df_scaled['hour0'] = dataframe['hour0']
df_scaled['hour1'] = dataframe['hour1']
df_scaled['hour2'] = dataframe['hour2']
df_scaled['hour3'] = dataframe['hour3']
df_scaled['hour4'] = dataframe['hour4']
df_scaled['hour5'] = dataframe['hour5']
df_scaled['hour6'] = dataframe['hour6']
df_scaled['hour7'] = dataframe['hour7']
df_scaled['hour8'] = dataframe['hour8']
df_scaled['hour9'] = dataframe['hour9']
df_scaled['hour10'] = dataframe['hour10']
df_scaled['hour11'] = dataframe['hour11']
df_scaled['hour12'] = dataframe['hour12']
df_scaled['hour13'] = dataframe['hour13']
df_scaled['hour14'] = dataframe['hour14']
df_scaled['hour15'] = dataframe['hour15']
df_scaled['hour16'] = dataframe['hour16']
df_scaled['hour17'] = dataframe['hour17']
df_scaled['hour18'] = dataframe['hour18']
df_scaled['hour19'] = dataframe['hour19']
df_scaled['hour20'] = dataframe['hour20']
df_scaled['hour21'] = dataframe['hour21']
df_scaled['hour22'] = dataframe['hour22']
df_scaled['hour23'] = dataframe['hour23']
# Rearrange column order
df_scaled = df_scaled[['price', 'consumption', 'dailyTempAvg(Celsius)', 'numberFreezingDays', 'numberIcyDays', 'monthlyRainVolume(mm)', 'numberRainyDays', 'dailySunnyHoursAvg', 'monthlyWindSpeedAvg(km/h)', 'price_dayahead', 'consumption_dayahead', 'holidayBefore', 'holidayAfter', 'isHoliday', 'participants', 'price_premium', 'cat_price_premium', 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'hour0', 'hour1', 'hour2', 'hour3', 'hour4', 'hour5', 'hour6', 'hour7', 'hour8', 'hour9', 'hour10', 'hour11', 'hour12', 'hour13', 'hour14', 'hour15', 'hour16', 'hour17', 'hour18', 'hour19', 'hour20', 'hour21', 'hour22', 'hour23']]

df_scaled.to_csv('../00 Data/Final/binaryScaledFinal.csv', index=False, sep=',')
