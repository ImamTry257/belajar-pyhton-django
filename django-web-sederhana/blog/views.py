from django.shortcuts import render

# Create your views here.
def index(req):
	context = {
		'title' : 'Blog'		
	}
	return render(req, 'index.html', context)
