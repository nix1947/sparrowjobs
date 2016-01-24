from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from .models import Job
from .forms import JobForm
from django.db.models import Q


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


def search(request):
	if request.method == "GET":

		search_terms = request.GET.get('title', False)
		search_location = request.GET.get('location', False)

		if search_terms or search_location:
			search_terms = search_terms.split(',')
			search_location = search_location.split(',')
			search_terms = set(search_terms) #remove duplicates
			search_location = set(search_location)
			title_query_args = [Q(title__contains=word) for word in search_terms ]
			location_query_args = [Q(location__contains=l) for l in search_location]
			jobs = Job.objects.filter(*title_query_args).filter(*location_query_args)
			return	render(request, 'jobs/index.html', {'jobs':jobs})

		else:
			return	render(request, 'jobs/index.html', {'jobs':None})





