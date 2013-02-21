# -*- coding: utf-8 -*-

from _settings import PROJECT_NAME

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_COOKIE_AGE = 60 * 60 * 24 * 7 * 4  # coockies and session must live one month
SESSION_COOKIE_NAME = PROJECT_NAME
