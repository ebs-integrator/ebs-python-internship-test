import logging

from config.base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')%1nllc!l^6lnwjgmA7tfs9@%9axr_^=^h%krzs&keih+!j+#q'

ALLOWED_HOSTS = ["*"]

WSGI_AUTO_RELOAD = True

DEBUG = True

DEBUG_LEVEL = "INFO"

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s]- %(message)s'}

    },
    'handlers': {
        'console': {
            'level': DEBUG_LEVEL,
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        }
    },
    'loggers': {
        'info': {
            'handlers': ["console"],
            'level': DEBUG_LEVEL,
            'propagate': True
        },
        'django': {
            'handlers': ['console'],
            'level': DEBUG_LEVEL,
            'propagate': True,
        },
        'django.request': {
            'handlers': ['console'],
            'level': DEBUG_LEVEL,
            'propagate': True,
        }
    },
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}
