from django.shortcuts import render
from django.views.generic.edit import FormView,CreateView
from django.views.generic import TemplateView
from .forms import ContactForm
from .models import Student


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
    

class StudentCreateView(CreateView):
    model= Student
    fields ="__all__"
    # success_url='/thankyou/'

    