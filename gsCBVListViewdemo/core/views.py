from urllib import request
from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Student

class StudentListView(ListView):
    model = Student
    template_name_suffix='_set' #for changing suffix of default html file
    ordering=['name']
    # template_name='core/home.html'
    context_object_name='allstudent'

    def get_queryset(self):#to modify existing queryset
        # return Student.objects.filter(name__istartswith='s')
        return Student.objects.all()

    def get_context_data(self, **kwargs): #modification in context dictionary content can be done here
        context = super().get_context_data(**kwargs)
        context["freshers"] = Student.objects.filter(name='rena')
        return context
    
    def get_template_names(self):#condition based template rendering for different cases can be held here
        if self.request.user.is_superuser:
            template='core/home.html'
        else:
            template='core/student_set.html'

        return [template]

class StudentDetailView(DetailView):  
    model=Student  
    # context_object_name = stu 
    # template_name='core/home.html' 
    #pk_url_kwarg='id' change by default pk or slug paramter in url


    def get_context_data(self, **kwargs): #modification in context dictionary content can be done here
        context = super().get_context_data(**kwargs)
        
        context["all_other"] = Student.objects.all()
        return context