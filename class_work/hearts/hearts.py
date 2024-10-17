import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


data = pd.read_csv("./heart_processed_cleveland.csv")
data.columns = [
    "age",
    "sex",
    "cp",
    "trestbps",
    "chol",
    "fbs",
    "restecg",
    "thalach",
    "exang",
    "oldpeak",
    "slope ",
    "ca",
    "thal",
    "num"
]
# print(data)

df = pd.DataFrame(data)
summary = df.describe()

# print(df.describe())

print(df.describe())


# lineplot = summary.plot.line()


male = df[df['sex']==1]
print("MALE", male.describe())


female = df[df['sex']==0]
print("FEMALE", female.describe())

c_m = [np.mean(male['chol']), np.mean(female['chol'])]
print(c_m)

labels = ["male_chol", "female_chol"]

# plt.bar(labels, c_m)

c_s = [np.std(male["chol"], ddof=1), np.std(female["chol"], ddof=1)]

plt.bar(labels, c_s)

plt.show()
