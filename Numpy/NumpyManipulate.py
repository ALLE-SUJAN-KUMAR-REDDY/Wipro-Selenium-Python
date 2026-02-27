import numpy as np
from numpy.ma.core import transpose

# Changing Shape

# reshape

a = np.arange(1,7)
print("Original array", a)
# reshape the array
reshaped = a.reshape(2,3)
print(reshaped)

# flat = return 1D iterator over the array

arr = np.array([[1,2], [3,4]])
for x in arr.flat:
    print(x)


# flatten - Returns a copy of the array collapsed into one dimension.

arr = np.array([[1,2],[3,4]])
print(arr)
at_arr = arr.flatten()
print(at_arr)

# ravel() - Returns a flattened array
arr = np.array([[1,2],[3,4]])
print(arr)
at_arr = arr.ravel()
print(at_arr)

# pad() - Returns a padded array with shape increased according to pad_width
arr = np.array([[1,2,3]])
padded = np.pad(arr, 2,'constant')
print(padded)

# Transpose operations
'''
1 transpose

Permutes the dimensions of an array
2 ndarray.T

Same as self.transpose()

3 rollaxis

Rolls the specified axis backwards

4 swapaxes

Interchanges the two axes of an array

5 moveaxis()

Move axes of an array to new positions
'''

#1 transpose
# reorders the dimensions of an array.

arr = np.array([[1,2,3],[4,5,6]])
print(arr)
transpose = arr.transpose()
print(transpose)

# 2 ndarray.T
arr = np.array([[1,2,3],[4,5,6]])
print(arr)
transpose = arr.T
print(transpose)

# rollaxis - Rolls the specified axis backwards

arr = np.zeros((2,3,4))
print(arr)

# 2 is the blocks - axis 0
# 3 - rows - axis 1
# 4 columns - axis 2

#(0,1,2) - (2,3,4)
#(2,0,1) - (4,2,3)

# arr[blocks][row][column]

new_arr = np.rollaxis(arr, 2)
print(new_arr)

#swapaxes() - interchanges two axes of an array
arr = np.zeros((2,3,4))
print(arr)

new_arr = np.swapaxes(arr, 0, 2)
print(new_arr)
# (4,3,2)

# moveaxis() - Moves specified axes to new positions
arr = np.zeros((2,3,4))
print(arr)
new_arr = np.moveaxis(arr, 0,-1)
print(new_arr)

# (3,4,2)