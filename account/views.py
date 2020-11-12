from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
#from .models import extendedUser
from .models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.
def login(request):
    #Checking the request method
    
    #Login the user if POST method is used
    if request.method == 'POST':

        #Fetching data from the HTML page
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(email = email, password = password)

        if user is not None:
            auth_login(request, user)
        
            messages.error(request, "Login Successful")
            return redirect('/')
        
        else:
            messages.error(request, "Credentials doesnt match")
            return redirect('login')

    #Load the Login Page if GET method is used
    else:
        return render(request, 'login.html')



def register(request):
    #Checking the request method
    #Login the user if POST method is used
    if request.method == 'POST':
        
        #Fetching data from the HTML page
        name = request.POST['name']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['password2']


        #try:
        #    user = User.objects.get(email=email)
            #Raising an exception
        #    messages.error(request, "Email Already Registered")
         #   return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
        #except User.DoesNotExist:

        user = authenticate(request, email = email, password = password1)

        if user is not None:
            messages.error(request, "User Already Exsists")
        
        else:
            user = User.objects.create_user(email=email, password=password1, name=name)
            user.save()
            messages.error(request, "Registration Successfull")
        return HttpResponseRedirect('login')


    #Load the Login Page if GET method is used
    else:
        return render(request, 'register.html')


def logout(request):
    auth_logout(request)
    messages.error(request, "Logged Out")
    return redirect('/')
