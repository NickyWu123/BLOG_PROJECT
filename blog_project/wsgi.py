"""
WSGI config for blog_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application
root=os.path.dirname(__file__)
sys.path.insert(0,os.path.join(root,'..','program/Lib/site-packages'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog_project.settings")

application = get_wsgi_application()
