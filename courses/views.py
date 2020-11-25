from django.shortcuts import render

# Create your views here.
def kinematics(request):
    return render(request, 'kinematics.html')


def control(request):
    return render(request, 'control.html')


def computer_vision(request):
    return render(request, 'computer_vision.html')