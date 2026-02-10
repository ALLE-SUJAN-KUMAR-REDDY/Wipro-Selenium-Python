# Lab 4: Operator Overloading
# Create a class BankAccount with attribute balance.

#Create BankAccount Class

class BankAccount:
    def __init__(self, balance):
        self.balance = balance


# Overload + to add balances and > to compare balances.

# Overload + Operator (__add__)

    def __add__(self, other):
        return BankAccount(self.balance + other.balance)

# Overload > Operator (__gt__)

    def __gt__(self, other):
        return self.balance > other.balance


# Demonstrate polymorphic behavior of operators.

acc1 = BankAccount(5000)
acc2 = BankAccount(3000)

acc3 = acc1 + acc2

print("Total Balance:", acc3.balance)

if acc1 > acc2:
    print("Account 1 has more balance")
else:
    print("Account 2 has more balance")
