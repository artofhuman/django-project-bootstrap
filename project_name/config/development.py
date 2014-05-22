"""
Development settings.
from https://github.com/twoscoops/django-twoscoops-project
and modified with love
"""

from __future__ import absolute_import
from .base import *

# Recipients of traceback emails and other notifications.
ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)
MANAGERS = ADMINS

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

# SECURITY WARNING: don't run with debug turned on in production!
# Debugging displays nice error messages, but leaks memory. Set this to False
# on all server instances and True only for development.
DEBUG = TEMPLATE_DEBUG = True

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# SECURITY WARNING: keep the secret key used in production secret!
# Hardcoded values can leak through source control. Consider loading
# the secret key from an environment variable or a file instead.
SECRET_KEY = 'secret'

## Log settings

# Remove this configuration variable to use your custom logging configuration
LOGGING_CONFIG = None
LOGGING = {
    'version': 1,
    'loggers': {
        '{{ project_name }}': {
            'level': "DEBUG"
        }
    }
}

INTERNAL_IPS = ('127.0.0.1')
