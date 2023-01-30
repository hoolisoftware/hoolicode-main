from captcha import widgets as captcha_widgets 
from captcha.fields import ReCaptchaField
from core.mixins import AddClassNameMixin
from django.forms import ModelForm

from . import models

class PostCommentForm(ModelForm):
    captcha = ReCaptchaField(
        widget=captcha_widgets.ReCaptchaV2Checkbox(
            attrs={
                'data-theme': 'dark',
            }
        )
    )
    class Meta:
        model = models.PostComment
        fields = (
            'full_name',
            'email',
            'comment',
        )
