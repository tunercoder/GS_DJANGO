from django.shortcuts import render
from .models import Student,Teacher,Contractor
# Create your views here.
def db_data(request):
    students=Student.objects.all()
    teachers=Teacher.objects.all()
    contractors=Contractor.objects.all()
    print(contractors)
    return render(request,'core/dbdata.html',{'students':students,'teachers':teachers,'contractors':contractors})


