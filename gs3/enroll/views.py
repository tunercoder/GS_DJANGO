from mimetypes import init
from wsgiref.util import request_uri
from django.shortcuts import render
from django.http import HttpResponseRedirect
from enroll.models import Student
from .forms import StudentregistrationForm
# Create your views here.
def thankyou(request):
    return render(request,'enroll/success.html')

def studeninfo(request):
    stud = Student.objects.all()
    return render(request,'enroll/studetails.html',{'stu':stud})


def studentRegistration(request):
    print(request.POST)
    if request.method == "POST":
       fm =  StudentregistrationForm(request.POST)
       if fm.is_valid():
        print("form validated cleaned data in dictionart cleaned_data")
        stuid = fm.cleaned_data['stuid']
        name= fm.cleaned_data['name']
        email = fm.cleaned_data['email']
        password = fm.cleaned_data['password']
        comment = fm.cleaned_data['comment']
        stu = Student(stuid=stuid,stuname=name,stumail=email,stupass=password,comment=comment)
        stu.save()
        return HttpResponseRedirect('/enroll/success',{'name':name})
    else:
        fm = StudentregistrationForm(label_suffix='',initial={'comment':'Comment here'})
    # fm.order_fields(field_order=['comment','email','name'])
    # fm = StudentregistrationForm(auto_id='',label_suffix='-',initial={'name':'Enter name here','comment':'Comment here'})
    return render(request,'enroll/studentRegistration.html',{'form':fm})