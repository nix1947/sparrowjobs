from django.db import models

class Address(models.Model):
	COUNTRY = (
		("Nepal", "Nepal"),
	)
	STATE = (
		("Bagmati", "BAGMATI"),
	)
	CITY = (
		("kathamdnu", "Kathmandu"),
	)
	country = models.CharField(max_length=50, choices=COUNTRY, default="Nepal")
	state = models.CharField(max_length=100, choices=STATE, default="Bagmati")
	city = models.CharField(max_length=255, choices=CITY, default="Kathmandu")
	address1 = models.CharField(max_length=255)
	address2 = models.CharField(max_length=255)
	address3 = models.CharField(max_length=255)

	class Meta:
		verbose_name_plural = "Addresses"

	def __str__(self):
		return self.city