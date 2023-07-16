import datetime
from datetime import time

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from users.models import User


# Create your views here.
def users_list(request):
    users = User.objects.all()
    users_dict = []
    for item in users:
        id = item.id
        username = item.username
        email = item.email
        timestamp = item.date_joined
        # date = datetime.datetime.fromtimestamp(timestamp)
        # formated_date = date.strftime('%Y-%m-%d %H:%M:%S')
        first_name = item.first_name
        last_name = item.last_name
        print(timestamp)
        user = {'id': id,
                'username': username,
                'email': email,
                # 'date': formated_date,
                'first_name': first_name,
                'last_name': last_name,
                }
        users_dict.append(user)
    return JsonResponse(users_dict, safe=False)
