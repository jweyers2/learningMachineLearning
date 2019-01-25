import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


path='../../00 Data/Final/binaryFinal.csv'

dataframe=pd.read_csv(path)

print("Länge:", len(dataframe))

print(type(dataframe.datetime))

dataframe['datetime'] = pd.to_datetime(dataframe['datetime'])

hour=[]
day=[]
month=[]
weekday=[]
for values in dataframe.datetime:
    #print(values.hour)
    hour.append(values.hour)
    day.append(values.day)
    month.append(values.month)
    weekday.append(values.weekday())


dataframe['hour']= hour
dataframe['day']= day
dataframe['month']= month
dataframe['weekday']= weekday

price_premium=dataframe.groupby("hour")["price_premium"].mean()
price_dayahead=dataframe.groupby("hour")["price_dayahead"].mean()
price_daily=dataframe.groupby("hour")["price"].mean()

pp_y= price_premium.values.tolist()
pp_x= price_premium.index.tolist()
pd_x=price_dayahead.index.tolist()
pd_y=price_dayahead.values.tolist()
pdaily_x=price_daily.index.tolist()
pdaily_y=price_daily.values.tolist()
plt.locator_params(axis='x', nbins=24)
plt.plot(pp_x,pp_y, label="price premium")
plt.plot(pdaily_x,pdaily_y, label="daily price")
plt.plot(pd_x,pd_y, label="price dayahead")
plt.title("Mean of prices by hour")
plt.legend()
plt.show()


price_premium_std=dataframe.groupby("hour")["price_premium"].std()
price_dayahead_std=dataframe.groupby("hour")["price_dayahead"].std()
price_daily_std=dataframe.groupby("hour")["price"].std()

pp_y_std= price_premium_std.values.tolist()
pp_x_std= price_premium_std.index.tolist()
pd_x_std=price_dayahead_std.index.tolist()
pd_y_std=price_dayahead_std.values.tolist()
pdaily_x_std=price_daily_std.index.tolist()
pdaily_y_std=price_daily_std.values.tolist()
plt.locator_params(axis='x', nbins=24)
plt.plot(pp_x_std,pp_y_std, label="price premium")
plt.plot(pdaily_x_std,pdaily_y_std, label="daily price")
plt.plot(pd_x_std,pd_y_std, label="price dayahead")
plt.title("Standard deviation of prices by hour")
plt.legend()
plt.show()

cat_by_hour= dataframe.groupby("hour")['cat_price_premium'].value_counts()

for values in cat_by_hour:
    print(values)

print(cat_by_hour)

y_cat_hour_1=cat_by_hour.iloc[::2].values.tolist()
x_cat_hour_1= list(range(24))


y_cat_hour_0=cat_by_hour.iloc[1::2].values.tolist()
x_cat_hour_0= list(range(24))


plt.plot(x_cat_hour_1,y_cat_hour_1, label="Positive Price Premiums")
plt.plot(x_cat_hour_0,y_cat_hour_0, label="Negative Price Premiums")
plt.locator_params(axis='x', nbins=24)
plt.legend()
plt.show()


price_premium_day=dataframe.groupby("day")["price_premium"].mean()
price_dayahead_day=dataframe.groupby("day")["price_dayahead"].mean()
price_daily_day=dataframe.groupby("day")["price"].mean()

pp_y_day= price_premium_day.values.tolist()
pp_x_day= price_premium_day.index.tolist()
pd_x_day=price_dayahead_day.index.tolist()
pd_y_day=price_dayahead_day.values.tolist()
pdaily_x_day=price_daily_day.index.tolist()
pdaily_y_day=price_daily_day.values.tolist()
plt.locator_params(axis='x', nbins=31)
plt.plot(pp_x_day,pp_y_day, label="price premium")
plt.plot(pdaily_x_day,pdaily_y_day, label="daily price")
plt.plot(pd_x_day,pd_y_day, label="price dayahead")
plt.title("Amount of positive and negative price premiums by hour")
plt.legend()
plt.title("Mean of prices by day")
plt.show()

price_premium_month=dataframe.groupby("month")["price_premium"].mean()
price_dayahead_month=dataframe.groupby("month")["price_dayahead"].mean()
price_daily_month=dataframe.groupby("month")["price"].mean()

pp_y_month= price_premium_month.values.tolist()
pp_x_month= price_premium_month.index.tolist()
pd_x_month=price_dayahead_month.index.tolist()
pd_y_month=price_dayahead_month.values.tolist()
pdaily_x_month=price_daily_month.index.tolist()
pdaily_y_month=price_daily_month.values.tolist()
plt.locator_params(axis='x', nbins=12)
plt.plot(pp_x_month,pp_y_month, label="price premium")
plt.plot(pdaily_x_month,pdaily_y_month, label="daily price")
plt.plot(pd_x_month,pd_y_month, label="price dayahead")
plt.legend()
plt.title("Mean of prices by month")
plt.show()


cat_by_day= dataframe.groupby("day")['cat_price_premium'].value_counts()

for values in cat_by_day:
    print(values)

print(cat_by_day)

y_cat_day_1=cat_by_day.iloc[::2].values.tolist()
x_cat_day_1= list(range(1,32))


y_cat_day_0=cat_by_day.iloc[1::2].values.tolist()
x_cat_day_0= list(range(1,32))

print(x_cat_day_0)


plt.plot(x_cat_day_1,y_cat_day_1, label="Positive Price Premiums")
plt.plot(x_cat_day_0,y_cat_day_0, label="Negative Price Premiums")
plt.locator_params(axis='x', nbins=31)
plt.legend()
plt.title("Amount of positive and negative price premiums by day")
plt.show()

cat_by_month= dataframe.groupby("month")['cat_price_premium'].value_counts()

for values in cat_by_month:
    print(values)

print(cat_by_month)

y_cat_month_1=cat_by_month.iloc[::2].values.tolist()
x_cat_month_1= list(range(1,13))


y_cat_month_0=cat_by_month.iloc[1::2].values.tolist()
x_cat_month_0= list(range(1,13))

print(x_cat_month_0)


plt.plot(x_cat_month_1,y_cat_month_1, label="Positive Price Premiums")
plt.plot(x_cat_month_0,y_cat_month_0, label="Negative Price Premiums")
plt.locator_params(axis='x', nbins=12)
plt.legend()
plt.title("Amount of positive and negative price premiums by month")
plt.show()


price_premium_weekday=dataframe.groupby("weekday")["price_premium"].mean()
price_dayahead_weekday=dataframe.groupby("weekday")["price_dayahead"].mean()
price_daily_weekday=dataframe.groupby("weekday")["price"].mean()
price_premium_weekday.index=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
price_dayahead_weekday.index=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
price_daily_weekday.index=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

print(type(price_daily_weekday))
print(price_dayahead_weekday)
print(price_premium_weekday)

pp_y_weekday= price_premium_weekday.values.tolist()
pp_x_weekday= price_premium_weekday.index.tolist()
pd_x_weekday=price_dayahead_weekday.index.tolist()
pd_y_weekday=price_dayahead_weekday.values.tolist()
pdaily_x_weekday=price_daily_weekday.index.tolist()
pdaily_y_weekday=price_daily_weekday.values.tolist()
plt.locator_params(axis='x', nbins=7)
plt.plot(pp_x_weekday,pp_y_weekday, label="price premium")
plt.plot(pdaily_x_weekday,pdaily_y_weekday, label="daily price")
plt.plot(pd_x_weekday,pd_y_weekday, label="price dayahead")
plt.xticks(rotation='vertical')
plt.title("Mean of prices by Weekday")
plt.legend()
plt.show()


cat_by_weekday= dataframe.groupby("weekday")['cat_price_premium'].value_counts()

for values in cat_by_weekday:
    print(values)

print(cat_by_weekday)

y_cat_weekday_1=cat_by_weekday.iloc[::2].values.tolist()
x_cat_weekday_1= ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]


y_cat_weekday_0=cat_by_weekday.iloc[1::2].values.tolist()
x_cat_weekday_0= ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

print(x_cat_weekday_0)


plt.plot(x_cat_weekday_1,y_cat_weekday_1, label="Positive Price Premiums")
plt.plot(x_cat_weekday_0,y_cat_weekday_0, label="Negative Price Premiums")
plt.locator_params(axis='x', nbins=7)
plt.legend()
plt.title("Amount of positive and negative price premiums by month")
plt.show()
