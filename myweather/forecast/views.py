from django.shortcuts import render
from datetime import datetime
# from django.http import HttpResponse
import requests
from . import weather_key

def index(request):
    context = {}
    current_date = datetime.now().date()

    if request.method == "POST":
        location = request.POST['location']

        # Fetching weather data from WeatherAPI
        BASE_URL = 'http://api.weatherapi.com/v1'
        ENDPOINT = '/forecast.json'
        DAYS = 4

        response = requests.get(f"{BASE_URL}{ENDPOINT}?key={weather_key.weather_api_key}&q={location}&days={DAYS}")
        data = response.json()

        # print("API Response Data:", data)

        # Extracting relevant weather information
        location_name = data['location']['name']
        current_temperature = data['current']['temp_c']
        current_condition = data['current']['condition']['text']
        current_icon_url = data['current']['condition']['icon']

        forecast_data = []
        for day in data['forecast']['forecastday']:
            date_obj = datetime.strptime(day['date'], '%Y-%m-%d')
            day_name = date_obj.strftime('%A')
            max_temp = day['day']['maxtemp_c']
            min_temp = day['day']['mintemp_c']
            condition = day['day']['condition']['text']
            icon_url = day['day']['condition']['icon']
            forecast_data.append({
                'date': date_obj,
                'day_name': day_name,
                'max_temp': max_temp,
                'min_temp': min_temp,
                'condition': condition,
                'icon_url': icon_url
            })

        context = {
            'location_name': location_name,
            'current_temperature': current_temperature,
            'current_condition': current_condition,
            'current_icon_url': current_icon_url,
            'forecast_data': forecast_data,
            'current_date': current_date
        }
        # print("Context Data:", context)

        # Fetching image for the location from Unsplash
        IMAGE_API_ENDPOINT = "https://api.unsplash.com/search/photos"
        headers = {
            "Authorization": f"Client-ID {weather_key.unsplash_api_key}"
        }
        params = {
            "query": location_name,
            "page": 1,
            "per_page": 1
        }
        image_response = requests.get(IMAGE_API_ENDPOINT, headers=headers, params=params)
        image_data = image_response.json()
        if image_data['results']:
            city_image_url = image_data['results'][0]['urls']['full']
        else:
            city_image_url = "default_background_url"  # Replace with a URL to your default image
        context['city_image_url'] = city_image_url

    return render(request, 'forecast/index.html', context)