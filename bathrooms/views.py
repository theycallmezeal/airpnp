from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Bathroom, Rating

def list(request):
	bathroom_list = Bathroom.objects.all()
	return render(request, 'list.html', {
		'bathroom_list': bathroom_list
	})
	
def detail(request, bathroom_id):
	bathroom = get_object_or_404(Bathroom, id=bathroom_id)
	return render(request, 'bathroom.html', {
		'bathroom': bathroom
	})

def vote(request, bathroom_id):
	rating = Rating()
	rating.bathroom = Bathroom.objects.get(id=bathroom_id)
	rating.cleanliness_rating = request.POST['cleanliness']
	rating.save()
	
	bathroom = get_object_or_404(Bathroom, id=bathroom_id)
	return render(request, 'bathroom.html', {
		'bathroom': bathroom
	})