# sitemaps.py
from django.contrib import sitemaps
from django.urls import reverse

from . import models

class StaticViewSitemap(sitemaps.Sitemap):
    # priority = 0.5
    # changefreq = 'daily'

    def items(self):
        return [
            'company:home', 
            'company:contact', 
            'company:about',
            'company:vacancy-list',            
            'users:login',
            'users:register',
            'posts:list',
        ]

    def location(self, item):
        return reverse(item)


class VacancySitemap(sitemaps.Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return models.Vacancy.objects.all()

    def lastmod(self, obj):
        return obj.posted
