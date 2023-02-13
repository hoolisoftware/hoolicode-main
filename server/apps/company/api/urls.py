from django.urls import path

from . import views

app_name = 'api'

urlpatterns = [
    path('feedback-request-create/', views.FeedbackRequestCreateAV.as_view(),
         name='feedback-request-create'),
    path('vacancy-request-create/', views.VacancyRequestCreateAV.as_view(),
         name='vacancy-request-create')
]
