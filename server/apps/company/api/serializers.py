from rest_framework import serializers
from drf_recaptcha.fields import ReCaptchaV2Field

from .. import models


class CaptchaMixin:
    def validate(self, attrs):
        attrs.pop("captcha")
        return attrs


class FeedbackRequestSerializer(CaptchaMixin, serializers.ModelSerializer):
    captcha = ReCaptchaV2Field()

    class Meta:
        model = models.FeedbackRequest
        fields = '__all__'


class VacancyRequestSerializer(CaptchaMixin, serializers.ModelSerializer):
    captcha = ReCaptchaV2Field()

    class Meta:
        model = models.VacancyRequest
        fields = '__all__'
