import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import scipy
import scipy.stats as stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd

pd.set_option("display.max_columns", 15)
fevData = pd.read_csv("FEV-1.csv")
fevData.drop(labels = ("Id"), axis=1)
numerics = fevData.describe()
numerics.to_csv("numericalData.csv")
mData = fevData[(fevData.Sex == 1)]
fData = fevData[(fevData.Sex == 0)]
smokers_b = mData[(fevData['Smoke'] == 1)]
nonSmokers_b = mData[(fevData['Smoke'] == 0)]
smokers_g = fData[(fevData['Smoke'] == 1)]
nonSmokers_g = fData[(fevData['Smoke'] == 0)]

def performHypothesisTests(itemOne, itemTwo):
    twoSidedTest = stats.ttest_ind(itemOne, itemTwo, alternative="two-sided")
    greaterThanTest = stats.ttest_ind(itemOne, itemTwo, alternative="greater")
    lessThanTest = stats.ttest_ind(itemOne, itemTwo, alternative="less")
    if twoSidedTest.pvalue > 0.05:
        return ("null accepted: no significant difference", f"pvalue={twoSidedTest.pvalue}, statistic={twoSidedTest.statistic}")
    elif greaterThanTest.pvalue <= 0.05:
        return ("greater than accepted: parameter 1 is greater than parameter 2", f"pvalue={greaterThanTest.pvalue}, statistic={greaterThanTest.statistic}", f"two-sided pvalue={twoSidedTest.pvalue}")
    elif lessThanTest.pvalue <= 0.05:
        return ("less than accepted: parameter 1 is less than parameter 2", f"pvalue={lessThanTest.pvalue}, statistic={lessThanTest.statistic}", f"two-sided pvalue={twoSidedTest.pvalue}")
# FEV Age groups computation
ageIntervals = [(5, 9), (10, 14), (15, 19)]
ageArray = []
for i in range(len(ageIntervals)):
    ageSubsetToInsert = fevData[((fevData.Age >= ageIntervals[i][0]) & (fevData.Age <= ageIntervals[i][1]))]
    ageArray.append(ageSubsetToInsert)
ageIntervalsSm = [(10, 14), (15, 19)]
ageArraySm = []
for i in range(len(ageIntervalsSm)):
    ageSubsetToInsert = fevData[((fevData.Age >= ageIntervalsSm[i][0]) & (fevData.Age <= ageIntervalsSm[i][1]))]
    ageArraySm.append(ageSubsetToInsert)
for i in range(len(ageArray)):
    item = ageArray[i]
    #CI
    #print(stats.t.interval(confidence = 0.95, df=len(item[item.Sex == 1].FEV), loc=np.mean(item[item.Sex == 1].FEV), scale=stats.sem(item[item.Sex == 1].FEV)))
    #print(stats.t.interval(confidence = 0.95, df=len(item[item.Sex == 0].FEV), loc=np.mean(item[item.Sex == 0].FEV), scale=stats.sem(item[item.Sex == 0].FEV)))
    print(performHypothesisTests(item[item.Sex == 1]['FEV'], item[item.Sex == 0]['FEV']))
for i in range(len(ageArraySm)):
    item = ageArraySm[i]
    #print(stats.t.interval(confidence = 0.95, df=len(item[(item.Sex == 1) & (item.Smoke == 1)].FEV), loc=np.mean(item[(item.Sex == 1) & (item.Smoke == 1)].FEV), scale=stats.sem(item[(item.Sex == 1) & (item.Smoke == 1)].FEV)))
    #print(stats.t.interval(confidence = 0.95, df=len(item[(item.Sex == 1) & (item.Smoke == 0)].FEV), loc=np.mean(item[(item.Sex == 1) & (item.Smoke == 0)].FEV), scale=stats.sem(item[(item.Sex == 1) & (item.Smoke == 0)].FEV)))
    #print(stats.t.interval(confidence = 0.95, df=len(item[(item.Sex == 0) & (item.Smoke == 0)].FEV), loc=np.mean(item[(item.Sex == 0) & (item.Smoke == 0)].FEV), scale=stats.sem(item[(item.Sex == 0) & (item.Smoke == 0)].FEV)))
    #print(stats.t.interval(confidence = 0.95, df=len(item[(item.Sex == 0) & (item.Smoke == 1)].FEV), loc=np.mean(item[(item.Sex == 0) & (item.Smoke == 1)].FEV), scale=stats.sem(item[(item.Sex == 0) & (item.Smoke == 1)].FEV)))
    print(performHypothesisTests(item[(item.Sex == 1) & (item.Smoke == 1)]['FEV'], item[(item.Sex == 1) & (item.Smoke == 0)]['FEV']))
    print(performHypothesisTests(item[(item.Sex == 0) & (item.Smoke == 1)]['FEV'], item[(item.Sex == 0) & (item.Smoke == 0)]['FEV']))
#End FEV work

hormoneData = pd.read_csv("HORMONE.csv")
hormoneData.insert(len(hormoneData.columns), "BilsecDiff", hormoneData.Bilsecpr - hormoneData.Bilsecpt, True)
hormoneData.insert(len(hormoneData.columns), "BilphDiff", hormoneData.Bilphpr - hormoneData.Bilphpt, True)
hormoneData.insert(len(hormoneData.columns), "PansecDiff", hormoneData.Pansecpr - hormoneData.Pansecpt, True)
hormoneData.insert(len(hormoneData.columns), "PanphDiff", hormoneData.Panphpr - hormoneData.Panphpt, True)
hormoneArray = []
hormoneTags = ["SAL", "APP", "CCK", "SEC", "VIP"]
hormoneArray.append(hormoneData[hormoneData.Hormone == 1])
hormoneArray.append(hormoneData[hormoneData.Hormone == 2])
hormoneArray.append(hormoneData[hormoneData.Hormone == 3])
hormoneArray.append(hormoneData[hormoneData.Hormone == 4])
hormoneArray.append(hormoneData[hormoneData.Hormone == 5])

for i in range(len(hormoneArray)):
    print(hormoneTags[i])
    item = hormoneArray[i]
    print("Bilsec")
    print(performHypothesisTests(item.Bilsecpr, item.Bilsecpt))
    print("Pansec")
    print(performHypothesisTests(item.Pansecpr, item.Pansecpt))
    print("Bilph")
    print(performHypothesisTests(item.Bilphpr, item.Bilphpt))
    print("Panph")
    print(performHypothesisTests(item.Panphpr, item.Panphpt))
for i in range(len(hormoneArray)):
    item = hormoneArray[i]
    if item[(item.Hormone == 1)].empty:
        print(hormoneTags[i])
        print("Bilsecdiff")
        print(performHypothesisTests(item.BilsecDiff, hormoneArray[0].BilsecDiff))
        print("Pansecdiff")
        print(performHypothesisTests(item.PansecDiff, hormoneArray[0].PansecDiff))
        print("Bilphdiff")
        print(performHypothesisTests(item.BilphDiff, hormoneArray[0].BilphDiff))
        print("Panphdiff")
        print(performHypothesisTests(item.PanphDiff, hormoneArray[0].PanphDiff))
