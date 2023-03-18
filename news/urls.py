from django.urls  import path
from .views import NewsListView, NewsSingleView, NewsSearchView, NewsCategoryView, NewsTagView
from . import views


urlpatterns = [
    path('', NewsListView.as_view(), name='news-home'),
    path('news/<slug:slug>/', NewsSingleView.as_view(), name="news-single"),
    path('news/search/', NewsSearchView.as_view(), name="news-search"),
    path('news/category/<slug:slug>', NewsCategoryView.as_view(), name="news-category"),
    path('news/tag/<slug:slug>', NewsTagView.as_view(), name="news-tag"),
    path('load-more-trending-news', views.load_more_trending_news, name="load-more-trending-news"),
    path('subscribe-newsletter', views.subscribe_newsletter, name='subscribe-newsletter'),
    path('download-magazine', views.download_magazine, name='download-magazine'),
]
