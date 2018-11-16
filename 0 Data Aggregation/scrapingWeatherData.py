# Source (Beispielhafter Link): https://www.weatheronline.de/weather/maps/city?FMM=1&FYY=2016&LMM=12&LYY=2016&WMO=10481&CONT=dldl&REGION=0001&LAND=DL&ART=TMX&R=0&NOREGION=1&LEVEL=162&LANG=de&MOD=tab

from bs4 import BeautifulSoup as bs
from robobrowser import RoboBrowser
import pandas as pd

# Define the link
url = 'https://www.weatheronline.de/weather/maps/city?FMM=1&FYY=2016&LMM=12&LYY=2016&WMO=10481&CONT=dldl&REGION=0001&LAND=DL&ART=TMX&R=0&NOREGION=1&LEVEL=162&LANG=de&MOD=tab'
# Define the dates for scraping data from
startdate = pd.datetime(2016, 1, 1, 0)
datelist = pd.date_range(startdate, periods=24, freq='M').tolist()
# Define the path where to save the scraped Data
outputPath = './00 Data/weatherData.csv'

#  SAVE LIST To CSV METHOD:
def saveToCSV(path, months, dailyTempAvg, dailyTempMax, dailyTempMin, numberFreezingDays, numberIcyDays,
              monthlyRainVolume, numberRainyDays, dailySunnyHoursAvg, monthlyWindSpeedAvg, monthlySnowyDays):
    df  =pd.DataFrame(columns=['datetime', 'dailyTempAvg', 'dailyTempMax', 'dailyTempMin', 'numberFreezingDays',
                               'numberIcyDays', 'monthlyRainVolume', 'numberRainyDays', 'dailySunnyHoursAvg',
                               'monthlyWindSpeedAvg', 'monthlySnowyDays'])
    df['datetime'] = months
    df['dailyTempAvg'] = dailyTempAvg
    df['dailyTempMax'] = dailyTempMax
    df['dailyTempMin'] = dailyTempMin
    df['numberFreezingDays'] = numberFreezingDays
    df['numberIcyDays'] = numberIcyDays
    df['monthlyRainVolume'] = monthlyRainVolume
    df['numberRainyDays'] = numberRainyDays
    df['dailySunnyHoursAvg'] = dailySunnyHoursAvg
    df['monthlyWindSpeedAvg'] = monthlyWindSpeedAvg
    df['monthlySnowyDays'] = monthlySnowyDays
    df.to_csv(path, index=False, sep=',')


months = []
dailyTempAvg = []
dailyTempMax = []
dailyTempMin = []
numberFreezingDays = []
numberIcyDays = []
monthlyRainVolume = []
numberRainyDays = []
dailySunnyHoursAvg = []
monthlyWindSpeedAvg = []
monthlySnowyDays = []

towns = []
# Spalten mit Umlauten werden benötigt um beim Scrapen die HTML Elemente zu finden
weatherCategories = ['Temperatur', 'Tageshöchsttemperatur', 'Nächtl. Tiefsttemperatur', 'Frosttage', 'Eistage',
                     'Niederschlagsmenge', 'Niederschlagstage', 'Sonnenstunden pro Tag', 'Windstärke', 'Schneetage',
                     'Schneehöhen']
# Für DataFrames und CSV Dateien werden Spalten ohne Umlaute benötigt
weatherCategoriesFormatted = ['Temperatur', 'Tageshoechsttemperatur', 'Naechtl. Tiefsttemperatur', 'Frosttage',
                              'Eistage', 'Niederschlagsmenge', 'Niederschlagstage', 'Sonnenstunden pro Tag',
                              'Windstaerke', 'Schneetage', 'Schneehoehen']

# Schritt 1: Befülle das "towns" Array mit allen Städten zu denen man Daten abrufen kann
# Open URL and create RoboBrowser Instance
browser = RoboBrowser(history=True)
browser2 = RoboBrowser(history=True)
browser.open(url)
townList = browser.find(class_="scroll_c1_r").findChildren("ul", recursive=False)
for ul in townList:
    for child in ul.findAll('li', recursive=False):
        name = child.find('a').contents[0].replace(u'\xa0', u'')
        name = name.replace('ä', 'ae')
        name = name.replace('ö', 'oe')
        name = name.replace('ü', 'ue')
        towns.append(name)


print(townList)
print(towns)


# Schritt 2: Importiere die Wetterdaten
# Herangehensweise: Iteriere über (1) Monate, (2) Wetterkategorien, (3) Städte. Für jeden Monat befülle ein
# DataFrame (mit den Wetterkategorien als Spalten und Städten als Zeilen). Berechne für alle Wetterkategorien in diesem
# Monat den deutschlandweiten Durchschnitt und fülle diese Werte in das Ergebnis DataFrame
monthInputs = {'01': 'Januar', '02': 'Februar', '03': 'März', '04': 'April', '05': 'Mai', '06': 'Juni',
               '07': 'Juli', '08': 'August', '09': 'September', '10': 'Oktober', '11': 'November', '12': 'Dezember'}
for date in datelist:
    month = date.strftime('%m')
    year = date.strftime('%Y')
    monthInput = monthInputs.get(month)
    townIndex = 0
    monthData = pd.DataFrame(columns=weatherCategories)
    for ul in townList:
        for child in ul.findAll('li', recursive=False):
            linkTown = child.find('a', recursive=False).attrs['href']
            browser.open(linkTown)
            linkKlima = browser.find('a', class_=lambda x: x!='men1Link', href=True, text='Klima')
            if linkKlima != None:
                browser.open(linkKlima.attrs['href'])
                linkKlimaRechner = browser.find('a', href=True, text='Klimarechner')
                if linkKlimaRechner!= None:
                    #todo: im Link den Monat und das Jahr für die Suche setzen
                    browser.open(linkKlimaRechner.attrs['href'])
                    # mInputFields = browser.find_all(class_='history')
                    # for mInputField in mInputFields:
                    #     if (mInputField.attrs['name'] == 'FMM' or mInputField.attrs['name'] == 'LMM'):
                    #         mInputField.value = monthInput
                    #     elif (mInputField.attrs['name'] == 'FYY' or mInputField.attrs['name'] == 'LYY'):
                    #         mInputField.value = year
                    # form = browser.get_form(value='Go')
                    # browser.submit_form(form)
                    catValues = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
                    catIndex = 0
                    for cat in weatherCategories:
                        catLink = browser.find('a', href=True, text=cat)
                        if catLink != None:
                            browser.open(catLink.attrs['href'])