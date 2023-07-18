from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from purchases.models import Purchase


# def purchases_list(request):
#     purchases = Purchase.objects.select_related('user', 'book').\
#         values('user__username', 'book__title', 'book__author', 'book__price', 'created_at')
#     purchases_dict = []
#
#     for item in purchases:
#         created_at = item['created_at']
#         username = item['user__username']
#         title = item['book__title']
#         author = item['book__author']
#         price = item['book__price']
#         purchase = {
#             'user': username,
#             'book': title,
#             'time': created_at,
#             'author': author,
#             'price': price,
#         }
#         purchases_dict.append(purchase)
#
#     return JsonResponse(purchases_dict, safe=False)


class PurchaseListView(ListView):
    model = Purchase

    def get_queryset(self):
        return Purchase.objects.select_related('user', 'book')


class PurchaseDetailView(DetailView):
    model = Purchase
    context_object_name = 'purchase'

    def get_queryset(self):
        return Purchase.objects.select_related('user', 'book')
