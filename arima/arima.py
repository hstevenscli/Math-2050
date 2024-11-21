import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pylab import rcParams
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.arima.model import ARIMA

# %matplotlib inline

df = pd.read_csv("./international-airline-passengers.csv")
print(df.head())

df.columns=["Month", "Sales"]
print(df.head())
print(df.describe())
df.set_index("Month", inplace=True)


rcParams["figure.figsize"] = 15, 7


print()
print(adfuller(df["Sales"]))
df["Sales First Difference"] = df["Sales"].diff()
print()



print(adfuller(df["Sales First Difference"].dropna()))


df["Sales Second Difference"] = df["Sales First Difference"].diff()


print(adfuller(df["Sales Second Difference"].dropna()))

df.plot()
# plt.show()
# df["Sales First Difference"].plot()
# plt.show()

# df["Sales Second Difference"].plot()
# plt.show()


# plot_acf(df["Sales First Difference"].dropna())
# plt.show()

# plot_pacf(df["Sales First Difference"].dropna())
# plt.show()


# This is the AIC
# Change the values in the order and see what happens
# If AIC goes up, it means its a little bit worse
model = ARIMA(df["Sales"], order=(4, 1, 4))
model_fit = model.fit()
print(model_fit.summary())


forecast = model_fit.forecast(steps = len(df))

# df['Sales'].plot()
forecast.plot()
# plt.show()


df["Seasonal First Difference"] = df["Sales"] - df["Sales"].shift(12)

print(df["Seasonal First Difference"])

plot_acf(df["Seasonal First Difference"].dropna())
plot_pacf(df["Seasonal First Difference"].dropna())

plt.show()
