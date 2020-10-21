import requests

#API URL
url= "https://reqres.in/api/users?page=2"

#Send Get Request

response =requests.get(url)
#Display Response Content
print(" 1 " + str( response.content))
print(' 2 ' + str(response.cookies))
print(' 3 ' + str(response.headers))
print(' 4 ' + str(response.request))
print(' 5 ' + str(response.apparent_encoding))
print(' 6 ' + str(response.is_permanent_redirect))
print(' 7 ' + str(response.is_redirect))
print(' 8 ' + str(response.iter_content()))
print(' 9 ' + str(response.iter_lines()))
print(' 10 ' + str(response.json()))