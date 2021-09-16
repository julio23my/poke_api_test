from .base import *

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

CACHE_TIMEOUT = 30

INSTALLED_APPS += ['poke_base_test.pokemon', ]
