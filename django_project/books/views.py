from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from books.models import Book


class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'


class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'


class BookCreateView(CreateView):
    model = Book
    template_name = 'books/book_create.html'
    fields = ('title', 'author', 'price',)
    success_url = reverse_lazy('books:book-list')


class BookUpdateView(UpdateView):
    model = Book
    template_name = 'books/book_update.html'
    fields = ('title', 'author', 'price',)


class BookDeleteView(DeleteView):
    model = Book
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy('books:book-list')
    context_object_name = 'book'
