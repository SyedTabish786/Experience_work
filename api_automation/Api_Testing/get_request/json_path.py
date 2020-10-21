import requests
import json
import jsonpath

# API URL
url = "https://reqres.in/api/users?page=2"

# Send Get Request
response = requests.get(url)
# Converitn data into json format
json_response = json.loads(response.text)
# print(json_response)
# fetch particular value using jsonpath
data = jsonpath.jsonpath(json_response, "total_pages")
assert data[0] == 2
