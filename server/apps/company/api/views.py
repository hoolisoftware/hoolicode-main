from rest_framework import generics, permissions

from . import serializers
from .. import models


class FeedbackRequestCreateAV(generics.CreateAPIView):
    queryset = models.FeedbackRequest.objects.all()
    serializer_class = serializers.FeedbackRequestSerializer
    permission_classes = [permissions.IsAuthenticated]


class VacancyRequestCreateAV(generics.CreateAPIView):
    queryset = models.VacancyRequest.objects.all()
    serializer_class = serializers.VacancyRequestSerializer
    permission_classes = [permissions.IsAuthenticated]
