# -*- coding: utf-8 -*-

import os
from _settings.media import MEDIA_ROOT

CKEDITOR_UPLOAD_PATH = os.path.join(MEDIA_ROOT, 'user')

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Full',
        'autoParagraph': False
    }
}
