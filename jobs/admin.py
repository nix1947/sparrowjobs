from django.contrib import admin
from .models import Job, JobCategory

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
	# change_form_template = 'fun/admin/change_form.html'
	list_display = ['title', 'category', 'status', 'expire_at']
	search_fields = ('title',)

@admin.register(JobCategory)
class JobAdmin(admin.ModelAdmin):
	list_display = ('cat_name',)


