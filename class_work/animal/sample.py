import random
import matplotlib.pyplot as plt
import scipy.stats as stats

list_1 = [20.5, 40.5, 30.5, 50.5, 70.5]

simple_list1 = random.sample(list_1, 4)
# print(simple_list1)

simple_list3 = random.choices(list_1, k=100)
# print(simple_list3)

random.seed(100)
list2 = [1,2,3,4,5,6]
x = random.choices(list2, k=1000)
plt.hist(x)
plt.close()


data = stats.poisson.rvs(20,.2,size=1000)
stats.probplot(data, plot = plt)


plt.show()
