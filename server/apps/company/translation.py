from modeltranslation.translator import  register, TranslationOptions

from . import models


@register(models.FAQ)
class FAQTranslateOptions(TranslationOptions):
    fields = ('question', 'answer')

@register(models.Vacancy)
class VacancyTranslateOptions(TranslationOptions):
    fields = (
        'position', 
        'salary',
        'description'
    )

@register(models.Feature)
class FeatureTranslateOptions(TranslationOptions):
    fields = (
        'placeholder',
    )

@register(models.Settings)
class SettingsTranslateOptions(TranslationOptions):
    fields = (
        'quote',
    )