from django.shortcuts import render
from .models import Student
# Create your views here.
def db_data(request):
    
    # std=Student.objects.all()
    std=Student.students.all()
    std=Student.students.get_stu_roll_range(1,2)
    
    return render(request,'core/dbdata.html',{'std':std})


