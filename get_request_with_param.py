import requests

id = 1
url = "https://fakerestapi.azurewebsites.net/api/v1/Activities/{}".format(id)
# Make a GET request to an API endpoint
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Get the JSON data from the response
    data = response.json()
    print(data)
else:
    print("Request failed with status code:", response.status_code)
