from django.shortcuts import render

# Create your views here.
def index(req):
	context = {
		'title' : 'Blog',
		'subTitle' : 'Selamat Datang di halaman Blog',
		'nav' : [
			['/home', 'Home'],
			['/blog', 'Blog']
		]
	}

	return render(req, 'blog.html', context)
