from django.shortcuts import render

from .models import Job

# Create your views here.

def home_page(request):
    Jobs = Job.objects
    context = {'Jobs':Jobs}
    return render(request, 'jobs/home_page.html', context)
