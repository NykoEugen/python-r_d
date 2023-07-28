from django.urls import path
from rest_framework.routers import SimpleRouter

from users import views
from users.api import views as api_views

app_name = 'users'

urlpatterns = [
    path('', views.UserListView.as_view(), name='user-list'),
    path('<int:pk>', views.UserDetailView.as_view(), name='user-detail'),
    path('create/', views.UserCreateView.as_view(), name='user-create'),
    path('<int:pk>/update/', views.UserUpdateView.as_view(), name='user-update'),
    path('<int:pk>/delete/', views.UserDeleteView.as_view(), name='user-delete'),
]

router = SimpleRouter()
router.register('api', api_views.UserModelViewSet)

urlpatterns += router.urls
