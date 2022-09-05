from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    # user= models.OneToOneField(User,on_delete=models.PROTECT,primary_key=True,limit_choices_to={'is_staff':True})
    post_title=models.CharField(max_length=70)
    post_cat=models.CharField(max_length=70)
    post_publish_date=models.DateField()



class Song(models.Model):
    user= models.ManyToManyField(User)
    song_name=models.CharField(max_length=70)
    song_duration=models.IntegerField()

    def written_by(self):
        return ','.join([str(p) for p in self.user.all()])
        

