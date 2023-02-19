from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models import Q
from .models import Post
from django.http import HttpResponse


# Create your views here.
class NewsListView(ListView):
    model = Post
    queryset = Post.objects.order_by('-created_at')
    template_name = 'news/home.html'
    context_object_name = 'news_list'

    def get_queryset(self):
        return Post.objects.all().order_by('-created_at')[1:6]

    def get_context_data(self, **kwargs):
        context = super(NewsListView, self).get_context_data(**kwargs)
        context['first_news'] = Post.objects.first()
    
        return context

class NewsSingleView(DetailView):
    model = Post
    template_name = 'news/single.html'


class NewsSearchView(ListView):
    model = Post
    template_name = 'news/search.html'
    context_object_name = 'news_list'

    def get_queryset(self):
        q = self.request.GET.get('q') if self.request.GET.get('q') != None else ''

        news_list = Post.objects.filter(
            Q(content__icontains=q) |
            Q(title__icontains=q)
        )
   
        return news_list
    