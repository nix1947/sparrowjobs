from django.contrib import admin
from .models import Job, JobCategory


class JobAdmin(admin.ModelAdmin):
	list_display = ['title', 'category', 'status', 'expire_at']

admin.site.register(Job, JobAdmin)
admin.site.register(JobCategory)
