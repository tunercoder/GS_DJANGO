from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.db.models.signals import pre_delete,pre_init,pre_save,post_delete,post_init,post_save,pre_migrate,post_migrate
from django.core.signals import request_finished,request_started,got_request_exception
from django.db.backends.signals import connection_created
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



#request retated signals

@receiver(request_started)
def at_request_started(sender,environ,**kwargs):
    print(' before request_started called  and signal request_started===================')
    print('sender details:::',sender)
    print('environ details:::',environ)
    print('keargs are::::',kwargs)


@receiver(request_finished)
def at_request_finished(sender,**kwargs):
    print(' after request_finished  and signal request_finished===================')
    print('sender details:::',sender)
    print('keargs are::::',kwargs)

@receiver(got_request_exception)
def at_got_request_exception(sender,request,**kwargs):
    print(' got_request_exception called and signal got_request_exception===================')
    print('sender details:::',sender)
    print('request is ::: ',request)
    print('keargs are::::',kwargs)

#management signals for migrations

@receiver(pre_migrate)
def at_pre_migrate(sender, app_config, verbosity, interactive, using, plan, apps,**kwargs):
    print(' before pre_migrate called  and signal pre_migrate===================')
    print('sender details:::',sender)
    print('app_config details:::',app_config)
    print('verbosity details:::',verbosity)
    print('app_config details:::',app_config)
    print('interactive are::::',interactive)
    print('using details:::',using)
    print('plan details:::',plan)
    print('apps are::::',apps)
    print('kwargs are::::',kwargs)


@receiver(post_migrate)
def at_post_migrate(sender, app_config, verbosity, interactive, using, plan, apps,**kwargs):
    print(' after post_migrate  and signal post_migrate===================')
    print('sender details:::',sender)
    print('app_config details:::',app_config)
    print('verbosity details:::',verbosity)
    print('app_config details:::',app_config)
    print('interactive are::::',interactive)
    print('using details:::',using)
    print('plan details:::',plan)
    print('apps are::::',apps)
    print('kwargs are::::',kwargs)


#databse wrapper signals sent by the database wrapper when a database connection is initiated.

@receiver(connection_created)
def at_connection_created(sender,connection,**kwargs):
    print(' before connection_created called  and signal connection_created===================')
    print('sender details:::',sender)
    print('connection details:::',connection)
    print('kwargs are::::',kwargs)
