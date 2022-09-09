from atexit import register
from django.contrib import admin
from .models import Human

@admin.register(Human)
class HumanAdmin(admin.ModelAdmin):
    list_display=['id','msisdn','requestdatetime','smstext']