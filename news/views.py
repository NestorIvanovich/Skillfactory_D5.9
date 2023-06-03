from django.views.generic import ListView, DetailView
from .models import Post
from django.shortcuts import render


class NewsList(ListView):
    model = Post
    ordering = '-created_time'
    template_name = 'news.html'
    context_object_name = 'posts'


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'
