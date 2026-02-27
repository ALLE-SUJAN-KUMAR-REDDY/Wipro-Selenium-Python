'''
Using numpy.array() Function
Using numpy.zeros() Function
Using numpy.ones() Function
Using numpy.arange() Function
Using numpy.linspace() Function
Using numpy.random.rand() Function
Using numpy.empty() Function
Using numpy.full() Function
numpy.eye()
numpy
'''
import numpy
import numpy as np
from jinja2.runtime import identity

# 1D array
# This function creates a Numpy array with zeros
# By default , the data type is float
a = np.zeros(5)
print(a)


# using numpy.ones() Function
a = np.ones(5)
print(a)

# 2D array of ones
a_2D = np.zeros((4,3))
print(a_2D)

# 2D array of ones
a_2D = np.ones((4,3))
print(a_2D)


# with only the stop
a = np.arange(10)
print(a)

# providing the start , stop and step values
a = np.arange(1,10,1)
print(a)

# Using numpy.linespace() Function
# linspace() is used to generate evenly spaced numbers over a specified interval.
a = np.linspace(0, 10,5,True)
print(a)

# exclude the last number
a = np.linspace(0, 10,5,False)
print(a)

# Using numpy.random.rand() Function
# Generates an array of the specified shaspe with random values between 0 and 2
# if no arguments is provided, it returns a single random float value.

a = np.random.rand(5)
print(a)

# 2D
a = np.random.rand(2,3)
print(a)

# 3D
a = np.random.rand(2,3,4)
print(a)

# Using numpy.empty() Function
# 2D
# This function initializes an array without initializing its elements;
# the content of the array is arbitary and may vary

a = np.empty((2,3))
print(a)

# Using numpy.full() Function
# filled entirely with the value 5
a = np.full((2,3), 5)
print(a)

# numpy.eye()
# The Numpy eye() function is used to
# create a 2D array with ones on the diagonal and zeros in all other positions

identity_matrix = np.eye((4))
print(identity_matrix)

# numpy.identity - function is used generate a square identity matrix
identity_matrix = np.identity((5))
print(identity_matrix)

# numpy.diag
# In case of 2D array, the function extracts the diagonal elements of the array.
# In case of 1D array, the function a square diagonal matrix with the elements of the
# the diagonal values and zeros in remaining positions

Matrix = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
print("Original matrix", Matrix)
Diagonal_elements = np.diag(Matrix)
print("Diagonal elements", Diagonal_elements)
