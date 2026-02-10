class A:
    def show(self):
        print("Class A")

class B (A):
    pass
    #def show(self):
        # print("Class C")

class C (A):
    pass
    # print("class D")

class D (B , C):
    pass
    # print("class D")

d = D()
d.show()
print(D.mro())

# method from left to right

# D,B,C,A

