# coding: utf-8
from _settings import *

INSTALLED_APPS = (
    # Grapelli
    'grappelli.dashboard',
    'grappelli',

    # Django apps
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',

    # Must have Vendor apps
    'mptt',
    'south',
    'ckeditor',
    'pytils',
    'sorl.thumbnail',
    'widget_tweaks',
    'debug_toolbar',
    'feincms',
    'treemenu',
    'page'

    # Vendors
    # ...

    #Project apps
    # ...
)

try:
    from local_settings import *
except ImportError:
    pass
