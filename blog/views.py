from django.shortcuts import render, redirect, get_object_or_404
"""from .models import techspresso as tech
from .models import iros2020 as ir 
from .models import research as rs"""
from .models import subscribe as sb
from .models import Blog, BlogComment
from django.contrib import messages
from django.views.generic import ListView, DetailView
from blog.templatetags import get_dicts


class IROSListView(ListView):
    model = Blog#.objects.filter(blog_type="IROS")
    #queryset = Blog.objects.filter(blog_type="IROS")
    template_name = 'iros_landing.html'
    context_object_name = 'data'
    ordering = ['-date_posted']


class ResearchListView(ListView):
    model = Blog#.objects.filter(blog_type="Research")
    template_name = 'research_simplified.html'
    context_object_name = 'data'
    ordering = ['-date_posted']


class TechListView(ListView):
    model = Blog#.objects.filter(blog_type="Techespresso")
    template_name = 'techspresso.html'
    context_object_name = 'data'
    ordering = ['-date_posted']


class IROSDetailView(DetailView):
    model = Blog#.objects.filter(blog_type="IROS")
    template_name = 'blog_post.html'
    context_object_name = 'blog'

    #def get_queryset(self):
    #    print(get_object_or_404(Blog, id=self.kwargs['pk']))
    #    self.title = get_object_or_404(Blog, id=self.kwargs['pk'])
    #    return Blog.objects.filter(title = self.title)[0]

    def get_context_data(self, **kwargs):
        post = Blog.objects.filter(id = self.kwargs['pk']).first()
        replies = BlogComment.objects.filter(post=post).exclude(parent=None).order_by('-timestamp').all()
        replydict = {}
        for reply in replies:
            if reply.parent.sno in replydict:
               replydict[reply.parent.sno].append(reply)
            else:
               replydict[reply.parent.sno] = [reply]

        context = { 'post': post, 'comments': BlogComment.objects.filter(post=post, parent=None).order_by('-timestamp').all(), 'replies': replydict, 'user': self.request.user}
        return context

class ResearchDetailView(DetailView):
    model = Blog #.objects.filter(blog_type="IROS")
    template_name = 'blog_post.html'
    context_object_name = 'blog'

    #def get_queryset(self):
    #    print(get_object_or_404(Blog, id=self.kwargs['pk']))
    #    self.title = get_object_or_404(Blog, id=self.kwargs['pk'])
    #    return Blog.objects.filter(title = self.title)[0]

    def get_context_data(self, **kwargs):
        post = Blog.objects.filter(id = self.kwargs['pk']).first()
        replies = BlogComment.objects.filter(post=post).exclude(parent=None).order_by('-timestamp').all()
        replydict = {}
        for reply in replies:
            if reply.parent.sno in replydict:
               replydict[reply.parent.sno].append(reply)
            else:
               replydict[reply.parent.sno] = [reply]

        context = { 'post': post, 'comments': BlogComment.objects.filter(post=post, parent=None).order_by('-timestamp').all(), 'replies': replydict, 'user': self.request.user}
        return context

class TechDetailView(DetailView):
    model = Blog#.objects.filter(blog_type="IROS")
    template_name = 'blog_post.html'
    context_object_name = 'blog'

    #def get_queryset(self):
    #    print(get_object_or_404(Blog, id=self.kwargs['pk']))
    #    self.title = get_object_or_404(Blog, id=self.kwargs['pk'])
    #    return Blog.objects.filter(title = self.title)[0]

    def get_context_data(self, **kwargs):
        post = Blog.objects.filter(id = self.kwargs['pk']).first()
        replies = BlogComment.objects.filter(post=post).exclude(parent=None).order_by('-timestamp').all()
        replydict = {}
        for reply in replies:
            if reply.parent.sno in replydict:
               replydict[reply.parent.sno].append(reply)
            else:
               replydict[reply.parent.sno] = [reply]

        context = { 'post': post, 'comments': BlogComment.objects.filter(post=post, parent=None).order_by('-timestamp').all(), 'replies': replydict, 'user': self.request.user}
        return context


def subscribe(request):

    if 'email' in request.GET:
        sub_email = request.GET['email']
        sub = sb(email= sub_email)
        sub.save()

        print(request.path)
        messages.success(request, "Thank You for Subscribing")
        return redirect(request.META.get('HTTP_REFERER'))


def postComment(request):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        user = request.user
        postId =  request.POST.get('postid')
        post = Blog.objects.get(id=postId)
        parentSno = request.POST.get('parentsno')


        if parentSno is None:
            blogComment = BlogComment(comment=comment, user=user, post=post)
            blogComment.save()
            #messages.success(request, "Comment Posted")
        
        else:
            parent = BlogComment.objects.get(sno=parentSno)
            blogComment = BlogComment(comment=comment, user=user, post=post, parent=parent)
            blogComment.save()
            #messages.success(request, "Reply Posted")
        
        return redirect(request.META.get('HTTP_REFERER'))