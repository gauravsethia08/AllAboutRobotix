#Importing Libraries
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home_page"),
    path('contact', views.contact, name="contact"),
    path('lab', views.lab, name='lab'),
    path('team', views.team, name="team")
]