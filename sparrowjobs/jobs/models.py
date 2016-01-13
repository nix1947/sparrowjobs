from django.db import models
from django.utils import timezone
from core.models import TimeStampedModel
from companies.models import Company

class JobCategory(TimeStampedModel):
	cat_name = models.CharField('job category name', max_length=255)
	description = models.TextField()

	def __str__(self):
		return self.cat_name

	class Meta:
		verbose_name_plural = "Job Categories"

	

class Job(TimeStampedModel):
	
	LEVEL=(
		('entry', 'entry'),
		('intermediate', 'intermediate'),
		('expert', 'expert'),
	)

	title = models.CharField('job title', max_length=255, null=False)
	summary = models.CharField('job summary',max_length=255)
	description = models.TextField()
	requirements = models.TextField()
	category = models.ForeignKey(JobCategory)
	job_level = models.CharField('job level', max_length=12, choices=LEVEL, default='entry')
	vacencies = models.IntegerField(default=0)
	location = models.CharField(max_length=255)
	salary	= models.CharField('Salary', max_length=255, default="negotiable")
	expire_at = models.DateTimeField()
	other_info = models.TextField('other information')
	company = models.ForeignKey(Company, default="")
	def status(self):
		if  (self.expire_at - timezone.now()).days <= 0:
			return True
		else:
			return False

	status.short_description = "Job status"
	status.boolean = True

	def __str__(self):
		return	self.title






