import pandas as pd

paths = ['../00 Data/Final/final.csv', '../00 Data/Final/binaryFinal.csv']
newPaths = ['../00 Data/Final/cleanFinal.csv', '../00 Data/Final/binaryCleanFinal.csv']
developerPaths = ['../00 Data/Final/developerDataset.csv', '../00 Data/Final/binaryDeveloperDataset.csv']

for index, path in enumerate(paths):
    dataframe = pd.read_csv(path, dayfirst=True)

    # remove daily maximum and minimum temperature columns due to multicollinearity with average temperature and very
    # similar values to the average temperature (-> no extra benefit expected)
    dataframe = dataframe.drop(['dailyTempMax(Celsius)','dailyTempMin(Celsius)'], axis=1)
    # Drop snow columns due to low data availability resulting in very biased averages
    dataframe = dataframe.drop(['monthlySnowyDays', 'dailySnowVolumeAvg(cm)'], axis=1)

    devData = dataframe.sample(1000)
    devData = devData.sort_values(by='datetime')
    if path == '../00 Data/Final/binaryFinal.csv':
        dataframe = dataframe.drop(['datetime'], axis=1)
        devData = devData.drop(['datetime'], axis=1)

    dataframe.to_csv(newPaths[index], index=False)
    devData.to_csv(developerPaths[index], index=False, sep=',')


