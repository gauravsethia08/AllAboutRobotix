#Importing Libraries
from django.urls import path
from . import views

urlpatterns = [
    path('techspresso', views.techspresso, name = "techspresso"),
    path('iros2020', views.iros, name = "iros"),
    path('research', views.research, name = "research"),
]