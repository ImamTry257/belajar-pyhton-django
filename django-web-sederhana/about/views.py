from django.shortcuts import render

# Create your views here.
def index(req):
	content = {
		'title' : 'About',
		'bannerBlog' : 'about/img/about.jpeg'
	}
	return render(req, 'about.html', content)
