import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline

df=pd.read_csv("./international-airline-passengers.csv")
df.head()

# Updating the header
df.columns=["Month","Sales"]
df.head()
df.describe()

 

df['Month'] = pd.to_datetime(df['Month']).apply(lambda x: x.date())


df.set_index('Month',inplace=True)


# Check the type of the index before conversion
# print("Index type before conversion:", type(df.index[0]))

# df.index = pd.to_datetime(df.index)

# print("Index type before conversion:", type(df.index[0]))

from pylab import rcParams
rcParams['figure.figsize'] = 15, 7
df.plot()

from statsmodels.tsa.stattools import adfuller
test_result=adfuller(df['Sales'])

adfuller(df['Sales'])
#Ho: It is non-stationary#H1: It is stationary

df['Sales First Difference'] = df['Sales'] - df['Sales'].shift(1)
df['Seasonal First Difference']=df['Sales']-df['Sales'].shift(12)
df.head()

# Again testing if data is stationary
adfuller(df['Seasonal First Difference'].dropna())

df['Seasonal First Difference'].plot()


from statsmodels.graphics.tsaplots import plot_acf,plot_pacf
import statsmodels.api as sm
fig = plt.figure(figsize=(12,8))
ax1 = fig.add_subplot(211)
fig = sm.graphics.tsa.plot_acf(df['Seasonal First Difference'].dropna(),lags=40,ax=ax1)
ax2 = fig.add_subplot(212)
fig = sm.graphics.tsa.plot_pacf(df['Seasonal First Difference'].dropna(),lags=40,ax=ax2)

from statsmodels.tsa.arima.model import ARIMA
model=ARIMA(df['Sales'],order=(3,1,2))
model_fit=model.fit()
model_fit.summary()

import statsmodels.api as sm
model=sm.tsa.statespace.SARIMAX(df['Sales'],order=(1, 1, 1),seasonal_order=(1,1,1,12))
results=model.fit()
df['forecast']=results.predict(start=110,end=144,dynamic=True)
df[['Sales','forecast']].plot(figsize=(12,8))

plt.show()

import statsmodels.api as sm
model=sm.tsa.statespace.SARIMAX(df['Sales'],order=(1, 1, 1),seasonal_order=(1,1,1,12))
results=model.fit()
df['forecast']=results.predict(start=90,end=144,dynamic=True)
df[['Sales','forecast']].plot(figsize=(12,8))


from pandas.tseries.offsets import DateOffset
future_dates=[df.index[-1]+ DateOffset(months=x)for x in range(0,24)]
future_datest_df=pd.DataFrame(index=future_dates[1:],columns=df.columns)

future_datest_df.tail()

future_df=pd.concat([df,future_datest_df])

future_df['forecast'] = results.predict(start = 141, end = 160, dynamic= True)
future_df[['Sales', 'forecast']].plot(figsize=(12, 8))
