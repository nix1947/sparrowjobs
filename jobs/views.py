from django.shortcuts import render
from .models import Job


def index(request):
	'''list and send all jobs
	'''
	jobs = Job.objects.all()
	return render(request, 'jobs/index.html', {'jobs': jobs})

