from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Bathroom

def index(request):
	bathroom_list = Bathroom.objects.all()
	vars = {
		'bathroom_list': bathroom_list
	}
	return render(request, 'index.html', vars)
	
def detail(request, bathroom_id):
	bathroom = get_object_or_404(Bathroom, pk=bathroom_id)
	vars = {
		'bathroom': bathroom
	}
	return render(request, 'bathroom.html', vars)
