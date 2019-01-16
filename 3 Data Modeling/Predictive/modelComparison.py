# libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# set width of bar
barWidth = 0.25

accuracy = [0.79,0.8,0.66,0.77,0.8,0.8,0.814,0.0,0.72]
roc =      [0.72,0.73,0.7,0.74,0.73,0.72,0.75,0.0,0.5]


# values = [accuracy, roc]
# df = pd.DataFrame(values, columns=['accuracy', 'roc'],
#     index=['SGD','SVC','GaussianNB', 'Soft Voting', 'Hard Voting', 'Logistic Reg.', 'RNN', 'Decision Tree', 'Random Forest'])
# df.loc[len(df)] = [0.79, 0.72] #SGD
# df.loc[len(df)] = [0.8, 0.73] #SVC
# df.loc[len(df)] = [0.66, 0.7] #GNB
# df.loc[len(df)] = [0.77, 0.74] #Soft
# df.loc[len(df)] = [0.8, 0.73] #Hard
# df.loc[len(df)] = [0.8, 0.72] #Logistic
# df.loc[len(df)] = [0.814, 0.75] #RNN
# df.loc[len(df)] = [0, 0] #Tree
# df.loc[len(df)] = [0.72, 0.5] #RF
# df.sort_values(by='accuracy', ascending=False)
# print(df)

# Set position of bar on X axis
r1 = np.arange(len(accuracy))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]

# Make the plot
plt.bar(r1, accuracy, color='#FE2E2E', width=barWidth, edgecolor='white', label='accuracy')
plt.bar(r2, roc, color='#81F781', width=barWidth, edgecolor='white', label='roc')

# Add xticks on the middle of the group bars
plt.xlabel('group', fontweight='bold')
plt.xticks([r + barWidth for r in range(len(accuracy))], ['SGD','SVC','Gaussian NB', 'Soft Voting', 'Hard Voting', 'Logistic Reg.', 'RNN', 'Decision Tree', 'Random Forest'])
plt.xticks(rotation=60)

#Labels
plt.xlabel('Model')
plt.ylabel('Performance')

#Legend
legend = ['Accuracy', 'ROC']
plt.legend(legend, loc=1)

#Make Bottom visible
plt.gcf().subplots_adjust(bottom=0.3)
axes = plt.gca()
axes.set_ylim([0, 1])

#set y axis
plt.ylim([0.4, 1])

plt.savefig('./modelComparision.png')
