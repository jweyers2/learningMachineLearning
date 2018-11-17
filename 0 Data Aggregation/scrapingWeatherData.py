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
              monthlyRainVolume, numberRainyDays, dailySunnyHoursAvg, monthlyWindSpeedAvg, monthlySnowyDays,
              dailySnowVolumeAvg):
    df  =pd.DataFrame(columns=['datetime', 'dailyTempAvg(Celsius)', 'dailyTempMax(Celsius)', 'dailyTempMin(Celsius)',
                               'numberFreezingDays', 'numberIcyDays', 'monthlyRainVolume(mm)', 'numberRainyDays',
                               'dailySunnyHoursAvg', 'monthlyWindSpeedAvg(km/h)', 'monthlySnowyDays',
                               'dailySnowVolumeAvg(cm)'])
    df['datetime'] = months
    df['dailyTempAvg(Celsius)'] = dailyTempAvg
    df['dailyTempMax(Celsius)'] = dailyTempMax
    df['dailyTempMin(Celsius)'] = dailyTempMin
    df['numberFreezingDays'] = numberFreezingDays
    df['numberIcyDays'] = numberIcyDays
    df['monthlyRainVolume(mm)'] = monthlyRainVolume
    df['numberRainyDays'] = numberRainyDays
    df['dailySunnyHoursAvg'] = dailySunnyHoursAvg
    df['monthlyWindSpeedAvg(km/h)'] = monthlyWindSpeedAvg
    df['monthlySnowyDays'] = monthlySnowyDays
    df['dailySnowVolumeAvg(cm)'] = dailySnowVolumeAvg
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
dailySnowVolumeAvg = []

towns = []
# Spalten mit Umlauten werden benötigt um beim Scrapen die HTML Elemente zu finden
weatherCategories = ['Temperatur', 'Tageshöchsttemperatur', 'Nächtl. Tiefsttemperatur', 'Frosttage', 'Eistage',
                     'Niederschlagsmenge', 'Niederschlagstage', 'Sonnenstunden pro Tag', 'Windstärke', 'Schneetage',
                     'Schneehöhen']
# Für DataFrames und CSV Dateien werden Spalten ohne Umlaute benötigt
weatherCategoriesFormatted = ['Stadt', 'Temperatur', 'dataAvailability1', 'Tageshoechsttemperatur', 'dataAvailability2',
                              'Naechtl. Tiefsttemperatur', 'dataAvailability3', 'Frosttage', 'dataAvailability4',
                              'Eistage', 'dataAvailability5', 'Niederschlagsmenge', 'dataAvailability6',
                              'Niederschlagstage', 'dataAvailability7', 'Sonnenstunden pro Tag', 'dataAvailability8',
                              'Windstaerke', 'dataAvailability9', 'Schneetage', 'dataAvailability10', 'Schneehoehen',
                              'dataAvailability11']

# Schritt 1: Befülle das "towns" Array mit allen Städten zu denen man Daten abrufen kann
# Open URL and create RoboBrowser Instance
# browser = RoboBrowser(history=True)
# browser.open(url)
# townList = browser.find(class_="scroll_c1_r").findChildren("ul", recursive=False)
# for ul in townList:
#     for child in ul.findAll('li', recursive=False):
#         name = child.find('a').contents[0].replace(u'\xa0', u'')
#         name = name.replace('ä', 'ae')
#         name = name.replace('ö', 'oe')
#         name = name.replace('ü', 'ue')
#         towns.append(name)
#
#
# print(townList)
# print(towns)

def cleanTownName(name):
    name = child.find('a').contents[0].replace(u'\xa0', u'')
    name = name.replace('ä', 'ae')
    name = name.replace('ö', 'oe')
    name = name.replace('ü', 'ue')
    return name


# Schritt 2: Importiere die Wetterdaten
# Herangehensweise: Iteriere über (1) Monate, (2) Wetterkategorien, (3) Städte. Für jeden Monat befülle ein
# DataFrame (mit den Wetterkategorien als Spalten und Städten als Zeilen). Berechne für alle Wetterkategorien in diesem
# Monat den deutschlandweiten Durchschnitt und fülle diese Werte in das Ergebnis DataFrame
monthInputs = {'01': '1', '02': '2', '03': '3', '04': '4', '5': '5', '06': '6',
               '07': '7', '08': '8', '09': '9', '10': '10', '11': '11', '12': '12'}
browser = RoboBrowser(history=True)
browser.open(url)
townList = browser.find(class_="scroll_c1_r").findChildren("ul", recursive=False)
for date in datelist:
    month = date.strftime('%m')
    year = date.strftime('%Y')
    monthInput = monthInputs.get(month)
    townIndex = 0
    monthData = pd.DataFrame(columns=weatherCategoriesFormatted)
    for ul in townList:
        for child in ul.findAll('li', recursive=False):
            newRow = [cleanTownName(child.text), None, None, None, None, None, None, None, None, None, None, None, None,
                      None, None, None, None, None, None, None, None, None]
            #linkTown = child.find('a', recursive=False).attrs['href']
            linkTown = 'https://www.weatheronline.de/Deutschland/Berlin.htm'
            browser.open(linkTown)
            linkKlima = browser.find('a', class_=lambda x: x != 'men1Link' and x != 'inactive', href=True, text='Klima')
            if linkKlima is not None:
                browser.open(linkKlima.attrs['href'])
                linkKlimaRechner = browser.find('a', href=True, text='Klimarechner')
                if linkKlimaRechner is not None:
                    browser.open(linkKlimaRechner.attrs['href'])
                    form = browser.get_form(action='/weather/maps/city')
                    form.fields['FMM'].value = monthInput
                    form.fields['LMM'].value = monthInput
                    form.fields['FYY'].value = year
                    form.fields['LYY'].value = year
                    browser.submit_form(form)
                    catIndex = 1
                    for cat in weatherCategories:
                        catLink = browser.find('a', href=True, text=cat, class_=lambda x: x != 'inactive')
                        if catLink is not None:
                            browser.open('https://www.weatheronline.de' + catLink.attrs['href'])
                            if cat == 'Temperatur':
                                tables = browser.find_all('table', class_='gr1')
                                if len(tables)>0:
                                    table = None
                                    if int(monthInput) < 7:
                                        table = tables[0]
                                    else:
                                        table = tables[1]
                                    t = table.findChild('tr')
                                    value = table.findChild('tr').contents[15].contents[(int(monthInput)*2)-1].contents[0].text
                                    dataAvailability = table.findChild('tr').contents[17].contents[(int(monthInput)*2)-1].text
                                    newRow[(2 * catIndex) - 1] = value
                                    newRow[(2 * catIndex)] = dataAvailability
                                    catIndex += 1
                            # elif cat == 'Tageshöchsttemperatur':
                            # elif cat == 'Nächtl. Tiefsttemperatur':
                            # elif cat == 'Frosttage':
                            # elif cat == 'Eistage':
                            # elif cat == 'Niederschlagsmenge':
                            # elif cat == 'Niederschlagstage':
                            # elif cat == 'Sonnenstunden pro Tag':
                            # elif cat == 'Windstärke':
                            # elif cat == 'Schneetage':
