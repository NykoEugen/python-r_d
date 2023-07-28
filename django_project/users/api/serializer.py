from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(min_length=3, max_length=30)
    first_name = serializers.CharField(min_length=5, max_length=30)
    last_name = serializers.CharField(min_length=5, max_length=30)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',)
