from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
    path('main/', views.index, name='index'),
    path('about/', views.about_view, name='about_page'),
    path('contacts/', views.contacts_view, name='contacts_page'),
    path('account/', views.account_view, name='account_page'),
    ##url(r'^books/$', views.BookListView.as_view(), name='books'),
    ##url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    ##url(r'^authors/$', views.AuthorListView.as_view(), name='authors'),
    ##url(r'^author/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name='author-detail'),
]