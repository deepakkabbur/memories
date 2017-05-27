# -*- coding: utf-8 -*-

from .settings import *

DEBUG = True

TEMPLATE_DEBUG = DEBUG

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
