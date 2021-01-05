from django.shortcuts import render, redirect
from .models import Course, Module, ModuleContent
from account.models import Enrollment, learning_progress
from django.contrib import messages

# Create your views here.
def kinematics(request):
    course_detail = Course.objects.filter(course_title='Kinematics').first()
    modules = Module.objects.filter(course=course_detail).order_by('-moduel_no')
    user = request.user
    #Checking if user is logged in
    if str(user) == 'AnonymousUser':
        messages.error(request, "Login to Enroll for the Course")
        is_enrolled = False
    else:
        is_enrolled = Enrollment.objects.filter(user_id=user, course_id=course_detail).first()
        if is_enrolled is None:
            is_enrolled = False
        else:
            is_enrolled = True
    return render(request, 'course_landing.html', {'course': course_detail, 'modules': modules, 'is_enrolled': is_enrolled})


def control(request):
    course_detail = Course.objects.filter(course_title='Controls').first()
    modules = Module.objects.filter(course=course_detail).order_by('-moduel_no')
    user = request.user
    #Checking if user is logged in
    if str(user) == 'AnonymousUser':
        messages.error(request, "Login to Enroll for the Course")
        is_enrolled = False
    else:
        is_enrolled = Enrollment.objects.filter(user_id=user, course_id=course_detail).first()
        if is_enrolled is None:
            is_enrolled = False
        else:
            is_enrolled = True
    return render(request, 'course_landing.html', {'course': course_detail, 'modules': modules, 'is_enrolled': is_enrolled})


def computer_vision(request):
    course_detail = Course.objects.filter(course_title='Computer Vision').first()
    modules = Module.objects.filter(course=course_detail).order_by('-moduel_no')
    user = request.user
    #Checking if user is logged in
    if str(user) == 'AnonymousUser':
        messages.error(request, "Login to Enroll for the Course")
        is_enrolled = False
    else:
        is_enrolled = Enrollment.objects.filter(user_id=user, course_id=course_detail).first()
        if is_enrolled is None:
            is_enrolled = False
        else:
            is_enrolled = True
    return render(request, 'course_landing.html', {'course': course_detail, 'modules': modules, 'is_enrolled': is_enrolled})


def enroll(request):
    #Getting the user details
    user = request.user

    #Checking if user is logged in
    if str(user) == 'AnonymousUser':
        messages.error(request, "Login to Enroll for the Course")

    else:
        #Getting the course details
        #x = str(request.META.get('HTTP_REFERER')).split('/')
        #print(x[-1])
        course_name = request.POST['course_name']
        course = Course.objects.filter(course_title=course_name).first()
        print(course)
        enrollment = Enrollment(user_id=user, course_id=course)
        enrollment.save()
        learning_init = learning_progress(enroll_id=enrollment)
        learning_init.save()

    return redirect(request.META.get('HTTP_REFERER'))
