# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 20:09:44 2024

@author: surfe
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('FEV-1.csv')

#Part1
#Problem1
print(df.drop(columns=['Id']).describe())

df['Age'].hist()
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Distribution of Age')
plt.show()

df['FEV'].hist()
plt.xlabel('FEV')
plt.ylabel('Frequency')
plt.title('Distribution of FEV')
plt.show()

df['Hgt'].hist()
plt.xlabel('Height')
plt.ylabel('Frequency')
plt.title('Distribution of Height')
plt.show()

gender_counts = df['Sex'].value_counts()  
gender_counts.plot(kind='bar')

plt.xlabel('Gender')
plt.ylabel('Count')
plt.title('Number of Boys and Girls')
plt.show()

smoke_counts = df['Smoke'].value_counts()  
smoke_counts.plot(kind='bar')

plt.ylabel('Count')
plt.title('Number of Smokers')
plt.show()
#Problem2
bins = [3, 5, 10, 15, 20]
labels = ['3-4', '5-9', '10-14', '15-19']
df['AgeGroup'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)

mean_fev = df.groupby(['AgeGroup', 'Sex'])['FEV'].mean().unstack()

mean_fev.plot(kind='bar', figsize=(10, 6))
plt.title('Mean FEV by Age Group for Boys (0) and Girls (1)')
plt.xlabel('Age Group')
plt.ylabel('Mean FEV')
plt.legend(['Boys', 'Girls'])
plt.show()

#Part2
df = pd.read_csv('water_potability_new.csv')
df = df.dropna()

print(df.describe())

df.hist(figsize=(20, 10), bins=20)
plt.show()

df.plot(kind='box', subplots=True, layout=(4, 3), figsize=(15, 10))
plt.show()

print(df.groupby('Potability').describe())

for potability in df['Potability'].unique():
    subset = df[df['Potability'] == potability]
    plt.hist(subset['ph'], bins=20, alpha=0.5, label=f'Potability {potability}')
plt.title('Histogram of ph by Potability')
plt.xlabel('ph')
plt.ylabel('Frequency')
plt.show()

for potability in df['Potability'].unique():
    subset = df[df['Potability'] == potability]
    plt.hist(subset['Hardness'], bins=20, alpha=0.5, label=f'Potability {potability}')
plt.title('Histogram of ph by Potability')
plt.xlabel('Hardness')
plt.ylabel('Frequency')
plt.show()


for potability in df['Potability'].unique():
    subset = df[df['Potability'] == potability]
    plt.hist(subset['Solids'], bins=20, alpha=0.5, label=f'Potability {potability}')
plt.title('Histogram of ph by Potability')
plt.xlabel('Solids')
plt.ylabel('Frequency')
plt.show()

for potability in df['Potability'].unique():
    subset = df[df['Potability'] == potability]
    plt.hist(subset['Chloramines'], bins=20, alpha=0.5, label=f'Potability {potability}')
plt.title('Histogram of ph by Potability')
plt.xlabel('Chloramines')
plt.ylabel('Frequency')
plt.show()

for potability in df['Potability'].unique():
    subset = df[df['Potability'] == potability]
    plt.hist(subset['Sulfate'], bins=20, alpha=0.5, label=f'Potability {potability}')
plt.title('Histogram of ph by Potability')
plt.xlabel('Sulfate')
plt.ylabel('Frequency')
plt.show()

for potability in df['Potability'].unique():
    subset = df[df['Potability'] == potability]
    plt.hist(subset['Conductivity'], bins=20, alpha=0.5, label=f'Potability {potability}')
plt.title('Histogram of ph by Potability')
plt.xlabel('Conductivity')
plt.ylabel('Frequency')
plt.show()

for potability in df['Potability'].unique():
    subset = df[df['Potability'] == potability]
    plt.hist(subset['Organic_carbon'], bins=20, alpha=0.5, label=f'Potability {potability}')
plt.title('Histogram of ph by Potability')
plt.xlabel('Organic_carbon')
plt.ylabel('Frequency')
plt.show()

for potability in df['Potability'].unique():
    subset = df[df['Potability'] == potability]
    plt.hist(subset['Trihalomethanes'], bins=20, alpha=0.5, label=f'Potability {potability}')
plt.title('Histogram of ph by Potability')
plt.xlabel('Trihalomethanes')
plt.ylabel('Frequency')
plt.show()

Potable_Site1 = df[(df["Potability"]==1) & (df["site"]==1)]
Potable_Site2 = df[(df["Potability"]==1) & (df["site"]==2)]
Potable_Site3 = df[(df["Potability"]==1) & (df["site"]==3)]

Non_Potable_Site1 = df[(df["Potability"]==0) & (df["site"]==1)]
Non_Potable_Site2 = df[(df["Potability"]==0) & (df["site"]==2)]
Non_Potable_Site3 = df[(df["Potability"]==0) & (df["site"]==3)]

plt.boxplot(Non_Potable_Site1["ph"])
plt.title('Non Potable water, site 1, ph')
plt.show()

plt.boxplot(Non_Potable_Site2["ph"])
plt.title('Non Potable water, site 2, ph')
plt.show()

plt.boxplot(Non_Potable_Site3["ph"])
plt.title('Non Potable water, site 3, ph')
plt.show()


plt.boxplot(Non_Potable_Site1["Hardness"])
plt.title('Non Potable water, site 1, hardness')
plt.show()

plt.boxplot(Non_Potable_Site2["Hardness"])
plt.title('Non Potable water, site 2, hardness')
plt.show()

plt.boxplot(Non_Potable_Site3["Hardness"])
plt.title('Non Potable water, site 3, hardness')
plt.show()


plt.boxplot(Non_Potable_Site1["Solids"])
plt.title('Non Potable water, site 1, Solids')
plt.show()

plt.boxplot(Non_Potable_Site2["Solids"])
plt.title('Non Potable water, site 2, Solids')
plt.show()

plt.boxplot(Non_Potable_Site3["Solids"])
plt.title('Non Potable water, site 3, Solids')
plt.show()


plt.boxplot(Non_Potable_Site1["Chloramines"])
plt.title('Non Potable water, site 1, Chloramines')
plt.show()

plt.boxplot(Non_Potable_Site2["Chloramines"])
plt.title('Non Potable water, site 2, Chloramines')
plt.show()

plt.boxplot(Non_Potable_Site3["Chloramines"])
plt.title('Non Potable water, site 3, Chloramines')
plt.show()


plt.boxplot(Non_Potable_Site1["Sulfate"])
plt.title('Non Potable water, site 1, Chloramines')
plt.show()

plt.boxplot(Non_Potable_Site2["Sulfate"])
plt.title('Non Potable water, site 2, Sulfate')
plt.show()

plt.boxplot(Non_Potable_Site3["Sulfate"])
plt.title('Non Potable water, site 3, Sulfate')
plt.show()


plt.boxplot(Non_Potable_Site1["Conductivity"])
plt.title('Non Potable water, site 1, Conductivity')
plt.show()

plt.boxplot(Non_Potable_Site2["Conductivity"])
plt.title('Non Potable water, site 2, Conductivity')
plt.show()

plt.boxplot(Non_Potable_Site3["Conductivity"])
plt.title('Non Potable water, site 3, Conductivity')
plt.show()


plt.boxplot(Non_Potable_Site1["Organic_carbon"])
plt.title('Non Potable water, site 1, Organic_carbon')
plt.show()

plt.boxplot(Non_Potable_Site2["Organic_carbon"])
plt.title('Non Potable water, site 2, Organic_carbon')
plt.show()

plt.boxplot(Non_Potable_Site3["Organic_carbon"])
plt.title('Non Potable water, site 3, Organic_carbon')
plt.show()


plt.boxplot(Non_Potable_Site1["Trihalomethanes"])
plt.title('Non Potable water, site 1, Trihalomethanes')
plt.show()

plt.boxplot(Non_Potable_Site2["Trihalomethanes"])
plt.title('Non Potable water, site 2, Trihalomethanes')
plt.show()

plt.boxplot(Non_Potable_Site3["Trihalomethanes"])
plt.title('Non Potable water, site 3, Trihalomethanes')
plt.show()


plt.boxplot(Non_Potable_Site1["Turbidity"])
plt.title('Non Potable water, site 1, Turbidity')
plt.show()

plt.boxplot(Non_Potable_Site2["Turbidity"])
plt.title('Non Potable water, site 2, Turbidity')
plt.show()

plt.boxplot(Non_Potable_Site3["Turbidity"])
plt.title('Non Potable water, site 3, Turbidity')
plt.show()

#------------------------------------------------------------------------

plt.boxplot(Potable_Site1["ph"])
plt.title('Potable water, site 1, ph')
plt.show()

plt.boxplot(Potable_Site2["ph"])
plt.title('Potable water, site 2, ph')
plt.show()

plt.boxplot(Potable_Site3["ph"])
plt.title('Potable water, site 3, ph')
plt.show()


plt.boxplot(Potable_Site1["Hardness"])
plt.title('Potable water, site 1, hardness')
plt.show()

plt.boxplot(Potable_Site2["Hardness"])
plt.title('Potable water, site 2, hardness')
plt.show()

plt.boxplot(Potable_Site3["Hardness"])
plt.title('Potable water, site 3, hardness')
plt.show()


plt.boxplot(Potable_Site1["Solids"])
plt.title('Potable water, site 1, Solids')
plt.show()

plt.boxplot(Potable_Site2["Solids"])
plt.title('Potable water, site 2, Solids')
plt.show()

plt.boxplot(Potable_Site3["Solids"])
plt.title('Potable water, site 3, Solids')
plt.show()


plt.boxplot(Potable_Site1["Chloramines"])
plt.title('Potable water, site 1, Chloramines')
plt.show()

plt.boxplot(Potable_Site2["Chloramines"])
plt.title('Potable water, site 2, Chloramines')
plt.show()

plt.boxplot(Potable_Site3["Chloramines"])
plt.title('Potable water, site 3, Chloramines')
plt.show()


plt.boxplot(Potable_Site1["Sulfate"])
plt.title('Potable water, site 1, Chloramines')
plt.show()

plt.boxplot(Potable_Site2["Sulfate"])
plt.title('Potable water, site 2, Sulfate')
plt.show()

plt.boxplot(Potable_Site3["Sulfate"])
plt.title('Potable water, site 3, Sulfate')
plt.show()


plt.boxplot(Potable_Site1["Conductivity"])
plt.title('Potable water, site 1, Conductivity')
plt.show()

plt.boxplot(Potable_Site2["Conductivity"])
plt.title('Potable water, site 2, Conductivity')
plt.show()

plt.boxplot(Potable_Site3["Conductivity"])
plt.title('Potable water, site 3, Conductivity')
plt.show()


plt.boxplot(Potable_Site1["Organic_carbon"])
plt.title('Potable water, site 1, Organic_carbon')
plt.show()

plt.boxplot(Potable_Site2["Organic_carbon"])
plt.title('Potable water, site 2, Organic_carbon')
plt.show()

plt.boxplot(Potable_Site3["Organic_carbon"])
plt.title('Potable water, site 3, Organic_carbon')
plt.show()


plt.boxplot(Potable_Site1["Trihalomethanes"])
plt.title('Potable water, site 1, Trihalomethanes')
plt.show()

plt.boxplot(Potable_Site2["Trihalomethanes"])
plt.title('Potable water, site 2, Trihalomethanes')
plt.show()

plt.boxplot(Potable_Site3["Trihalomethanes"])
plt.title('Potable water, site 3, Trihalomethanes')
plt.show()


plt.boxplot(Potable_Site1["Turbidity"])
plt.title('Potable water, site 1, Turbidity')
plt.show()

plt.boxplot(Potable_Site2["Turbidity"])
plt.title('Potable water, site 2, Turbidity')
plt.show()

plt.boxplot(Potable_Site3["Turbidity"])
plt.title('Potable water, site 3, Turbidity')
plt.show()













