from django.db import models

class Bathroom(models.Model):
	name = models.CharField(max_length=100)
	urinals = models.PositiveSmallIntegerField()
	
	def __str__(self):
		return self.name