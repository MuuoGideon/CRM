from django.db import models


class Customer(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100, blank=True, null=True)
	email = models.EmailField()
	city = models.CharField(max_length=100)
	phone = models.CharField(max_length=100)
	date = models.CharField(max_length=100, blank=True, null=True)
	image = models.ImageField(blank=True, null=True)

	def __str__(self):
		return self.first_name

