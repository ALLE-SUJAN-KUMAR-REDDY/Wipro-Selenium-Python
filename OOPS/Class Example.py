# class is a blue print or a template
# which describes the state / behaviour of its object

class Student:

    # data or the properties
    studentname = "Ravi"
    studentID = 677887

    # self is used to access the attributes of the class we ahve defined
    # it is automically loaded
    # self represents the instance of the class

# create a function to access the data

    def displaystudentdetails(self):
        print(self.studentname)
        print(self.studentID)

# create the object of the class
a = Student()
a.displaystudentdetails()

