import django_filters

from purchases.models import Purchase


class PurchaseFilter(django_filters.FilterSet):
    class Meta:
        model = Purchase
        fields = {
            'created_at': ['exact', 'lte', 'gte'],
        }
