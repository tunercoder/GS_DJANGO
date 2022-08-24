from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def home(request):
    a=10/0
    return HttpResponse("hello")