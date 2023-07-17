import datetime
from datetime import time

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from users.models import User


# Create your views here.
def users_list(request):
    users = User.objects.all().values()
    users_dict = []
    for item in users:
        pk = item['id']
        username = item['username']
        email = item['email']
        timestamp = item['date_joined']
        first_name = item['first_name']
        last_name = item['last_name']
        print(timestamp)
        user = {'id': pk,
                'username': username,
                'email': email,
                'date': timestamp,
                'first_name': first_name,
                'last_name': last_name,
                }
        users_dict.append(user)
    return JsonResponse(users_dict, safe=False)
