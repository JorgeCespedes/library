from unicodedata import category
from django.db import models

class Category(models.Model):
    category = models.CharField('Category', max_length=100)
    
    def __str__(self):
        return self.category