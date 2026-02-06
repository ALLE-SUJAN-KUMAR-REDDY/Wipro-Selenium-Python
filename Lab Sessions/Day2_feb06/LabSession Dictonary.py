#1.Create a dictionary with student roll number as key and name as value. Print the dictionary.
students = {
    101: "Ravi",
    102: "Sita",
    103: "Amit"
}

print(students)

#2.Access the value of a key that exists and one that does not exist
print(students[101])

#3.Update the value of an existing key in a dictionary.
students[102] = "Sita Reddy"
print(students)

#4.Delete a key from a dictionary using:
#Using del
del students[103]
print(students)

#Using pop()
students.pop(101)
print(students)

#5.Find the number of key–value pairs in a dictionary.
print(len(students))

#6.Print only
#Keys
print(students.keys())

#Values
print(students.values())

#Key–Value pairs
print(students.items())
