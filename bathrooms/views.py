from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import Bathroom, Rating

def list(request):
	bathroom_list = Bathroom.objects.all()
	return render(request, 'list.html', {
		'bathroom_list': bathroom_list
	})
	
def detail(request, bathroom_id):
	bathroom = get_object_or_404(Bathroom, id=bathroom_id)
	ratings = Rating.objects.filter(bathroom__id=bathroom_id)
	
	cleanliness_rating_sum = 0
	design_rating_sum = 0
	rating_n = 0
	for rating in ratings:
		cleanliness_rating_sum += rating.cleanliness_rating
		design_rating_sum += rating.design_rating
		rating_n += 1
	
	cleanliness_rating = 'no ratings yet'
	design_rating = 'no ratings yet'
	if rating_n > 0:
		cleanliness_rating = cleanliness_rating_sum / rating_n
		design_rating = design_rating_sum / design_n
	
	return render(request, 'bathroom.html', {
		'bathroom': bathroom,
		'cleanliness_rating': cleanliness_rating,
		'design_rating': design_rating
	})

def vote(request, bathroom_id):
	rating = Rating()
	rating.bathroom = Bathroom.objects.get(id=bathroom_id)
	rating.cleanliness_rating = request.POST['cleanliness']
	rating.design_rating = request.POST['design']
	rating.save()
	
	bathroom = get_object_or_404(Bathroom, id=bathroom_id)
	return redirect('bathrooms:detail', bathroom_id)