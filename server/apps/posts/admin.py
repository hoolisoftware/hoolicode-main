from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django_summernote.admin import SummernoteModelAdmin

from . import models


@admin.register(models.Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'created', 'is_published')
    list_filter = ('is_published',)
    search_fields = ('title', 'content')
    summernote_fields = ('content', )

    fieldsets = (
        (_('Content information'), {
            'fields': (
                'title',
                'content',
                'thumbnail',
                'category',
                'tags'
            ),
        }),
        (_('Post information'), {
            'fields': (
                'is_published',
            )
        })
    )


@admin.register(models.PostComment)
class PostCommentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'post', 'created')


admin.site.register(models.Category)
admin.site.register(models.Tag)
