import pandas as pd

outputPath = '../00 Data/Final/cleanFinal.csv'
dirtyData = pd.read_csv('../00 Data/Final/final.csv')

# Drop snow columns due to low data availability resulting in very biased averages
dirtyData = dirtyData.drop(['monthlySnowyDays', 'dailySnowVolumeAvg(cm)'], axis=1)
dirtyData.to_csv(outputPath, index=False, sep=',')
