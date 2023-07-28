from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from users.models import User


class UserListView(ListView):
    model = User
    template_name = 'users/user_list.html'


class UserDetailView(DetailView):
    model = User
    template_name = 'users/user_detail.html'
    context_object_name = 'user'


class UserCreateView(CreateView):
    model = User
    template_name = 'users/user_create.html'
    fields = ('username', 'password', 'email', 'first_name', 'last_name',)
    success_url = reverse_lazy('users:user-list')


class UserUpdateView(UpdateView):
    model = User
    template_name = 'users/user_update.html'
    fields = ('email', 'first_name', 'last_name',)


class UserDeleteView(DeleteView):
    model = User
    template_name = 'users/user_delete.html'
    success_url = reverse_lazy('users:user-list')
    context_object_name = 'user'
