

"""What is a DataFrame?
A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns."""

import pandas as pd

data={
    "calories": [420,380,390],
    "duration" : [50,40,45]
}


df = pd.DataFrame(data)
print(df)


"""Locate Row
As you can see from the result above, the DataFrame is like a table with rows and columns.

Pandas use the loc attribute to return one or more specified row(s)"""

print(df.loc[0])
print(df.loc[[0,1]])


"""Named Indexes
With the index argument, you can name your own indexes."""

df = pd.DataFrame(data, index= ["day1", "day2", "day3"])
print(df)


print(df.loc["day2"])



"""Load Files Into a DataFrame
If your data sets are stored in a file, Pandas can load them into a DataFrame."""

df = pd.read_csv('Cleaning Data/data.csv')

print(df)
