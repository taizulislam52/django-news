from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.template.loader import render_to_string
from .models import Post, Category
from django.http import JsonResponse
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from smtplib import SMTPException


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
        context['total_trending_news'] = Post.objects.filter(category__slug='trending').count()
        context['trending_news'] = Post.objects.filter(category__slug='trending')[0:6]
        context['features_news'] = Post.objects.filter(category__slug='features')
        context['categories'] = Category.objects.all()
    
        return context

class NewsSingleView(DetailView):
    model = Post

    def get_context_data(self, *args, **kwargs):
        context = super(NewsSingleView, self).get_context_data(*args, **kwargs)
        post = self.get_object()
        category = post.category.slug
        context['related_news'] = Post.objects.filter(
            Q(category__slug=category) &
            ~Q(pk=post.pk)
        )[:3]  
        return context
    
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
    paginate_by = 3

    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return Post.objects.filter(category=self.category).order_by('-created_at')
    
    def get_context_data(self, **kwargs):
        context = super(NewsCategoryView, self).get_context_data(**kwargs)
        context['category_name'] = self.kwargs['slug']
    
        return context

def load_more_trending_news(request):
    offset = request.POST.get('offset')
    offset_int = int(offset)
    limit = 3
    trending_news_obj = Post.objects.filter(category__slug='trending')[offset_int:offset_int+limit]
    trending_news = ''
   
    for news in trending_news_obj:
        trending_news += render_to_string('components/card-top-image.html', {'news':news} )
    
    data = {
        'trending_news': trending_news
    }
    return JsonResponse(data=data)

def subscribe_newsletter(request):
    user_email = request.POST.get('email', '')
    body = f'''A new user subscribe to our newsletter
    Email Address: {user_email}'''
    try:
        send_mail(
            'Newsletter Subcribtion',
            body,
            user_email,
            [settings.ADMIN_EMAIL_ADDRESS],
            fail_silently=False,
        )
        data = {
            'error': False,
            'message': 'Thanks for subscribing.'
        }
    except BadHeaderError:              # If mail's Subject is not properly formatted.
        data = {
            'error': True,
            'message': 'Invalid header found.'
        }
    except SMTPException as e:          # It will catch other errors related to SMTP.
        data = {
            'error': True,
            'message': 'There was an error sending an email.'+ e
        }
    except:                             # It will catch All other possible errors.
        data = {
            'error': True,
            'message': 'Mail Sending Failed!'
        }
    
    return JsonResponse(data=data)

def download_magazine(request):
    return render(request, 'news/magazine.html')