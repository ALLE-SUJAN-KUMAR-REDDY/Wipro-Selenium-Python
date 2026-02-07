# 1.1.Write a Python function to sum all the numbers in a list.
def sum_of_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

my_list = [10, 20, 30, 40]
result = sum_of_list(my_list)
print(result)

# 2.Write a Python function to find the maximum of three numbers.
def max_of_three(a, b, c):
    return max(a, b, c)

print(max_of_three(10, 25, 15))


