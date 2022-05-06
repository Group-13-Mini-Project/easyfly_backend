import requests

# obtain the authentication token
# p = requests.post("http://127.0.0.1:8000/api-token-auth/", data={'email':'gyanp0686@gmail.com', 'password':'prince'})
# print(p.status_code)
#
# try:
#     token = p.json()['token']
#     print(token)
# except KeyError:
#     print("Token not available")

# login
p = requests.post("http://127.0.0.1:8000/login/", data={'email':'gyanp0686@gmail.com', 'password':'prince'})
print(p.status_code)
t = p.json()["token"]


# a request with the authentication token
r = requests.get("http://127.0.0.1:8000/flights", headers={"Authorization": f"Token {t}"})

print(r.status_code)
print(r.text)
#
# data = r.json()

