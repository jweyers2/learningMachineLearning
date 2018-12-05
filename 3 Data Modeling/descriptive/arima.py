import pandas as pd
import arima_utils as utils
path = '../../00 Data/Final/cleanFinal.csv'

df = pd.read_csv(path,sep=',')
df['datetime']= pd.to_datetime(df['datetime'])
df.set_index('datetime', inplace=True)



def ARIMA(df):
    utils.stationaryTest(df)

def main():
    ARIMA(df)

if __name__ == '__main__':
    main()