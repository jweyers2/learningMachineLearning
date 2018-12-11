import pandas as pd
import numpy as np

path='../../00 Data/Final/cleanFinal.csv'
dataframe=pd.read_csv(path)

dataframe.set_index('datetime',inplace=True)

new_df= dataframe.drop(['price_premium'], axis= 1)

#Add new price premium...
new_df['price_premium']= new_df['price_dayahead'] - new_df['price']

out_path='../../00 Data/Final/new_pricepremium.csv'
new_df.to_csv(out_path)