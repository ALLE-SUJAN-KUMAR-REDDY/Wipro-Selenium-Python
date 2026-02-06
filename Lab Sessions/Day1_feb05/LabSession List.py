#1.Write a Python program to get the largest number from a list.
numbers = [10, 45, 23, 89, 12]

largest = max(numbers)
print("Largest number is:", largest)


#2.remove the even numbers from the list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd_numbers = []

for num in numbers:
    if num % 2 != 0:
        odd_numbers.append(num)

print("List after removing even numbers:", odd_numbers)


#3.multiply the items in the list
numbers = [2, 3, 4, 5]

result = 1

for num in numbers:
    result = result * num

print("Multiplication of list items:", result)

