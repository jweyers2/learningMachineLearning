# For development purposes a subset of the data with 1000 rows will be created. The purpose is to accelerate technical tests of code
import pandas as pd

outputPath = '../00 Data/Final/DeveloperDataset.csv'
cleanData = pd.read_csv('../00 Data/Final/cleanFinal.csv')
devData = cleanData.sample(1000)
devData = devData.sort_values(by='datetime')
devData.to_csv(outputPath, index=False, sep=',')
