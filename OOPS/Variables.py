# variables = used to store the data
# instance variables - global variables at class level
# local variables - inside the method only

# instance variables example
class Student:

    # class Variables
    school = "St Joseph Convert"

    def __init__(self, name, marks):
        self.name = name # instance variables
        self.marks = marks # instance variables or global variables

    def show(self):
        schoolcity = "Banglore" # local variable - scope is inside the method
        print(self.marks, self.name)
        print(schoolcity)
        print(self.school)

s1 = Student("Harsha", 85)
s2 = Student("Amit", 90)

s1.show()
s2.show()

class Employee:
    company = "IBM india PVT LTD"

e1 = Employee()
e2 = Employee()

print(e1.company)
print(e2.company)
