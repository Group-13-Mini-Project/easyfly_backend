import requests
import random
#
# # obtain the authentication token

# login
p = requests.post("http://127.0.0.1:8000/login/", data={'email':'janprince002@gmail.com', 'password':'prince', 'name': "gyan"})
print(p.status_code)
print(p.text)
token = p.json()["token"]


# a request with the authentication token
r = requests.get("http://127.0.0.1:8000/book-flight/", headers={"Authorization": f"Token {token}"}, params={'flight_id': 1, 'payment_status': 'successful'})

print(r.status_code)
print(r.text)
#
data = r.json()
