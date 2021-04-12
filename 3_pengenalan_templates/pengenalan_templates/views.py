from django.http import HttpResponse

# add import to render html
from django.shortcuts import render

# method view
# def home(req):
#     infoPageHome = "Ini adalah Halaman Home"
#     return HttpResponse(infoPageHome)

def home(req):
    return render(req,'index.html')

def blog(req):
    infoPageBlog = "Ini adalah Halaman Blog"
    return HttpResponse(infoPageBlog)

def contact(req):
    infoPageContact = "Ini adalah Halaman Contact"
    return HttpResponse(infoPageContact)