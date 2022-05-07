import requests
import random
#
# # obtain the authentication token
#
# # login
# p = requests.post("http://127.0.0.1:8000/signup/", data={'email':'janprince002@gmail.com', 'password':'prince', 'name': "gyan"})
# print(p.status_code)
# print(p.text)
# token = p.json()["token"]
#
#
# # a request with the authentication token
# r = requests.get("http://127.0.0.1:8000/flights", headers={"Authorization": f"Token {token}"})
#
# print(r.status_code)
# print(r.text)
# #
# data = r.json()
r=  random.randint(100, 999)
print(r)

