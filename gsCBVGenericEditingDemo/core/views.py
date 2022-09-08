from django.shortcuts import render
from django.views.generic.edit import FormView,CreateView
from django.views.generic import TemplateView,UpdateView,DeleteView
from .forms import ContactForm
from .models import Student
from django import forms
from .forms import StudentForm


class ContactFormView(FormView):
    template_name='core/contact.html'
    form_class = ContactForm
    success_url='/thankyou/'
    initial= {'name':'Dummy'}

    def form_valid(self, form):
        print(form)
        print(form.cleaned_data['name'])
        print(form.cleaned_data['email'])
        return super().form_valid(form)

class ThankyouView(TemplateView):
    template_name='core/thankyou.html'
    

# class StudentCreateView(CreateView):
#     model= Student
#     fields ="__all__"
#     # success_url='/thankyou/'

#     def get_form(self):#used to add any form field classes attributes same as form and modelform
#         form =super().get_form()
#         form.fields['name'].widget=forms.TextInput(attrs={'class':"myclass"})
#         form.fields['password'].widget=forms.PasswordInput(attrs={'class':"myclass"})
#         return form


#second way to define form is by using model form and in this case we are applying same classes on fields of form by model form
class StudentCreateView(CreateView):
    form_class=StudentForm
    template_name='core/student_form.html'
    success_url='/thankyou/'

class StudentUpdateView(UpdateView):
    model= Student
    fields ="__all__"
    success_url='/thankyou/'

class StudentDeleteView(DeleteView):
    model= Student
    success_url='/studentcreate/'

    