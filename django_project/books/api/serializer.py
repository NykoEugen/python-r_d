from rest_framework import serializers

from books.models import Book


class BookSerializer(serializers.ModelSerializer):
    title = serializers.CharField(min_length=3, max_length=30)
    author = serializers.CharField(min_length=5, max_length=30)
    price = serializers.IntegerField()

    class Meta:
        model = Book
        fields = ('title', 'author', 'price',)

