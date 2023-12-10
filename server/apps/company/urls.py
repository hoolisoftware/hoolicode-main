from django.urls import path, include
from django.contrib.sitemaps.views import sitemap

from . import views
from . import sitemaps

app_name = 'company'

urlpatterns = [
    path('sitemap.xml', sitemap, {'sitemaps': {
         'static': sitemaps.StaticViewSitemap}},
         name='django.contrib.sitemaps.views.sitemap'),
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('portfolio/', views.PortfolioListView.as_view(),
         name='portfolio-list'),
    path('portfolio/<str:slug>/', views.PortfolioDetailView.as_view(),
         name='portfolio-detail'),
    path('vacancies/', views.VacancyListView.as_view(), name='vacancy-list'),
    path('vacancies/sitemap.xml', sitemap, {'sitemaps': {
         'vacancy': sitemaps.VacancySitemap}},
         name='django.contrib.sitemaps.views.sitemap'),
    path('vacancies/<str:slug>/',
         views.VacancyDetailView.as_view(), name='vacancy-detail'),
    path('test/', views.TestView.as_view(), name='test'),
]
