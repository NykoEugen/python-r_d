from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=20)
    last_name = serializers.CharField(max_length=20)

    class Meta:
        model = User
        fields = ('username', 'email',
                  'date_joined', 'first_name', 'last_name',)
        read_only_fields = ('date_joined',)
