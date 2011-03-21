"""
Settings for local development.

These settings are not fast or efficient, but allow local servers to be run
using the django-admin.py utility.
"""


import os, getpass

from production import *


# Run in debug mode.

DEBUG = True

TEMPLATE_DEBUG = DEBUG


# Save media files to the uploads directory in the user's home folder.

MEDIA_ROOT = os.path.expanduser("~/Sites/%s/media" % SITE_DOMAIN)


# Use local server.

SITE_DOMAIN = "localhost:8000"


# Disable prepending www, as local servers run from localhost.

PREPEND_WWW = False


# Optional separate database settings

DATABASES["default"]["USER"] = getpass.getuser()