from decouple import config
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
from datetime import timedelta
from django.utils import timezone

from .models import WeatherCache

class WeatherView(APIView):
    def get(self, request, *args, **kwargs):
        city_name = self.request.GET.get('city', '')

        if not city_name:
            return Response({'error': 'City parameter is required'}, status=status.HTTP_400_BAD_REQUEST)

        weather_data = self.get_cached_weather_data(city_name)

        if not weather_data:
            weather_data = self.fetch_weather_data(city_name)
            if weather_data:
                self.cache_weather_data(city_name, weather_data)

        if weather_data:
            return Response(weather_data)
        else:
            return Response({'error': 'Could not fetch weather data'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get_cached_weather_data(self, city_name):
        cache_entry = WeatherCache.objects.filter(city=city_name).first()

        if cache_entry:
            # Проверяем, были ли данные обновлены в течение последних 30 минут
            if timezone.now() - cache_entry.last_updated <= timedelta(minutes=30):
                return {
                    'temperature': cache_entry.temperature,
                    'pressure': cache_entry.pressure,
                    'wind_speed': cache_entry.wind_speed
                }
            else:
                # Если данные устарели, удаляем их из кэша
                cache_entry.delete()

        return None

    def fetch_weather_data(self, city_name):
        api_key = config('OPENWEATHERMAP_API_KEY')
        base_url = 'https://api.openweathermap.org/data/2.5/weather'

        try:
            response = requests.get(base_url, params={'q': city_name, 'appid': api_key, 'units': 'metric'})
            response.raise_for_status()
            data = response.json()

            temperature = data['main']['temp']
            pressure = data['main']['pressure']
            wind_speed = data['wind']['speed']

            return {'temperature': temperature, 'pressure': pressure, 'wind_speed': wind_speed}
        except requests.RequestException as e:
            print(f'Error fetching weather data: {e}')
            return None

    def cache_weather_data(self, city_name, weather_data):
        WeatherCache.objects.create(
            city=city_name,
            temperature=weather_data['temperature'],
            pressure=weather_data['pressure'],
            wind_speed=weather_data['wind_speed']
        )



