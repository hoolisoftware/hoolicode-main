from django.views import generic
from django_filters.views import FilterView

from . import forms
from . import models
from . import filters


class PostListView(FilterView):
    template_name = 'posts/list.django-html'
    model = models.Post
    filterset_class = filters.PostFilter 


class PostDetailView(generic.FormView, generic.DetailView):
    template_name = 'posts/detail.django-html'
    form_class = forms.PostCommentForm
    model = models.Post
