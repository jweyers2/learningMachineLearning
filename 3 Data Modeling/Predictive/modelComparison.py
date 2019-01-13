# libraries
import numpy as np
import matplotlib.pyplot as plt

# set width of bar
barWidth = 0.25

#values
accuracy = [0.8,0.8,0.8,0.8,0.8,0.8,0.8,0.8,0.8,0.8]
roc = [0.8,0.8,0.8,0.8,0.8,0.8,0.8,0.8,0.8,0.8]

# Set position of bar on X axis
r1 = np.arange(len(accuracy))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]

# Make the plot
plt.bar(r1, accuracy, color='#FE2E2E', width=barWidth, edgecolor='white', label='accuracy')
plt.bar(r2, roc, color='#81F781', width=barWidth, edgecolor='white', label='roc')

# Add xticks on the middle of the group bars
plt.xlabel('group', fontweight='bold')
plt.xticks([r + barWidth for r in range(len(accuracy))], ['SGD','SVC','GaussianNB', 'Soft Voting', 'Soft Voting', 'Logistic Reg.', 'RNN', 'Decision Tree', 'ARIMA', 'Random Forest'])
plt.xticks(rotation=70)

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

# Create legend & Show graphic
#plt.show()
plt.savefig('./modelComparision.png')
