import requests

try:
    data = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }

    # make a POST request to API endpoint
    response = requests.post(
        "https://api.restful-api.dev/objects",
        json=data
    )

    print(response)   # <Response [200]>

    # check if the status code is 200 or 201
    if response.status_code in [200, 201]:
        print("POST request successful")

        # parse JSON response
        response_data = response.json()
        print(response_data)

    else:
        print(f"Error: Received status code {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
