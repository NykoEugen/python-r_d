from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet

from books.api.filters import BookFilter
from books.api.serializer import BookSerializer
from books.models import Book
from django_project import settings


class BookModelViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    default_filters_backend = settings.REST_FRAMEWORK.get('DEFAULT_FILTER_BACKENDS', [])
    filter_backends = default_filters_backend + [SearchFilter, OrderingFilter]
    filter_class = BookFilter
    search_fields = ('title', 'author',)
    ordering_fields = ('-id',)
