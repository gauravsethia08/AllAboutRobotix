from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from .models import Contact
from blog.models import Blog#iros2020, techspresso, research

# Create your views here.
def home(request):
    ir = Blog.objects.filter(blog_type="IROS2020", make_public=True).last()
    tech = Blog.objects.filter(blog_type="Techspresso", make_public=True).last()
    res = Blog.objects.filter(blog_type="Research", make_public=True).last()
    print(ir, tech, res)
    return render(request, 'index.html', {'iros': ir, 'tech': tech, 'research': res})


def lab(request):
    return render(request, 'vrl.html')


def team(request):
    return render(request, 'team.html')


def privacy_policy(request):
    return render(request, 'privacy.html')


def search(request):
    word = request.GET['keyword']
    if len(word) > 80:
        posts = []
    else:
        posts = Blog.objects.filter(title__icontains = word, abstract__icontains = word)
    print(posts)
    return render(request, 'search_result.html', {'posts': posts, 'query': word})


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        number = request.POST['number']
        msg = request.POST['msg']

        contact_query = Contact(name = name, email = email, contact_no = number, message = msg)
        contact_query.save()

        messages.success(request, "We have got your query. We will contact you shortly")
        return HttpResponseRedirect('/')
    else:
        return render(request, 'contact_us.html')