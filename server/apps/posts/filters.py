import django_filters

from . import models


class PostFilter(django_filters.FilterSet):
    class Meta:
        model = models.Post
        fields = ['tags', 'category']