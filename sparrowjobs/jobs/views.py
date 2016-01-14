from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from .models import Job
from .forms import JobForm


def index(request):
	'''list and send all jobs
	'''
	jobs = Job.objects.all()
	return render(request, 'jobs/index.html', {'jobs': jobs})


def job(request, pk):
	"""get the detail of job and render
	the template
	"""

	job = get_object_or_404(Job, pk=pk)
	return render(request, 'jobs/job.html', {'job':job})

def new(request):
	if request.method  == "POST":

		form = JobForm(request.POST)
	else:
		form = JobForm()

	return render(request, 'jobs/new.html', {'form': form})

