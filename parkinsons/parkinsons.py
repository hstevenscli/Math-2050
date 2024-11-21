# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 11:07:25 2024

@author: Hunter
"""
import sklearn
import seaborn as sn
import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import mathplotlib.pyplot as plt

x_train, x_test, y_train, y_test = train_test_split(new_x, df1.TenYearCHD, test_size)


logreg = LogisticRegression()
logreg.fit(x_train,y_train)
y_pred = logreg.predict(x_test)


sklearn.metrics.accuracy_score(y_test, y_pred)


cm = confusion_matrix(y_test,y_pred)
conf_matrix=pd.DataFrame(data=cm, columns=["Predicted:0", "Predicted:1"])
plt.figure(figsize = (8,5))
sn.heatmap(conf_matrix, annot=True, fmt='d', cmap="YlGnBu")





df = pd.read_csv("C:/Users/Hunter/school/MATH-2050/parkinsons/parkinsons.csv")

df = df.drop('name', axis=1)
df = df.drop('status', axis=1)

print(df)


