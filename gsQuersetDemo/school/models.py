from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    roll = models.IntegerField(unique=True,null=False)
    city = models.CharField(max_length=70)
    marks = models.IntegerField()
    pass_date = models.DateField()

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=50)
    empnum = models.IntegerField(unique=True,null=False)
    city = models.CharField(max_length=70)
    salary = models.IntegerField()
    join_date = models.DateField()