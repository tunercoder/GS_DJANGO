from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver

@receiver(user_logged_in,sender=User)
def login_success(sender,request,user,**kwargs):
    print('user logged in success===================')
    print('sender details:::',sender)
    print('request is ::: ',request)
    print('user is ::: ',user)
    print('user name is ::: ',user.username)
    print('keargs are::::',kwargs)

# user_logged_in.connect(login_success,sender=User)

@receiver(user_logged_out,sender=User)
def login_success(sender,request,user,**kwargs):
    print('user user_logged_out===================')
    print('sender details:::',sender)
    print('request is ::: ',request)
    print('user is ::: ',user)
    print('keargs are::::',kwargs)



@receiver(user_login_failed)
def login_success(sender,credentials,request,**kwargs):
    print('user logged in failed===================')
    print('sender details:::',sender)
    print('request is ::: ',request)
    print('credentials is ::: ',credentials)