from django.db import models


class WeatherCache(models.Model):
    city = models.CharField(max_length=255, unique=True)
    temperature = models.FloatField()
    pressure = models.FloatField()
    wind_speed = models.FloatField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.city} - Temperature: {self.temperature}°C, Pressure: {self.pressure} mmHg, Wind Speed: {self.wind_speed} m/s'


