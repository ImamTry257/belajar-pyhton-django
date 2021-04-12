from django.shortcuts import render

# Create your views here.

def home(req):
	context = {
		'title':'Home',
		'content':'ini adalah halaman Home' 
	}
	return render(req, 'page.html', context)

def detail(req):
	context = {
		'title':'detail',
		'content':'ini adalah halaman detail' 
	}
	return render(req, 'page.html', context)

def contact(req):
	context = {
		'title':'contact',
		'content':'ini adalah halaman contact' 
	}
	return render(req, 'page.html', context)