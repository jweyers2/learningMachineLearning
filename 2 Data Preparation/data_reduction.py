import pandas as pd

path = '../00 Data/Final/final.csv'
dataframe = pd.read_csv(path, dayfirst=True)

# remove daily maximum and minimum temperature columns due to multicollinearity with average temperature and very
# similar values to the average temperature (-> no extra benefit expected)
dataframe = dataframe.drop(['dailyTempMax(Celsius)','dailyTempMin(Celsius)'], axis=1)
# Drop snow columns due to low data availability resulting in very biased averages
dataframe = dataframe.drop(['monthlySnowyDays', 'dailySnowVolumeAvg(cm)'], axis=1)

dataframe.to_csv('../00 Data/Final/cleanFinal.csv', index=False)
outputPath = '../00 Data/Final/developerDataset.csv'
devData = dataframe.sample(1000)
devData = devData.sort_values(by='datetime')
devData.to_csv(outputPath, index=False, sep=',')

