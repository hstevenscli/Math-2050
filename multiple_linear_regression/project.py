import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
import statsmodels.api as smf
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import r2_score

df_bodyfat = pd.read_csv("./BodyFat.csv")

# Separate the target variable (PercentBodyFat) and the explanatory variables
x = df_bodyfat.drop(columns=["PercentBodyFat", "BodyDensity"])  # Exclude BodyDensity
y = df_bodyfat["PercentBodyFat"]

# Add a constant to the model (for the intercept)
x = smf.add_constant(x)

# Fit a linear regression model using statsmodels
model = smf.OLS(y, x).fit()

print(model.summary())

prediction = model.predict(x)


df2 = { 'y':df_bodyfat.PercentBodyFat, 'pred': prediction }

df2 = pd.DataFrame(df2)

df2['error'] = df2.y-df2.pred

smf.qqplot(df2.error)

plt.scatter(y, df2.error)

plt.show()

#################################

# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.3, random_state=100)

mlr = LinearRegression()

mlr.fit(x_train, y_train)

print(mlr.intercept_)

print(mlr.coef_)

y_pred = mlr.predict(x_test)

df3 = {'y': y_test, 'pred': y_pred}

df3 = pd.DataFrame(df3)

print(df3)

MAE = metrics.mean_absolute_error(y_test, y_pred)
MSE = metrics.mean_squared_error(y_test, y_pred)

RMSE = np.sqrt(MSE)

# Predict and calculate R^2 on the test set
# y_pred = model.predict(x_test)
r2 = r2_score(y_test, y_pred)

# Print the model summary and R^2 value
print("R^2 on test set:", r2)
print("Mean Absolute Error:", MAE)
print("Mean Squared Error:", MSE)
print("RMSE", RMSE)


print("####################PART 2###########################################")
############################################## MPG

mpg_df = pd.read_csv('./auto-mpg.csv')

x = mpg_df.iloc[:,:8]
y = mpg_df.iloc[:,1]
x = x.drop(columns=["mpg"])

# print(x)
# print(y)

dummies = pd.get_dummies(x['origin'])
# print(dummies)

x = pd.concat([x, dummies], axis=1)
# print(x)

x = x.drop('origin', axis=1)
# print(x)
x.columns.values[6] = "USA"
x.columns.values[7] = "Europe"
x.columns.values[8] = "Asia"
print(x)

x = smf.add_constant(x)

model = smf.OLS(y, x).fit()

print(model.summary())

prediction = model.predict(x)

df2 = { 'y': mpg_df.mpg, 'pred': prediction }

df2 = pd.DataFrame(df2)

df2['error'] = df2.y-df2.pred

smf.qqplot(df2.error)

plt.scatter(y, df2.error)

plt.show()

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.3, random_state=100)

mlr = LinearRegression()

mlr.fit(x_train, y_train)

print(mlr.intercept_)

print(mlr.coef_)

y_pred = mlr.predict(x_test)

df3 = {'y': y_test, 'pred': y_pred}

df3 = pd.DataFrame(df3)
r2 = r2_score(y_test, y_pred)

print(df3)

MAE = metrics.mean_absolute_error(y_test, y_pred)
MSE = metrics.mean_squared_error(y_test, y_pred)
RMSE = np.sqrt(MSE)

print("R^2 on test set mpg:", r2)
print("MAE:", MAE)
print("MSE:", MSE)
print("RMSE:", RMSE)
