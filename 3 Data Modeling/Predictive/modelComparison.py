# libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# set width of bar
barWidth = 0.25
resolution = 600

#results for prediction analysis
df = pd.DataFrame(columns=['accuracy', 'roc'])
df.loc['SGD'] = [0.79, 0.72] #SGD
df.loc['SVC'] = [0.8, 0.73] #SVC
df.loc['Gaussian NB'] = [0.66, 0.7] #GNB
df.loc['Soft Voting'] = [0.78, 0.75] #Soft
df.loc['Hard Voting'] = [0.8, 0.73] #Hard
df.loc['Logistic Ref.'] = [0.8, 0.72] #Logistic
df.loc['RNN'] = [0.814, 0.75] #RNN
df.loc['Decision Tree'] = [0.78, 0.8] #Tree
df.loc['Random Forest'] = [0.72, 0.5] #RF
df = df.sort_values(by='accuracy', ascending=False)
accuracy = df['accuracy'].tolist()
roc = df['roc'].tolist()

# Set position of bar on X axis
r1 = np.arange(len(accuracy))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]

#plt.style.use('dark_background')

# Make the plot
plt.bar(r1, accuracy, color='#6D9EEB', width=barWidth, edgecolor='black', label='accuracy')
plt.bar(r2, roc, color='#F35B69', width=barWidth, edgecolor='black', label='roc')

# Add xticks on the middle of the group bars
plt.xlabel('group', fontweight='bold')
plt.xticks([r + barWidth for r in range(len(accuracy))], df.index.values)
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
plt.ylim([0, 1])

plt.savefig('./modelComparision.png', transparent=True, dpi=resolution)