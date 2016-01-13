from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import Job
from .forms import JobForm


def jobs(request):
	'''list and send all jobs
	'''
	jobs = Job.objects.all()
	return render(request, 'jobs/jobs.html', {'jobs': jobs})


def new(request):
	if request.method  == "POST":

		form = JobForm(request.POST)
	else:
		form = JobForm()

	return render(request, 'jobs/new.html', {'form': form})

