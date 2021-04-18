from django.shortcuts import render
from .models import Post

# Create your views here.
def index(req):
	# getting data using query
	posts = Post.objects.all()
	print(posts)

	content = {
		'Title' : 'Blog',
		'Heading' : 'Blog di My Website',
		'Posts' : posts
	}

	return render(req, 'blog/index.html', content)
