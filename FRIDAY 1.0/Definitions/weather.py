import requests

#https://api.openweathermap.org/data/2.5/weather?lat=43.77&lon=-79.23&units=metric&appid=ed5b8dbb31740d7d0921491b323ed14b

url = 'https://api.openweathermap.org/data/2.5/weather?lat=43.7764&lon=-79.2318&units=metric&appid=ed5b8dbb31740d7d0921491b323ed14b'
            
res = requests.get(url)
data = res.json()
weather = data['weather'][0]['main']
description = data['weather'][0]['description']
temp = str(data['main']['temp'])
temp_feels_like = str(data['main']['feels_like'])
pressure = str(data['main']['pressure'])
wind_speed = str(data['wind']['speed'])
humidity = str(data['main']['humidity'])
