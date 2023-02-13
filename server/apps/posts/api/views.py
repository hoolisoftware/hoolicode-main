from rest_framework import generics, permissions

from . import serializers
from .. import models


class PostCommentCreateAV(generics.CreateAPIView):
    queryset = models.PostComment.objects.all()
    serializer_class = serializers.PostCommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.validated_data['post'] = models.Post.objects.get(
            id=self.request.parser_context['kwargs']['pk'])
        serializer.save()
