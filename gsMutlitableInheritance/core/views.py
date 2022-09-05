from django.shortcuts import render
from .models import Student,ExamCenter
# Create your views here.
def db_data(request):
    students=Student.objects.all()
    examcenter=ExamCenter.objects.all()
    
    return render(request,'core/dbdata.html',{'students':students,'examcenter':examcenter})


