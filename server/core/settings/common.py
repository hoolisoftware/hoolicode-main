from os import environ
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

ALLOWED_HOSTS = ['127.0.0.1', '0.0.0.0', 'localhost', 'maxyazilim.com', 'hoolisoftware.xyz']
CSRF_TRUSTED_ORIGINS = ['http://0.0.0.0', 'http://127.0.0.1', 'http://localhost', 'https://maxyazilim.com', 'https://hoolisoftware.xyz']

if (HOST := environ.get('HOST')):
    ALLOWED_HOSTS.append(HOST)
    CSRF_TRUSTED_O
    RIGINS.append(f'https://{HOST}')

INSTALLED_APPS = [
    'corsheaders',
    'modeltranslation',
    'rest_framework',

    'apps.users',
    'apps.posts',
    'apps.company',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.vk',
    'allauth.socialaccount.providers.google',
    'captcha',
    "drf_recaptcha",
    'django_summernote',
    'django_filters',
]

SITE_ID = int(environ.get('SITE_ID', '1'))

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware'
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates'
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages'
            ],
            'libraries': {
                'core': 'templatetags.core',
                'company': 'templatetags.company',
                'posts': 'templatetags.posts'
            }
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'
    },
]


LANGUAGE_CODE = 'ru-RU'
LOCALE_PATHS = [BASE_DIR / 'locale']

USE_TZ = True
USE_I18N = True
TIME_ZONE = 'UTC'

LANGUAGES = (
    ('ru', 'Russian'),
    ('en', 'English'),
    ('tr', 'Turkish'),
)
DEFAULT_LANGUAGE = LANGUAGES[1]


STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = (
    BASE_DIR / 'core/static',
)

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'mediafiles'

X_FRAME_OPTIONS = 'SAMEORIGIN'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'users.User'

LOGIN_REDIRECT_URL = 'company:home'
LOGOUT_REDIRECT_URL = 'company:home'

LOGIN_URL = 'users:login'
LOGOUT_URL = 'users:logout'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

SOCIALACCOUNT_PROVIDERS = {}

RECAPTCHA_PUBLIC_KEY = "6LcarSspAAAAANslm1_QK52QOR5WOSdtvcqrUdin"
RECAPTCHA_PRIVATE_KEY = "6LcarSspAAAAADBaf87BlmYOQL4wuzKMUicZFgIl"
DRF_RECAPTCHA_SECRET_KEY = RECAPTCHA_PRIVATE_KEY
RECAPTCHA_REQUIRED_SCORE = 0.85
