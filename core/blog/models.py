from tabnanny import verbose
from turtle import update
from django.db import models
from django.contrib.auth.models import User
from pytz import timezone
from django.utils import timezone
from django.urls import reverse
# Create your models here.
# managers

class PostManager(models.Manager):
    def published_posts(self):
        return self.filter(status='p')


class Post(models.Model):
    STATUS_CHOICES = (
        ('d','draft_date'),
        ('p','published_date'),
        
    )
    title = models.CharField(max_length=200)
    slug=models.SlugField(max_length=200, unique=True)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    status=models.CharField(max_length=1, choices=STATUS_CHOICES, default='draft_date')
    objects = PostManager()
    
    def get_absolute_url(self):
        return reverse('blog:post_detail', args={'slug': self.slug})
    
    class Meta:
        ordering = ['-published_date']
        verbose_name_plural = 'Posts'
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    