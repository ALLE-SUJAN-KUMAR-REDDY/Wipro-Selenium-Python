# dictionary items - key value
#similar to list and tuples
#for integers, tuples and strings - Keys must be immutable
#list cannot be used in the key for dict as it is mutable in nature

country = {
    "India": "Delhi",
    "Canada":"Ottawa",
    "England":"London"
}

print(country)
#access the values with keys
print(country["Canada"])

#add elements
country["Italy"] = "Rome"
print(country)

#remove elements
del country["India"]
print(country)

# iterate among the dict
for coun in country:
    print(coun)

# length of the dict
print(len(country))

#for integers, tuples and strings - keys must be immutable

#Integer as a key
my_dict = {1:"one", 2:"two", 3:"three"}
print(my_dict)

my_dict = {1:"four", 2:"two", 3:"three", 1:"one"}
print(my_dict)

#tuples as a key
my_dict = {(1,2): "one two", 3:"three"}

my_dict = {(1,2): "one two", 3:"three", 3:"four"}
print(my_dict)

#list as key
my_dict = {1:"Hello", (1 , 2): "There you"}
print(my_dict)

#pop - removes the item with spec key
student = {"name": "Ravi", "age": 21, "course": "CSE"}
student.pop("age")
print(student)

#update() - adds or changes the dict
student = {"name": "Ravi", "age": 21}
student.update({"age": 22, "city": "Hyderabad"})
print(student)

#keys()
student = {"name": "Ravi", "age": 21, "course": "CSE"}
print(student.keys())

#Values()
student = {"name": "Ravi", "age": 21, "course": "CSE"}
print(student.values())

#popitem() return the last inserted keyword
student = {"name": "Ravi", "age": 21, "course": "CSE"}
item = student.popitem()
print(item)
print(student)

#copy returns the copy of dict
student = {"name": "Ravi", "age": 21}
new_student = student.copy()
print(new_student)

# dict inside the list

employees = [
    {"id": 1, "name": "Harsha", "role":"QA"}
    {"id": 2, "name":"Anil", "role":"Dev"}
    {"id": 3, "name":"Ravi", "role":"Manager"}
]

print(employees[0])
print(employees[0]["name"])

for emp in employees:
    print(emp["name"], emp["role"])

employees.append(({"id":4, "name":"Sita", "role":"Tester"}))
print(employees)

employees.pop(0)
print(employees)

#Search a item in the list
for emp in employees:
    if emp["name"] == "Harsha":
        print(emp)