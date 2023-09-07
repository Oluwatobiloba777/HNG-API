from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from datetime import datetime
import calendar


def task(request):
    name = request.GET.get('slack_name', 'Oluwatobiloba777')
    track = request.GET.get('track', 'backend')
    utc_time = datetime.now()
    current_day = calendar.day_name[utc_time.weekday()]

    data = {
    "slack_name": name,
    "current_day": current_day,
    "utc_time": utc_time,
    "track": track,
    "github_file_url": "https://github.com/Oluwatobiloba777/HNG-API/blob/main/hngtask/hngapi/views.py",
    "github_repo_url": "https://github.com/Oluwatobiloba777/HNG-API",
    "status_code": 200
}
    return JsonResponse(data, safe=False)