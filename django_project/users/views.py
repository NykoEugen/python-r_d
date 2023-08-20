from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from users.models import User
from users.tasks import print_message, count_purchase


class UserListView(ListView):
    model = User
    template_name = 'users/user_list.html'

    def get_queryset(self):
        print_message.delay()
        return super().get_queryset()


class UserDetailView(DetailView):
    model = User
    template_name = 'users/user_detail.html'
    context_object_name = 'user'
    print_message.delay()


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
