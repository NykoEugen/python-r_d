from django.db import models


class Book(models.Model):
    title = models.TextField()
    author = models.TextField()
    price = models.TextField()

    class Meta:
        db_table = 'books'
        unique_together = ['title', 'author']
