import requests

# Define the API endpoint and the payload to be sent in the request
url = "https://fakerestapi.azurewebsites.net/api/v1/Activities"
payload = {
  "id": 0,
  "title": "string",
  "dueDate": "2023-02-01T12:46:52.403Z",
  "completed": True
  }

# Make a POST request to the API endpoint
response = requests.post(url, json=payload)

# Check if the request was successful
if response.status_code == 200:
    # Get the JSON data from the response
    data = response.json()
    print(data)
else:
    print("Request failed with status code:", response.status_code)