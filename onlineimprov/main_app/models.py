from django.db import models

# Create your models here
class Suggestion(models.Model):
	famePerson = models.CharField(max_length=100)
	place = models.CharField(max_length=100)
	weapon = models.CharField(max_length=100)
	guardian = models.CharField(max_length=100)
	audience = models.CharField(max_length=100)

	def __str__(self):
		return self.name