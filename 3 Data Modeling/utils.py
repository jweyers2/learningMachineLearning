import pandas as pd
from sklearn.decomposition import PCA

def train_test_split_predictive(path, pcaRatio = None):
    dataframe = pd.read_csv(path, dayfirst=True)
    X = dataframe.drop(['price_premium', 'cat_price_premium', 'price_dayahead', 'consumption_dayahead', 'price', 'consumption'],axis=1)
    if pcaRatio is not None:
        pca = PCA(n_components=float(pcaRatio))
        X = pca.fit_transform(X)
    # X = dataframe.drop(['cat_price_premium','price_dayahead','price'],axis=1)
    # X = dataframe.drop(['price_premium', 'cat_price_premium', 'price_dayahead', 'price'],axis=1)
    # X = dataframe[['price_dayahead','price']]
    y = dataframe['cat_price_premium']
    # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    rowCount = len(dataframe.index)
    trainRatio = 0.7
    rowSplit = int(trainRatio * rowCount)
    # X_train = X.iloc[0:rowSplit]
    # X_test = X.iloc[rowSplit:rowCount]
    # y_train = y.iloc[0:rowSplit]
    # y_test = y.iloc[rowSplit:rowCount]
    X_train = X[0:rowSplit]
    X_test = X[rowSplit:rowCount]
    y_train = y[0:rowSplit]
    y_test = y[rowSplit:rowCount]
    return X_train, X_test, y_train, y_test
