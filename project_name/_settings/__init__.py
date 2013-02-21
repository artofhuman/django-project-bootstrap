# -*- coding: utf-8 -*-

import os
import sys
from {{ project_name }}.local_settings import DEBUG


PROJECT_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(PROJECT_DIR)

SITE_ID = 1
DEBUG = DEBUG

PROJECT_NAME = '{{ project_name }}'

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Asia/Yekaterinburg'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'ru'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

ROOT_URLCONF = '{{ project_name }}.urls'
SECRET_KEY = '{{ secret_key }}'

# System settings
from _settings.media import *
from _settings.template import *
# from _settings.session import *
from _settings.cache import *
from _settings.logging import *
from _settings.fixtures import *
from _settings.middlewares import *

# Applications
from _settings.applications import *
