from django.http import HttpResponse
import json

import LaunchAwareService.models

AppLaunch = LaunchAwareService.models.AppLaunch


def index(request):
    return HttpResponse("Hello world!")


def app_launch(request):
    launch_json = json.loads(request.body)
    package_name = launch_json['packageName']
    launch_time = launch_json['launchTime']
    latitude = launch_json['locationInfo']['latitude']
    longitude = launch_json['locationInfo']['longitude']
    wifi_SSID = launch_json['wifiSSId']

    app_launch_data = AppLaunch(
        package_name, launch_time, latitude, longitude, wifi_SSID
    )
    app_launch_data.save()

    return HttpResponse(package_name + ' ' + launch_time)
