from django.db import models
from django.urls import reverse_lazy


class Book(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    price = models.IntegerField()

    class Meta:
        db_table = 'books'
        unique_together = ['title', 'author']

    def __str__(self):
        return f'{self.title}, {self.author}, {self.price}'

    def get_absolut_url(self):
        return reverse_lazy('books:book-detail', kwargs={'pk': self.id})
