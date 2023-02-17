from django.shortcuts import render
from django.views.generic import ListView
from .models import Post
from django.http import HttpResponse


# Create your views here.
class PostListView(ListView):
    model = Post
    queryset = Post.objects.order_by('-created_at')
    template_name = 'news/home.html'
    context_object_name = 'news_list'

    def get_queryset(self):
        return Post.objects.all().order_by('-created_at')[1:6]

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['first_news'] = Post.objects.first()
    
        return context