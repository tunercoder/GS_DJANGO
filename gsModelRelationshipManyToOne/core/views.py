from django.shortcuts import render
from .models import Post
# Create your views here.
def home(request):
    post = Post.objects.all() 
    return render(request,'core/data.html',{'post':post})