from django.conf.urls import url
from . import views

app_name = "jobs"

urlpatterns = [
	url(r'^$', views.jobs, name="jobs"),
]