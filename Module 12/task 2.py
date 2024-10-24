import requests
API_key=input("enter your weathermap API key: ")
city=input("Enter city name: ")
request="http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+API_key
response = requests.get(request)
print(response.json()["weather"][0]["description"])
print(round(response.json()['main']['temp']-273.15,2),"Celsius")
