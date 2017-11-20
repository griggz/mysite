"""
Django settings for MySite project.

Generated by 'django-admin startproject' using Django 1.10.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
import dj_database_url
import datetime

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'check root'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['www.vvayne.co', 'vvayne.co', 'wgsite.herokuapp.com']

EMAIL_HOST = 'mail.name.com'
EMAIL_HOST_USER = 'hello@vvayne.co'
DEFAULT_FROM_EMAIL = 'hello@vvayne.co'
EMAIL_HOST_PASSWORD = 'WCg7G0707!!'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# Application definition

INSTALLED_APPS = [
    # Django Apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Third Party Apps
    'crispy_forms',
    'django.contrib.humanize',
    'django_hosts',
    'rest_framework',
    'pagedown',
    'markdown_deux',
    'storages',
    # My Apps
    'argent',
    'home',
    'accounts',
    'posts',
    'comments',

]

MIDDLEWARE = [
    'django_hosts.middleware.HostsRequestMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'MySite.middleware.LoginRequiredMiddleware',
    'django_hosts.middleware.HostsResponseMiddleware',
]

LOGIN_URL = '/account/login'

LOGIN_EXEMPT_URLS = [
    '/account/logout',
    '/account/register',
    '/account/reset-password/',
    '/account/reset-password/done/',
    '/account/reset-password/confirm/',
    '/account/reset-password/complete/',
    '/about',
    '/feedback',
    '/posts',
]

ROOT_URLCONF = 'MySite.urls'
ROOT_HOSTCONF = 'MySite.hosts'
DEFAULT_HOST = 'www'
DEFAULT_REDIRECT_URL = 'http://www.vvayne.co'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'MySite.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Update database configuration with $DATABASE_URL.
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'EST'

USE_I18N = True

USE_L10N = True

USE_TZ = True

CRISPY_TEMPLATE_PACK = 'bootstrap3'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

# STATIC_URL = '/static/'
#
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, "static"),
# )
#
# STATIC_ROOT = os.path.join(BASE_DIR, "live-static", "static-root")
#
# MEDIA_URL = "/media/"
#
# MEDIA_ROOT = os.path.join(BASE_DIR, "live-static", "media-root")

AWS_ACCESS_KEY_ID = "AKIAJ7ATZNUFF22D4Y7Q"
AWS_SECRET_ACCESS_KEY = "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"

AWS_FILE_EXPIRE = 200
AWS_PRELOAD_METADATA = True
AWS_QUERYSTRING_AUTH = True

DEFAULT_FILE_STORAGE = 'MySite.utils.MediaRootS3BotoStorage'
STATICFILES_STORAGE = 'MySite.utils.StaticRootS3BotoStorage'
AWS_STORAGE_BUCKET_NAME = 'vvayneco'
S3DIRECT_REGION = 'us-east'
S3_URL = '//%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
MEDIA_URL = '//%s.s3.amazonaws.com/media/' % AWS_STORAGE_BUCKET_NAME
MEDIA_ROOT = MEDIA_URL
STATIC_URL = S3_URL + 'static/'
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

two_months = datetime.timedelta(days=61)
date_two_months_later = datetime.date.today() + two_months
expires = date_two_months_later.strftime("%A, %d %B %Y 20:00:00 GMT")

AWS_HEADERS = {
    'Expires': expires,
    'Cache-Control': 'max-age=%d' % (int(two_months.total_seconds()),),
}
