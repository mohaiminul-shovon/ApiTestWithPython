import requests

# Define the id which will be used as parameter
id = 2
# Define the API endpoint to delete
url = "https://fakerestapi.azurewebsites.net/api/v1/Activities/{}".format(id)

# Make a DELETE request to the API endpoint
response = requests.delete(url)

# Check if the request was successful
if response.status_code == 200:
    print("User deleted successfully.")
else:
    print("Request failed with status code:", response.status_code)