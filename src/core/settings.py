"""
Django settings for il2_stats project.

Generated by 'django-admin startproject' using Django 1.8.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""
from datetime import timedelta
import pathlib

from django.utils.translation import ugettext_lazy as _

BASE_DIR = pathlib.Path('.').absolute()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

DEV_MODE = False

# People who get code error notifications.
# In the format (('Full Name', 'email@example.com'), ('Full Name', 'anotheremail@example.com'))
ADMINS = ()

# Tuple of IP addresses, as strings, that:
#   * See debug comments, when DEBUG is true
#   * Receive x-headers
INTERNAL_IPS = ()

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_FILE = BASE_DIR.joinpath('SECRET_KEY')
try:
    with SECRET_FILE.open() as f:
        SECRET_KEY = f.read()
except IOError:
    import string
    from django.utils.crypto import get_random_string
    try:
        with SECRET_FILE.open('w') as f:
            SECRET_KEY = get_random_string(50, string.printable)
            f.write(SECRET_KEY)
    except IOError:
        raise Exception('Cannot open file %s for writing.' % SECRET_FILE)


ALLOWED_HOSTS = ['*']

# Default email address to use for various automated correspondence from
# the site managers.
DEFAULT_FROM_EMAIL = 'webmaster@localhost'

# Email address that error messages come from.
SERVER_EMAIL = 'root@localhost'

# Application definition

INSTALLED_APPS = [
    'modeltranslation',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.postgres',
    'django.contrib.sessions',
    'django.contrib.staticfiles',

    'chunks',
    'users',
    'squads',
    'mission_report',
    'stats',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'core.middleware.time_zone_middleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'stats.middleware.tour_middleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'DIRS': [],
        'DIRS': [str(BASE_DIR.joinpath('custom', 'templates'))],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
                'core.context_processors.server_info',
                'core.context_processors.settings',
                'core.context_processors.version',
                'stats.context_processors.tours',
            ],
            # 'loaders': [
            #     'django.template.loaders.filesystem.Loader',
            #     'django.template.loaders.app_directories.Loader',
            # ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': '127.0.0.1',
        'PORT': '5432',
        'NAME': 'il2_stats',
        'USER': 'il2_stats',
        'PASSWORD': 'il2_stats',
        'CONN_MAX_AGE': 0,
        'ATOMIC_REQUESTS': True,
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

LANGUAGES = (
    ('en', _('English')),
    ('ru', _('Russian')),
    ('de', _('German')),
    ('fr', _('French')),
    ('es', _('Spanish')),
)

TIME_ZONE = 'UTC'

TIME_ZONES = {
    'en': 'UTC',
    'ru': 'Europe/Moscow',
    'de': 'Europe/Berlin',
    'fr': 'Europe/Paris',
    'es': 'Europe/Madrid',
}

USE_I18N = True

USE_L10N = False

USE_TZ = True

LOCALE_PATHS = (
    str(BASE_DIR.joinpath('locale')),
)

DATE_FORMAT = 'd.m.Y'
DATETIME_FORMAT = 'd.m.Y H:i'

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = str(BASE_DIR.parent.joinpath('media'))

# URL that handles the media served from MEDIA_ROOT.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_ROOT = str(BASE_DIR.parent.joinpath('static'))
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    str(BASE_DIR.joinpath('custom', 'static')),
)

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

##################
# AUTHENTICATION #
##################

AUTH_USER_MODEL = 'users.User'

LOGIN_URL = '/profile/login/'
LOGOUT_URL = '/profile/logout/'
LOGIN_REDIRECT_URL = '/'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
        'OPTIONS': {
            'user_attributes': ('username', 'email'),
        },
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 6,
        },
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
]


#########
# CACHE #
#########

# The cache backends to use.
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
#         'LOCATION': 'cache',
#     }
# }
# CACHE_MIDDLEWARE_KEY_PREFIX = ''
# CACHE_MIDDLEWARE_SECONDS = 600
# CACHE_MIDDLEWARE_ALIAS = 'default'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'verbose': {
            'format': '%(asctime)s %(levelname)s %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        },
        'null': {
            'class': 'logging.NullHandler',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'logfile': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': str(BASE_DIR.parent.joinpath('django.log')),
            # 'filename': 'django.log',
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 1,
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'logfile'],
        },
        'django.request': {
            'handlers': ['mail_admins', 'logfile'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.security': {
            'handlers': ['mail_admins', 'logfile'],
            'level': 'ERROR',
            'propagate': False,
        },
        'py.warnings': {
            'handlers': ['console'],
        },
    }
}


#########
# STATS #
#########

# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
MISSION_REPORT_TZ = 'UTC'
MISSION_REPORT_PATH = pathlib.Path('c:/il2/data/logs/txt/')
MISSION_REPORT_DELETE = True
MISSION_REPORT_BACKUP_DAYS = 7
MISSION_REPORT_BACKUP_PATH = MISSION_REPORT_PATH.joinpath('mission_report_backup')

# 0 - disable
INACTIVE_PLAYER_DAYS = 7

SQUAD_MEMBERS_MINIMUM = 4

ACCOUNT_ACTIVATION_DAYS = 1

from config import *

try:
    from .settings_local import *
except ImportError:
    pass


if INACTIVE_PLAYER_DAYS:
    INACTIVE_PLAYER_DAYS = timedelta(days=INACTIVE_PLAYER_DAYS)
