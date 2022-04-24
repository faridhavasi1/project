from django import views
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('post/<slug:slug>', views.post_detail, name='post_detail'),
]


    