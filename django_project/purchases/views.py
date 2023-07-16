from django.http import JsonResponse
from django.shortcuts import render

from purchases.models import Purchase


def purchases_list(request):
    purchases = Purchase.objects.select_related('user', 'book').\
        values('user__first_name', 'user__last_name', 'user__username',
               'book__title', 'book__author', 'book__price',)
    purchases_dict = []

    for item in purchases:
        first_name = item['user__first_name']
        last_name = item['user__last_name']
        username = item['user__username']
        title = item['book__title']
        author = item['book__author']
        price = item['book__price']
        print(title)
        print(type(title))
        purchase = {
            'user': username,
            'book': title,
        }
        purchases_dict.append(purchase)

    return JsonResponse(purchases_dict, safe=False)
