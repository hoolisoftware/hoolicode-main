from typing import Tuple, Dict, List

from django.forms.widgets import NumberInput
from django.shortcuts import redirect
from django.http.request import HttpRequest
from django.http.response import HttpResponse


class AddClassNameMixin:
    '''
    Mixin to add html classes to form fields
    Usable for both Form and FilterSet(django_filters) objects
    '''
    class_name: str = 'form-control'
    class_name__checkbox: str = 'rn-check-box-input'
    not_modify_fields: List[str] = []

    def __init__(self, *args: Tuple, **kwargs: Dict):
        result = super().__init__(*args, **kwargs)
        form = self if hasattr(self, 'visible_fields') else self.form

        for field in filter(lambda field: field.name not in self.not_modify_fields, form.visible_fields()):
            if getattr(field.field.widget, 'input_type', None) == 'checkbox':
                field.field.widget.attrs['class'] = self.class_name__checkbox
            else:
                field.field.widget.attrs['class'] = self.class_name

        return result
