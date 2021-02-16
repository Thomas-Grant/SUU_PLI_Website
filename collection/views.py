from django.shortcuts import render
from .models import Collection

def home(request):
	context = {
		'collections':Collection.objects.all()
	}
	return render(request, 'collection/home.html', context)

def about(request):
	return render(request, 'collection/about.html', {'title':'About'})


