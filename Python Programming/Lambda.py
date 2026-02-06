# lambda functions - anonymous (nameless) functions , one line , simple operations

# syntax

# syntax lambda arguments: expression

# it can have any number of arguments
# must have only one expression
# the expression is automatically returned

# function - function name , arguments , return type , code ,

# normal function add 2 numbers

def add(a, b):
    return a+b

print(add(5,3))

#lambda function

add = lambda a,b: a+b
print(add(5,3))

# square of a number
square = lambda x : x*x
print(square(5))

# check even or add
check_even_odd = lambda x: "Even" if x % 2 == 0 else "Odd"

print(check_even_odd(10))
print(check_even_odd(7))

# find the max of 2 numbers

max = lambda a,b : a if a > b else b
print(max(10,30))

# filter, map and reduce in built functions in lambda

# filter - select data - filtering the data
# map - transform the data
# reduce - aggregate the data

# filter

numbers = [1,2,3,4,5,6]

evens = list(filter(lambda x: x%2 == 0, numbers ))
print((evens))

# filter the failed testcase

status  = ['pass', 'Fail', 'Pass', 'Fail']

failed = list(filter(lambda  s:s == 'Fail', status))
print((failed))

# filter the positive numbers

nums = [-5, 10, -3, 7, 0, 2]

positive_nums = list(filter(lambda x: x > 0, nums))

print(positive_nums)

# filter non-empty strings
data = ["hello", "", "world", "", "python"]

non_empty = list(filter(lambda x: x != "", data))

print(non_empty)


# reduce - aggerate - combining many values to a one single result

from functools import reduce

nums = [10,20,30,40]

print(reduce(lambda  x,y : x+ y , nums))

# multiply

product = reduce(lambda x, y: x * y, nums)
print(product)

# maximum value

maximum = reduce(lambda x, y: x if x > y else y, nums)
print(maximum)

# minimum value

minimum = reduce(lambda x, y: x if x < y else y, nums)
print(minimum)

# map - transform the data - the function is applied to every element

nums = [10, 20, 30, 40]

squares = list (map(lambda  x: x*x, nums))
print (squares)

#sorting in lambda
data = [(1, 3), (4, 1), (2, 2)]
sorteddata = sorted(data, key = lambda  x : x[1])
print(sorteddata)

marks = {"A": 75, "B":90, "C":60}
sorted_marks = dict(sorted(marks.items(), key=lambda x:x[1]))
print(sorted_marks)



