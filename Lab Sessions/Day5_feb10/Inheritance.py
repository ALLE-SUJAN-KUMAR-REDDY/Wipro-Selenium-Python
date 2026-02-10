# Lab 1: Method Overriding with Inheritance
# Create a base class Employee with a method calculate_salary().

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        return self.salary


# Create a subclass Manager that overrides calculate_salary() and adds a bonus.

class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def calculate_salary(self):
        return self.salary + self.bonus


# Demonstrate runtime polymorphism using parent class reference.

# Parent class reference
emp = Manager("Sujan", 50000, 10000)

print(emp.calculate_salary())

