from django import template
from django.db.models import Count
from django.utils.safestring import mark_safe
import markdown

from apps.posts import models

register = template.Library()

@register.filter(name='markdown')
def makrdown_format(text):
	return mark_safe(markdown.markdown(text))
