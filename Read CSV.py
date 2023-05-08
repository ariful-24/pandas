

"""Read CSV Files
A simple way to store big data sets is to use CSV files (comma separated files).

CSV files contains plain text and is a well know format that can be read by everyone including Pandas.

In our examples we will be using a CSV file called 'data.csv'."""

import pandas as pd

df=pd.read_csv('Cleaning Data/data.csv')
# print(df)
# print(df.to_string())

"""max_rows
The number of rows returned is defined in Pandas option settings.

You can check your system's maximum rows with the pd.options.display.max_rows statement."""

print(pd.options.display.max_rows)