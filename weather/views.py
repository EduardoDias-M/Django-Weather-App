import requests
from django.shortcuts import render
from .models import City

# Create your views here.

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=yourkey'
    city = 'London'

    cities = City.objects.all()
    weather_data = []

    for city in cities:
        req = requests.get(url.format(city)).json()

        city_weather = {
            'city' : city.name,
            'temperature' : req['main']['temp'],
            'description' : req['weather'][0]['description'],
            'icon' : req['weather'][0]['icon'],
        }
        weather_data.append(city_weather)
        
    context = {'weather_data' : weather_data}
    
    return render(request, 'index.html', context)