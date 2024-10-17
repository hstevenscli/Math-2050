import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


speed = [0.1, 17.5, 40, 48, 52, 69, 88]
lifespan = [2,8,70,1.5,25,12,28]

index = ['snail', 'pig', 'elephant', 'rabbit', 'giraffe', 'coyote', 'horse']

df = pd.DataFrame({'speed': speed, 'lifespan': lifespan}, index=index)

print(df)

# barplot = df.plot.bar()
# barplot = df.plot.bar(stacked=True)

# histogram = df.hist(bins=4)


# pie = df.plot.pie(subplots=True)
# pie = df.plot.pie()


# together

lineplot= df.plot.line()


# seperate lines
# lineplot= df.plot.line(subplots = True)


#scatter plot
# scatter = df.plot.scatter("speed", "lifespan")




data = pd.read_csv("./bike_buyers_clean.csv")

print(data)
# print(data["Gender"])
# print(data.Gender)

# plt.hist(data.Gender)

lbl = ["Male", "Female"]

print(data["Gender"].value_counts().plot.pie())

# data['sum'] = data['Cars'] + data['Age']
# print("HELLO", data['sum'])

data['Gender_m'] = data['Gender'].map({'Male':1, 'Female':0})
print(data["Gender_m"])
print("80", data["Gender_m"][80])
print("Males:", np.sum(data["Gender_m"]))
print("Total Entries:", len(data))

plt.show()
