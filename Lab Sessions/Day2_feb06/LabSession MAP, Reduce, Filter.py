# 1. nums = [1,2,3,4,5,6]
#Filter even numbers (filter)

nums = [1, 2, 3, 4, 5, 6]
even_nums = list(filter(lambda x: x % 2 == 0, nums))
print(even_nums)

#Square the even numbers (map)
squared_nums = list(map(lambda x: x * x, even_nums))
print(squared_nums)

#Find the sum of squared numbers (reduce)
from functools import reduce

total = reduce(lambda x, y: x + y, squared_nums)
print(total)

#2.2.salaries = [25000, 40000, 32000, 18000]

#Filter salaries greater than 30,000 (filter)
salaries = [25000, 40000, 32000, 18000]
filtered_salaries = list(filter(lambda x: x > 30000, salaries))
print(filtered_salaries)

#Add 10% hike (map)
hiked = list(map(lambda x: x * 1.10, filtered_salaries))
print(hiked)

#Find total payout using reduce
from functools import reduce

total_payout = reduce(lambda x, y: x + y, hiked)
print(total_payout)


