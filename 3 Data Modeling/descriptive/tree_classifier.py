import pandas as pd
import arima_utils as utils
import matplotlib.pyplot as plt

path = '../../00 Data/Final/cleanFinal.csv'
OUTPUT_PATH = 'decisionTree.png'
df = pd.read_csv(path,sep=',')
df['datetime']= pd.to_datetime(df['datetime'])
df.set_index('datetime', inplace=True)


def decisionTree(X,y,features,outputPath):
    from sklearn.tree import DecisionTreeClassifier
    from scipy import misc
    from sklearn.externals.six import StringIO
    from sklearn.tree import export_graphviz
    import pydotplus
    from sklearn.model_selection import GridSearchCV
    from sklearn.model_selection import TimeSeriesSplit

    parameters = {'min_samples_leaf': range(500, 1500,500),'max_depth':range(5,20,1)}
    my_cv = TimeSeriesSplit(n_splits=2).split(X,y)
    clf = GridSearchCV(estimator=DecisionTreeClassifier(),cv=my_cv, param_grid=parameters, n_jobs=4)
    clf.fit(X=X, y=y)
    fitted_tree = clf.best_estimator_
    print(clf.cv_results_)
    dot_data = StringIO()

    export_graphviz(fitted_tree, out_file=dot_data,
                    filled=True, rounded=True,
                    special_characters=True, feature_names=features)

    graph = pydotplus.graph_from_dot_data(dot_data.getvalue()).write_png(outputPath)
    img = misc.imread(outputPath)
    plt.imshow(img)
    plt.show()
    return fitted_tree


def main():
    features = ['dailyTempAvg(Celsius)', 'numberIcyDays', 'numberFreezingDays', 'monthlyRainVolume(mm)', 'numberRainyDays',
         'dailySunnyHoursAvg', 'monthlyWindSpeedAvg(km/h)', 'holidayBefore', 'holidayAfter', 'isHoliday',
         'participants']
    X = df[features]


    df['price_premium'][df['price_premium']>=0] = 1
    df['price_premium'][df['price_premium']<0] = 0
    y = df['price_premium']
    fitted_tree = decisionTree(X,y,features,OUTPUT_PATH)

if __name__ == '__main__':
    main()