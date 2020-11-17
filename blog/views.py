from django.shortcuts import render
from .models import techspresso as tech
from .models import iros2020 as ir 
from .models import research as rs
from django.views.generic import ListView, DetailView


class IROSListView(ListView):
    model = ir
    template_name = 'iros_landing.html'
    context_object_name = 'data'
    ordering = ['-date_posted']


class ResearchListView(ListView):
    model = rs
    template_name = 'research_simplified.html'
    context_object_name = 'data'
    ordering = ['-date_posted']


class TechListView(ListView):
    model = tech
    template_name = 'techspresso.html'
    context_object_name = 'data'
    ordering = ['-date_posted']


class IROSDetailView(DetailView):
    model = ir
    template_name = 'blog_post.html'
    context_object_name = 'blog'


class ResearchDetailView(DetailView):
    model = rs
    template_name = 'blog_post.html'
    context_object_name = 'blog'


class TechDetailView(DetailView):
    model = tech
    template_name = 'blog_post.html'
    context_object_name = 'blog'




# Create your views here.
def techspresso(request):
    #Fetching data
    data = tech.objects.all()
    return render(request, 'techspresso.html', {'data' : data})


def iros(request):
    #Fetching data
    data = ir.objects.all()
    return render(request, 'iros_landing.html', {'data' : data})

def research(request):
    #Fetching data
    data = rs.objects.all()
    return render(request, 'research_simplified.html', {'data' : data})