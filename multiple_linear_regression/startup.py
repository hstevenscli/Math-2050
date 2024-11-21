import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
import statsmodels.api as smf

# How to get values for each specific state instead of having a state category,
# Went from state category to a category for each state with a 1 in the actual state
# and 0's in the other states

startup_df = pd.read_csv('./50_Startups.csv')

x = startup_df.iloc[:,:4]
y = startup_df.iloc[:,4]

print(x)
print(y)

dummies = pd.get_dummies(x['State'])
print(dummies)

x = pd.concat([x, dummies], axis=1)
print(x)

x = x.drop('State', axis=1)
print(x)
