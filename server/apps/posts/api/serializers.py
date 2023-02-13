from rest_framework import serializers
from drf_recaptcha.fields import ReCaptchaV2Field

from .. import models


class CaptchaMixin:
    def validate(self, attrs):
        attrs.pop("captcha")
        return attrs


class PostCommentSerializer(CaptchaMixin, serializers.ModelSerializer):
    captcha = ReCaptchaV2Field()

    class Meta:
        model = models.PostComment
        exclude = ('post', )
