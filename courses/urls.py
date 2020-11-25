#Importing Libraries
from django.urls import path
from . import views

urlpatterns = [
    path('kinematics', views.kinematics, name = "kinematics"),
    path('control', views.control, name = "control"),
    path('computer_vision', views.computer_vision, name = "computer_vision")
]