from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def fees_django(request):
    return render(request,'fees/feesone.html',context={'title':'Django Fees','cname':'Django','fee':'500'})

    # return HttpResponse(300)
