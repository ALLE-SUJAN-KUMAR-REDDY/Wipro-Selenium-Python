#1.1.Write a Python program to sort a list of tuples using Lambda

data = [(1, 3), (4, 1), (2, 2), (5, 0)]

sorted_data = sorted(data, key=lambda x: x[1])

print(sorted_data)

#2.Write a Python program to extract year, month, date and time using Lambda.

from datetime import datetime

now = datetime.now()

extract = lambda d: (d.year, d.month, d.day, d.time())

result = extract(now)

print("Year:", result[0])
print("Month:", result[1])
print("Date:", result[2])
print("Time:", result[3])

#3.Write a Python script to concatenate the following dictionaries to create a new one.
dict1 = {1: 10, 2: 20}
dict2 = {3: 30, 4: 40}
dict3 = {5: 50, 6: 60}

new_dict = {}

new_dict.update(dict1)
new_dict.update(dict2)
new_dict.update(dict3)

print(new_dict)

