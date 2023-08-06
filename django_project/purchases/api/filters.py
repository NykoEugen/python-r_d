import django_filters

from purchases.models import Purchase


class PurchaseFilter(django_filters.FilterSet):
    class Meta:
        model = Purchase
        fields = {
            'user__id': ['exact'],
            'book__title': ['exact']
        }
