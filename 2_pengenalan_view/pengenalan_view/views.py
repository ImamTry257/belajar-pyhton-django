from django.http import HttpResponse

def index(req):
    return HttpResponse("<h1>halaman home</h1>")

def about(req):
    return HttpResponse("<h1>halaman about</h1>")