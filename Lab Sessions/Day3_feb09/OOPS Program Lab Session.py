# 1. Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def perimeter(self):
        return 2 * math.pi * self.radius


c = Circle(5)
print("Area:", c.area())
print("Perimeter:", c.perimeter())

# 2. .Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age.

from datetime import date

class Person:
    def __init__(self, name, country, dob):
        self.name = name
        self.country = country
        self.dob = dob  # dob in (year, month, day)

    def age(self):
        today = date.today()
        return today.year - self.dob[0]


p = Person("Amit", "India", (2000, 5, 10))
print("Name:", p.name)
print("Country:", p.country)
print("Age:", p.age())

# 3. Write a Python program to create a class that represents a shape. Include methods to calculate its area and perimeter. Implement subclasses for different shapes like circle, triangle, and square.

import math

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def perimeter(self):
        return 2 * math.pi * self.radius


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return 4 * self.side


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c


s = Square(4)
print("Square Area:", s.area())
print("Square Perimeter:", s.perimeter())


# 4. Write a python program to create a child class Bus that will inherit all of the variables and methods of the Vehicle class

class Vehicle:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("Vehicle Name:", self.name)


class Bus(Vehicle):
    pass


b = Bus("School Bus")
b.show()


# 5. Write a python program to create  a Vehicle class without any variables and methods

class Vehicle:
    pass


v = Vehicle()
print("Vehicle object created")
