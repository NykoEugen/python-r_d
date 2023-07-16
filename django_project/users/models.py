from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    first_name = models.TextField()
    last_name = models.TextField()

    class Meta:
        db_table = 'users'
