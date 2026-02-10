# Lab 3: Multilevel Inheritance with Polymorphism
# Create Vehicle → Car → ElectricCar.

# Base Class Vehicle

class Vehicle:
    def fuel_type(self):
        return "Uses fuel"

# Derived Class Car (inherits Vehicle)

class Car(Vehicle):
    def fuel_type(self):
        return "Uses petrol or diesel"


# Each class overrides the method fuel_type().

# Derived Class ElectricCar (inherits Car)

class ElectricCar(Car):
    def fuel_type(self):
        return "Uses electricity"


# Call the method using different object references.

v = Vehicle()
c = Car()
e = ElectricCar()

print(v.fuel_type())
print(c.fuel_type())
print(e.fuel_type())
