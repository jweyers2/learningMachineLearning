from robobrowser import RoboBrowser
from bs4 import BeautifulSoup as bs
import pandas as pd
import numpy as np

#Define the link
url='https://www.epexspot.com/de/marktdaten/intradayauktion'
# Define the dates for scraping data from
datelist = pd.date_range(pd.datetime(2016,1,1), periods=731).tolist()

#Open URL and create RoboBrowser Instance
browser = RoboBrowser(history=True)
browser.open(url)    

form = browser.get_forms('date_selector')

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
    # print(date)
    for row in rows:
        columns = row.find_all('td')
        if columns:
            if count % 2 == 0:
                hourlyPrices.append(columns[8].text)
            else:
                hourlyConsumption.append(columns[8].text)
            count += 1
            # print(columns[8].value)
    
    iteration = date - pd.datetime(2016,1,1)
    iteration = (iteration / np.timedelta64(1, 'D')).astype(int) +1
    print(iteration)
    if iteration % 30 == 0 or iteration == 731:
        df  =pd.DataFrame(columns=['datetime','price','consumption'])
        df['datetime'] = pd.date_range(pd.datetime(2016,1,1,0), periods=(24*iteration),freq='H').tolist()
        df['price'] = hourlyPrices
        df['consumption'] = hourlyConsumption
        print(df)
        df.to_csv('./00 Data/hourlyDayAheadData.csv',index=False,sep=',')

# datelist = pd.date_range(pd.datetime(2016,1,1,0), periods=(731*24),freq='H').tolist()
# df['price'] = hourlyPrices
# df['consumption'] = hourlyConsumption                

# df.to_csv('./Data/hourlyDayAheadData.csv',index=False)