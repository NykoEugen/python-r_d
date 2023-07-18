from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from books.models import Book


# def books_list(request):
#     books = Book.objects.all().values()
#     books_dict = []
#     for item in books:
#         pk = item['id']
#         title = item['title']
#         author = item['author']
#         price = item['price']
#         book = {
#             'id': pk,
#             'title': title,
#             'author': author,
#             'price': price,
#         }
#         books_dict.append(book)
#     return JsonResponse(books_dict, safe=False)


class BookListView(ListView):
    model = Book


class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'
