from django.urls import path

from purchases import views

urlpatterns = [
    path('', views.PurchaseListView.as_view(), name='purchase-list'),
    path('<int:pk>', views.PurchaseDetailView.as_view(), name='purchase-detail')
]