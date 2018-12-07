# Check the percentage of rows that have the value 1 in the column "cat_price_premium"
# If there isn't a strong imbalance use ROC score, otherwise F1 score
import pandas as pd

path = '../00 Data/Final/binaryFinal.csv'
dataframe = pd.read_csv(path, dayfirst=True)
totalAmount = len(dataframe.index)
dfPositive = dataframe.loc[dataframe['cat_price_premium'] == 1]
positivePremiumAmount = len(dfPositive.index)
print (positivePremiumAmount/totalAmount)
# Result: about 70% positive premium
