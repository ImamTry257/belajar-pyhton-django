from django.shortcuts import render
from .models import Posts

# Create your views here.
def index(req):
	allPosts = Posts.objects.all()
	print(allPosts)

	content = {
		'Title' : 'Blog',
		'Heading' : 'Selamat Datang di Blog',
		'Posts' : allPosts
	}

	return render(req, 'blog/index.html', content)


def jurnal(req):
	allPosts = Posts.objects.filter(category="jurnal")
	print(allPosts)

	content = {
		'Title' : 'Blog',
		'Heading' : 'Selamat Datang di Blog',
		'Posts' : allPosts
	}

	return render(req, 'blog/index.html', content)


def berita(req):
	allPosts = Posts.objects.filter(category="berita")
	print(allPosts)

	content = {
		'Title' : 'Blog',
		'Heading' : 'Selamat Datang di Blog',
		'Posts' : allPosts
	}

	return render(req, 'blog/index.html', content)

def gosip(req):
	allPosts = Posts.objects.filter(category="gosip")
	print(allPosts)

	content = {
		'Title' : 'Blog',
		'Heading' : 'Selamat Datang di Blog',
		'Posts' : allPosts
	}

	return render(req, 'blog/index.html', content)
