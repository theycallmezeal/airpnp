from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

class Location(models.Model):
	human_readable_location = models.CharField(max_length=100)
	google_maps_link = models.CharField(max_length=50)
	google_maps_embed = models.CharField(max_length=500)
	
	def __str__(self):
		return self.human_readable_location

class Bathroom(models.Model):
	name = models.CharField(max_length=100)
	gender = models.PositiveSmallIntegerField() # 0 = male; 1 = female; 2 = gender-neutral
	urinals = models.PositiveSmallIntegerField()
	stalls = models.PositiveSmallIntegerField()
	handicap_stalls = models.PositiveSmallIntegerField()
	sinks = models.PositiveSmallIntegerField()
	paper_towels = models.PositiveSmallIntegerField()
	hand_dryers = models.PositiveSmallIntegerField()
	windows = models.PositiveSmallIntegerField()
	
	location = models.ForeignKey(Location, on_delete=models.CASCADE)
	location_desc = models.CharField(max_length=300, blank=True)
	
	def __str__(self):
		return self.name

class Rating(models.Model):
	bathroom = models.ForeignKey(Bathroom, on_delete=models.CASCADE)
	cleanliness_rating = models.PositiveSmallIntegerField()
	amenities_rating = models.PositiveSmallIntegerField()
	
	def __str__(self):
		return str(self.cleanliness_rating) + "/" + str(self.amenities_rating) + " rating for " + self.bathroom.name
		
class Image(models.Model):
	bathroom = models.ForeignKey(Bathroom, on_delete=models.CASCADE)
	image = models.ImageField(upload_to='photos/')
	
	def __str__(self):
		return "Image of " + self.bathroom.name