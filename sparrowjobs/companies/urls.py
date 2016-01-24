from django.conf.urls import url 
from . import views

app_name = "companies"

urlpatterns = [
	url(r'^dashboard/$', views.dashboard, name="dashboard"),
	url(r'^$', views.companies, name="companies"),
	url(r'^company/(?P<id>\d+)/$', views.company, name="company"),
]