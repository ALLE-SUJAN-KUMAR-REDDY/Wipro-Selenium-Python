# 1. Create a base class Vehicle and derived class Bike.

class Vehicle:
    def start(self):
        print("Vehicle started")

class Bike(Vehicle):
    pass

b = Bike()
b.start()


# 2. Create Person → Employee → Manager (multilevel inheritance).

class Person:
    def speak(self):
        print("Person speaking")

class Employee(Person):
    def work(self):
        print("Employee working")

class Manager(Employee):
    def manage(self):
        print("Manager managing")


# ---- Object Creation ----
m = Manager()

# ---- Method Calls ----
m.speak()
m.work()
m.manage()



# 3. Override a method in child class and call parent method using super().

class Parent:
    def show(self):
        print("Parent method")

class Child(Parent):
    def show(self):
        super().show()
        print("Child method")

c = Child()
c.show()


