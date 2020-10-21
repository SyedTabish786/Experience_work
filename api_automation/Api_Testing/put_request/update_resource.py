import requests
import jsonpath
import json

url = "https://reqres.in/api/users?page=2"

#reading json input file
file = open("/Users/tabish/PycharmProjects/apitesting/put_request/data2","r")
json_input = file.read()
request_json = json.loads(json_input)
#make PUT request with json input body
response =requests.put(url,request_json)
print(response.content)
#validating request code
assert response.status_code == 200
#fetch header from request
print(response.headers)
#fetch any particular header from request
print(response.headers.get("Date"))
#coverting response to json format
response_json = json.loads(response.text)
#pick id using jsonpath
update =jsonpath.jsonpath(response_json,"updatedAt")
print(update[0])