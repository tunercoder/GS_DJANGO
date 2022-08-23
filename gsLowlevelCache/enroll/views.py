from functools import cache
from django.shortcuts import render
from django.core.cache import cache
# Create your views here.

# def home(request):
#     # mv=cache.get('movie','expired')
#     # if mv == 'expired':
#     #     cache.set('movie','The Markdown 2',30)
#     #     mv =cache.get('movie')

#     mv=cache.get_or_set('movie','The Enroll 1',30,version=1)
#     return render(request,'enroll/course.html',{'fm':mv})

def home(request):
    data={'name':'sonam','age':30}
    cache.set_many(data,40)
    stu=cache.get_many(data)
    return render(request,'enroll/course.html',{'stu':stu})