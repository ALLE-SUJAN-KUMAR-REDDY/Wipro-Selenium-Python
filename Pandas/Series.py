# Pandas - high performance data manipulation and data analysis tool
# 2008 Mckinnley
# data frame object
# list , csv , json , pdf
from operator import index

# series - A one-dimensional labeled homogenous array, size immutable.
# DataFrames  2 A two-dimensional labeled, size-mutable tabular structure with potentially heterogeneously

import pandas as pd
# creation of series Out of lists
data =['Steve', '35', 'Male', '3.5']
series = pd.Series(data, index= ['Name', 'Age', 'Gender', 'Rating'])
print(series)

# create series using custom index
data = [100, 200, 300]
s = pd.Series(data, index = ['a', 'b', 'c'])
print(s)

# create series from dictionary
data = {'a':1, 'b':2, 'c':3}
s = pd.Series(data)
print(s)

# create series Numpy array
import  numpy as  np

arr = np.array([5, 10, 15])
s = pd.Series(arr)
print(s)

# create a empty series

s = pd.Series(dtype=float)
print(s)

# Create Series with Specific Data Type

import pandas as pd

data = [1, 2, 3]
s = pd.Series(data, dtype='float')

print(s)

