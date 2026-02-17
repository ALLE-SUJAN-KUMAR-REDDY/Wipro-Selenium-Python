# 1. Create a class BankAccount with private balance.

class BankAccount:
    def __init__(self):
        self.__balance = 0   # private variable

    def show_balance(self):
        print("Balance:", self.__balance)


# ---- Object Creation ----
acc1 = BankAccount()

# ---- Method Call ----
acc1.show_balance()



# 2. Use getter and setter methods to update balance safely.

class BankAccount:
    def __init__(self):
        self.__balance = 0

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Balance cannot be negative")


# ---- Object Creation ----
acc2 = BankAccount()

# ---- Setter ----
acc2.set_balance(5000)

# ---- Getter ----
print("Balance:", acc2.get_balance())

acc2.set_balance(-100)


# 3. Prevent negative salary using property decorators.

class Employee:
    def __init__(self, salary):
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value >= 0:
            self._salary = value
        else:
            print("Salary cannot be negative")


# ---- Object Creation ----
emp = Employee(30000)

print("Salary:", emp.salary)

emp.salary = 45000
print("Updated Salary:", emp.salary)

emp.salary = -2000
