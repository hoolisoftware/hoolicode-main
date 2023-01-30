from django import template
from django.db.models import Count

from apps.company import models

register = template.Library()

@register.simple_tag
def get_recent_vacancies():
    return models.Vacancy.objects.order_by('-posted')

@register.simple_tag
def get_faq():
    return models.FAQ.objects.all()

@register.simple_tag
def get_features():
    return models.Feature.objects.all()