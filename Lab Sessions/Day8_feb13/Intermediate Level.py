# 6. Fetch all users and print usernames in uppercase.

import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")

if response.status_code == 200:
    users = response.json()
    for user in users:
        print(user["username"].upper())

# 7. Implement timeout handling (2 seconds) and catch Timeout exception.

import requests
from requests.exceptions import Timeout

try:
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users",
        timeout=2
    )
    print(response.json())

except Timeout:
    print("Request timed out")

# 8. Use Session object to send multiple requests and demonstrate cookie persistence.

import requests

session = requests.Session()

# First request
session.get("https://httpbin.org/cookies/set/sessionid/12345")

# Second request (cookie persists)
response = session.get("https://httpbin.org/cookies")

print(response.json())

# 9. Upload a file using requests and print server response.

import requests

files = {
    "file": open("C://Users//Sujan Kumar Reddy//OneDrive//Desktop//Lambda.txt", "rb")
}

response = requests.post(
    "https://httpbin.org/post",
    files=files
)

print(response.json())


# 10. Fetch posts and save response JSON into a file named posts.json.

import requests
import json

response = requests.get("https://jsonplaceholder.typicode.com/posts")

if response.status_code == 200:
    posts = response.json()

    with open("posts.json", "w") as file:
        json.dump(posts, file, indent=4)

    print("posts.json file saved successfully")
