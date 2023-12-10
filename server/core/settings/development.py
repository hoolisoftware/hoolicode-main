from .common import *

from os import environ
import logging.config

DEBUG = True
SECRET_KEY = 'django-insecure-secret-key'

CORS_ALLOW_ALL_ORIGINS = True

LOGGING_CONFIG = None
logging.config.fileConfig('logging.conf')

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "dev.sqlite",
    }
}