import pandas as pd
import arima_utils as utils
import matplotlib.pyplot as plt
import numpy as np

path = '../../00 Data/Final/cleanFinal.csv'
OUTPUT_PATH = 'decisionTree.png'
df = pd.read_csv(path,sep=',')
df['datetime']= pd.to_datetime(df['datetime'])
df.set_index('datetime', inplace=True)


def generateTimeDummyVars():
    return None


def decisionTree(X,y,features,outputPath):
    from sklearn.tree import DecisionTreeClassifier
    from scipy import misc
    from sklearn.externals.six import StringIO
    from sklearn.tree import export_graphviz
    import pydotplus
    from sklearn.model_selection import GridSearchCV
    from sklearn.model_selection import TimeSeriesSplit

    parameters = {'min_samples_leaf': range(500, 1500,500),'max_depth':range(5,20,1),'min_impurity_decrease':[0.0005,0.001,0.005,0.01]}
    my_cv = TimeSeriesSplit(n_splits=2).split(X,y)
    clf = GridSearchCV(estimator=DecisionTreeClassifier(random_state=1),cv=my_cv, param_grid=parameters, n_jobs=4)
    clf.fit(X=X, y=y)

    fitted_tree = clf.best_estimator_
    # print(clf.cv_results_)
    dot_data = StringIO()

    export_graphviz(fitted_tree, out_file=dot_data,
                    filled=True, rounded=True,
                    special_characters=True, feature_names=features)

    graph = pydotplus.graph_from_dot_data(dot_data.getvalue()).write_png(outputPath)
    img = misc.imread(outputPath)
    plt.imshow(img)
    plt.show()
    return fitted_tree,clf.cv_results_



def treeToRules(tree, feature_names,target_names=['1','0'],threshold= 0):
    from sklearn.tree import _tree
    '''
    Outputs a decision tree model as a Python function

    Parameters:
    -----------
    tree: decision tree model
        The decision tree to represent as a function
    feature_names: list
        The feature names of the dataset used for building the decision tree
    '''

    tree_ = tree.tree_
    feature_name = [
        feature_names[i] if i != _tree.TREE_UNDEFINED else "undefined!"
        for i in tree_.feature
    ]
    def maxProbability(v1, v2):
        sum = v1 + v2
        v = v1 if v1 > v2 else v2
        return v / sum
    def dominantTargetName(v1,v2):
        return target_names[0] if v1 > v2 else target_names[1]

    def recurse(node, depth, rule,rules):
        if tree_.feature[node] != _tree.TREE_UNDEFINED:
            name = feature_name[node]
            split_threshold = tree_.threshold[node]
            rule.append(" {} <= {} ".format(name, split_threshold))
            recurse(tree_.children_left[node],depth + 1, rule,rules)
            rule.pop()
            rule.append(" {} > {}".format(name, split_threshold))
            recurse(tree_.children_right[node],depth + 1, rule,rules)
            rule.pop()
        else:
            v1 = tree_.value[node][0][0]
            v2 = tree_.value[node][0][1]
            maxProb = maxProbability(v1,v2)

            if  maxProb > threshold:
                rule.append(" class {} with a probability of {} ( {},{} )".format(dominantTargetName(v1, v2),maxProb, v1,v2))
                rules.append(''.join(rule))
                rule.pop()

    rule = ['if']
    rules = []
    recurse(0,1,rule,rules)
    return rules


def main():
    features = ['dailyTempAvg(Celsius)', 'numberIcyDays', 'numberFreezingDays', 'monthlyRainVolume(mm)', 'numberRainyDays',
         'dailySunnyHoursAvg', 'monthlyWindSpeedAvg(km/h)', 'holidayBefore', 'holidayAfter', 'isHoliday',
         'participants']
    X = df[features]


    df['price_premium'][df['price_premium']>=0] = 1
    df['price_premium'][df['price_premium']<0] = 0
    # print(df['price_premium'][df['price_premium'] == 1].shape)
    y = df['price_premium']
    fitted_tree,cv_results = decisionTree(X,y,features,OUTPUT_PATH)
    rules = treeToRules(fitted_tree,features,target_names=['positive','negative'],threshold=0.6)
    # print(cv_results)
    # print(len(rules))
    for r in rules:
        print(''.join(r))

if __name__ == '__main__':
    main()