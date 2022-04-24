from pydoc import pager
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from . models import Post
# Create your views here.
def home(request):
   post=Post.objects.published_posts()
   Paginator=Paginator(Post.objects.published_posts(),1)
   page=request.GET.get('page')
           
   context={
       'posts':post
   }
   return render(request,'blog/home.html',context)


def post_detail(request,slug):
    
    post=get_object_or_404(Post,slug=slug,status='p')
    context={
        'post':post
    }
    return render(request,'blog/post_detail.html',context)
