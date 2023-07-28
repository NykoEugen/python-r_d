from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet

from django_project import settings
from purchases.api.filters import PurchaseFilter
from purchases.api.serializers import PurchaseSerializer
from purchases.models import Purchase


class PurchaseModelViewSet(ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    default_filters_backend = settings.REST_FRAMEWORK.get('DEFAULT_FILTER_BACKENDS', [])
    filter_backends = default_filters_backend + [SearchFilter, OrderingFilter]
    filter_class = PurchaseFilter
    search_fields = ('user__username', 'book__title', 'created_at',)
    ordering_fields = ('-id',)
