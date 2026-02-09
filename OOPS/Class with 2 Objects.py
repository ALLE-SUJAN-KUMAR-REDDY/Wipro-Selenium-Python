# write a program to create a class for an employee - with data - emp id , emp name , emp  dept and create function to display the data with 2 objects
class Employee:
    def __init__(self, emp_id, emp_name, emp_dept):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_dept = emp_dept

    def display(self):
        print("Employee ID   :", self.emp_id)
        print("Employee Name :", self.emp_name)
        print("Department    :", self.emp_dept)


# Creating 2 objects
emp1 = Employee(101, "Rahul", "IT")
emp2 = Employee(102, "Anita", "HR")

# Display employee details
emp1.display()
emp2.display()