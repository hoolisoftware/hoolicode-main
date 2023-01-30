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
    position = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='position')
    salary = models.CharField(max_length=255)
    description = models.TextField()
    posted = models.DateField(auto_now=True)

    class Meta:
        verbose_name = _('vacancy')
        verbose_name_plural = _('vacancies')
        
    def get_absolute_url(self):
        return reverse_lazy("company:vacancy-detail", kwargs={"slug": self.slug})


class VacancyRequest(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    cv = models.FileField(upload_to='company/cv/')
    created = models.DateTimeField(auto_now=True)
    proceed = models.BooleanField(default=False)


class FeedbackRequest(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created = models.DateTimeField(auto_now=True)
    proceed = models.BooleanField(default=False)


class FAQ(models.Model):
    question = models.TextField()
    answer = models.TextField()

    class Meta:
        verbose_name = _('FAQ')
        verbose_name_plural = _('FAQ')


class Feature(models.Model):
    placeholder = models.CharField(max_length=255)


class Settings(SingletonModel): 
    quote = models.TextField()
    
    class Meta:
        verbose_name = _('settings')
        verbose_name_plural = _('setttings')