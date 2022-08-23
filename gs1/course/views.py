from ssl import HAS_TLSv1_1
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    page = render(request,'course/course.html',context={'course':'home1 page'})
    print(page)
    return page

def learn_django(request):
    return render(request,'course/courseone.html',context={'title':'Learn Django','cname':'Django'})
    # return HttpResponse('Hello django')


def learn_python(request):
    return render(request,'course/coursetwo.html',context={'title':'Learn Python','cname':'Python'})
    # return HttpResponse('<h3>hello python</h3>')