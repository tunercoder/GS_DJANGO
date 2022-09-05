from atexit import register
from django.contrib import admin

# Register your models here.
from .models import Student,Teacher,Contractor


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','age','fees']

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display=['id','name','age','salary','date']

@admin.register(Contractor)
class ContractorAdmin(admin.ModelAdmin):
    list_display=['id','name','age','payment','date']