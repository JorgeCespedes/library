from unittest.util import _MAX_LENGTH
from django.db import models
from author.models import Author
from category.models import Category

# Create your models here.

class Book(models.Model):
    title = models.CharField('Title', max_length=200)
    price = models.FloatField('Price')
    status = models.CharField('Status', max_length=50)
    librero = models.CharField('Librero', max_length=50)

    id_author = models.ForeignKey( Author, on_delete=models.CASCADE)
    id_category = models.ForeignKey( Category, on_delete=models.CASCADE)

    rating = models.CharField('Rating', max_length=10)
    comment = models.CharField('Comment',  max_length=500)

    def __str__(self):
        return self.title