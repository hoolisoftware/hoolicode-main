from modeltranslation.admin import TranslationAdmin
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from django.utils.translation import gettext_lazy as _

from . import models

admin.site.register(models.ProjectTag)
admin.site.register(models.ProjectCategory)
admin.site.register(models.ProjectThumbnail)


@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'customer', 'published')
    fieldsets = (
        (
            _('Project info'),
            {
                'fields': (
                    'customer',
                    'customer_anonym',
                    'title',
                    'tags',
                    'category',
                    'thumbnails',
                    'description',
                    'review',
                    'link',
                )
            }
        ),
    )


@admin.register(models.Vacancy)
class VacancyAdmin(SummernoteModelAdmin):
    list_display = ('position', 'salary')
    summernote_fields = (
        'description',
        'description_tr',
        'description_ru',
        'description_en',
    )


@admin.register(models.VacancyRequest)
class VacancyRequestAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'proceed')


@admin.register(models.FeedbackRequest)
class FeedbackRequestAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'proceed')


@admin.register(models.FAQ)
class FAQAdmin(TranslationAdmin):
    list_display = ('question', )


@admin.register(models.Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('placeholder', )


@admin.register(models.Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ('quote', )
