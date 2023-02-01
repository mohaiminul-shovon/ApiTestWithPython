import requests

id = 2
# Define the API endpoint and the payload to be sent in the request
url = "https://fakerestapi.azurewebsites.net/api/v1/Activities/{}".format(id)
payload = {
  "id": 2,
  "title": "string",
  "dueDate": "2023-02-05T12:52:31.107Z",
  "completed": True
}

# Make a PUT request to the API endpoint
response = requests.put(url, json=payload)

# Check if the request was successful
if response.status_code == 200:
    # Get the JSON data from the response
    data = response.json()
    print(data)
else:
    print("Request failed with status code:", response.status_code)