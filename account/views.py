from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import students
import bcrypt
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import auth


# Create your views here.
def login(request):
    #Checking the request method
    
    #Login the user if POST method is used
    if request.method == 'POST':

        #Fetching data from the HTML page
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email = email, password = password)
        
        messages.error(request, "Login Successful")
        return HttpResponseRedirect('/')

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

        if email != str(students.objects.filter(email=email).first()):
            #Checking is Login password and repeated login password are same
            if password1 == password2:

                password = make_password(password1)

                user = students(email=email, name=name, password=password)
                user.save()

                messages.error(request, "Registration Successfull")
                return HttpResponseRedirect('login')
            

            else:
                #Raising an exception
                messages.error(request, "Password is not matching")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        else:
            #Raising an exception
            messages.error(request, "Email Already Registered")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    #Load the Login Page if GET method is used
    else:
        return render(request, 'register.html')