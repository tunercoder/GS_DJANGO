from django.shortcuts import render,HttpResponse
from django.template.response import TemplateResponse

# Create your views here.
def home(request):
    print('iam here in home view')
    return HttpResponse("This is Home Page")


def exc(request):
    # a=100/0
    print('iam here in exc view')
    return HttpResponse("This is exc Page")

def user_info(request):
    context={'name':'Ashish'}
    print('iam here in user_info view')
    return TemplateResponse(request,'blog/userinfo.html',context)