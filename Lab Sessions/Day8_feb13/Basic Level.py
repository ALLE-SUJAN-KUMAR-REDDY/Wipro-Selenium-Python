# 1. Write a Python script to send a GET request to https://jsonplaceholder.typicode.com/users and print only name and email.

import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")

if response.status_code == 200:
    users = response.json()
    for user in users:
        print("Name:", user["name"])
        print("Email:", user["email"])
        print("-" * 30)

# 2. Send a GET request with query parameter userId=2 and print number of posts returned.

import requests

params = {"userId": 2}
response = requests.get(
    "https://jsonplaceholder.typicode.com/posts",
    params=params
)

if response.status_code == 200:
    posts = response.json()
    print("Number of posts:", len(posts))

# 3. Write a POST request to create a new resource and verify status code 201.

import requests

data = {
    "title": "API Automation",
    "body": "Learning requests library",
    "userId": 1
}

response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=data
)

if response.status_code == 201:
    print("Resource created successfully")
else:
    print("Failed with status:", response.status_code)

# 4. Explain the difference between data= and json= in requests.post().

# data= Sends data as form-encoded

# Content-Type: application/x-www-form-urlencoded

# requests.post(url, data=data)

# json=

# Sends data as JSON

# Content-Type: application/json

# Automatically converts dict → JSON

# requests.post(url, json=data)

#APIs mostly expect json


# 5.Write code to check if response status code is not 200 and raise an exception.

import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")

if response.status_code != 200:
    raise Exception(f"Request failed with status code {response.status_code}")

print("Request successful")
