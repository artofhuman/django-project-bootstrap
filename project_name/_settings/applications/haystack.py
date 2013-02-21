# -*- coding: utf-8 -*-
#
from _settings import PROJECT_DIR
import os

HAYSTACK_XAPIAN_LANGUAGE = "russian"
HAYSTACK_SEARCH_ENGINE = 'xapian'
HAYSTACK_SITECONF = '{{ project_name }}'
HAYSTACK_XAPIAN_PATH = os.path.join(PROJECT_DIR, 'cache', 'search')
HAYSTACK_SEARCH_RESULTS_PER_PAGE = 10
