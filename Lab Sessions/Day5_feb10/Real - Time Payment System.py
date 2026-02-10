# Lab 8: Real-Time Payment System

# Create base class Payment with method pay().

class Payment:
    def pay(self, amount):
        raise NotImplementedError("Subclasses must implement this method")

# Create CreditCard, UPI, and NetBanking subclasses.

class CreditCard(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")

class UPI(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")

class NetBanking(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Net Banking")


# Use a single function to process all payments.

def process_payment(payment_method, amount):
    payment_method.pay(amount)


p1 = CreditCard()
p2 = UPI()
p3 = NetBanking()

process_payment(p1, 500)
process_payment(p2, 1200)
process_payment(p3, 3000)
