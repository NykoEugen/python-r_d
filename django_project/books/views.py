from django.http import JsonResponse
from django.shortcuts import render

from books.models import Book


def books_list(request):
    books = Book.objects.all()
    books_dict = []
    for item in books:
        id = item.id
        title = item.title
        author = item.author
        price = item.price
        book = {
            'id': id,
            'title': title,
            'author': author,
            'price': price,
        }
        books_dict.append(book)
    return JsonResponse(books_dict, safe=False)
