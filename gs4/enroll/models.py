from unicodedata import name
from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=80)
    email=models.EmailField()
    password=models.CharField(max_length=80)

    def __str__(self):
        return self.name