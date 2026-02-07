# 1. Create a custom iterator that prints numbers from 1 to 5.

class NumberIterator:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 5:
            value = self.num
            self.num += 1
            return value
        else:
            raise StopIteration


# Using the custom iterator
obj = NumberIterator()

for i in obj:
    print(i)


# 2.Write an iterator class that returns next even number.
class EvenNumberIterator:
    def __init__(self, start=0):
        self.num = start

    def __iter__(self):
        return self

    def __next__(self):
        self.num += 2
        return self.num

even = EvenNumberIterator()

print(next(even))
print(next(even))
print(next(even))
print(next(even))
print(next(even))


# 3.Explain and demonstrate the use of __iter__() and __next__().

"""
An iterator in Python is an object that allows traversal through a sequence
one element at a time.

To create a custom iterator, a class must implement:
1. __iter__()  → returns the iterator object
2. __next__()  → returns the next element and raises StopIteration when done
"""


class NumberIterator:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        # returns the iterator object
        return self

    def __next__(self):
        # returns the next value
        if self.num <= 5:
            value = self.num
            self.num += 1
            return value
        else:
            # stops the iteration
            raise StopIteration


# Demonstration
obj = NumberIterator()

for i in obj:
    print(i)
