from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import ContactForm
# Create your views here.
def fbv(request):
    return HttpResponse('this is home page by FBV')


class Myview(View):
    name='sonam'
    def get(self,request):   
        return HttpResponse('this is home page by CBV '+self.name.upper())

def home(request):
    return render(request,'core/home.html')

class MyHomeView(View):
    def get(self,request):   
        return render(request,'core/home.html')


def aboutfun(request):
    context={'name':'about fun page from fbv'}
    return render(request,'core/fun.html',context)

class AboutFunView(View):
    def get(self,request):   
        context={'name':'about fun page from CBV'}
        return render(request,'core/fun.html',context)



def contact(request):
    if request.method=="POST":
        form =ContactForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            print(name)
            return HttpResponse('thankyou request has been taken!')
    form =ContactForm()
    return render(request,'core/contact.html',{'form':form})


class ContactView(View):
    def get(self,request):   
        form =ContactForm()
        return render(request,'core/contact.html',{'form':form})
    
    def post(self,request):   
        form =ContactForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            print(name)
            return HttpResponse('thankyou request has been taken!')

def newsfun(request,template_name):
    template_name=template_name
    context={'info':'news breaking hai!!'}
    return render(request,template_name,context)



class NewsFunView(View):
    template_name=''
    def get(self,request):   
        context={'info':'news breaking hai!!'}
        return render(request,self.template_name,context)
    
    