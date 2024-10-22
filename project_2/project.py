import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

pd.set_option('display.max_columns', None)  # Show all columns
pd.set_option('display.max_rows', None)     # Show all rows

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

###### SMOKING STATUS

##### SMOKERS
boys_smokers_10_14 = boys_10_14[boys_10_14['Smoke']== 1]
boys_smokers_15_19 = boys_15_19[boys_15_19['Smoke']== 1]
girls_smokers_10_14 = girls_10_14[girls_10_14['Smoke']== 1]
girls_smokers_15_19 = girls_15_19[girls_15_19['Smoke']== 1]


##### NON SMOKERS
boys_nonsmokers_10_14 = boys_10_14[boys_10_14['Smoke']== 0]
boys_nonsmokers_15_19 = boys_15_19[boys_15_19['Smoke']== 0]
girls_nonsmokers_10_14 = girls_10_14[girls_10_14['Smoke']== 0]
girls_nonsmokers_15_19 = girls_15_19[girls_15_19['Smoke']== 0]

cinterval = stats.t.interval(alpha=0.95, df=len(data)-1, loc=np.mean(boys_smokers_10_14["FEV"]), scale=stats.sem(boys_smokers_10_14["FEV"]))
print("CI for boy smokers 10-14:", cinterval)
print("Actual mean:", np.mean(boys_smokers_10_14["FEV"]))

cinterval = stats.t.interval(alpha=0.95, df=len(data)-1, loc=np.mean(boys_smokers_15_19["FEV"]), scale=stats.sem(boys_smokers_15_19["FEV"]))
print("CI for boy smokers 15-19:", cinterval)
print("Actual mean:", np.mean(boys_smokers_15_19["FEV"]))

cinterval = stats.t.interval(alpha=0.95, df=len(data)-1, loc=np.mean(girls_smokers_10_14["FEV"]), scale=stats.sem(girls_smokers_10_14["FEV"]))
print("CI for girl smokers 10-14:", cinterval)
print("Actual mean:", np.mean(girls_smokers_10_14["FEV"]))

cinterval = stats.t.interval(alpha=0.95, df=len(data)-1, loc=np.mean(girls_smokers_15_19["FEV"]), scale=stats.sem(girls_smokers_15_19["FEV"]))
print("CI for girl smokers 15-19:", cinterval)
print("Actual mean:", np.mean(girls_smokers_15_19["FEV"]))

cinterval = stats.t.interval(alpha=0.95, df=len(data)-1, loc=np.mean(boys_nonsmokers_10_14["FEV"]), scale=stats.sem(boys_nonsmokers_10_14["FEV"]))
print("CI for boy nonsmokers 10-14:", cinterval)
print("Actual mean:", np.mean(boys_nonsmokers_10_14["FEV"]))

cinterval = stats.t.interval(alpha=0.95, df=len(data)-1, loc=np.mean(boys_nonsmokers_15_19["FEV"]), scale=stats.sem(boys_nonsmokers_15_19["FEV"]))
print("CI for boy nonsmokers 15-19:", cinterval)
print("Actual mean:", np.mean(boys_nonsmokers_15_19["FEV"]))

cinterval = stats.t.interval(alpha=0.95, df=len(data)-1, loc=np.mean(girls_nonsmokers_10_14["FEV"]), scale=stats.sem(girls_nonsmokers_10_14["FEV"]))
print("CI for girl nonsmokers 10-14:", cinterval)
print("Actual mean:", np.mean(girls_nonsmokers_10_14["FEV"]))

cinterval = stats.t.interval(alpha=0.95, df=len(data)-1, loc=np.mean(girls_nonsmokers_15_19["FEV"]), scale=stats.sem(girls_nonsmokers_15_19["FEV"]))
print("CI for girl nonsmokers 15-19:", cinterval)
print("Actual mean:", np.mean(girls_nonsmokers_15_19["FEV"]))


###################################################### HORMONES ############################################################
###################################################### HORMONES ############################################################
###################################################### HORMONES ############################################################
###################################################### HORMONES ############################################################
###################################################### HORMONES ############################################################
###################################################### HORMONES ############################################################

# Load the data
df = pd.read_csv('HORMONE.csv')

hormone_group = df.groupby("Hormone")
sal = hormone_group.get_group(1)
app = hormone_group.get_group(2)
cck = hormone_group.get_group(3)
sec = hormone_group.get_group(4)
vip = hormone_group.get_group(5)


print("1=SAL/2=APP/3=CCK/4=SEC/5=VIP")
print(hormone_group.mean())



# Separate the hormone group (Hormone != 1) and placebo group (Hormone == 1)
placebo = df[df['Hormone'] == 1]
hormone = df[df['Hormone'] != 1]

# Perform t-test for Bilsecpr (biliary secretion)
t_stat_bilsecpr, p_value_bilsecpr = stats.ttest_ind(placebo['Bilsecpr'], hormone['Bilsecpr'], equal_var=False)

# Perform t-test for Bilphpr (biliary pH)
t_stat_bilphpr, p_value_bilphpr = stats.ttest_ind(placebo['Bilphpr'], hormone['Bilphpr'], equal_var=False)

print(f"Bilsecpr P-value: {p_value_bilsecpr}")
print(f"Bilphpr P-value: {p_value_bilphpr}")


t_stat_pancsecpr, p_value_pancsecpr = stats.ttest_ind(placebo['Pansecpr'], hormone['Pansecpr'], equal_var=False)

# Perform t-test for Bilphpr (biliary pH)
t_stat_panphpr, p_value_panphpr = stats.ttest_ind(placebo['Panphpr'], hormone['Panphpr'], equal_var=False)

print(f"Pansecpr P-value: {p_value_pancsecpr}")
print(f"Panphpr P-value: {p_value_panphpr}")
