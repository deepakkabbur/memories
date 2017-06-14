# -*- coding: utf-8 -*-

from .settings import *

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'memories',
        'USER': 'postgres',
        'PASSWORD': 'postgres'
    }
}
