#1.Write a Python function to check whether a number falls within a given range.

num = int(input("Enter a number: "))
for i in range(10, 21):
    if num == i:
        print("Number is within the range")
        break
else:
    print("Number is Not within the range")


#2.Write a Python function to Print even numbers from 1 to 50
def print_even_numbers():
    for i in range(1,51):
        print(i)

print_even_numbers()

#3.Write a Python function to Sum of numbers from 1 to 100
def sum_numbers():
    total = 0
    for i in range(1, 101):
        total += i
    print("Sum:", total)

sum_numbers()

#4.Print all numbers divisible by 5 between 1 and 100
for i in range(5, 101, 5):
    print(i)

#5.Create a list of numbers from 50 to 100 with a step of 5
numbers = list(range(50, 101, 5))
print(numbers)

#6.Print the square of each number from 1 to 10.
for i in range(1, 11):
    print(i * i)

#7.Print numbers between -10 and 10
for i in range(-10, 11):
    print(i)