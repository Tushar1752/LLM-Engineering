import requests
response = requests.get("https://www.hellointerview.com/get")
print(response.status_code)
print(response.headers["Content-Type"])
print(type(response.text))