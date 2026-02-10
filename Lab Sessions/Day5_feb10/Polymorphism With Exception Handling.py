# Lab 7: Polymorphism with Exception Handling
# Create Calculator class with divide().
# Create SafeCalculator that overrides divide() and handles ZeroDivisionError.
# Demonstrate method overriding.

# Create Base Class Calculator

class Calculator:
    def divide(self, a, b):
        return a / b

# Create Subclass SafeCalculator (Method Overriding)

class SafeCalculator(Calculator):
    def divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Error: Division by zero is not allowed"

# Demonstrate Polymorphism

calc = Calculator()
safe_calc = SafeCalculator()

print("Calculator result:", calc.divide(10, 2))
print("SafeCalculator result:", safe_calc.divide(10, 0))
