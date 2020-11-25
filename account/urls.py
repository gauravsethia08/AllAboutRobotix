#Importing Libraries
from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name = "login"),
    path('register', views.register, name = "register"),
    path('logout', views.logout, name = 'logout'),
    path('user_profile', views.profile, name = 'profile'),
    path('update_personal', views.update_personal, name = 'update_personal'),
    path('update_password', views.update_password, name = 'update_password'),
    path('update_contact', views.update_contact, name = 'update_contact'),
    path('change_img', views.change_img, name='change_img')
]