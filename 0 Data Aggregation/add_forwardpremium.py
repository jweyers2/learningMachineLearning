import pandas as pd
import statistics
# Should not be used anymore because we calculate the price_premium now in another way... 
path='../00 Data/Final/final.csv'
dataframe=pd.read_csv(path)

dataframe.set_index('datetime',inplace=True)

dataframe.fillna('0.0',inplace=True)


def changeunknownvaluestozero(date,columnnames):
    location= dataframe.index.get_loc(date)
    locationlist=[location, location+1, location+2, location+3]
    columns=columnnames
    for values in columns:
        for i in locationlist:
            dataframe.loc[dataframe.index[i],values]='0'


changeunknownvaluestozero('2016-03-27 02:00:00',['price','consumption','price_dayahead','consumption_dayahead'])
changeunknownvaluestozero('2017-03-26 02:00:00',['price','consumption','price_dayahead','consumption_dayahead'])

#dataframe.index= pd.to_datetime(dataframe.index)



def stringtofloat(columnName):
    floatvalues=[]
    index = dataframe.columns.get_loc(columnName)
    for value in dataframe[columnName]:
        nodots=value.replace('.','')
        floatvalues.append(float(nodots.replace(',','.')))
    dataframe[columnName].iloc[0:]
    del dataframe[columnName]
    dataframe.insert(index, columnName, floatvalues)


stringtofloat('price')
stringtofloat('consumption')
stringtofloat('consumption_dayahead')
stringtofloat('price_dayahead')


def mean(date,columnname):
    location = dataframe.index.get_loc(date)
    for name in columnname:
        mean=[dataframe.loc[dataframe.index[location-1], name],dataframe.loc[dataframe.index[location+4], name]]
        mean= statistics.median(mean)
        for i in range(4):
            dataframe.loc[dataframe.index[location+i], name]= mean

mean('2016-03-27 02:00:00',['price','consumption','consumption_dayahead','price_dayahead'])
mean('2017-03-26 02:00:00',['price','consumption','consumption_dayahead','price_dayahead'])



def addcolumprice_premium(data):
    dayaheaddate= dataframe.index.get_loc('2018-01-01 00:00:00')
    startintradaydate= dataframe.index.get_loc('2016-01-02 00:00:00')
    intradayprice= dataframe['price'][startintradaydate:].reset_index()
    dayaheadprice=dataframe['price_dayahead'][0:dayaheaddate].reset_index()
    price_premium= dayaheadprice['price_dayahead'] - intradayprice['price']
    price_premium= pd.DataFrame(price_premium, columns={'price_premium'})
    data= pd.concat([data.reset_index(), price_premium],axis=1)
    data= data[:dayaheaddate]
    return data


dataframe= addcolumprice_premium(dataframe)

out_path='../00 Data/Final/final.csv'
dataframe.to_csv(out_path,index=False)