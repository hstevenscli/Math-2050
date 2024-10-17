import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

SAVE = False
num_tornados = [
    22,
    31,
    30,
    35,
    24,
    6
]

tornado_duration = [
    [1, 1, 5, 1, 1, 6, 4, 10, 5, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 30, 1, 9],
    [16, 13, 9, 8, 13, 10, 15, 1, 17, 23, 10, 8, 12, 5, 20, 31, 12, 5, 30, 13, 7, 1, 5, 13, 1, 2, 5, 10, 1, 20, 5],
    [7, 15, 2, 10, 23, 10, 7, 12, 8, 1, 8, 19, 5, 10, 15, 20, 10, 13, 20, 15, 13, 14, 1, 4, 2, 15, 30, 91, 11, 5],
    [9, 20, 8, 16, 26, 36, 10, 20, 50, 17, 26, 31, 21, 30, 23, 28, 23, 18, 35, 35, 15, 25, 30, 15, 22, 18, 58, 19, 23, 31, 13, 26, 40, 14, 11],
    [120, 23, 23, 42, 47, 25, 22, 22, 34, 50, 38, 28, 39, 29, 28, 25, 34, 16, 40, 55, 124, 30, 30, 31],
    [37, 69, 23, 52, 61, 122]
]

tornado_deaths = [
    0,
    0,
    14,
    32,
    129,
    130
]

tornado_deaths_community = [
    99,
    77,
    63,
    56,
    10
]

t_duration_all = []
for f in tornado_duration:
    for time in f:
        t_duration_all.append(time)
print("tdurationall:", t_duration_all)
scales = ["F0", "F1", "F2", "F3", "F4", "F5",]

df = pd.DataFrame({"Number of Tornados": num_tornados}, index=scales)
pie = df.plot.pie(subplots=True)
plt.savefig("./charts/pie_number_of_tornados.png")
plt.close()

dfhist = pd.DataFrame({"Tornado Distribution": t_duration_all})
historgram = dfhist.hist()
for ax in historgram.flatten():
    ax.set_xlabel("Duration in minutes")
    ax.set_ylabel("Number of Tornados")
plt.savefig("./charts/hist_time_and_number_distribution.png")
plt.close()

df0 = pd.DataFrame({"Duration at F0": tornado_duration[0]})
hist = df0.hist()
for ax in hist.flatten():
    ax.set_xlabel("Duration in minutes")
    ax.set_ylabel("Number of Tornados")
plt.savefig("./charts/hist_dur_by_fscale0.png")
plt.close()


df1 = pd.DataFrame({"Duration at F1": tornado_duration[1]})
hist = df1.hist()
for ax in hist.flatten():
    ax.set_xlabel("Duration in minutes")
    ax.set_ylabel("Number of Tornados")
plt.savefig("./charts/hist_dur_by_fscale1.png")
plt.close()


df2 = pd.DataFrame({"Duration at F2": tornado_duration[2]})
hist = df2.hist()
for ax in hist.flatten():
    ax.set_xlabel("Duration in minutes")
    ax.set_ylabel("Number of Tornados")
plt.savefig("./charts/hist_dur_by_fscale2.png")
plt.close()

df3 = pd.DataFrame({"Duration at F3": tornado_duration[3]})
hist = df3.hist()
for ax in hist.flatten():
    ax.set_xlabel("Duration in minutes")
    ax.set_ylabel("Number of Tornados")
plt.savefig("./charts/hist_dur_by_fscale3.png")
plt.close()

df4 = pd.DataFrame({"Duration at F4": tornado_duration[4]})
hist = df4.hist()
for ax in hist.flatten():
    ax.set_xlabel("Duration in minutes")
    ax.set_ylabel("Number of Tornados")
plt.savefig("./charts/hist_dur_by_fscale4.png")
plt.close()

df5 = pd.DataFrame({"Duration at F5": tornado_duration[5]})
hist = df5.hist()
for ax in hist.flatten():
    ax.set_xlabel("Duration in minutes")
    ax.set_ylabel("Number of Tornados")
plt.savefig("./charts/hist_dur_by_fscale5.png")
plt.close()


dfbar = pd.DataFrame({"Tornado Deaths by F-Scale": tornado_deaths, 'F-Scale':["F0", "F1", "F2", "F3", "F4", "F5",]})
bar = dfbar.plot.bar(x="F-Scale", color="red")
plt.savefig("./charts/bar_deaths_by_fscale.png")
plt.close()

dfbar1 = pd.DataFrame({"Tornado Deaths by Community Size": tornado_deaths_community, "Community Size":["Rural", "S Community", "S City", "M City", "L City"]})
bar = dfbar1.plot.bar(x="Community Size", color="green")
plt.savefig("./charts/bar_deaths_by_community.png")
plt.close()
