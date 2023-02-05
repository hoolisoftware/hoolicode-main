from modeltranslation.translator import  register, TranslationOptions

from . import models


@register(models.Category)
class CategoryTranslateOptions(TranslationOptions):
    fields = (
        'name', 
    )


@register(models.Tag)
class TagTranslateOptions(TranslationOptions):
    fields = (
        'name', 
    )


@register(models.Post)
class PostTranslateOptions(TranslationOptions):
    fields = (
        'content',
        'title', 
    )