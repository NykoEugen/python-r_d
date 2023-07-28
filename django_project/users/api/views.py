from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet

from django_project import settings
from users.api.filters import UserFilter
from users.api.pagination import CustomPagination
from users.api.serializer import UserSerializer
from users.models import User


class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    default_filters_backend = settings.REST_FRAMEWORK.get('DEFAULT_FILTER_BACKENDS', [])
    filter_backends = default_filters_backend + [SearchFilter, OrderingFilter]
    filter_class = UserFilter
    searching_field = ('username', 'first_name', 'last_name',)
    ordering_fields = ('id',)
    pagination_class = CustomPagination
