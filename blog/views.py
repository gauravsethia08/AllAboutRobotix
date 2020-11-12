from django.shortcuts import render
from .models import techspresso as tech
from .models import iros2020 as ir 
from .models import research as rs

# Create your views here.
def techspresso(request):
    #Fetching data
    data = tech.objects.all()
    return render(request, 'techspresso.html', {'data' : data})


def iros(request):
    data = ir.objects.all()
    return render(request, 'iros_landing.html', {'data' : data})

def research(request):
    data = rs.objects.all()
    return render(request, 'research_simplified.html', {'data' : data})