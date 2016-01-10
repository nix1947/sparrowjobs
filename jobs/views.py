from django.shortcuts import render
from .models import Job


def jobs(request):
	'''list and send all jobs
	'''
	jobs = Job.objects.all()
	return render(request, 'jobs/jobs.html', {'jobs': jobs})

