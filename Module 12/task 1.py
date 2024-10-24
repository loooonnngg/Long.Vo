import requests
request = "https://api.chucknorris.io/jokes/random"
response = requests.get(request)
print(response.json()['value'])