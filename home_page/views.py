from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    return render(request, 'index.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        number = request.POST['number']
        msg = request.POST['msg']

        print(name, " ", email, " ", number, " ", msg)

        messages.error(request, "We have got your query. We will contact you shortly")
        return HttpResponseRedirect('/')
    else:
        return render(request, 'contact_us.html')