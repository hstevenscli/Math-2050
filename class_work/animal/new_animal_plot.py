import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


speed = [0.1, 17.5, 40, 48, 52, 69, 88]
lifespan = [2,8,70,1.5,25,12,28]

index = ['snail', 'pig', 'elephant', 'rabbit', 'giraffe', 'coyote', 'horse']

df = pd.DataFrame({'speed': speed,
                   'lifespan': lifespan}, index=index)

print(df)

mean_speed = np.mean(speed)
median = np.median(speed)
sd_speed = np.std(speed, ddof=1)

quantile = np.quantile(speed, .25)

print("mean", mean_speed)
print("sd speed", sd_speed)
print("quantile", quantile)
print("median", median)



# df.boxplot(["speed", "lifespan"])

# plt.boxplot(df.speed)
sns.kdeplot(df.speed)

plt.show()
