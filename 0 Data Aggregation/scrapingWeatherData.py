from robobrowser import RoboBrowser
import pandas as pd

# Define the link
url = 'https://www.weatheronline.de/Deutschland/Berlin.htm'
# Define the dates for scraping data from
startdate = pd.datetime(2016, 1, 1, 0)
datelist = pd.date_range(startdate, periods=24, freq='M').tolist()
# Define the path where to save the scraped Data
outputPath = '../00 Data/aggregatedWeatherData.csv'
outputPathMonthly = '../00 Data/weatherDataMonthly/'
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
    tInput = pd.to_numeric(monthDataFrame['Temperatur'])
    da1 = pd.to_numeric(monthDataFrame['dataAvailability1'])
    s = (tInput*da1).sum()
    c = da1.sum()
    temp = s/c
    tmaxInput = pd.to_numeric(monthDataFrame['Tageshoechsttemperatur'])
    da2 = pd.to_numeric(monthDataFrame['dataAvailability2'])
    s = (tmaxInput * da2).sum()
    c = da2.sum()
    tempMax = s / c
    tminInput = pd.to_numeric(monthDataFrame['Naechtl. Tiefsttemperatur'])
    da3 = pd.to_numeric(monthDataFrame['dataAvailability3'])
    s = (tminInput * da3).sum()
    c = da3.sum()
    tempMin = s / c
    fInput = pd.to_numeric(monthDataFrame['Frosttage'])
    da4 = pd.to_numeric(monthDataFrame['dataAvailability4'])
    s = (fInput * da4).sum()
    c = da4.sum()
    fDays = s / c
    iInput = pd.to_numeric(monthDataFrame['Eistage'])
    da5 = pd.to_numeric(monthDataFrame['dataAvailability5'])
    s = (iInput * da5).sum()
    c = da5.sum()
    iDays = s / c
    rvInput = pd.to_numeric(monthDataFrame['Niederschlagsmenge'])
    da6 = pd.to_numeric(monthDataFrame['dataAvailability6'])
    s = (rvInput * da6).sum()
    c = da6.sum()
    rainVolume = s / c
    rInput = pd.to_numeric(monthDataFrame['Niederschlagstage'])
    da7 = pd.to_numeric(monthDataFrame['dataAvailability7'])
    s = (rInput * da7).sum()
    c = da7.sum()
    rDays = s / c
    sInput = pd.to_numeric(monthDataFrame['Sonnenstunden pro Tag'])
    da8 = pd.to_numeric(monthDataFrame['dataAvailability8'])
    s = (sInput * da8).sum()
    c = da8.sum()
    sHours = s / c
    wInput = pd.to_numeric(monthDataFrame['Windstaerke'])
    da9 = pd.to_numeric(monthDataFrame['dataAvailability9'])
    s = (wInput * da9).sum()
    c = da9.sum()
    wSpeed = s / c
    snowInput = pd.to_numeric(monthDataFrame['Schneetage'])
    da10 = pd.to_numeric(monthDataFrame['dataAvailability10'])
    s = (snowInput * da10).sum()
    c = da10.sum()
    sDays = s / c
    svInput = pd.to_numeric(monthDataFrame['Schneehoehen'])
    da11 = pd.to_numeric(monthDataFrame['dataAvailability11'])
    s = (svInput * da11).sum()
    c = da11.sum()
    sVolume = s / c

    aggregatedData = [timestamp, temp, tempMax, tempMin, fDays, iDays, rainVolume, rDays, sHours, wSpeed, sDays, sVolume]
    return aggregatedData


monthInputs = {'01': '1', '02': '2', '03': '3', '04': '4', '5': '5', '06': '6',
               '07': '7', '08': '8', '09': '9', '10': '10', '11': '11', '12': '12'}
yearlist = calcYearList(datelist)
browser = RoboBrowser(history=False)
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
    print(year)
    for ul in townList:
        townCount = len(ul.findAll('li', recursive=False))
        print('Number of towns: '+str(townCount))
        for child in ul.findAll('li', recursive=False):
            townCount -= 1
            newTownJan = [cleanTownName(child.text), None, None, None, None, None, None, None, None, None, None,
                          None,
                          None, None, None, None, None, None, None, None, None, None, None]
            newTownFeb = [cleanTownName(child.text), None, None, None, None, None, None, None, None, None, None,
                          None,
                          None, None, None, None, None, None, None, None, None, None, None]
            newTownMar = [cleanTownName(child.text), None, None, None, None, None, None, None, None, None, None,
                          None,
                          None, None, None, None, None, None, None, None, None, None, None]
            newTownApr = [cleanTownName(child.text), None, None, None, None, None, None, None, None, None, None,
                          None,
                          None, None, None, None, None, None, None, None, None, None, None]
            newTownMay = [cleanTownName(child.text), None, None, None, None, None, None, None, None, None, None,
                          None,
                          None, None, None, None, None, None, None, None, None, None, None]
            newTownJun = [cleanTownName(child.text), None, None, None, None, None, None, None, None, None, None,
                          None,
                          None, None, None, None, None, None, None, None, None, None, None]
            newTownJul = [cleanTownName(child.text), None, None, None, None, None, None, None, None, None, None,
                          None,
                          None, None, None, None, None, None, None, None, None, None, None]
            newTownAug = [cleanTownName(child.text), None, None, None, None, None, None, None, None, None, None,
                          None,
                          None, None, None, None, None, None, None, None, None, None, None]
            newTownSep = [cleanTownName(child.text), None, None, None, None, None, None, None, None, None, None,
                          None,
                          None, None, None, None, None, None, None, None, None, None, None]
            newTownOct = [cleanTownName(child.text), None, None, None, None, None, None, None, None, None, None,
                          None,
                          None, None, None, None, None, None, None, None, None, None, None]
            newTownNov = [cleanTownName(child.text), None, None, None, None, None, None, None, None, None, None,
                          None,
                          None, None, None, None, None, None, None, None, None, None, None]
            newTownDec = [cleanTownName(child.text), None, None, None, None, None, None, None, None, None, None,
                          None,
                          None, None, None, None, None, None, None, None, None, None, None]
            linkTown = child.find('a', recursive=False).attrs['href']
            # testprint
            # print(cleanTownName(child.text))
            if townCount % 50 == 0:
                print('Number of remaining towns: ' + str(townCount))
            browser.open(linkTown)
            linkKlima = browser.find('a', class_=lambda x: x != 'men1Link' and x != 'inactive', href=True, text='Klima')
            if linkKlima is not None:
                browser.open(linkKlima.attrs['href'])
                linkKlimaRechner = browser.find('a', href=True, text='Klimarechner',
                                                class_=lambda x: x != 'inactive')
                if linkKlimaRechner is not None:
                    browser.open(linkKlimaRechner.attrs['href'])
                    form = browser.get_form(action='/weather/maps/city')
                    if year in form.fields['FYY'].options and year in form.fields['LYY'].options:
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
                                            value = \
                                                table.findChild('tr').contents[15].contents[(j * 2) - 1].contents[0].text
                                            dataAvailability = table.findChild('tr').contents[17].contents[(j * 2) - 1].text
                                        else:
                                            table = tables[1]
                                            j -= 6
                                            value = table.contents[0].contents[3].contents[(j * 2) - 1].contents[0].text
                                            dataAvailability = table.contents[0].contents[5].contents[(j * 2) - 1].text
                                        if (dataAvailability != '0') and (value != '****'):
                                            dataAvailability = str(int(dataAvailability) / 100)
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
    for m in range(1, 13):
        monthDataArray[m-1].to_csv(outputPathMonthly+year+'-'+str(m)+'.csv', index=False, sep=',')
    for i in range(0, len(currentYearsMonths)-1):
        aggregatedData = getAvgMonthlyValues(monthDataArray[i], currentYearsMonths[i])
        result.loc[len(result)] = aggregatedData
result.to_csv(outputPath, index=False, sep=',')
