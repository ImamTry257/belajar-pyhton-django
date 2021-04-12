from django.shortcuts import render

def index(req):
	context = {
		'title' : 'Home',
		'subTitle' : 'Selamat Data di Halaman Home',
		'nav' : [
			['/home', 'Home'],
			['/blog', 'Blog']
		]
	}
	return render(req, 'home.html', context)