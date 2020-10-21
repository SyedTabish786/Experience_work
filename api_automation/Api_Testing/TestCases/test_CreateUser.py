import requests
import json
import jsonpath


url= "https://reqres.in/api/users"

def test_create_new_user():
    #Read Json Input file
    file = open("/Users/tabish/PycharmProjects/apitesting/post_request/data1", "r")
    json_input = file.read()
    request_json = json.loads(json_input)
    #make post request with json input body
    response =requests.post(url,request_json)
    print("This is reponse :" +response.content)
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


def test_validate_user():
    #Read Json Input file
    file = open("/Users/tabish/PycharmProjects/apitesting/post_request/data1", "r")
    json_input = file.read()
    request_json = json.loads(json_input)
    #make post request with json input body
    response =requests.post(url,request_json)
    print(response.content)
    #validating request code
    assert response.status_code == 201



def test_validate_request():
    #Read Json Input file
    file = open("/Users/tabish/PycharmProjects/apitesting/post_request/data1", "r")
    json_input = file.read()
    request_json = json.loads(json_input)
    #make post request with json input body
    response =requests.post(url,request_json)
    response_json = json.loads(response.text)
    print(response_json)
    #pick id using jsonpath
    id =jsonpath.jsonpath(response_json,"id")
    print(id[0])


url2 = "https://reqres.in/api/users?page=2"
def test_user_list():

    # Send Get Request
    response = requests.get(url)
    # Converitn data into json format
    json_response = json.loads(response.text)
    # print(json_response)
    # fetch particular value using jsonpath
    data = jsonpath.jsonpath(json_response, "total_pages")
    print(data)
    assert data[0] == 2

