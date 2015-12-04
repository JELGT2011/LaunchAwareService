
from django.http import HttpResponse
import json
from datetime import datetime

import LaunchAwareService.models

AppLaunch = LaunchAwareService.models.AppLaunch


def index(request):
    return HttpResponse("Hello world!")


def app_launch(request):

    launch_json = json.loads(request.body)

    package_name = str(launch_json['packageName'])
    launch_time = datetime.strptime(launch_json['launchTime'], '%b %d, %Y %I:%M:%S %p')
    latitude = float(launch_json['locationInfo']['latitude'])
    longitude = float(launch_json['locationInfo']['longitude'])
    wifi_SSID = str(launch_json['wifiSSId'])

    app_launch_data = AppLaunch(
        package_name=package_name,
        launch_time=str(launch_time),
        latitude=latitude,
        longitude=longitude,
        wifi_SSID=wifi_SSID
    )
    app_launch_data.save()

    return HttpResponse(package_name + ' ' + str(launch_time))
