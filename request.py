import requests

# Replace this with the actual URL of your API
base_url = "https://localhost:5000"

# Sample data for the request
request_data = {"city": "London"}

# Make a GET request to the /weather endpoint
response = requests.get(f"{base_url}/weather", json=request_data)

# Check the status code and print the response
if response.status_code == 200:
    print("Successful response:")
    print(response.json())
elif response.status_code == 400:
    print("Bad Request:")
    print(response.json())
elif response.status_code == 500:
    print("Internal Server Error:")
    print(response.json())
else:
    print(f"Unexpected status code: {response.status_code}")

