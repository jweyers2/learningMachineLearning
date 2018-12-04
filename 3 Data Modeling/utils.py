import pandas as pd

def train_test_split_predictive(useDevDataset, path):
    dataframe = pd.read_csv(path, dayfirst=True)
    dataframe['datetime'] = pd.to_datetime(dataframe['datetime'])
    dataframe['datetime'] = dataframe['datetime'].apply(lambda x: x.strftime('%Y%m%d%H%M'))
    dataframe['datetime'] = dataframe['datetime'].values.astype(int)
    X = dataframe.drop(
        ['price_premium', 'cat_price_premium', 'price_dayahead', 'consumption_dayahead', 'price', 'consumption'],
        axis=1)
    y = dataframe['cat_price_premium']
    # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    rowCount = len(dataframe.index)
    trainRatio = 0.7
    rowSplit = int(trainRatio * rowCount)
    X_train = X.iloc[0:rowSplit]
    X_test = X.iloc[rowSplit:rowCount]
    y_train = y.iloc[0:rowSplit]
    y_test = y.iloc[rowSplit:rowCount]
    return X_train, X_test, y_train, y_test
