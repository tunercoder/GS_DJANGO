import re
from django.shortcuts import render,HttpResponseRedirect
from django.contrib import messages
from .forms import SignUpForm,UserProfileForm,AdminProfileForm
from django.contrib.auth.forms import AuthenticationForm,SetPasswordForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash

# Create your views here.

def signup(request):
    form=SignUpForm()
    if request.method=="POST":
        fm=SignUpForm(request.POST)
        if fm.is_valid():
            # username=fm.cleaned_data['username']
            fm.save()
            messages.success(request,'user successfully saved in db')
            return HttpResponseRedirect('/gsauth/success/')
        else:
            form=SignUpForm()
    return render(request,'gsauth/signup.html',{'form':form})

def success(request):
    return render(request,'gsauth/success.html')

def profile(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            if request.user.is_superuser:
                fm=AdminProfileForm(instance=request.user)
            else:
                fm=UserProfileForm(instance=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request,'profile updatd successfully!')
                return HttpResponseRedirect('/gsauth/profile/')
        else:
            if request.user.is_superuser:
                fm=AdminProfileForm(instance=request.user)
            else:
                fm=UserProfileForm(instance=request.user)
            return render(request,'gsauth/profile.html',{'name': request.user.username,'form':fm})
    return HttpResponseRedirect('/gsauth/login/')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/gsauth/login/')

def user_change_pass(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm=PasswordChangeForm(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                messages.success(request,'password changed successfully!')
                return HttpResponseRedirect('/gsauth/profile/')
        else:
            fm=PasswordChangeForm(user=request.user)
            return render(request,'gsauth/changepass.html',{'form':fm})

    return HttpResponseRedirect('/gsauth/login/')
    
def user_change_pass1(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm=SetPasswordForm(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                messages.success(request,'password changed successfully!')
                return HttpResponseRedirect('/gsauth/profile/')
        else:
            fm=SetPasswordForm(user=request.user)
            return render(request,'gsauth/changepass1.html',{'form':fm})

    return HttpResponseRedirect('/gsauth/login/')
    


def user_login(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            fm=AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                pword=fm.cleaned_data['password']
                user= authenticate(username=uname,password=pword)
                if user is not None:
                    login(request,user)
                    messages.success(request,'user successfully authenticated')
                    return HttpResponseRedirect('/gsauth/profile/')
        fm=AuthenticationForm()
        return render(request,'gsauth/login.html',{'form':fm})
    else:
        return HttpResponseRedirect('/gsauth/profile/')