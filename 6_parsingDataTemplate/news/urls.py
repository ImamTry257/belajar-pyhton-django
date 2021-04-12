from django.urls import path
from .import views

urlpatterns = [
	path('', views.home),
	path('', views.detail),
	path('', views.contact)
]