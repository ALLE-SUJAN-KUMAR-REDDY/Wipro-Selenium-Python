# Lab 6: Multiple Inheritance and MRO
# Create classes A, B, C, and D (diamond structure).
# Override the same method in B and C.
# Call method using D object and observe MRO.

# Create Base Class A

class A:
    def show(self):
        print("Method from class A")

# Create Classes B and C (inherit from A)

class B(A):
    def show(self):
        print("Method from class B")

class C(A):
    def show(self):
        print("Method from class C")

# Create Class D (inherits from B and C)

class D(B, C):
    pass

# Call Method Using D Object

d = D()
d.show()

# Observe Method Resolution Order (MRO)

print(D.mro())
