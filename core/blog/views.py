from django.shortcuts import render
from django.http import HttpResponse
from . models import Post
# Create your views here.
def home(request):
   post=Post.objects.published_posts()
   context={
       'post':post
   }
   return render(request,'blog/home.html',context)