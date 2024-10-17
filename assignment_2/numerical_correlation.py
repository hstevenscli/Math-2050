import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


pres = pd.read_csv("./3_r_10-1.csv")
# print(pres)

print("MEAN:\n", pres.mean())
print("MEDIAN:\n", pres.median())

quartiles = pres.quantile([0.25, 0.50, 0.75])

print("Quartiles:\n", quartiles)

print("MAX:\n", pres.max())
print("MIN:\n", pres.min())

std = pres.std()
print("STD DEVIATION\n", std)

print(pres.describe())

#IQR
Q3 = pres.quantile(0.75)
Q1 = pres.quantile(0.25)
IQR = Q3 - Q1
print("IQr:\n", IQR)


lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Filter out outliers
filtered_pres = pres[~((pres < lower_bound) | (pres > upper_bound)).any(axis=1)]

# Optionally, you can compare the original data with the filtered one
print("Original data shape:", pres.shape)
print("Filtered data shape:", filtered_pres.shape)
print("Outliers are:", 8445, 5433)

pres.boxplot()
plt.savefig("./charts/boxplot.png")
plt.close()


################# SECOND DATA SET
print()
print()
print("-------------------------------------------------------------------------")

x = [ 5, 6, 7, 7, 8, 8, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, ]

y = [ 4.2, 5, 5.2, 5.9, 6, 6.2, 6.1, 6.9, 7.2, 8, 8.3, 7.4, 8.4, 7.8, 8.5, 9.5, ]

df = pd.DataFrame({"x": x, "y": y})
print(df)

df.plot.scatter(x="x", y="y", title="Scatter Diagram")
plt.savefig("./charts/generic_scatter.png")
plt.close()

plt.xlim(0, 30)
plt.ylim(0, 20)

correlation = df["x"].corr(df["y"])
print(correlation)

df2 = df * 2

df2.plot.scatter(x="x", y="y", title="Scatter Diagram")
plt.savefig("./charts/generic_scatter_times_2.png")
plt.close()

plt.xlim(0, 30)
plt.ylim(0, 20)
# plt.show()

correlation2 = df2["x"].corr(df["y"])
print(correlation2)


############### LYME DISEASE

print()
print()
print()

# month = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ]
months = ['J', 'F', 'M', 'A', 'M', 'J', 'J', 'A', 'S', 'O', 'N', 'D']
lyme_disease = [3, 2, 2, 4, 5, 15, 22, 13, 6, 5, 4, 1]
drowning_deaths = [0, 1, 2, 1, 2, 9, 16, 5, 3, 3, 1, 0]

lymedf = pd.DataFrame({
    "Month": months,
    "Lyme Cases": lyme_disease,
    "Drowning Deaths": drowning_deaths
})

lymedf.plot.scatter(x='Lyme Cases', y='Drowning Deaths', title='Scatter Diagram: Lyme Cases vs Drowning Deaths')
plt.savefig("./charts/scatter_lyme_drowning.png")
plt.close()
lymecorrelation = lymedf["Lyme Cases"].corr(lymedf["Drowning Deaths"])
print("Correlation Co between lyme and drowning:\n", lymecorrelation)


##################### MRI COUNT

data_mri = {
    'Gender': ['Female', 'Female', 'Female', 'Female', 'Female', 'Female', 'Female', 'Female', 'Female', 'Female', 'Male', 'Male', 'Male', 'Male', 'Male', 'Male', 'Male', 'Male', 'Male', 'Male'],
    'MRI Count': [816932, 951545, 991305, 833868, 856472, 852244, 790619, 866662, 857782, 948066, 949395, 1001121, 1038437, 965353, 955466, 1079549, 924059, 955003, 935494, 949589], 
    'IQ': [133, 137, 138, 132, 140, 132, 135, 130, 133, 133, 140, 140, 139, 133, 133, 141, 135, 139, 141, 144]
}

# Create a DataFrame
df_mri = pd.DataFrame(data_mri)
df_mri.plot.scatter(x="MRI Count", y="IQ", title="Scatter Diagram: MRI Count and IQ")
plt.savefig("./charts/scatter_mri_count.png")
plt.close()
mri_correlation = df_mri["MRI Count"].corr(df_mri["IQ"])
print("Correlation between mri count and IQ:", mri_correlation)

# Display the DataFrame
print(df_mri)

df_female = df_mri[df_mri['Gender'] == 'Female']
df_male = df_mri[df_mri['Gender'] == 'Male']

female_correlation = df_female["MRI Count"].corr(df_female["IQ"])
male_correlation = df_male["MRI Count"].corr(df_male["IQ"])

print("Male mri count and iq correlation:", male_correlation)
print("Female mri count and iq correlation:", female_correlation)
