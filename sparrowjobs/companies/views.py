from django.shortcuts import render, get_object_or_404
from .models import Company


def companies(request):
    """list all companies
    """
    companies = Company.objects.all()
    return render(request, 'companies/companies.html', {'companies': companies})


def company(request, id):
    company = get_object_or_404(Company, id=id)
    jobs = company.job_set.all()
    active_jobs = [job for job in jobs if job.status() == "Active"]
    return render(request, 'companies/company.html', {'company': company, 'active_jobs': active_jobs})

def dashboard(request):
    return render(request, 'dashboard/dashboard.html')