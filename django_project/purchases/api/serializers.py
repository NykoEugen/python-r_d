from rest_framework import serializers

from books.api.serializer import BookSerializer
from purchases.models import Purchase
from users.api.serializer import UserSerializer


class PurchaseSerializer(serializers.ModelSerializer):
    book = BookSerializer()
    user = UserSerializer()

    class Meta:
        model = Purchase
        fields = ['id', 'user', 'book', 'created_at', ]

