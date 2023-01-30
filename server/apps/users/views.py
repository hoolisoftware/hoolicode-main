from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import get_user_model, views as auth_views
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.hashers import make_password
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render, redirect
from django.http.response import HttpResponseRedirect, HttpResponse
from django.http.request import HttpRequest
from django.views import generic
from django.urls import reverse, reverse_lazy

from . import forms

User = get_user_model()


class LoginView(generic.View):
    form_class = forms.LoginForm
    template_name = 'users/login.django-html'
    logged_in_regirect_url = reverse_lazy('vacancies:home')

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, self.template_name, {'form': self.form_class()})

    def post(self, request: HttpRequest) -> HttpResponse:
        form = self.form_class(request.POST)

        if form.is_valid():

            if not (user := authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])):
                form.add_error(field='username', error='Incorrect Email or Password')
                return render(request, self.template_name, {'form': form})

            login(request, user)

            if not form.cleaned_data['remember_me']:
                request.session.set_expiry(0)

        else:
            return render(request, self.template_name, {'form': form})

        return redirect('company:home')


class RegisterView(generic.View):
    form_class = forms.RegisterForm
    template_name = 'users/register.django-html'
    logged_in_regirect_url = reverse_lazy('vacancies:home')

    def get(self, request: HttpRequest) -> HttpResponse:
        if (result := super().get(request)):
            return result

        return render(request, self.template_name, {'form': self.form_class()})

    def post(self, request: HttpRequest) -> HttpResponse:
        form = self.form_class(request.POST)

        if form.is_valid():
            user = User.objects.create(
                username=form.cleaned_data['username'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                password=make_password(form.cleaned_data['password1'])
            )
            login(request, user)
        else:
            return render(request, self.template_name, {'form': form})

        return redirect('vacancies:home')
