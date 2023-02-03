from modeltranslation.translator import  register, TranslationOptions

from . import models


@register(models.FAQ)
class FAQTranslateOptions(TranslationOptions):
    fields = ('question', 'answer')