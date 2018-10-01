from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.

def all_blogs(request):
    Blogs = Blog.objects.all()
    context = {'Blogs':Blogs}
    return render(request, 'blogs/all_blogs.html', context)

def blog_detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    context = {'blog':blog_detail}
    return render(request, 'blogs/blog_details.html', context)
