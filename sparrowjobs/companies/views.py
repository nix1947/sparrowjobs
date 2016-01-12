from django.shortcuts import render
from .models import Company

def companies(request):
	"""list all companies
	"""
	companies = Company.objects.all()
	return render(request, 'companies/companies.html', {'companies': companies})
