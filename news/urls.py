from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
    # path('', views.news, name='news'),
    ##path('news_list', views.NewsListView.as_view()),
    url(r'^$', views.NewsListView.as_view(), name='news'),
    url(r'^(?P<pk>\d+)$', views.ArticleDetailView.as_view(), name='article-detail'),
    ##url(r'^authors/$', views.AuthorListView.as_view(), name='authors'),
    ##url(r'^author/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name='author-detail'),
]