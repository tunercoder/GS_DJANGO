from django.db import models

# Create your models here.
class Student(models.Model):
    stuid = models.IntegerField()
    stuname = models.CharField(max_length=50)
    stumail = models.EmailField(max_length=70)
    stupass = models.CharField(max_length=50)
    comment = models.CharField(max_length=100,default='Not available')

    def __str__(self):
        return self.stuname