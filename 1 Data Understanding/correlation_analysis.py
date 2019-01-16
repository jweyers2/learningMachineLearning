import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

path = '../00 Data/Final/cleanFinal.csv'
data = pd.read_csv(path, index_col='datetime')
corr = data.corr()
fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(corr,cmap='coolwarm', vmin=-1, vmax=1)
fig.colorbar(cax)
ticks = np.arange(0,len(data.columns),1)
ax.set_xticks(ticks)
plt.xticks(rotation=90)
ax.set_yticks(ticks)
ax.set_xticklabels(data.columns)
ax.set_yticklabels(data.columns)

#make op bigger for displaying whole labels
plt.gcf().subplots_adjust(top=0.55)

#plt.show()

plt.savefig('../00 Data/Figures/correlations.png')