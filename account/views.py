from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
#from .models import extendedUser
from .models import User, Enrollment, learning_progress
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from .forms import ImageUploadForm


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
        
            messages.success(request, "Login Successful")
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

        if password1 == password2:
            user = authenticate(request, email = email, password = password1)

            if user is not None:
                messages.error(request, "User Already Exsists")
            
            else:
                user = User.objects.create_user(email=email, password=password1, name=name)
                user.save()
                messages.success(request, "Registration Successfull")
            return HttpResponseRedirect('login')

        else:
            messages.error(request, "Password don't match")
            return HttpResponseRedirect('register')



    #Load the Login Page if GET method is used
    else:
        return render(request, 'register.html')


def logout(request):
    auth_logout(request)
    messages.success(request, "Logged Out")
    return redirect('/')


@login_required
def profile(request):
    i_form = ImageUploadForm()
    
    #Get current user
    user = request.user

    #Getting the enrollments
    courses_enrolled = Enrollment.objects.filter(user_id=user).all()
    course = []
    learning_completed = []
    for course_enrolled in courses_enrolled:
        learning = learning_progress.objects.filter(enroll_id=course_enrolled).first()

        course.append([course_enrolled.course_id.course_title, learning.status])

    return render(request, 'profile.html', {'form': i_form, 'data': course})

def change_img(request):
    i_form = ImageUploadForm(request.POST, request.FILES, instance=request.user)
    if i_form.is_valid():
        i_form.save()
        messages.success(request, "Profile Updated")
        return HttpResponseRedirect('user_profile')

def update_personal(request):
    #Getting the details
    name = request.POST['name']
    email = request.POST['email']
    institution = request.POST['institution']
    github = request.POST['github']

    curr_user = request.user
    curr_user.name = name
    curr_user.email = email
    curr_user.institution = institution
    curr_user.github = github

    #Updating the details
    curr_user.save()

    #Redirecting to the profile page
    messages.success(request, "Profile Updated")
    return HttpResponseRedirect('user_profile')


def update_password(request):
    #Getting the details
    old_password = request.POST['old_password']
    new_password = request.POST['new_password']
    confirm_password = request.POST['confirm_password']

    curr_user = request.user
    
    #Checking if password matches
    user = authenticate(email = curr_user.email, password = old_password)

    if user is not None:

        if new_password == confirm_password:
            curr_user.set_password(new_password)
            messages.success(request, "Password Updated")
        
        else:
            messages.error(request, "Password don't match")

    else:
        messages.error(request, "Incorrect Password")
        

    #Updating the details
    curr_user.save()

    #Redirecting to the profile page
    return HttpResponseRedirect('user_profile')


def update_contact(request):
    #Getting the details
    address = request.POST['address']
    city = request.POST['city']
    country = request.POST['country']

    curr_user = request.user
    curr_user.address = address
    curr_user.city = city
    curr_user.country = country

    #Updating the details
    curr_user.save()

    #Redirecting to the profile page
    messages.success(request, "Profile Updated")
    return HttpResponseRedirect('user_profile')