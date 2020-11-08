from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.
def login(request):
    #Checking the request method
    
    #Login the user if POST method is used
    if request.method == 'POST':

        #Fetching data from the HTML page
        email = request.POST['email']
        password = request.POST['password']



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
        password = request.POST['password']
        password2 = request.POST['password2']

        #Checking is Login password and repeated login password are same
        if password == password2:
           pass
        else:
            #Raising an exception
            messages.error(request, "Password is not matching")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    #Load the Login Page if GET method is used
    else:
        return render(request, 'register.html')