import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd


y_1990 = [2.5,2.5,2.49,2.53,2.46,2.5,2.47,2.53,2.51,2.49,2.48]
y_1995 = [2.52,2.54,2.5,2.48,2.52,2.5,2.49,2.53,2.48,2.55,2.49]
y_2000 = [2.5,2.48,2.49,2.5,2.48,2.52,2.51,2.49,2.51,2.5,2.52]


g1 = ['1990']*len(y_1990)
g2 = ['1995']*len(y_1995)
g3 = ['2000']*len(y_2000)

treatments = g1+g2+g3

value = y_1990 + y_1995 + y_2000

lis = list(zip(value, treatments))

df = pd.DataFrame(lis, columns = [ 'value', 'treatments' ])

# get ANOVA table as R like output

# Ordinary Least Squares (OLS) model
model = ols('value ~ C(treatments)', data=df).fit()
anova_table = sm.stats.anova_lm(model, typ=2)
print(anova_table)


tukey =  pairwise_tukeyhsd(endog=df['value'], groups=df['treatments'], alpha=.01)
print(tukey)
