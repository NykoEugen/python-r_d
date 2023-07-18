from django.db import models

from books.models import Book
from users.models import User


class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='purchases')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='purchases')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'purchases'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id}. {self.user.username}, {self.book.title}'
