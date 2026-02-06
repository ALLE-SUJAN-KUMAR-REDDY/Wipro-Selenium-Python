#1.What is the output? list(enumerate(['a', 'b', 'c']))
print(list(enumerate(['a', 'b', 'c'])))

#2.Q2 What is the output? for i, v in enumerate([10, 20, 30]): print(i, v)
for i, v in enumerate([10, 20, 30]):
    print(i, v)

#3.Q3 Write code to print index + value from: colors = ['red', 'green', 'blue'] Index should start from 1.
colors = ['red', 'green', 'blue']
for i, v in enumerate(colors, start=1):
    print(i, v)

#4.Q4 What is the output? list(enumerate("PYTHON", start=1))
print(list(enumerate("PYTHON", start=1)))

#5.Q5 Find the index of value 50 using enumerate(): nums = [10, 20, 30, 40, 50, 60]
nums = [10, 20, 30, 40, 50, 60]
for i, v in enumerate(nums):
    if v == 50:
        print(i)

#6.Q6 What is the output? for i, n in enumerate(range(10, 60, 10)): print(i, n)
for i, n in enumerate(range(10, 60, 10)):
    print(i, n)

#7.Q7 Convert this into an enumerate() loop: for i in range(len(data)): print(i, data[i])
data =[1,2,3,4]
for i, v in enumerate(data):
    print(i, v)

#8.Q8 What is printed? items = ['a', 'b', 'c'] for i in enumerate(items): print(i)
items = ['a', 'b', 'c']
for i in enumerate(items):
    print(i)

#9.Q9 What is the output? list(enumerate([], start=5))
print(list(enumerate([], start=5)))

#10.Q10 What is the output? for i, v in enumerate([100, 200, 300], start=-1): print(i, v)
for i, v in enumerate([100, 200, 300], start=-1):
    print(i, v)

#11.Q11 What happens here? i, v = enumerate(['x', 'y', 'z'])
i, v = next(enumerate(['x', 'y', 'z']))
print(i, v)

#12.Q12 Explain the difference: enumerate(data) enumerate(data, start=1)
print(list(enumerate(['a', 'b', 'c'])))
print(list(enumerate(['a', 'b', 'c'], start=1)))

