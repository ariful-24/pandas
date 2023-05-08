

"""Viewing the Data
One of the most used method for getting a quick overview of the DataFrame, is the head() method.

The head() method returns the headers and a specified number of rows, starting from the top."""

import pandas as pd

df = pd.read_csv('Cleaning Data/data.csv')
# print(df.head(10))
#if the number of rows is not specified, the head() method will return the top 5 rows.

# print(df.head())

#There is also a tail() method for viewing the last rows of the DataFrame.

#print(df.tail())

"""Info About the Data
The DataFrames object has a method called info(), that gives you more information about the data set."""
print(df.info())