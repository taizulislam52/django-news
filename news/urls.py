from django.urls  import path
from .views import NewsListView, NewsSingleView, NewsSearchView
from . import views


urlpatterns = [
    path('', NewsListView.as_view(), name='news-home'),
    path('news/<slug:slug>/', NewsSingleView.as_view(), name="news-single"),
    path('news/search/', NewsSearchView.as_view(), name="news-search"),
]
