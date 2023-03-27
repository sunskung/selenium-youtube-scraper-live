# pip install requests
import requests

# obj = [[1, 2, 3], list(range(10000))]
# print(r.repr(obj))

# response = requests.get("https://randomuser.me/api/")
# print(response.text)

# response = requests.get("https://api.thedogapi.com/")
# print(response.text)
# print(response.headers)
# print(response.status_code)

###################################

# response = requests.get("https://api.thedogapi.com/v1/breeds")
# request = response.request
# print(request.url)
# print(request.path_url)
# print(request.method)
# print(request.headers)

# response = requests.get("http://placegoat.com/200/200")
# print(response.headers.get("Content-Type"))

headers = {"X-Request-Id": "<my-request-id>"}
response = requests.get("https://example.org", headers=headers)
print(response.request.headers)
