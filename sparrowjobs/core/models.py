from django.db import models
from django.utils import timezone
from datetime import timedelta

class TimeStampedModel(models.Model):
	"""
	An abstract base class model that provide self-updateing
	created_at and update_at field
	"""
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True