from __future__ import unicode_literals

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
