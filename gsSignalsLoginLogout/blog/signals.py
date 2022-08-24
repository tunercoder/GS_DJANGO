from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.db.models.signals import pre_delete,pre_init,pre_save,post_delete,post_init,post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

#auth signals 
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
def log_out(sender,request,user,**kwargs):
    print('user user_logged_out===================')
    print('sender details:::',sender)
    print('request is ::: ',request)
    print('user is ::: ',user)
    print('keargs are::::',kwargs)



@receiver(user_login_failed)
def login_failed(sender,credentials,request,**kwargs):
    print('user logged in failed===================')
    print('sender details:::',sender)
    print('request is ::: ',request)
    print('credentials is ::: ',credentials)



#Model retated signals

@receiver(pre_save,sender=User)
def at_begining_save(sender,instance,**kwargs):
    print('user model before save called for model user and signal pre_save===================')
    print('sender details:::',sender)
    print('instance is ::: ',instance)
    print('keargs are::::',kwargs)


@receiver(post_save,sender=User)
def at_ending_save(sender,instance,created,**kwargs):
    if created:
        print('user model after save called new object created for model user and signal post_save===================')
        print('sender details:::',sender)
        print('request is ::: ',instance)
        print('keargs are::::',kwargs)
    else:
        print('user model after save called but update run for model user and signal post_save===================')
        print('sender details:::',sender)
        print('request is ::: ',instance)
        print('keargs are::::',kwargs)


@receiver(pre_delete,sender=User)
def at_begining_delete(sender,instance,**kwargs):
    print('user model before delete called for model user and signal pre_detele===================')
    print('sender details:::',sender)
    print('instance is ::: ',instance)
    print('keargs are::::',kwargs)


@receiver(post_delete,sender=User)
def at_ending_delete(sender,instance,**kwargs):
    print('user model after delete called for model user and signal post_detele===================')
    print('sender details:::',sender)
    print('request is ::: ',instance)
    print('keargs are::::',kwargs)


@receiver(pre_init,sender=User)
def at_begining_init(sender,*args,**kwargs):
    print('user model before init called for model user and signal pre_init===================')
    print('sender details:::',sender)
    print('request is ::: ',args)
    print('keargs are::::',kwargs)


@receiver(post_init,sender=User)
def at_ending_init(sender,*args,**kwargs):
    print('user model after init called for model user and signal pre_init===================')
    print('sender details:::',sender)
    print('request is ::: ',args)
    print('keargs are::::',kwargs)