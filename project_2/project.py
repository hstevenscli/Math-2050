import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("./FEV-1.csv")
print("Stats on the data:\n", data.drop(columns="Id").describe())
print()


bins = [0,4,9,14,19]
labels = ['3-4', '5-9', '10-14', '15-19']

data['AgeGroup'] = pd.cut(data['Age'], bins=bins, labels=labels, right=True)

sex_group_stats = data.groupby("Sex")

boys_data = sex_group_stats.get_group(1)
girls_data = sex_group_stats.get_group(0)
boy_age_group_stats = boys_data.groupby('AgeGroup').mean()
girl_age_group_stats = girls_data.groupby('AgeGroup').mean()

# girl_height_group_stats = girls_data.groupby("Hgt").mean()
# boy_height_group_stats = boys_data.groupby("Hgt").mean()

# print(boy_age_group_stats)
# print(girl_age_group_stats)

# print(girl_height_group_stats)
# print(boy_height_group_stats)

##################### Mean fev by age group

fev_mean_by_age = data.groupby(['Sex', 'AgeGroup'])['FEV'].mean().unstack()

print("FEV and Age:\n", fev_mean_by_age)
print()
