from django.http import HttpResponse

# import to add render
from django.shortcuts import render

# method view home
def home(req):
	return render(req, 'home.html')


# method view about
def about(req):
	return render(req, 'about.html')
