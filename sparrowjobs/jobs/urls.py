from django.conf.urls import url
from . import views

app_name = "jobs"

urlpatterns = [
	#list all jobs
	url(r'^$', views.index, name="jobs"),
	#get the detail of a job
	url(r'^job/(?P<pk>\d)/$', views.job, name="job"),
	#create a new job
	url(r'^new/$', views.new, name="new")
]