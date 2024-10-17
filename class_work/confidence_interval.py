import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

data = pd.read_csv("./AAPL.csv")

p_mean = np.mean(data['Close'])

sample = data.sample(n=60)

#
cinterval = stats.t.interval(alpha=0.95, df=len(data)-1, loc=np.mean(sample["Close"]), scale=stats.sem(sample["Close"]))
print("confidence interval: ", cinterval)

lowerbound = cinterval[0]
upperbound = cinterval[1]
print()
print("lowerbound", lowerbound)
print("pmean", p_mean)
print("uppderbound", upperbound)

print()
if lowerbound <= p_mean <= upperbound:
    print("Pop mean is within the range of the CI")
##################### SPAM

data = pd.read_csv("./emails.csv")
data.describe()

# Portion of the spams

counts = data['spam'].value_counts()
spam_counts = counts.values[1]
not_spam_counts = counts.values[0]

print("Spam:", spam_counts)
print("Not spam:", not_spam_counts)
print("Proportion spam/notspam:", spam_counts/(not_spam_counts + spam_counts))

sample70 = data.sample(n=70)
sample100 = data.sample(n=100)
sample200 = data.sample(n=200)


cinterval = stats.t.interval(alpha=0.95, df=len(data)-1, loc=np.mean(sample["Close"]), scale=stats.sem(sample["Close"]))


