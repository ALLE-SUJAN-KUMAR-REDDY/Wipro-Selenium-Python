# 1.Write a generator to generate numbers from 1 to N.

def number_generator(n):
    for i in range(1, n + 1):
        yield i


N = int(input("Enter value of N: "))

for num in number_generator(N):
    print(num)


# 2.Create a generator to generate even numbers only.

def even_number_generator(n):
    for i in range(2, n + 1, 2):
        yield i


# Demonstration
N = int(input("Enter the limit: "))

for num in even_number_generator(N):
    print(num)

# 3.Write a generator to read a file line by line.

def read_file_line_by_line(filename):
    with open(filename, 'r') as file:
        for line in file:
            yield line.strip()   # removes newline character


file_path = "C://Users//Sujan Kumar Reddy//PycharmProjects//PythonAdvancedProgramming//Dataformats//data.csv"

for line in read_file_line_by_line(file_path):
    print(line)


# 4.Create a generator for Fibonacci series.


def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

N = int(input("Enter number of terms: "))

for num in fibonacci_generator(N):
    print(num)

# 5.Write a generator that simulates retry attempts (max 3 tries).


def retry_attempts(max_tries):
    attempt = 1
    while attempt <= max_tries:
        yield f"Retry attempt {attempt}"
        attempt += 1


# Take input from user
tries = int(input("Enter number of retry attempts: "))

for attempt in retry_attempts(tries):
    print(attempt)

