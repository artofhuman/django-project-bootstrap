#coding: utf-8
from settings import *

# make tests faster
SOUTH_TESTS_MIGRATE = False
SKIP_SOUTH_TESTS = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'testing.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

EMAIL_BACKEND = 'eml_email_backend.EmailBackend'
EMAIL_FILE_PATH = MEDIA_ROOT + '/eml/'
