from unicodedata import name
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=120)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=12)
    date=models.DateField()


    def __str__(self):
        return 'Message from'+' '+ self.name + '-'+self.email