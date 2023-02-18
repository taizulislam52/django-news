from django.urls  import path
from .views import NewsListView,NewsSingleView
from . import views


urlpatterns = [
    path('', NewsListView.as_view(), name='news-home'),
    path('news/<int:pk>', NewsSingleView.as_view(), name="news-single")
]
