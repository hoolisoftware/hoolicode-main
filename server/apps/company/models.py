from autoslug import AutoSlugField

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy


User = get_user_model()


class SingletonModel(models.Model):

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj


class ProjectThumbnail(models.Model):
    image = models.ImageField(upload_to='company/projects/thumbnails')

    class Meta:
        verbose_name = _('project thumbnail')
        verbose_name_plural = _('project thumbnails')

    def __repr__(self):
        return self.image.url

    def __str__(self):
        return self.image.url


class ProjectTag(models.Model):
    name = models.CharField(_('name'), max_length=55)
    slug = AutoSlugField(populate_from='name')

    class Meta:
        verbose_name = _('project tag')
        verbose_name_plural = _('project tags')

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


class ProjectCategory(models.Model):
    name = models.CharField(_('name'), max_length=55)
    slug = AutoSlugField(populate_from='name')

    class Meta:
        verbose_name = _('project category')
        verbose_name_plural = _('project categories')

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


class Project(models.Model):
    category = models.ForeignKey(verbose_name=_(
        'categories'), to=ProjectCategory, on_delete=models.SET_NULL,
        blank=True, null=True)
    customer = models.ForeignKey(verbose_name=_(
        'customer'), to=User, on_delete=models.SET_NULL, blank=True, null=True)
    customer_anonym = models.BooleanField(_('do you want to stay anonym?'))
    description = models.TextField(_('description'))
    link = models.URLField(_('project link'))
    published = models.DateField(auto_now=True)
    review = models.TextField(_('review'))
    slug = AutoSlugField(populate_from='title')
    tags = models.ManyToManyField(verbose_name=_('tags'), to=ProjectTag)
    thumbnails = models.ManyToManyField(
        verbose_name=_('thumbnails'), to=ProjectThumbnail)
    title = models.CharField(_('title'), max_length=55)

    class Meta:
        verbose_name = _('project')
        verbose_name_plural = _('projects')

    def __repr__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('company:portfolio-detail', args=[self.slug])


class Vacancy(models.Model):
    position = models.CharField(_('position'), max_length=255)
    slug = AutoSlugField(populate_from='position')
    salary = models.CharField(_('salary'), max_length=255)
    description = models.TextField(_('description'))
    posted = models.DateField(auto_now=True)

    class Meta:
        verbose_name = _('vacancy')
        verbose_name_plural = _('vacancies')

    def get_absolute_url(self):
        return reverse_lazy("company:vacancy-detail",
                            kwargs={"slug": self.slug})


class VacancyRequest(models.Model):
    full_name = models.CharField(_('full name'), max_length=255)
    email = models.EmailField(_('e-mail'))
    message = models.TextField(_('message'))
    cv = models.FileField(_('cv'), upload_to='company/cv/')
    created = models.DateTimeField(auto_now=True)
    proceed = models.BooleanField(_('is proceed?'), default=False)

    class Meta:
        verbose_name = _('vacancy request')
        verbose_name_plural = _('vacancy requests')


class FeedbackRequest(models.Model):
    full_name = models.CharField(_('full name'), max_length=255)
    email = models.EmailField(_('e-mail'))
    subject = models.CharField(_('subject'), max_length=255)
    message = models.TextField(_('message'))
    created = models.DateTimeField(auto_now=True)
    proceed = models.BooleanField(_('is proceed?'), default=False)

    class Meta:
        verbose_name = _('feedback request')
        verbose_name_plural = _('feedback requests')


class FAQ(models.Model):
    question = models.TextField(_('question'))
    answer = models.TextField(_('answer'))

    class Meta:
        verbose_name = _('FAQ')
        verbose_name_plural = _('FAQ')


class Feature(models.Model):
    placeholder = models.CharField(_('placeholder'), max_length=255)

    class Meta:
        verbose_name = _('feature')
        verbose_name_plural = _('features')


class Settings(SingletonModel):
    quote = models.TextField(_('quote'))
    email_support = models.EmailField(_('support email'))

    class Meta:
        verbose_name = _('settings')
        verbose_name_plural = _('settings')
