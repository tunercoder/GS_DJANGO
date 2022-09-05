from django.db import models
from core.managers import CustomManager

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=70)
    roll=models.IntegerField()
    fees =models.IntegerField()

    objects=models.Manager() #for default manager
    students=CustomManager() # for cusotmized order by queryset and for range cutomized method
    

