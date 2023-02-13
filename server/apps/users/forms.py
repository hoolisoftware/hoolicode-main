from typing import Dict, Any
from captcha import widgets as captcha_widgets
from captcha.fields import ReCaptchaField

from django import forms
from django.forms import Form
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from core.mixins import AddClassNameMixin

User = get_user_model()


class LoginForm(AddClassNameMixin, Form):
    username = forms.CharField(label=_('Username'), widget=forms.TextInput())
    password = forms.CharField(
        label=_('Password'), widget=forms.PasswordInput())
    captcha = ReCaptchaField(
        label=_("Aren't you robot?"),
        widget=captcha_widgets.ReCaptchaV2Checkbox(
            attrs={
                'data-theme': 'dark',
            }
        )
    )
    remember_me = forms.BooleanField(
        label=_('Remember me'), widget=forms.CheckboxInput(
            attrs={'id': 'flexCheckDefault'}
        ), required=False
    )


class RegisterForm(forms.Form):
    first_name = forms.CharField(
        label=_('First name'), widget=forms.TextInput())
    last_name = forms.CharField(label=_('Last name'), widget=forms.TextInput())
    email = forms.EmailField(label=_('E-mail'), widget=forms.EmailInput())
    username = forms.CharField(label=_('Username'), widget=forms.TextInput())
    password1 = forms.CharField(
        label=_('Password'), widget=forms.PasswordInput(
            attrs={'id': 'password1'})
        )
    password2 = forms.CharField(label=_(
        'Passowrd confirm'), widget=forms.PasswordInput(
            attrs={'id': 'password2'})
        )
    captcha = ReCaptchaField(
        label=_("Aren't you robot?"),
        widget=captcha_widgets.ReCaptchaV2Checkbox(
            attrs={
                'data-theme': 'dark',
            }
        )
    )

    def clean(self) -> Dict:
        cleaned_data = super().clean()

        if cleaned_data['password1'] != cleaned_data['password2']:
            raise ValidationError('Passwords do not match!')

        return cleaned_data

    def clean_email(self) -> Any:
        email = self.cleaned_data['email']

        if User.objects.filter(email=email).exists():
            raise ValidationError('This email is already taken!')

        return email
