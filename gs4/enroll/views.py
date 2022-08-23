import re
from django.shortcuts import render
from .models import User
from .forms import UserRegisterationForm
from django.http import HttpResponseRedirect
from django.contrib import messages
# Create your views here.

def home(request,check):
    user=User.objects.all()
    print(check)
    return render(request,'enroll/home.html',{'user':user})


def userdetail(request,id=1):
    user=User.objects.get(pk=id)
    return render(request,'enroll/userdetails.html',{'user':user})

def userreg(request):
    # user=User.objects.get(pk=1) #for update first get instance and supply during form object creation
    fm = UserRegisterationForm()
    if request.method == "POST":
        details = UserRegisterationForm(request.POST)
        #for update add insatance to details = UserRegisterationForm(request.POST,instance=user)
        if details.is_valid():
            #details.save() for update directly save form object
            name=details.cleaned_data['name']
            email=details.cleaned_data['email']
            password=details.cleaned_data['password']
            print(name,email,password)
            reg=User(name=name,email=email,password=password)
            reg.save()
            messages.add_message(request,messages.SUCCESS,'user successfully saved ')
            print(messages.get_level(request))
            # messages.success(request,'user successfully saved in database')
            return HttpResponseRedirect('/enroll/success/')
    return render(request,'enroll/user.html',{'form':fm})


def success(request):
    return render(request,'enroll/success.html')
