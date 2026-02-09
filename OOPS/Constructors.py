# Constructors - first function of the class
# Syntax __init__()
# we can parametrized the constructors
# self is manadatory
# constructor overloading is not supported directly

class Student:
    def __init__(self):
        print("Constructor is called")

    def addsum(self):
        print("Adding 2 numbers")

s1 = Student()
s1.addsum()

# parametrized constructors

# self.name is a instance variable or a global variable (belongs to object)
# name is a local parameter (exists inside the method)
# if we dont assign it to the self.name the object will not remember the value

class Employee:

    def __init__(self, name, salary):

        self.name = name
        self.salary = salary

    def display(self):
        print(self.name, self.salary)

e1 = Employee("Harsha", 50000)
e2 = Employee("Ravi", 656776)

e1.display()
e2.display()

# using * arguments in constructor
# constructor overloading is suported by *args keyword
# we can any number of parameters to the constructor using *args

class Numbers:
    def __init__(self , *args):
        self.values = args

n = Numbers(10,20,30)
print(n.values)

m = Numbers(3,4)
print(m.values)

p = Numbers(3)
print(p.values)


# Parent and child constructors
# super keyword for accessing parent constructor

class Parent:
    def __init__(self):
        print("I am the parent constructor")

class Child(Parent):
    def __init__(self):
        print("I am the child constructor")


c = Child()





