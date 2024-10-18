# Notes for certain things in pandas

## Separate a df into groups and making a new df

using groupby
example, grouping by boys and girls
```python
data = pd.read_csv("./SomeCSV")
sex_group = data.groupby("Sex")

# sex_group is a groupby object, not an actual dataframe
# turn it into a dataframe with get_group

boys = sex_group.get_group(1)
boys = sex_group.get_group(0)
```
the values given to get_group() are going to be the values that you find inside of the csv file. If it is a string use a string value, sex is usually stored as 1's and 0's. 0=female 1=male

### Another way to group

```python
data = pd.read_csv("./SomeCSV")

#if i want to separate by boys and girls
df_females = data[data["Sex"] == 0]
df_males = data[data["Sex"] == 1]

```

## Get numbers on a certain group in a df

Use groupby() and use an operation on it

```python
data = pd.read_csv("./SomeCSV")
sex_group = data.groupby("Sex")

sex_group.mean()
```
other options include .sum() .size() .apply()
