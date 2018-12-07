import pandas as pd

path = './searchResults.csv'
resultPath = './bestParamSet.csv'
results = pd.read_csv(path)
results = results.fillna('None')
ordered = results.sort_values(by='score', ascending=False)
best = ordered.iloc[:15]
ranking = pd.DataFrame(columns=['ratio', 'loss', 'penalty', 'n_splits', 'tol'])
param_grid = [
    # pca variance ratio
    [0.75, 0.7, 0.85, 0.9, 0.95, None],
    # loss
    ['hinge', 'log', 'modified_huber', 'squared_hinge', 'perceptron'],
    # penalty
    ['l2', 'elasticnet'],
    # n_splits
    [50, 100, 150],
    # tol
    [0.001, 0.003, 0.005, 0.007, 0.01]
]
param_list = ['ratio', 'loss', 'penalty', 'n_splits', 'tol']
bestParamSet = []
for param in param_list:
    ranking = best[param].value_counts().to_dict()
    top = list(ranking.keys())[0]
    bestParamSet.append(top)

result = pd.DataFrame(columns=['ratio', 'loss', 'penalty', 'n_splits', 'tol', 'score'])
score = results.loc[(results['ratio'] == bestParamSet[0]) & (results['loss'] == bestParamSet[1]) & (results['penalty'] == bestParamSet[2]) & (results['n_splits'] == bestParamSet[3]) & (results['tol'] == bestParamSet[4])]['score']
bestParamSet.append(score.iloc[0])
result.loc[len(result)] = bestParamSet
result.to_csv(resultPath, index=False, sep=',')
