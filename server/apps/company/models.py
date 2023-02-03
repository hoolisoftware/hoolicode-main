from autoslug import AutoSlugField

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy

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
        return reverse_lazy("company:vacancy-detail", kwargs={"slug": self.slug})


class VacancyRequest(models.Model):
    full_name = models.CharField(_('full name'), max_length=255)
    email = models.EmailField(_('e-mail'))
    message = models.TextField(_('message'))
    cv = models.FileField(_('cv'), upload_to='company/cv/')
    created = models.DateTimeField(auto_now=True)
    proceed = models.BooleanField(_('is proceed?'), default=False)


class FeedbackRequest(models.Model):
    full_name = models.CharField(_('full name'), max_length=255)
    email = models.EmailField(_('e-mail'))
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created = models.DateTimeField(auto_now=True)
    proceed = models.BooleanField(default=False)


class FAQ(models.Model):
    question = models.TextField(_('question'))
    answer = models.TextField(_('answer'))

    class Meta:
        verbose_name = _('FAQ')
        verbose_name_plural = _('FAQ')


class Feature(models.Model):
    placeholder = models.CharField(_('placeholder'), max_length=255)


class Settings(SingletonModel): 
    quote = models.TextField(_('quote'))
    email_support = models.EmailField(_('support email'))
    
    class Meta:
        verbose_name = _('settings')
        verbose_name_plural = _('settings')