import pandas as pd

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}
myvar = pd.DataFrame(mydataset)
print(myvar)

a = [1, 7, 2]
myvar = pd.Series(a)
print(myvar)

a = [1, 7, 2]
myvar = pd.Series(a, index=["x", "y", "z"])
print(myvar)
print(myvar["y"])

calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories)
print(myvar)

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
myvar = pd.DataFrame(data)
print(myvar)
#refer to the row index:
print(myvar.loc[0])

#use a list of indexes:
print(myvar.loc[[0, 1]])

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
df = pd.DataFrame(data, index=["day1", "day2", "day3"])
print(df)
#refer to the named index:
print(df.loc["day2"])

# Read from CSV file
df = pd.read_csv('diabetes.tab.txt', sep='\t')
print(df)

print(pd.options.display.max_rows)
pd.options.display.max_rows = 15
print(df.head(10))
print(df.tail(10))
print(df.info())
print(df["AGE"].mean())
print(df["AGE"].median())
print(df.corr())
