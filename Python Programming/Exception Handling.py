# exceptions - runtime errors which will disrupt the normal; program flow
# benefits
# helps in debugging
# prevents program crashing
# handling errors and exceptions in the code more effeciency

# try except
# try - code tp be executed
# except - exceptions details catching
# else : if the exception does not occur then else part will be extended
# finally - mandated code
# custom exceptions

try:
    a = int(input("Enter the number"))
    b = int(input("Enter the number"))
    print(a/b)
except ZeroDivisionError:
    print("Cannot divided by zero")
except ValueError:
    print("Please enter valid numbers")


# Generic excpetion
try:
    a = 5/0
except Exception as e:
    print(e)
else:
    print("Division Successfully")
finally:
    print("Close the Browser")

# Custom exceptions - creating a own exception
age = int(input("Enter the age"))
if age < 18:
    raise ValueError("Age must be 18 or Above")
