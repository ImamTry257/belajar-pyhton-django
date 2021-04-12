from django.shortcuts import render

def index(req):
	context = {
		'title' : 'Home',
		'subTitle' : 'Selamat Data di Halaman Home'
	}
	return render(req, 'index.html', context)