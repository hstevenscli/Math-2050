import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
import statsmodels.api as smf
from sklearn.model_selection import train_test_split
from sklearn import metrics

df = pd.read_csv('./advertising.csv')

cor = df.corr()

x = df[['TV', 'Radio']]
y = df.Sales

x = smf.add_constant(x)

model = smf.OLS(y, x).fit()

print(model.summary())

prediction = model.predict(x)









df2 = { 'y':df.Sales, 'pred': prediction }

df2 = pd.DataFrame(df2)

df2['error'] = df2.y-df2.pred

smf.qqplot(df2.error)

plt.scatter(y, df2.error)

########################


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.3, random_state=100)

mlr = LinearRegression()

mlr.fit(x_train, y_train)


print(mlr.intercept_)

print(mlr.coef_)

y_pred = mlr.predict(x_test)

df3 = {'y': y_test, 'pred': y_pred}

df3 = pd.DataFrame(df3)

MAE = metrics.mean_absolute_error(y_test, y_pred)
MSE = metrics.mean_squared_error(y_test, y_pred)

RMSE = np.sqrt(MSE)

