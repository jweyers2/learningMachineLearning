import pandas as pd

useGridSearch = False
columns=['ratio', 'penalty', 'c', 'solver', 'score', 'probability']
i = 0

path = './searchResults.csv'
resultPath = './bestParamSet.csv'
results = pd.read_csv(path)
results = results.fillna('None')
results = results.sort_values(by=['score'], ascending=False)
# results = results.sort_values(by=['score', 'probability'], ascending=False)

best = pd.DataFrame(columns=columns)
best.loc[i] = results.iloc[i]
i = i + 1
best2 = pd.DataFrame(columns=columns)
best2.loc[0] = results.iloc[i]

while best.loc[0,'score'] == best2.loc[0,'score']:
    #and best.loc[0,'probability'] == best2.loc[0,'probability']:
    best.loc[i] = best2.loc[0]
    i = i + 1
    best2.loc[0] = results.iloc[i]

print(best)
best.to_csv(resultPath, index=False, sep=',')
