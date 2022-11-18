import requests

# endpoint = "http://httpbin.org/status/200/"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/" # http://127.0.0.1:8000/

# requests.get() # API -> Method // Application programing interface

# NOT Rest APIs / Just Library APIs
# Phone -> Camera -> App -> API -> CAMERA

# Rest APIs -> Web API (One we are using)
# HTTP Request

# get_response = requests.get(endpoint, json={"query":"Hello world"}) # HTTP Request
# get_response = requests.get(endpoint, params={"abc": 123}, json={"query":"Hello world"}) # HTTP Request
# get_response = requests.get(endpoint, json={"product_id": 123 }) # HTTP Request
# get_response = requests.post(endpoint, json={"product_id": 123 }) # HTTP Request
# get_response = requests.post(endpoint, json={"title":"Hello world"}) # HTTP Request
get_response = requests.post(endpoint, json={"content":"Hello world"}) # HTTP Request
# print(get_response.text) # print source code

# print(get_response.text)
# print(get_response.status_code)
# print(get_response.json())
# print(get_response.json()['message'])
print(get_response.json())

