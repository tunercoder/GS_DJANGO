from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView

class MyTemplateView(TemplateView):
    template_name='core/home.html'

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['name']='sonam'
        context['age']='21'
        print(context,kwargs)
        context['salary']=kwargs.get('salary')
        return context