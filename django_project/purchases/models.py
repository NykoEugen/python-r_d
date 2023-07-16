from django.db import models

from books.models import Book
from users.models import User


class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    data = models.DateTimeField(null=False)

    class Meta:
        db_table = 'purchases'
        ordering = ['-data']
