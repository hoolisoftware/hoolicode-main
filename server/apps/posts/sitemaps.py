from django.contrib.sitemaps import Sitemap
from . import models

class PostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return models.Post.objects.filter(is_published=True)

    def lastmod(self, obj):
        return obj.created