from django.shortcuts import render
from .models import Job

# Create your views here.
def job_list(request):
    all_jobs = Job.objects.all()
    return render(request, 'job/job_list.html', {'jobs':all_jobs})

def job_detail(request, slug):
    job = Job.objects.get(slug=slug)
    return render(request, 'job/job_detail.html', {'job':job})