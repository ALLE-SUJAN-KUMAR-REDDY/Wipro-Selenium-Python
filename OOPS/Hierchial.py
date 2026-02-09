# Hierarchy inheritance

# Parent class
class Employee:

    def login(self):
        print("Employee is logged in")


# Child class 1
class Developer(Employee):

    def write_code(self):
        print("Writing code")


# Child class 2
class Tester(Employee):

    def test_app(self):
        print("Testing the application")


# Creating objects
dev = Developer()   # child 1
test = Tester()    # child 2

# Calling methods
dev.login()
dev.write_code()

test.login()
test.test_app()
