# Parent class
class SavingsAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)
        print("Balance after deposit:", self.balance)


# Child class
class InterestAccount(SavingsAccount):
    def addInterest(self, rate):
        interest = self.balance * rate / 100
        self.balance += interest
        print("Interest added:", interest)
        print("Balance after interest:", self.balance)


# Creating object of child class
acc = InterestAccount(1000)

# Calling parent class method
acc.deposit(500)

# Calling child class method
acc.addInterest(5)

# Multi Level Inheritance

# Level 1 - Parent class
class SavingsAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)
        print("Balance:", self.balance)


# Level 2 - Child class
class InterestAccount(SavingsAccount):
    def addInterest(self, rate):
        interest = self.balance * rate / 100
        self.balance += interest
        print("Interest Added:", interest)
        print("Balance after interest:", self.balance)


# Level 3 - Child of InterestAccount
class PremiumAccount(InterestAccount):
    def giveBonus(self, bonus):
        self.balance += bonus
        print("Bonus Added:", bonus)
        print("Final Balance:", self.balance)


# Creating object of last child class
acc = PremiumAccount(1000)

acc.deposit(500)        # From SavingsAccount
acc.addInterest(5)      # From InterestAccount
acc.giveBonus(200)      # From PremiumAccount

