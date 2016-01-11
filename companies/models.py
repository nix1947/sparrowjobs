from django.db import models
from address.models import Address

class Industry(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()

	class Meta:
		verbose_name_plural = "Industries"

	def __str__(self):
		return self.name

class Company(models.Model):
	name = models.CharField(max_length=255)
	overview = models.TextField('company overview')
	description = models.TextField('description')
	# logo = models.ImageField()
	industry = models.ForeignKey(Industry)
	website = models.URLField()
	telephone = models.CharField(max_length=10)
	company_size = models.CharField(max_length=6, blank=True, default="10-20")
	why_jon_us = models.TextField('Why join us')
	address = models.ForeignKey(Address, default="")
	# processing_time = models.IntegerField('processing days', default=15)

	class Meta:
		verbose_name_plural = 'Companies'

	def __str__(self):
		return self.name