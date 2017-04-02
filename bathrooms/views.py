from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import Bathroom, Rating, Image

def list(request):
	bathroom_list = Bathroom.objects.all()
	ratings_list = []
	for bathroom in bathroom_list:
		ratings = Rating.objects.filter(bathroom__id=bathroom.id)
		ratings_list.append(getRatings(bathroom, ratings))
	
	return render(request, 'bathrooms/list.html', {
		'bathroom_list': zip(bathroom_list, ratings_list)
	})
	
def detail(request, bathroom_id):
	bathroom = get_object_or_404(Bathroom, id=bathroom_id)
	ratings = Rating.objects.filter(bathroom__id=bathroom_id)
	images = Image.objects.filter(bathroom__id=bathroom_id)
	
	results = getRatings(bathroom, ratings)
	cleanliness_rating = results['cleanliness']
	amenities_rating = results['amenities']
		
	gender = 'Mens\''
	if bathroom.gender == 1:
		gender = 'Womens\''
	if bathroom.gender == 2:
		gender = 'Gender-neutral'
	
	return render(request, 'bathrooms/bathroom.html', {
		'bathroom': bathroom,
		'cleanliness_rating': cleanliness_rating,
		'amenities_rating': amenities_rating,
		'images': images,
		'gender': gender
	})

def vote(request, bathroom_id):
	rating = Rating()
	rating.bathroom = Bathroom.objects.get(id=bathroom_id)
	rating.cleanliness_rating = request.POST.get('cleanliness', None)
	rating.amenities_rating = request.POST.get('amenities', None)
	if rating.cleanliness_rating != None and rating.amenities_rating != None:
		rating.save()
	
	bathroom = get_object_or_404(Bathroom, id=bathroom_id)
	return redirect('bathrooms:detail', bathroom_id)

def getRatings(bathroom, ratings):
	cleanliness_rating_sum = 0
	amenities_rating_sum = 0
	rating_n = 0
	for rating in ratings:
		cleanliness_rating_sum += rating.cleanliness_rating
		amenities_rating_sum += rating.amenities_rating
		rating_n += 1
	
	cleanliness_rating = 'no ratings yet'
	amenities_rating = 'no ratings yet'
	if rating_n > 0:
		cleanliness_rating = cleanliness_rating_sum / rating_n
		amenities_rating = amenities_rating_sum / rating_n
		
	return {
		'cleanliness': cleanliness_rating,
		'amenities': amenities_rating
	}