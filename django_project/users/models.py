from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse_lazy


class User(AbstractUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    class Meta:
        db_table = 'users'
        verbose_name = 'Super user'
        verbose_name_plural = 'Super users'

    def get_absolute_url(self):
        return reverse_lazy('users:user-detail', kwargs={'pk': self.id})
