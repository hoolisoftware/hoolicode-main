from autoslug import AutoSlugField

from django.db import models
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(_('category name'), max_length=50)
    parent_category = models.ForeignKey('self', verbose_name=_('parent category'), blank=True, null=True, on_delete=models.CASCADE)
    slug = AutoSlugField(populate_from='name', unique=True)

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'<{self._meta.verbose_name.title()}: {self.name}>'


class Tag(models.Model):
    name = models.CharField(_('tag name'), max_length=50)
    slug = AutoSlugField(populate_from='name', unique=True)

    class Meta:
        verbose_name = _('tag')
        verbose_name_plural = _('tags')

    def __str__(self):
        return f'#{self.name}'

    def __repr__(self):
        return f'{self._meta.verbose_name.title()}: {self.name}>'


class Post(models.Model):
    content = models.TextField(_('content'))
    created = models.DateField(_('creation date'), auto_now=True)
    is_published = models.BooleanField(_('is post published?'), default=False)
    read_duration = models.IntegerField(_('reading duration'), default=5)
    slug = AutoSlugField(populate_from='title', unique=True)
    thumbnail = models.ImageField(_('thumbnail'), upload_to='posts/thumbnail/')
    title = models.CharField(_('title'), max_length=255)
    slug = AutoSlugField(populate_from='title')
    
    category = models.ForeignKey(Category, verbose_name=Category._meta.verbose_name, on_delete=models.CASCADE, related_name='posts')
    tags = models.ManyToManyField(Tag, verbose_name=Tag._meta.verbose_name_plural, blank=True, related_name='posts')

    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('posts')

    def __str__(self):
        return self.title

    def __repr__(self):
        return f'{self._meta.verbose_name.title()}: {self.title}>'

    def get_related(self):
        return type(self).objects.exclude(id=self.id).filter(category=self.category)

    def get_absolute_url(self):
        return reverse_lazy("posts:detail", kwargs={"slug": self.slug})
    

class PostComment(models.Model):
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name='comments')
    full_name = models.CharField(max_length=55)
    email = models.EmailField()
    comment = models.TextField()
    created = models.DateTimeField(auto_now=True)
