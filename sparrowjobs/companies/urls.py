from django.conf.urls import url 
from . import views

app_name = "companies"

urlpatterns = [
	url(r'^$', views.companies, name="companies")
]