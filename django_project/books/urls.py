from django.urls import path
from rest_framework.routers import SimpleRouter

from books import views
from books.api import views as api_views

app_name = 'books'

urlpatterns = [
    path('', views.BookListView.as_view(), name='book-list'),
    path('<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('create/', views.BookCreateView.as_view(), name='book-create'),
    path('<int:pk>/update/', views.BookUpdateView.as_view(), name='book-update'),
    path('<int:pk>/delete/', views.BookDeleteView.as_view(), name='book-delete'),
]

router = SimpleRouter()
router.register('api', api_views.BookModelViewSet)

urlpatterns += router.urls
