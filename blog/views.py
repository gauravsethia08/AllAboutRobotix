from django.shortcuts import render, redirect
from .models import techspresso as tech
from .models import iros2020 as ir 
from .models import research as rs
from .models import subscribe as sb
from django.contrib import messages
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


def subscribe(request):

    if 'email' in request.GET:
        sub_email = request.GET['email']
        sub = sb(email= sub_email)
        sub.save()

        print(request.path)
        messages.error(request, "Thank You for Subscribing")
        return redirect('/')
