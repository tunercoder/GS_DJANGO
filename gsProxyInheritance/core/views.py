from django.shortcuts import render
from .models import ExamCenter,MyExamCenter
# Create your views here.
def db_data(request):
    
    examcenter=ExamCenter.objects.all()
    myexamcenter=MyExamCenter.objects.all()
    
    return render(request,'core/dbdata.html',{'myexamcenter':myexamcenter,'examcenter':examcenter})


