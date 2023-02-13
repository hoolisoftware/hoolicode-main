from django import template
from django.db.models import Count

from apps.posts import models

register = template.Library()


@register.simple_tag
def get_recent_posts():
    return models.Post.objects.order_by('-created')[:5]


@register.simple_tag
def get_popular_categories():
    return models.Category.objects.annotate(
        count_posts=Count('posts')
    ).order_by('-count_posts')[:10]


@register.simple_tag
def get_popular_tags():
    return models.Tag.objects.annotate(
        count_posts=Count('posts')
    ).order_by('-count_posts')[:10]
