import requests

try:
    # Make a GET request to API endpoint
    response = requests.get("https://api.restful-api.dev/objects")
    print(response)   # <Response [200]>

    # Check status code
    if response.status_code == 200:
        print("Status code is 200")

        # Parse JSON response (LIST)
        data = response.json()

        # Check response is a list
        if isinstance(data, list):
            print(f"Total objects received: {len(data)}\n")

            # Iterate through list
            for obj in data:
                print("ID:", obj.get("id"))
                print("Name:", obj.get("name"))

                # Handle data field
                if obj.get("data") is None:
                    print("Data: null")
                else:
                    print("Data:")
                    for key, value in obj["data"].items():
                        print(f"  {key}: {value}")

                print("-" * 40)

        else:
            print("Response is not a list")

    else:
        print(f"Error: Received status code {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
