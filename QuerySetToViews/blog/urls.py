from django.urls import path
from .import views

urlpatterns = [
	path('index', views.index),
	path('berita', views.berita),
	path('jurnal', views.jurnal),
	path('gosip', views.gosip)
]