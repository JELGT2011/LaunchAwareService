
from django.db import models


class AppLaunch(models.Model):
    package_name = models.CharField(max_length=80)
    launch_time = models.DateTimeField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    wifi_SSID = models.CharField(max_length=80)


