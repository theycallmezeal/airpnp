from django.db import models

class Bathroom(models.Model):
	name = models.CharField(max_length=100)
	urinals = models.PositiveSmallIntegerField()
	stalls = models.PositiveSmallIntegerField()
	handicap_stalls = models.PositiveSmallIntegerField()
	sinks = models.PositiveSmallIntegerField()
	paper_towels = models.PositiveSmallIntegerField()
	hand_dryers = models.PositiveSmallIntegerField()
	windows = models.PositiveSmallIntegerField()
	
	def __str__(self):
		return self.name