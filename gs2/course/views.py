from django.shortcuts import render

# Create your views here.
def learndjango(request):
    return render(request,'course/courseinfo.html')