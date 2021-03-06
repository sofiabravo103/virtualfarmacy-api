import os
import string
import random
import django
import pytest
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
# We manually designate which settings we will be using in an environment variable
# This is similar to what occurs in the `manage.py`


# `pytest` automatically calls this function once when tests are run.
def pytest_configure():
    settings.DEBUG = False
    django.setup()
