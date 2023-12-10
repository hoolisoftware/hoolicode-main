from django.contrib.sitemaps.views import sitemap
from django.urls import path, include

from . import views
from . import sitemaps

app_name = 'posts'

urlpatterns = [
    path('sitemap.xml', sitemap, {'sitemaps': {
         'post': sitemaps.PostSitemap}},
         name='django.contrib.sitemaps.views.sitemap'),
    path('', views.PostListView.as_view(), name='list'),
    path('<str:slug>', views.PostDetailView.as_view(), name='detail'),
]
