"""
Django settings for cmdbeas project.

Generated by 'django-admin startproject' using Django 4.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from datetime import timedelta
from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-afv^$)pcd=u7m(in5$z4mp0484y*#5%qj@dqm&*%mo-7x-)m1*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1','0.0.0.0']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_select2',
    'api',
    'axes',
    'simple_history',
    'base',
    'easy_pdf',
    'rest_framework',
    'accounts',
    'guardian',

]


# Tell select2 which cache configuration to use:


AXES_FAILURE_LIMIT = 10
AXES_LOCK_OUT_AT_FAILURE = True
AXES_COOLOFF_TIME = timedelta(minutes=30) 

LOGGING = {
    "version": 1,  # the dictConfig format version
    "disable_existing_loggers": False,  # retain the default loggers
    "handlers": {
        "file_accounts": {
            "class": "logging.FileHandler",
            "filename": os.path.join(BASE_DIR, 'accounts.log'),
            "formatter": "verbose",
        },
        "file_base": {
            "class": "logging.FileHandler",
            "filename": os.path.join(BASE_DIR, 'base.log'),
            "formatter": "verbose",
        },   
        "file_django": {
            "class": "logging.FileHandler",
            "filename": os.path.join(BASE_DIR, 'django.log'),
            "formatter": "verbose",
        },    
    },
    "loggers": {
        "accounts": {
            "level": "INFO",
            "handlers": ["file_accounts"],
        },
        "base": {
            "level": "INFO",
            "handlers": ["file_base"],
        },
        "django": {
            "handlers": ["file_django"],
            "level": "DEBUG",
            "propagate": True,
        },
    },
    "formatters": {
        "verbose": {
            "format": "{name} {levelname} {asctime} {module} {message}",
            "style": "{",
        },
        "simple": {
            "format": "{levelname} {message}",
            "style": "{",
        },
    },
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'axes.middleware.AxesMiddleware',
]

AUTHENTICATION_BACKENDS = (
    'axes.backends.AxesStandaloneBackend',
    'django.contrib.auth.backends.ModelBackend', # this is default
    'guardian.backends.ObjectPermissionBackend',
)

STATIC_URL = 'static/'
MEDIA_URL = '/media/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'static')
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_ROOT=BASE_DIR/'media'


SIMPLE_HISTORY_HISTORY_CHANGE_REASON_USE_TEXT_FIELD=True
SIMPLE_HISTORY_ENFORCE_HISTORY_MODEL_PERMISSIONS = True

ROOT_URLCONF = 'cmdbeas.urls'
AUTH_USER_MODEL = 'accounts.User'
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

WSGI_APPLICATION = 'cmdbeas.wsgi.application'

##########email smtp config##########
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # Adresse du serveur SMTP Gmail
EMAIL_PORT = 587  # Port SMTP pour TLS
EMAIL_USE_TLS = True  # Utiliser TLS pour les connexions SMTP
EMAIL_HOST_USER = 'jozacoder@gmail.com'  # Votre adresse e-mail Gmail
EMAIL_HOST_PASSWORD = 'qsse pjsp jiyx bzaf'  # Mot de passe de votre compte Gmail
#####################################################



# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    },
    'select2': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'select2-cache',
    },
}
# Tell select2 which cache configuration to use:
SELECT2_CACHE_BACKEND = "select2"
X_FRAME_OPTIONS = 'SAMEORIGIN'