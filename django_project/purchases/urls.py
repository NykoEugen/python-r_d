from django.urls import path
from rest_framework.routers import SimpleRouter

from purchases import views
from purchases.api import views as api_views

app_name = 'purchases'

urlpatterns = [
    path('', views.PurchaseListView.as_view(), name='purchase-list'),
    path('<int:pk>', views.PurchaseDetailView.as_view(), name='purchase-detail'),
    path('create/', views.PurchaseCreateView.as_view(), name='purchase-create'),
    path('<int:pk>/update/', views.PurchaseUpdateView.as_view(), name='purchase-update'),
    path('<int:pk>/delete/', views.PurchaseDeleteView.as_view(), name='purchase-delete'),
]

router = SimpleRouter()
router.register('api', api_views.PurchaseModelViewSet)

urlpatterns += router.urls
