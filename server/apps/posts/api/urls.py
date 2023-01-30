from django.urls import path

from . import views

app_name = 'api'

urlpatterns = [
    path('post-comment-create/<int:pk>/', views.PostCommentCreateAV.as_view(), name='post-comment-create'),
    path('post-comment-create/', views.PostCommentCreateAV.as_view(), name='post-comment-create'),
]