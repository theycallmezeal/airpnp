from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import Bathroom, Rating, Image

def list(request):
	bathroom_list = Bathroom.objects.all()
	return render(request, 'bathrooms/list.html', {
		'bathroom_list': bathroom_list
	})
	
def detail(request, bathroom_id):
	bathroom = get_object_or_404(Bathroom, id=bathroom_id)
	ratings = Rating.objects.filter(bathroom__id=bathroom_id)
	images = Image.objects.filter(bathroom__id=bathroom_id)
	
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
	
	return render(request, 'bathrooms/bathroom.html', {
		'bathroom': bathroom,
		'cleanliness_rating': cleanliness_rating,
		'amenities_rating': amenities_rating,
		'images': images
	})

def vote(request, bathroom_id):
	rating = Rating()
	rating.bathroom = Bathroom.objects.get(id=bathroom_id)
	rating.cleanliness_rating = request.POST['cleanliness']
	rating.amenities_rating = request.POST['amenities']
	rating.save()
	
	bathroom = get_object_or_404(Bathroom, id=bathroom_id)
	return redirect('bathrooms:detail', bathroom_id)