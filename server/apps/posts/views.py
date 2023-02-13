from django.views import generic

from . import forms
from . import models


class PostListView(generic.ListView):
    template_name = 'posts/list.django-html'
    model = models.Post


class PostDetailView(generic.FormView, generic.DetailView):
    template_name = 'posts/detail.django-html'
    form_class = forms.PostCommentForm
    model = models.Post
