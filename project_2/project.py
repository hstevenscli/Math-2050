import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

data = pd.read_csv("./FEV-1.csv")
print("Stats on the data:\n", data.drop(columns="Id").describe())
print()


bins = [0,4,9,14,19]
labels = ['3-4', '5-9', '10-14', '15-19']

data['AgeGroup'] = pd.cut(data['Age'], bins=bins, labels=labels, right=True)

sex_group_stats = data.groupby("Sex")

sex_group_stats.describe()

boys_data = sex_group_stats.get_group(1)
girls_data = sex_group_stats.get_group(0)

############ i. CI for the mean fev to age and smoking status

############ BOYS #######################
##### AGEGROUP

boys_5_9 = boys_data[boys_data['AgeGroup'] == '5-9']
boys_10_14 = boys_data[boys_data['AgeGroup'] == '10-14']
boys_15_19 = boys_data[boys_data['AgeGroup'] == '15-19']

# Boys 5-9
cinterval = stats.t.interval(alpha=0.95, df=len(data)-1, loc=np.mean(boys_5_9["FEV"]), scale=stats.sem(boys_5_9["FEV"]))
print("CI for boys aged 5-9:", cinterval)
print("Actual mean:", np.mean(boys_5_9["FEV"]))

# Boys 10-14
cinterval = stats.t.interval(alpha=0.95, df=len(data)-1, loc=np.mean(boys_10_14["FEV"]), scale=stats.sem(boys_10_14["FEV"]))
print("CI for boys aged 10-14:", cinterval)
print("Actual mean:", np.mean(boys_10_14["FEV"]))

# Boys 15-19
cinterval = stats.t.interval(alpha=0.95, df=len(data)-1, loc=np.mean(boys_15_19["FEV"]), scale=stats.sem(boys_15_19["FEV"]))
print("CI for boys aged 15-19:", cinterval)
print("Actual mean:", np.mean(boys_15_19["FEV"]))

###### SMOKING STATUS

boys_smokers = boys_data[boys_data["Smoke"] == 1]
boys_nonsmokers = boys_data[boys_data["Smoke"] == 0]

# Boys smokers
cinterval = stats.t.interval(alpha=0.95, df=len(data)-1, loc=np.mean(boys_smokers["FEV"]), scale=stats.sem(boys_smokers["FEV"]))
print("CI for boy smokers:", cinterval)
print("Actual mean:", np.mean(boys_smokers["FEV"]))

# Boys nonsmokers

cinterval = stats.t.interval(alpha=0.95, df=len(data)-1, loc=np.mean(boys_nonsmokers["FEV"]), scale=stats.sem(boys_nonsmokers["FEV"]))
print("CI for boys nonsmokers:", cinterval)
print("Actual mean:", np.mean(boys_nonsmokers["FEV"]))

################# GIRLS ###################
########### AGE ########

girls_5_9 = girls_data[girls_data['AgeGroup'] == '5-9']
girls_10_14 = girls_data[girls_data['AgeGroup'] == '10-14']
girls_15_19 = girls_data[girls_data['AgeGroup'] == '15-19']

# Girls 5-9
cinterval = stats.t.interval(alpha=0.95, df=len(data)-1, loc=np.mean(girls_5_9["FEV"]), scale=stats.sem(girls_5_9["FEV"]))
print("CI for girls aged 5-9:", cinterval)
print("Actual mean:", np.mean(girls_5_9["FEV"]))

# Girls 10-14
cinterval = stats.t.interval(alpha=0.95, df=len(data)-1, loc=np.mean(girls_10_14["FEV"]), scale=stats.sem(girls_10_14["FEV"]))
print("CI for girls aged 10-14:", cinterval)
print("Actual mean:", np.mean(girls_10_14["FEV"]))

# Girls 15-19
cinterval = stats.t.interval(alpha=0.95, df=len(data)-1, loc=np.mean(girls_15_19["FEV"]), scale=stats.sem(girls_15_19["FEV"]))
print("CI for girls aged 15-19:", cinterval)
print("Actual mean:", np.mean(girls_15_19["FEV"]))

######## SMOKING STATUS #############

girls_smokers = girls_data[girls_data["Smoke"] == 1]
girls_nonsmokers = girls_data[girls_data["Smoke"] == 0]

# Girls smokers
cinterval = stats.t.interval(alpha=0.95, df=len(data)-1, loc=np.mean(girls_smokers["FEV"]), scale=stats.sem(girls_smokers["FEV"]))
print("CI for girl smokers:", cinterval)
print("Actual mean:", np.mean(girls_smokers["FEV"]))

# Girls nonsmokers

cinterval = stats.t.interval(alpha=0.95, df=len(data)-1, loc=np.mean(girls_nonsmokers["FEV"]), scale=stats.sem(girls_nonsmokers["FEV"]))
print("CI for girls nonsmokers:", cinterval)
print("Actual mean:", np.mean(girls_nonsmokers["FEV"]))


