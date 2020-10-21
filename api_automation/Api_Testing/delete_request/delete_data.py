import requests

#API URL
url = "https://reqres.in/api/users/2"

response = requests.delete(url)
print(response.status_code)
assert response.status_code == 204
details =requests.get(url)
#its is sample api request thats why it is showing data after deleting it but in real situation it will not show the data 
print(details.content)