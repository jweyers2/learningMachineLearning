from robobrowser import RoboBrowser
from bs4 import BeautifulSoup as bs
import pandas as pd
import numpy as np

#Define the link
url='https://www.epexspot.com/de/marktdaten'
# Define the dates for scraping data from
startdate = pd.datetime(2016,1,1,0)
datelist = pd.date_range(startdate, periods=731,freq='D').tolist()
# Define the path where to save the scraped Data
outputPath ='./00 Data/hourlyDayAheadData.csv'

#  SAVE LIST To CSV METHOD:
def saveToCSV(startdate,hours,hourlyPrices,hourlyConsumption,path):
    df  =pd.DataFrame(columns=['datetime','price','consumption'])
    df['datetime'] = hours
    df['price'] = hourlyPrices
    df['consumption'] = hourlyConsumption
    df.to_csv(path,index=False,sep=',')

#Open URL and create RoboBrowser Instance
browser = RoboBrowser(history=True)
browser.open(url)    

form = browser.get_forms('date_selector')

hours = []
hourlyPrices = []
hourlyConsumption = []
# df  =pd.DataFrame(columns=['datetime','price','consumption'])
for date in datelist:
    # print(date.strftime("%d.%m.%Y"))
    form[0]['EPEXSpotMarketData-show_auction[date]'].value=date.strftime('%d.%m.%Y')
    #Submit form
    browser.submit_form(form[0])

    #pass code to beatufulsoup tool
    html = bs(str(browser.parsed), 'html.parser')
  

    hourlyTable = html.find('table',attrs={'class':'list hours responsive'})
    tableBody = hourlyTable.find('tbody')
    rows = tableBody.find_all('tr')
    count = 0
    for row in rows:
        columns = row.find_all('td')
        if columns:
            if count % 2 == 0:
                s = int(columns[0].text.strip()[:2])
                hours.append(pd.datetime(date.year,date.month,date.day,s))
                hourlyPrices.append(columns[8].text)
            else:
                hourlyConsumption.append(columns[8].text)
                
            count += 1
    
    iteration = date - startdate
    iteration = iteration.days
    print("Iteration: " + str(iteration) + " scraped Date: " + str(date))
    if iteration % 30 == 0:
        saveToCSV(startdate,hours,hourlyPrices,hourlyConsumption,outputPath)

saveToCSV(startdate,iteration,hourlyPrices,hourlyConsumption,outputPath)
