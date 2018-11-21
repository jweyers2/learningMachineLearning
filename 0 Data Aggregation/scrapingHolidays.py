import pandas as pd
from bs4 import BeautifulSoup
import requests
from dateutil.parser import parse
from datetime import date, timedelta

#global variables
outputPath ='../00 Data/holidays.csv'
start = 2015
end = 2018
holidays = []
d1 = date(2016, 1, 1)
d2 = date(2017, 12, 31)
before = []
after= []
flag = []

#check if string is date
def is_date(string):
    try:
        parse(string)
        return True
    except ValueError:
        return False

#  save data to csv
def saveToCSV(dates, before, after, flag, path):
    df = pd.DataFrame(columns=['date','holidayBefore','holidayAfter', 'isHoliday'])
    df['date'] = dates
    df['holidayBefore'] = before
    df['holidayAfter'] = after
    df['isHoliday'] = flag
    df.to_csv(path,index=False,sep=',')

def givedates(start, end):
  datelist = []
  delta = end - start
  for i in range(delta.days + 1):
    datelist.append(start + timedelta(i))
  return datelist



year = start
while year <= end:
    url = 'https://feiertage-api.de/api/?jahr=' + `year` + '&nur_land=NATIONAL'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, features="html.parser")
    list = soup.text.split('"')
    for i in list:
        if is_date(i):
            i = parse(i)
            i = i.date()
            holidays.append(i)
    year = year + 1


dates = givedates(d1, d2)
for date in dates:
    same = 0
    for day in holidays:
        if day == date:
            same = 1
        if day < date:
            savebefore = (date - day).days
        if day > date:
            before.append(savebefore)
            saveafter = (day - date).days
            after.append(saveafter)
            break
    flag.append(same)
    print (date, before[-1], after[-1], flag[-1])

saveToCSV(dates, before, after, flag, outputPath)