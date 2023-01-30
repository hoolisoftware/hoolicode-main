from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from . import models

@admin.register(models.Vacancy)
class VacancyAdmin(SummernoteModelAdmin):
    list_display = ('position', 'salary')
    summernote_fields = ('description', )

@admin.register(models.VacancyRequest)
class VacancyRequestAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'proceed')

@admin.register(models.FeedbackRequest)
class FeedbackRequestAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'proceed')

@admin.register(models.FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', )

@admin.register(models.Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('placeholder', )

@admin.register(models.Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ('quote', )
