# Source (Beispielhafter Link): https://www.weatheronline.de/weather/maps/city?FMM=1&FYY=2016&LMM=12&LYY=2016&WMO=10481&CONT=dldl&REGION=0001&LAND=DL&ART=TMX&R=0&NOREGION=1&LEVEL=162&LANG=de&MOD=tab

from bs4 import BeautifulSoup as bs
from robobrowser import RoboBrowser
import pandas as pd

# Define the link
url = 'https://www.weatheronline.de/Deutschland/Berlin.htm'
# Define the dates for scraping data from
startdate = pd.datetime(2016, 1, 1, 0)
datelist = pd.date_range(startdate, periods=24, freq='M').tolist()
# Define the path where to save the scraped Data
outputPath = './00 Data/aggregatedWeatherData.csv'
outputPathMonthly = './00 Data/weatherDataMonthly/'
# Spalten mit Umlauten werden benötigt um beim Scrapen die HTML Elemente zu finden
weatherCategories = ['Temperatur', 'Tageshöchsttemperatur', 'Nächtl. Tiefsttemperatur', 'Frosttage', 'Eistage',
                     'Niederschlagsmenge', 'Niederschlagstage', 'Sonnenstunden pro Tag', 'Windstärke', 'Schneetage',
                     'Schneehöhen']
# Für DataFrames und CSV Dateien werden Spalten ohne Umlaute benötigt
weatherCategoriesDataFrameColumns = ['Stadt', 'Temperatur', 'dataAvailability1', 'Tageshoechsttemperatur',
                                     'dataAvailability2', 'Naechtl. Tiefsttemperatur', 'dataAvailability3', 'Frosttage',
                                     'dataAvailability4','Eistage', 'dataAvailability5', 'Niederschlagsmenge',
                                     'dataAvailability6', 'Niederschlagstage', 'dataAvailability7',
                                     'Sonnenstunden pro Tag', 'dataAvailability8', 'Windstaerke', 'dataAvailability9',
                                     'Schneetage', 'dataAvailability10', 'Schneehoehen', 'dataAvailability11']

def cleanTownName(name):
    name = child.find('a').contents[0].replace(u'\xa0', u'')
    name = name.replace('ä', 'ae')
    name = name.replace('ö', 'oe')
    name = name.replace('ü', 'ue')
    return name

def calcYearList(dateList):
    yearlist = []
    for date in datelist:
        if date.strftime('%Y') not in yearlist:
            yearlist.append(date.strftime('%Y'))
    return yearlist


def getCurrentYearSubset(datelist, year):
    subset = []
    for date in datelist:
        if date.strftime('%Y')==year:
            subset.append(date)
    return subset

def getAvgMonthlyValues(monthDataFrame, timestamp):
    temp = ((monthDataFrame['Temperatur']*monthDataFrame['dataAvailability1']).sum)/((monthDataFrame['Temperatur']*monthDataFrame['dataAvailability1']).count)
    tempMax = ((monthDataFrame['Tageshoechsttemperatur']*monthDataFrame['dataAvailability2']).sum)/((monthDataFrame['Tageshoechsttemperatur']*monthDataFrame['dataAvailability2']).count)
    tempMin = ((monthDataFrame['Naechtl. Tiefsttemperatur']*monthDataFrame['dataAvailability3']).sum)/((monthDataFrame['Naechtl. Tiefsttemperatur']*monthDataFrame['dataAvailability3']).count)
    fDays = ((monthDataFrame['Frosttage']*monthDataFrame['dataAvailability4']).sum)/((monthDataFrame['Frosttage']*monthDataFrame['dataAvailability4']).count)
    iDays = ((monthDataFrame['Eistage']*monthDataFrame['dataAvailability5']).sum)/((monthDataFrame['Eistage']*monthDataFrame['dataAvailability5']).count)
    rainVolume = ((monthDataFrame['Niederschlagsmenge']*monthDataFrame['dataAvailability6']).sum)/((monthDataFrame['Niederschlagsmenge']*monthDataFrame['dataAvailability6']).count)
    rDays = ((monthDataFrame['Niederschlagstage']*monthDataFrame['dataAvailability7']).sum)/((monthDataFrame['Niederschlagstage']*monthDataFrame['dataAvailability7']).count)
    sHours = ((monthDataFrame['Sonnenstunden pro Tag']*monthDataFrame['dataAvailability8']).sum)/((monthDataFrame['Sonnenstunden pro Tag']*monthDataFrame['dataAvailability8']).count)
    wSpeed = ((monthDataFrame['Windstaerke']*monthDataFrame['dataAvailability9']).sum)/((monthDataFrame['Windstaerke']*monthDataFrame['dataAvailability9']).count)
    sDays = ((monthDataFrame['Schneetage']*monthDataFrame['dataAvailability10']).sum)/((monthDataFrame['Schneetage']*monthDataFrame['dataAvailability10']).count)
    sVolume = ((monthDataFrame['Schneehoehen']*monthDataFrame['dataAvailability11']).sum)/((monthDataFrame['Schneehoehen']*monthDataFrame['dataAvailability11']).count)
    aggregatedData = [timestamp, temp, tempMax, tempMin, fDays, iDays, rainVolume, rDays, sHours, wSpeed, sDays, sVolume]
    return aggregatedData


# Schritt 2: Importiere die Wetterdaten
# Herangehensweise: Iteriere über (1) Monate, (2) Wetterkategorien, (3) Städte. Für jeden Monat befülle ein
# DataFrame (mit den Wetterkategorien als Spalten und Städten als Zeilen). Berechne für alle Wetterkategorien in diesem
# Monat den deutschlandweiten Durchschnitt und fülle diese Werte in das Ergebnis DataFrame
monthInputs = {'01': '1', '02': '2', '03': '3', '04': '4', '5': '5', '06': '6',
               '07': '7', '08': '8', '09': '9', '10': '10', '11': '11', '12': '12'}
yearlist = calcYearList(datelist)
browser = RoboBrowser(history=True)
browser.open(url)
townList = browser.find(class_="scroll_c1_r").findChildren("ul", recursive=False)
result = pd.DataFrame(columns=['datetime', 'dailyTempAvg(Celsius)', 'dailyTempMax(Celsius)', 'dailyTempMin(Celsius)',
                               'numberFreezingDays', 'numberIcyDays', 'monthlyRainVolume(mm)', 'numberRainyDays',
                               'dailySunnyHoursAvg', 'monthlyWindSpeedAvg(km/h)', 'monthlySnowyDays',
                               'dailySnowVolumeAvg(cm)'])
for year in yearlist:
    monthDataJan = pd.DataFrame(columns=weatherCategoriesDataFrameColumns)
    monthDataFeb = pd.DataFrame(columns=weatherCategoriesDataFrameColumns)
    monthDataMar = pd.DataFrame(columns=weatherCategoriesDataFrameColumns)
    monthDataApr = pd.DataFrame(columns=weatherCategoriesDataFrameColumns)
    monthDataMay = pd.DataFrame(columns=weatherCategoriesDataFrameColumns)
    monthDataJun = pd.DataFrame(columns=weatherCategoriesDataFrameColumns)
    monthDataJul = pd.DataFrame(columns=weatherCategoriesDataFrameColumns)
    monthDataAug = pd.DataFrame(columns=weatherCategoriesDataFrameColumns)
    monthDataSep = pd.DataFrame(columns=weatherCategoriesDataFrameColumns)
    monthDataOct = pd.DataFrame(columns=weatherCategoriesDataFrameColumns)
    monthDataNov = pd.DataFrame(columns=weatherCategoriesDataFrameColumns)
    monthDataDec = pd.DataFrame(columns=weatherCategoriesDataFrameColumns)
    currentYearsMonths = getCurrentYearSubset(datelist, year)
    for ul in townList:
        for child in ul.findAll('li', recursive=False):
            newTownJan = [cleanTownName(child.text), None, None, None, None, None, None, None, None, None, None, None,
                          None, None, None, None, None, None, None, None, None, None, None]
            newTownFeb = [cleanTownName(child.text), None, None, None, None, None, None, None, None, None, None, None,
                          None, None, None, None, None, None, None, None, None, None, None]
            newTownMar = [cleanTownName(child.text), None, None, None, None, None, None, None, None, None, None, None,
                          None, None, None, None, None, None, None, None, None, None, None]
            newTownApr = [cleanTownName(child.text), None, None, None, None, None, None, None, None, None, None, None,
                          None, None, None, None, None, None, None, None, None, None, None]
            newTownMay = [cleanTownName(child.text), None, None, None, None, None, None, None, None, None, None, None,
                          None, None, None, None, None, None, None, None, None, None, None]
            newTownJun = [cleanTownName(child.text), None, None, None, None, None, None, None, None, None, None, None,
                          None, None, None, None, None, None, None, None, None, None, None]
            newTownJul = [cleanTownName(child.text), None, None, None, None, None, None, None, None, None, None, None,
                          None, None, None, None, None, None, None, None, None, None, None]
            newTownAug = [cleanTownName(child.text), None, None, None, None, None, None, None, None, None, None, None,
                          None, None, None, None, None, None, None, None, None, None, None]
            newTownSep = [cleanTownName(child.text), None, None, None, None, None, None, None, None, None, None, None,
                          None, None, None, None, None, None, None, None, None, None, None]
            newTownOct = [cleanTownName(child.text), None, None, None, None, None, None, None, None, None, None, None,
                          None, None, None, None, None, None, None, None, None, None, None]
            newTownNov = [cleanTownName(child.text), None, None, None, None, None, None, None, None, None, None, None,
                          None, None, None, None, None, None, None, None, None, None, None]
            newTownDec = [cleanTownName(child.text), None, None, None, None, None, None, None, None, None, None, None,
                          None, None, None, None, None, None, None, None, None, None, None]
            linkTown = child.find('a', recursive=False).attrs['href']
            # testprint
            print(cleanTownName(child.text))
            browser.open(linkTown)
            linkKlima = browser.find('a', class_=lambda x: x != 'men1Link' and x != 'inactive', href=True, text='Klima')
            if linkKlima is not None:
                browser.open(linkKlima.attrs['href'])
                linkKlimaRechner = browser.find('a', href=True, text='Klimarechner', class_=lambda x: x != 'inactive')
                if linkKlimaRechner is not None:
                    browser.open(linkKlimaRechner.attrs['href'])
                    form = browser.get_form(action='/weather/maps/city')
                    form.fields['FMM'].value = '1'
                    form.fields['LMM'].value = '12'
                    form.fields['FYY'].value = year
                    form.fields['LYY'].value = year
                    browser.submit_form(form)
                    catIndex = 1
                    for cat in weatherCategories:
                        catLink = browser.find('a', href=True, text=cat, class_=lambda x: x != 'inactive')
                        if catLink is not None:
                            browser.open('https://www.weatheronline.de' + catLink.attrs['href'])
                            tables = browser.find_all('table', class_='gr1')
                            if len(tables) > 0:
                                for i in range(1, len(currentYearsMonths)):
                                    table = None
                                    j = i
                                    value = 0
                                    dataAvailability = 0
                                    if i < 7:
                                        table = tables[0]
                                        value = table.findChild('tr').contents[15].contents[(j * 2) - 1].contents[0].text
                                        dataAvailability = table.findChild('tr').contents[17].contents[(j * 2) - 1].text
                                    else:
                                        table = tables[1]
                                        j -= 6
                                        value = table.contents[0].contents[3].contents[(j * 2) - 1].contents[0].text
                                        dataAvailability = table.contents[0].contents[5].contents[(j * 2) - 1].text
                                    if dataAvailability is not 0:
                                        if i == 1:
                                            newTownJan[(2 * catIndex) - 1] = value
                                            newTownJan[(2 * catIndex)] = dataAvailability
                                        elif i == 2:
                                            newTownFeb[(2 * catIndex) - 1] = value
                                            newTownFeb[(2 * catIndex)] = dataAvailability
                                        elif i == 3:
                                            newTownMar[(2 * catIndex) - 1] = value
                                            newTownMar[(2 * catIndex)] = dataAvailability
                                        elif i == 4:
                                            newTownApr[(2 * catIndex) - 1] = value
                                            newTownApr[(2 * catIndex)] = dataAvailability
                                        elif i == 5:
                                            newTownMay[(2 * catIndex) - 1] = value
                                            newTownMay[(2 * catIndex)] = dataAvailability
                                        elif i == 6:
                                            newTownJun[(2 * catIndex) - 1] = value
                                            newTownJun[(2 * catIndex)] = dataAvailability
                                        elif i == 7:
                                            newTownJul[(2 * catIndex) - 1] = value
                                            newTownJul[(2 * catIndex)] = dataAvailability
                                        elif i == 8:
                                            newTownAug[(2 * catIndex) - 1] = value
                                            newTownAug[(2 * catIndex)] = dataAvailability
                                        elif i == 9:
                                            newTownSep[(2 * catIndex) - 1] = value
                                            newTownSep[(2 * catIndex)] = dataAvailability
                                        elif i == 10:
                                            newTownOct[(2 * catIndex) - 1] = value
                                            newTownOct[(2 * catIndex)] = dataAvailability
                                        elif i == 11:
                                            newTownNov[(2 * catIndex) - 1] = value
                                            newTownNov[(2 * catIndex)] = dataAvailability
                                        elif i == 12:
                                            newTownDec[(2 * catIndex) - 1] = value
                                            newTownDec[(2 * catIndex)] = dataAvailability
                        catIndex += 1
            monthDataJan.loc[len(monthDataJan)] = newTownJan
            monthDataFeb.loc[len(monthDataFeb)] = newTownFeb
            monthDataMar.loc[len(monthDataMar)] = newTownMar
            monthDataApr.loc[len(monthDataApr)] = newTownApr
            monthDataMay.loc[len(monthDataMay)] = newTownMay
            monthDataJun.loc[len(monthDataJun)] = newTownJun
            monthDataJul.loc[len(monthDataJul)] = newTownJul
            monthDataAug.loc[len(monthDataAug)] = newTownAug
            monthDataSep.loc[len(monthDataSep)] = newTownSep
            monthDataOct.loc[len(monthDataOct)] = newTownOct
            monthDataNov.loc[len(monthDataNov)] = newTownNov
            monthDataDec.loc[len(monthDataDec)] = newTownDec
    monthDataArray = [monthDataJan, monthDataFeb, monthDataMar, monthDataApr, monthDataMay, monthDataJun, monthDataJul,
                      monthDataAug, monthDataSep, monthDataOct, monthDataNov, monthDataDec]
    for m in range(1, 12):
        monthDataArray[m-1].to_csv(outputPathMonthly+year+' '+str(m), index=False, sep=',')
    for i in range(0, len(currentYearsMonths)-1):
        aggregatedData = getAvgMonthlyValues(monthDataArray[i], currentYearsMonths[i])
        result.loc[len(result)] = aggregatedData
result.to_csv(outputPath, index=False, sep=',')
