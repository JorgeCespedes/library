from email.policy import default
from django.db import models

class Author(models.Model):

    full_name = models.CharField('Full name', max_length=120, default='None')
    
    def __str__(self):
        return self.full_name