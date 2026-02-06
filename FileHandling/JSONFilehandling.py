import json

with open("C://Users//Sujan Kumar Reddy//PycharmProjects//PythonAdvancedProgramming//Dataformats//employee.json", 'r') as file:
    data = json.load(file)

print(data)
print(data["name"])

with open("C://Users//Sujan Kumar Reddy//PycharmProjects//PythonAdvancedProgramming//Dataformats//nestedjson.json", 'r') as file:
    data = json.load(file)

email = data["user"]["profile"]["email"]
print(email)

# writing  to json file - dump method()
data ={
    "name": "Harsha",
    "role": "Tester",
    "experience": 5,
    "skills": ["Python", "Automation", "API"]
}

with open("C://Users//Sujan Kumar Reddy//PycharmProjects//PythonAdvancedProgramming//Dataformats//writejson.json", 'w') as file:
    json.dump(data, file)

#update or modify the json file

#read the json file
#modify the data
#write it back to the file
with open("C://Users//Sujan Kumar Reddy//PycharmProjects//PythonAdvancedProgramming//Dataformats//updatejson.json", 'r') as file:
    data = json.load(file)

#update the value
data["experience"] = 6

#write back
with open("C://Users//Sujan Kumar Reddy//PycharmProjects//PythonAdvancedProgramming//Dataformats//updatejson.json", 'w') as file:
    json.dump(data, file, indent =4)

