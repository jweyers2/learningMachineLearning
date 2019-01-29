import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

path = '../../00 Data/Final/binaryFinal.csv'

df_raw = pd.read_csv(path,sep=',')

features_raw = ['datetime', 'price', 'consumption', 'dailyTempAvg(Celsius)',
       'dailyTempMax(Celsius)', 'dailyTempMin(Celsius)', 'numberFreezingDays',
       'numberIcyDays', 'monthlyRainVolume(mm)', 'numberRainyDays',
       'dailySunnyHoursAvg', 'monthlyWindSpeedAvg(km/h)', 'monthlySnowyDays',
       'dailySnowVolumeAvg(cm)', 'price_dayahead', 'consumption_dayahead',
       'holidayBefore', 'holidayAfter', 'isHoliday', 'participants',
       'price_premium', 'price_dayahead_lastDay',
       'consumption_dayahead_lastDay', 'price_intraday_lastDay',
       'consumption_intraday_lastDay', 'price_dayahead_increase_lastWeek',
       'consumption_dayahead_increase_lastWeek',
       'price_intraday_increase_lastWeek',
       'consumption_intraday_increase_lastWeek', 'cat_price_premium',
       'january', 'february', 'march', 'april', 'may', 'june', 'july',
       'august', 'september', 'october', 'november', 'december', 'monday',
       'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday',
       'hour0', 'hour1', 'hour2', 'hour3', 'hour4', 'hour5', 'hour6', 'hour7',
       'hour8', 'hour9', 'hour10', 'hour11', 'hour12', 'hour13', 'hour14',
       'hour15', 'hour16', 'hour17', 'hour18', 'hour19', 'hour20', 'hour21',
       'hour22', 'hour23']
features = ['price', 'consumption', 'dailyTempAvg(Celsius)',
       'dailyTempMax(Celsius)', 'dailyTempMin(Celsius)', 'numberFreezingDays',
       'numberIcyDays', 'monthlyRainVolume(mm)', 'numberRainyDays',
       'dailySunnyHoursAvg', 'monthlyWindSpeedAvg(km/h)', 'monthlySnowyDays',
       'dailySnowVolumeAvg(cm)', 'price_dayahead', 'consumption_dayahead',
       'holidayBefore', 'holidayAfter', 'isHoliday', 'participants', 'price_dayahead_lastDay',
       'consumption_dayahead_lastDay', 'price_intraday_lastDay',
       'consumption_intraday_lastDay', 'price_dayahead_increase_lastWeek',
       'consumption_dayahead_increase_lastWeek',
       'price_intraday_increase_lastWeek',
       'consumption_intraday_increase_lastWeek']

featureLabels = ["Daily sunny hours on average","Daily average Temperature"]
# preparing the categorical datafranmes
df_cat_pos = df_raw[df_raw['cat_price_premium'] == 1]
df_cat_neg = df_raw[df_raw['cat_price_premium'] == 0]


import matplotlib.transforms as mtrans
import mpl_toolkits.axes_grid1.inset_locator as inset
from matplotlib import collections
import seaborn as sns

def connect_spines(left_ax, right_ax, left_y, right_y, **line_kwds):
    left_trans = mtrans.blended_transform_factory(left_ax.transData, left_ax.transAxes)
    right_trans = mtrans.blended_transform_factory(right_ax.transData, right_ax.transAxes)

    left_data_trans = left_ax.transScale + left_ax.transLimits
    right_data_trans = right_ax.transScale + right_ax.transLimits

    left_pos = left_data_trans.transform((0, left_y))[1]
    right_pos = right_data_trans.transform((0, right_y))[1]

    bbox = mtrans.Bbox.from_extents(0, left_pos, 0, right_pos)
    right_bbox = mtrans.TransformedBbox(bbox, right_trans)
    left_bbox = mtrans.TransformedBbox(bbox, left_trans)

    connecter = inset.BboxConnector(left_bbox, right_bbox, loc1=3, loc2=2, **line_kwds)
    connecter.set_clip_on(False)

    return connecter

def multipleLinePlot(X,cluster_center):
    features = X.columns
    num_of_features = len(features)

    df = pd.DataFrame(cluster_center)
    df.columns = features
    num_of_clusters = df.shape[0]
    data = cluster_center
    with sns.axes_style('ticks'):
        fig, axes = plt.subplots(ncols=num_of_features, figsize=(14,8))
        colors = dict(zip(np.unique(data[:, -1]), sns.color_palette(n_colors=num_of_clusters)))
        for i in range(num_of_features):
            axes[i].set_ylim(0, df[features[i]].max()*1.25)

        for n, (ax1, ax2) in enumerate(zip(axes[:-1], axes[1:])):
            lines = []
            for row in data:
                line = connect_spines(ax1, ax2, row[n], row[n+1], color=colors[row[-1]])
                l  = ax1.add_line(line)
                lines.append(l)

        for n, ax in enumerate(axes):
            ax.set_xticks([0])
            ax.set_xticklabels([features[n]])
            ax.xaxis.set_tick_params(rotation=45)

        fig.subplots_adjust(wspace=0)

        fig.legend((l for l in lines),('Cluster ' + str(i) for i in range(num_of_clusters)),loc='upper right')
        sns.despine(fig=fig, bottom=True, trim=True)


def plotNumericInterrelationPPWithFeature(violinFeatures):
    import seaborn as sns
    violinDF = pd.melt(df_raw,id_vars=['cat_price_premium'], value_vars=violinFeatures,var_name="feature", value_name="value")
    f= plt.subplots(figsize=(6,5))
    g =sns.violinplot(x='value',y="feature",hue='cat_price_premium',split=True,data=violinDF, legend_out = True)
    new_title = ''
    g.legend_.set_title(new_title)
    new_labels = ['positive price premium','negative price premium']
    for t, l in zip(g.legend_.texts, new_labels): t.set_text(l)
    plt.tight_layout()
    plt.show()

def plotInterrelationRatio(feature):
    plt.style.use('seaborn-deep')
    fig, (ax1, ax2) = plt.subplots(nrows=2)

    ns, bins, patches = ax1.hist([df_cat_pos[feature].values,df_cat_neg[feature].values],bins=8,label=['positive', 'negative'])
    ax1.legend()

    ax2.bar(bins[:-1],  # this is what makes it comparable
            ns[0] / (ns[0] + ns[1]),  # maybe check for div-by-zero!
            width=6)

    ax1.set_ylabel('Num of occurrences')
    ax2.set_ylabel('Positive share')
    ax2.axhline(y=0.5, color='r', linestyle='-')
    ax2.set_yticks([0.0,0.25,0.5,0.75,1.0])
    plt.title(feature)
    plt.tight_layout()
    plt.show()
# plotInterrelationRatio('dailyTempAvg(Celsius)')
# plotInterrelationRatio('dailySunnyHoursAvg')
# plotInterrelationRatio('numberFreezingDays')
# plotInterrelationRatio('monthlyWindSpeedAvg(km/h)')
# plotInterrelationRatio('price_dayahead_lastDay')
# plotInterrelationRatio('price_intraday_lastDay')
# plotInterrelationRatio('holidayAfter')
# plotInterrelationRatio('consumption_dayahead')
# plotInterrelationRatio('consumption_dayahead_lastDay')
# plotInterrelationRatio('dailySnowVolumeAvg(cm)')

features_violin = ['dailyTempAvg(Celsius)', 'dailySunnyHoursAvg', 'numberFreezingDays']
# plotNumericInterrelationPPWithFeature(features_violin)
features_violin = ['monthlyWindSpeedAvg(km/h)']
# plotNumericInterrelationPPWithFeature(features_violin)
features_violin = ['price_dayahead_lastDay', 'price_intraday_lastDay', 'holidayAfter']
# plotNumericInterrelationPPWithFeature(features_violin)
features_violin = ['consumption_dayahead','consumption_dayahead_lastDay']
# plotNumericInterrelationPPWithFeature(features_violin)
features_violin = ['dailySnowVolumeAvg(cm)']
# plotNumericInterrelationPPWithFeature(features_violin)


def plotHistCatPricePremiumWithFeature(feature,xlabel,bins,alpha=0.5,log=False):
    f = plt.figure(figsize=(6,5))
    p1 = plt.hist( df_cat_pos[feature],bins=bins,log=log,alpha=alpha,label="positive")
    p2 = plt.hist( df_cat_neg[feature],bins=bins,log=log,alpha=alpha,label="negative")
    plt.xlabel(xlabel)
    plt.ylabel("Num of occurrences")
    plt.legend(loc='upper right')
    plt.show()

# riskPrice = df_cat_pos
# print("Share of positive Price premiums: " + str(df_cat_pos.shape[0] / (df_cat_pos.shape[0] + df_cat_neg.shape[0])))
# plotHistCatPricePremiumWithFeature('price_premium',"Price premium",20,alpha=0.6,log=True)
# plotHistCatPricePremiumWithFeature('dailySunnyHoursAvg',"Daily average sunny hours",10)
# plotHistCatPricePremiumWithFeature('dailyTempAvg(Celsius)',"Daily average Temperature",20)
# plotHistCatPricePremiumWithFeature('numberFreezingDays',"Num of freezing days last month",20)
# plotHistCatPricePremiumWithFeature('dailySnowVolumeAvg(cm)',"Average daily snow volumne in cm",20)
# plotHistCatPricePremiumWithFeature('consumption',"consumption",20)
# plotHistCatPricePremiumWithFeature('consumption_dayahead_increase_lastWeek',"consumption",20)


def riskAnalysis(feature,binsize):
    f,(ax1,ax2) = plt.subplots(nrows=2,figsize=(6,5))
    ax1.scatter(df_cat_pos[feature],df_cat_pos['price_premium'],color='g',label="positive price premium")
    ax1.scatter(df_cat_neg[feature],df_cat_neg['price_premium'],color='r',label="negative price premium")

    ax1.legend()
    # support = []
    probs = []
    premiums = []
    for i in range(int(df_raw[feature].min()-1),int(df_raw[feature].max()-1),binsize):
        num_pos = df_cat_pos.ix[(df_cat_pos[feature]>= i) & (df_cat_pos[feature] <i+binsize)][feature].count()
        num_neg = df_cat_neg.ix[(df_cat_neg[feature]>= i) & (df_cat_neg[feature] <i+binsize)][feature].count()
        prob = num_pos / (num_pos + num_neg)
        # support.append((num_pos + num_neg))
        probs.append(prob)
        # print(((1-prob)*df_cat_neg.ix[(df_cat_neg[feature]>= i) & (df_cat_neg[feature] <i+1)]['price_premium']).sum())
        premiums.append(((prob* df_cat_pos.ix[(df_cat_pos[feature]>= i) & (df_cat_pos[feature] <i+1)]['price_premium']).sum() + ((1-prob)*df_cat_neg.ix[(df_cat_neg[feature]>= i) & (df_cat_neg[feature] <i+1)]['price_premium']).sum())/(num_pos + num_neg))

    ax2.plot(range(int(df_raw[feature].min()-1),int(df_raw[feature].max()-1),binsize),premiums,label="'Expected profit when buying\n  at intraday auction'")
    # ax2.plot(range(int(df_raw[feature].min()-1),int(df_raw[feature].max()-1),binsize),support,label="Support")
    ax2.legend()
    plt.title("Feature: " + feature)
    plt.tight_layout()
    plt.show()

# riskAnalysis('dailyTempAvg(Celsius)',1)
# riskAnalysis('dailySunnyHoursAvg',1)
# riskAnalysis('numberFreezingDays',1)
# riskAnalysis('monthlyWindSpeedAvg(km/h)',1)
# riskAnalysis('price_dayahead_lastDay',25)
# riskAnalysis('price_intraday_lastDay',25)
# riskAnalysis('holidayAfter',10)
# riskAnalysis('consumption_dayahead',50)
# riskAnalysis('consumption_dayahead_lastDay',50)
riskAnalysis('dailySnowVolumeAvg(cm)',10)

def findRegression():
    # possible reasoning: find function to approximate the underlying pattern
    return None