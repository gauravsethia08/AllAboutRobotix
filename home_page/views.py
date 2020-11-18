from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Contact
from blog.models import iros2020, techspresso, research

# Create your views here.
def home(request):
    ir = iros2020.objects.last()
    tech = techspresso.objects.last()
    research = iros2020.objects.last()
    return render(request, 'index.html')


def lab(request):
    return render(request, 'vrl.html')


def team(request):
    return render(request, 'team.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        number = request.POST['number']
        msg = request.POST['msg']

        contact_query = Contact(name = name, email = email, contact_no = number, message = msg)
        contact_query.save()

        messages.error(request, "We have got your query. We will contact you shortly")
        return HttpResponseRedirect('/')
    else:
        return render(request, 'contact_us.html')