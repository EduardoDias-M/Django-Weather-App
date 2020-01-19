from django.shortcuts import render
import requests

# Create your views here.

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=yourkey'
    city = 'Las Vegas'
    
    req = requests.get(url.format(city)).json()

    city_weather = {
        'city' : city,
        'temperature' : req['main']['temp'],
        'description' : req['weather'][0]['description'],
        'icon' : req['weather'][0]['icon'],
    }

    context = {'city_weather' : city_weather}
    
    return render(request, 'index.html', context)