from django.shortcuts import render
from django.views import generic

from . import models
from . import forms

class HomeView(generic.TemplateView):
    template_name = 'company/home.django-html'

class AboutView(generic.TemplateView):
    template_name = 'company/about.django-html'

class ContactView(generic.TemplateView, generic.FormView):
    form_class = forms.FeedbackRequestForm
    template_name = 'company/contact.django-html'

class PortfolioListView(generic.ListView):
    model = models.Project
    template_name = 'company/portfolio-list.django-html'

class PortfolioDetailView(generic.DetailView):
    model = models.Project
    template_name = 'company/portfolio-detail.django-html'

class VacancyListView(generic.ListView):
    model = models.Vacancy
    template_name = 'company/vacancy-list.django-html'

class VacancyDetailView(generic.DetailView, generic.FormView):
    model = models.Vacancy
    form_class = forms.VacancyRequestForm
    template_name = 'company/vacancy-detail.django-html'

class TestView(generic.TemplateView):
    template_name = 'test.django-html'