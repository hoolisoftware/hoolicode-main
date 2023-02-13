from captcha import widgets as captcha_widgets
from captcha.fields import ReCaptchaField
from django.forms import ModelForm

from . import models


class VacancyRequestForm(ModelForm):
    captcha = ReCaptchaField(
        widget=captcha_widgets.ReCaptchaV2Checkbox(
            attrs={
                'data-theme': 'dark',
            }
        )
    )

    class Meta:
        model = models.VacancyRequest
        fields = (
            'full_name',
            'email',
            'message',
            'cv',
        )


class FeedbackRequestForm(ModelForm):
    captcha = ReCaptchaField(
        widget=captcha_widgets.ReCaptchaV2Checkbox(
            attrs={
                'data-theme': 'dark',
            }
        )
    )

    class Meta:
        model = models.FeedbackRequest
        fields = (
            'full_name',
            'email',
            'subject',
            'message',
        )
