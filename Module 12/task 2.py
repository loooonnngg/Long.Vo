import requests
city=input("Enter city name: ")
request="http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=8d7fae354e6f647175e5b2b957a0f610"
response = requests.get(request)
print(response.json()["weather"][0]["description"])
print(round(response.json()['main']['temp']-273.15,2),"Celsius")