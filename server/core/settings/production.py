from .common import *

from os import environ
import logging.config

DEBUG = False
SECRET_KEY = 'django-insecure-secret-key'

CORS_ALLOW_ALL_ORIGINS = False

LOGGING_CONFIG = None
logging.config.fileConfig('logging.conf')

POSTGRES_DB = environ.get('POSTGRES_DB', 'django')
POSTGRES_HOST = environ.get('POSTGRES_HOST', 'database')
POSTGRES_USER = environ.get('POSTGRES_USER', 'django')
POSTGRES_PASSWORD = environ.get('POSTGRES_PASSWORD', 'django')
POSTGRES_PORT = environ.get('POSTGRES_PORT', '5432')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': POSTGRES_DB,
        'HOST': POSTGRES_HOST,
        'USER': POSTGRES_USER,
        'PASSWORD': POSTGRES_PASSWORD,
        'PORT': POSTGRES_PORT
    }
}