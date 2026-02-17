# 1.Create a Car class with attributes brand, model, price.

class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

car1 = Car("Toyota", "Innova", 2500000)
print(car1.brand, car1.model, car1.price)


# 2. Create a Student class with method get_grade() based on marks.

class Student:
    def __init__(self, marks):
        self.marks = marks

    def get_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        else:
            return "C"

s1 = Student(88)
print(s1.get_grade())


# 3. Create a BankAccount class with deposit() and withdraw() methods.

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")


# ---- Object Creation ----
account = BankAccount(1000)

account.deposit(500)
account.withdraw(300)

print("Final Balance:", account.balance)



# 4. Write a class Employee that initializes name, id, salary using __init__.

class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary


# ---- Object Creation ----
emp1 = Employee("Sujan", 101, 50000)

print("Name:", emp1.name)
print("ID:", emp1.emp_id)
print("Salary:", emp1.salary)



# 5. Create a class that counts how many objects are created.

class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

obj1 = Counter()
obj2 = Counter()
print("Objects created:", Counter.count)


# 6. Create a class Company with a class variable company_name.

class Company:
    company_name = "Wipro"

print(Company.company_name)


# 7. Implement a static method to validate email format.

class Validator:
    @staticmethod
    def validate_email(email):
        return "@" in email and "." in email

print(Validator.validate_email("test@gmail.com"))

