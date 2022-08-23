from django.contrib import admin

from .models import Student

# Register your models here.
#1 way
# admin.site.register(Student)

#by decorator
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('stuid','stuname','stumail','stupass','comment')

#Without decorator
# admin.site.register(Student,StudentAdmin)