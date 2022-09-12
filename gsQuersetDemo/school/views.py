
from django.shortcuts import render
from school.models import Student, Teacher
from django.db.models import Q


def student_list(request):
    # qs = Student.objects.all() # return list of objects <QuerySet [<Student: Student object (1)>, <Student: Student object (2)>,<Student: Student object (3)>]>
    
    # qs = Student.objects.filter(name='chiku')
    # qs = Student.objects.exclude(name='chiku')
    
    # qs = Student.objects.order_by('name')
    # qs = Student.objects.order_by('-name')
    # qs = Student.objects.order_by('?')
    # qs = Student.objects.order_by('name').reverse() #works only with order by clause
    
    # qs1 = Student.objects.values() #returns list of dictionary <QuerySet [{'id': 1, 'name': 'tinu', 'roll': 1, 'city': 'dehradun', 'marks': 2, 'pass_date': datetime.date(2022, 8, 1)}, {'id': 2, 'name': 'chiku', 'roll': 2, 'city': 'dun', 'marks': 5, 'pass_date': datetime.date(2022, 8, 2)}, {'id': 3, 'name': 'chintu', 'roll': 3, 'city': 'delhi', 'marks': 2, 'pass_date': datetime.date(2022, 8, 2)}]>
    # qs1 = Student.objects.values('name','roll') 
   
    # qs = Student.objects.distinct() 
    
    # qs = Student.objects.values_list(named=True) # returns list of tuple <QuerySet [(1, 'tinu', 1, 'dehradun', 2, datetime.date(2022, 8, 1)), (2, 'chiku', 2, 'dun', 5, datetime.date(2022, 8, 2)), (3, 'chintu', 3, 'delhi', 2, datetime.date(2022, 8, 2))]>
    # qs = Student.objects.values_list('name','marks')#<QuerySet [('tinu', 2), ('chiku', 5), ('chintu', 2)]>
    # qs = Student.objects.values_list('name','marks',named=True)# <QuerySet [Row(name='tinu', marks=2), Row(name='chiku', marks=5), Row(name='chintu', marks=2)]>
    # qs = Student.objects.values_list('name')# <QuerySet [('tinu',), ('chiku',), ('chintu',)]>
    # qs = Student.objects.values_list('name',flat=True)# <QuerySet ['tinu', 'chiku', 'chintu']>
    # qs = Student.objects.using('default') #used for which database to be used in case of multiple DB defult as in DAtabase option in setting file
    # qs=Student.objects.dates('pass_date',kind='day',order='ASC')# <QuerySet [datetime.date(2022, 8, 1), datetime.date(2022, 8, 2)]>
    # qs=Student.objects.none()

    # qs1=Student.objects.values_list('id','name','roll',named=True)
    # qs2=Teacher.objects.values_list('id','name','empnum',named=True)
    # qs= qs1.union(qs2,all=True)


    # qs1=Student.objects.values_list('id','name',named=True)
    # qs2=Teacher.objects.values_list('id','name',named=True)
    # qs= qs1.intersection(qs2)

    # qs1=Student.objects.values_list('id','name',named=True)
    # qs2=Teacher.objects.values_list('id','name',named=True)
    # qs= qs1.difference(qs2)


    #####################AND and OR operator############################

    # qs=Student.objects.filter(name='chiku') & Student.objects.filter(roll=2)  
    # qs=Student.objects.filter(name='chiku',roll=2)
    # qs=Student.objects.filter(Q(name='chiku') & Q(roll=2))  

    # qs=Student.objects.filter(name='chiku') | Student.objects.filter(roll=1)
    qs=Student.objects.filter(Q(name='chiku') | Q(roll=1))  

    qs=Student.objects.all().order_by('-pass_date__week_day')


    

    print(qs.query,qs)
    return render(request,'school/studentall.html',{'students':qs})