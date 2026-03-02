import  pandas as pd

from Numpy.NumpyManipulate import result

"""
Creating data

Selecting data

Filtering data

Cleaning data

Transforming columns

Aggregating data

Merging datasets

Exporting results
"""

# creating data DFR using the dictionary

import pandas as pd

data = {
    "Name": ["Ram", "Sam", "John", "Priya"],
    "Age": [25, 30, 28, 22],
    "Salary": [40000, 50000, 45000, 38000]
}

df = pd.DataFrame(data)
print(df)

# Selecting single data
print(df["Age"])

# select multiple data
print(df[["Age", "Name"]])

# Select rows using iloc or location
print(df.loc[0:2]) # nth index
print(df.loc[0:1]) # n-1 index


# filtering based on the conditions
import pandas as pd
df = pd.DataFrame(data)
print(df)

# employees with salary > 40000
filtered = df[df["Salary"] > 40000]
print(filtered)
filtered = df[df["Salary"] <= 40000]
print(filtered)

# multiple conditions
filtered = df[(df["Salary"] > 40000) & (df["Age"] > 25)]
print(filtered)

# Cleaning data - adding or modifying the columns

import pandas as pd

data = {
    "Name": ["Ram", "Sam", "John"],
    "Salary": [40000, 50000, 45000]
}

df = pd.DataFrame(data)

# add the bonus column
df["Bonus"] = df["Salary"]*0.10
print(df)

# modify the current column - increase the salary
df["Salary"] = df["Salary"] + 2000

print(df)

#Sorthing Data ascending or descending

import pandas as pd

data = {
    "Name": ["Ram", "Sam", "John", "Priya"],
    "Age": [25, 30, 28, 22],
    "Salary": [40000, 50000, 45000, 38000]
}

df = pd.DataFrame(data)
print(df)

# sort the salary in ascending order
sorted_df = df.sort_values("Salary", ascending=False)
print(sorted_df)

# handling missing value

import pandas as pd
import numpy as np

data = {
    "Name": ["Ram", "Sam", None],
    "Age": [25, np.nan, 30]
}

df = pd.DataFrame(data)

print("missing values")
print(df.isnull())

# Replace all missing values (Nan, None, NaT) in
df_filled = df.fillna(0)
print(df_filled)

import pandas as pd

data = {
    "Age": [25, None, 30],
    "Salary": [50000, 60000, None]
}

df = pd.DataFrame(data)
print(df)

df = df.fillna(0)
print(df)

# Drop missing rows
import pandas as pd

# Drop missing rows
data = {
    "Name": ["A", "B", "C"],
    "Age": [25, None, 30],
    "Salary": [50000, 60000, None]
}

df = pd.DataFrame(data)
print(df)

df = df.dropna()
print(df)

# GroupBy and Aggregation

import pandas as pd

data = {
    "City": ["Delhi", "Mumbai", "Delhi", "Chennai"],
    "Salary": [40000, 50000, 45000, 38000]
}

df = pd.DataFrame(data)

# average salary per city
result = df.groupby("City")["Salary"].mean()
print(result)

# multiple aggregation
result = df.groupby("City")["Salary"].agg(["mean", "sum", "count"])
print(result)

# Merging of data frames

import pandas as pd

df1 = pd.DataFrame({
    "ID": [1, 2],
    "Name": ["Ram", "Sam"]
})

df2 = pd.DataFrame({
    "ID": [1, 2],
    "Salary": [40000, 50000]
})

merged = pd.merge(df1, df2)
print(merged)

# Removing Duplicates

import pandas as pd

data = {
    "Name": ["Ram", "Sam", "Ram"],
    "Salary": [40000, 50000, 40000]
}

df = pd.DataFrame(data)

print("Before removing duplicates:")
print(df)

df = df.drop_duplicates()

print("After removing duplicates:")
print(df)