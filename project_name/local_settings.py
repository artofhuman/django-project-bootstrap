# -*- coding: utf-8 -*-
# Local settings for {{ project_name }} project.
LOCAL_SETTINGS = True
from settings import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',       # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '{{ project_name }}',               # Or path to database file if using sqlite3.
        'USER': 'root',                             # Not used with sqlite3.
        'PASSWORD': 'root',                         # Not used with sqlite3.
        'HOST': '',                                 # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                                 # Set to empty string for default. Not used with sqlite3.
        'OPTIONS': {
            "init_command": "SET storage_engine=INNODB",
        }
    }
}
