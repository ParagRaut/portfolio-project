from django.shortcuts import render
from .models import Blog

# Create your views here.

def all_blogs(request):
    Blogs = Blog.objects.all()
    context = {'Blogs':Blogs}
    return render(request, 'blogs/all_blogs.html', context)
