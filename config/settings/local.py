from .base import *

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

CACHE_TIMEOUT = 30

INSTALLED_APPS += ['poke_base_test.pokemon', ]

from django.core.management.commands import diffsettings

output = diffsettings.Command().handle(default=None, output="hash", all=False)