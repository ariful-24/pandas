

"""What is a Series?
A Pandas Series is like a column in a table.

It is a one-dimensional array holding data of any type."""

#Create a simple Pandas Series from a list:

import pandas as pd

a  = [1,7,2]
myvar = pd.Series(a)
print(myvar)

print(myvar[0])


"""Labels
If nothing else is specified, the values are labeled with their index number. First value has index 0, second value has index 1 etc.

This label can be used to access a specified value."""

"""Create Labels
With the index argument, you can name your own labels."""

a = [1, 7, 2]
myvar = pd.Series(a, index= ["x", "y", "z"])
print(myvar)


"""Key/Value Objects as Series
You can also use a key/value object, like a dictionary, when creating a Series."""

calories = { "day1":420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)
print(myvar)


#Create a Series using only data from "day1" and "day2":
calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories, index = ["day1", "day2"])

print(myvar)


"""DataFrames
Data sets in Pandas are usually multi-dimensional tables, called DataFrames.
Series is like a column, a DataFrame is the whole table."""


data = {
    "calories": [420,380,390],
    "duration": [50,40,45]
}

myvar = pd.DataFrame(data)
print(myvar)
