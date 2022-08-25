from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    print('iam here in view')
    return HttpResponse("This is Home Page")