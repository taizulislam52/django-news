from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from django.db.models import Q
from .models import Post, Category
from django.http import HttpResponse


# Create your views here.
class NewsListView(ListView):
    model = Post
    queryset = Post.objects.order_by('-created_at')
    template_name = 'news/home.html'
    context_object_name = 'news_list'

    def get_queryset(self):
        return Post.objects.all().order_by('-created_at')[:5]

    def get_context_data(self, **kwargs):
        context = super(NewsListView, self).get_context_data(**kwargs)
        context['first_news'] = Post.objects.first()
        context['trending_news'] = Post.objects.filter(category__slug='trending')[0:5]
    
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


class NewsCategoryView(ListView):
    model = Post
    template_name = 'news/category.html'
    context_object_name = 'categories'

    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return Post.objects.filter(category=self.category).order_by('-created_at')[:6]
    
    def get_context_data(self, **kwargs):
        context = super(NewsCategoryView, self).get_context_data(**kwargs)
        context['category_name'] = self.kwargs['slug']
    
        return context