import requests
import json
import jsonpath

url= "https://reqres.in/api/users"

#Read Json Input file
file = open("/Users/tabish/PycharmProjects/apitesting/post_request/data1","r")
json_input = file.read()
request_json = json.loads(json_input)
#make post request with json input body
response =requests.post(url,request_json)
print(response.content)
#validating request code
assert response.status_code == 201
#fetch header from request
print(response.headers)
#fetch any particular header from request
print(response.headers.get("Date"))
#coverting response to json format
response_json = json.loads(response.text)
#pick id using jsonpath
id =jsonpath.jsonpath(response_json,"id")
print(id[0])