from django.shortcuts import render
from .models import Job  # Ensure your Job model exists

def home(request):
    return render(request, 'home.html')

def job_list(request):
    job_title = request.GET.get('job_title', '')  # Get search input
    location = request.GET.get('location', '')

    jobs = Job.objects.all()  # Get all jobs initially

    # Apply filters based on user input
    if job_title:
        jobs = jobs.filter(title__icontains=job_title)  # Case-insensitive search
    
    if location:
        jobs = jobs.filter(location__icontains=location)

    return render(request, 'job_list.html', {'jobs': jobs})