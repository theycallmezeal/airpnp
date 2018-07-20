from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import Bathroom, Rating, Image

def list(request):
	bathroom_list = Bathroom.objects.all()
	
	heading = 'all bathrooms'
	
	filtertype = request.GET.get('filtertype')
	if filtertype == 'singles':
		bathroom_list = Bathroom.objects.filter(urinals=1)
		heading = 'single bathrooms'
	if filtertype == 'mens':
		bathroom_list = Bathroom.objects.filter(gender=0)
		heading = 'men\'s rooms'
	if filtertype == 'womens':
		bathroom_list = Bathroom.objects.filter(gender=1)
		heading = 'women\'s rooms'
	if filtertype == 'genderneutral':
		bathroom_list = Bathroom.objects.filter(gender=2)
		heading = 'gender-neutral rooms'
	
	length = len(bathroom_list)
	
	ratings_list = []
	for bathroom in bathroom_list:
		ratings = Rating.objects.filter(bathroom__id=bathroom.id)
		numberRatings = getRatings(bathroom, ratings)
		starRatings = {
			'cleanliness': numToStars(numberRatings['cleanliness']),
			'amenities': numToStars(numberRatings['amenities']),
		}
		ratings_list.append(starRatings)
	
	view_list = zip(bathroom_list, ratings_list)
	view_list = sorted(view_list, key=lambda bathroom_tuple: bathroom_tuple[0].name)
	view_list = sorted(view_list, key=lambda bathroom_tuple: bathroom_tuple[0].location.human_readable_location)
	
	return render(request, 'bathrooms/list.html', {
		'bathroom_list': view_list,
		'heading': heading,
		'length': length
	})
	
def detail(request, bathroom_id):
	bathroom = get_object_or_404(Bathroom, id=bathroom_id)
	ratings = Rating.objects.filter(bathroom__id=bathroom_id)
	images = Image.objects.filter(bathroom__id=bathroom_id)
	
	results = getRatings(bathroom, ratings)
	cleanliness_rating = results['cleanliness']
	amenities_rating = results['amenities']
	
	cleanliness_stars = numToStars(cleanliness_rating)
	amenities_stars = numToStars(amenities_rating)
		
	gender = 'Men\'s'
	if bathroom.gender == 1:
		gender = 'Women\'s'
	if bathroom.gender == 2:
		gender = 'Gender-neutral'
	
	return render(request, 'bathrooms/bathroom.html', {
		'bathroom': bathroom,
		'cleanliness_rating': cleanliness_rating,
		'amenities_rating': amenities_rating,
		'cleanliness_stars': cleanliness_stars,
		'amenities_stars': amenities_stars,
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
	
def numToStars(rating):
	if rating == 'no ratings yet':
		return rating
	
	rating = round(rating)
	string = ''
	for i in range(rating):
		string += '&#9733;'
	return string