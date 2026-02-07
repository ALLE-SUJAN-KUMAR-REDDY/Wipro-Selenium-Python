# 1.Handle FileNotFoundError Exception When Opening a File

# Handle FileNotFoundError while reading JSON

import json

try:
    with open("C://Users//Sujan Kumar Reddy//PycharmProjects//PythonAdvancedProgramming//Dataformats//employee.json", 'r') as file:
        data = json.load(file)
        print(data)
        print(data["name"])

except FileNotFoundError:
    print("Error: employee.json file not found")

# Handle error for nested JSON file

try:
    with open("C://Users//Sujan Kumar Reddy//PycharmProjects//PythonAdvancedProgramming//Dataformats//nestedjson.json", 'r') as file:
        data = json.load(file)

        email = data["user"]["profile"]["email"]
        print(email)

except FileNotFoundError:
    print("Error: nestedjson.json file not found")

except KeyError:
    print("Error: Required key not found in JSON")

# Handle error while writing JSON

data = {
    "name": "Harsha",
    "role": "Tester",
    "experience": 5,
    "skills": ["Python", "Automation", "API"]
}

try:
    with open("C://Users//Sujan Kumar Reddy//PycharmProjects//PythonAdvancedProgramming//Dataformats//writejson.json", 'w') as file:
        json.dump(data, file, indent=4)

except FileNotFoundError:
    print("Error: Folder path not found while writing file")

# Handle error while updating JSON

import json

try:
    # Read JSON file
    with open("C://Users//Sujan Kumar Reddy//PycharmProjects//PythonAdvancedProgramming//Dataformats//updatejson.json", 'r') as file:
        data = json.load(file)

    # Update value
    data["experience"] = 6

    # Write back to file
    with open("C://Users//Sujan Kumar Reddy//PycharmProjects//PythonAdvancedProgramming//Dataformats//updatejson.json", 'w') as file:
        json.dump(data, file, indent=4)

except FileNotFoundError:
    print("Error: updatejson.json file not found")

except json.JSONDecodeError:
    print("Error: JSON file is empty or corrupted")


# 2.write a program to handle invalid user input

try:
    num = int(input("Enter a number: "))
    print("You entered:", num)

except ValueError:
    print("Invalid input! Please enter an integer.")

# 3.Write a Python program that generates random alphabetical characters, alphabetical strings, and alphabetical strings of a fixed length. Use random.choice()

import random
import string

# Generate a random alphabetical character
random_char = random.choice(string.ascii_letters)
print("Random Alphabetical Character:", random_char)


# Generate a random alphabetical string (random length)
random_string = ''.join(random.choice(string.ascii_letters) for _ in range(6))
print("Random Alphabetical String:", random_string)


# Generate a random alphabetical string of fixed length
fixed_length = 10
fixed_string = ''.join(random.choice(string.ascii_letters) for _ in range(fixed_length))
print("Random Alphabetical String (Fixed Length):", fixed_string)
