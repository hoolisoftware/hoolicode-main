from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views 

app_name = 'users'

urlpatterns = [
    path('password-reset/', views.PasswordResetView.as_view(), name='password-reset'),
    path('password-reset/done/', views.PasswordResetDoneView.as_view(), name='password-reset-done'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password-reset-confirm'),
    path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password-reset-complete'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('sign-in/', views.LoginView.as_view(), name='login'),
    path('sign-up/', views.RegisterView.as_view(), name='register'),
]