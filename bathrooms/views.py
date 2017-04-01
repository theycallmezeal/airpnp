from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Bathroom

def list(request):
	bathroom_list = Bathroom.objects.all()
	vars = {
		'bathroom_list': bathroom_list
	}
	return render(request, 'list.html', vars)
	
def detail(request, bathroom_id):
	bathroom = get_object_or_404(Bathroom, pk=bathroom_id)
	vars = {
		'bathroom': bathroom
	}
	return render(request, 'bathroom.html', vars)
