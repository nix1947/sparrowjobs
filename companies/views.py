from django.shortcuts import render
from .models import Company

def index(request):
	"""list all companies
	"""
	companies = Company.objects.all()
	return render(request, 'companies/index.html', {'companies': companies})
