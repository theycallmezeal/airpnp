from django.db import models
from django.shortcuts import get_object_or_404

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

class Rating(models.Model):
	bathroom = models.ForeignKey(Bathroom, on_delete=models.CASCADE)
	cleanliness_rating = models.PositiveSmallIntegerField()
	design_rating = models.PositiveSmallIntegerField()
	
	def __str__(self):
		return str(self.cleanliness_rating) + " star rating for " + self.bathroom.name