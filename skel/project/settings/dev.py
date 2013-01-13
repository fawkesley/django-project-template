"""Development settings and globals."""
import os
from common import *

########## DEBUG CONFIG
DEBUG = True
TEMPLATE_DEBUG = DEBUG
########## END DEBUG CONFIGURATION 

########## LOGGING CONFIG
LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'verbose': {
                'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
                },
            'simple': {
                'format': '%(levelname)s %(module)s %(message)s'
                },
            },
        'handlers': {
            'null': {
                'level':'DEBUG',
                'class':'django.utils.log.NullHandler',
                },
            'console':{
                'level': 'INFO',
                'class': 'logging.StreamHandler',
                'formatter': 'simple'
                },
            # I always add this handler to facilitate separating loggings
            'log_file':{
                'level': 'DEBUG',
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': os.path.join(SITE_ROOT, 'logs/django.log'),
                'maxBytes': '16777216', # 16megabytes
                'formatter': 'verbose'
                },
            'mail_admins': {
                'level': 'ERROR',
                'class': 'django.utils.log.AdminEmailHandler',
                'include_html': True,
                }
            },
        'loggers': {
            'django.request': {
                'handlers': ['mail_admins'],
                'level': 'ERROR',
                'propagate': True,
                },
            'apps': { # I keep all my of apps under 'apps' folder, but you can also add them one by one, and this depends on how your virtualenv/paths are set
                'handlers': ['log_file'],
                'level': 'INFO',
                'propagate': True,
                },
            },
        # you can also shortcut 'loggers' and just configure logging for EVERYTHING at once
        'root': {
            'handlers': ['console', 'mail_admins'],
            'level': 'INFO'
            },
        }

########## END LOGGING CONFIG


########## EMAIL CONFIGURATION

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'localhost'
EMAIL_PORT = '1025'

EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False

########## END EMAIL CONFIGURATION


########## DATABASE CONFIGURATION
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': normpath(join(SITE_ROOT, 'db', 'default.db')),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}
########## END DATABASE CONFIGURATION

########## CACHE CONFIGURATION
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}
########## END CACHE CONFIGURATION


########## DJANGO-DEBUG-TOOLBAR CONFIGURATION
MIDDLEWARE_CLASSES += (
'debug_toolbar.middleware.DebugToolbarMiddleware',
)


INSTALLED_APPS += (
    'debug_toolbar',
)



########## MEDIA CONFIGURATION
# Dev mode uses normal django-served static files.

# Absolute filesystem path to the directory that will hold user-uploaded files.
MEDIA_ROOT = normpath(join(DJANGO_ROOT, 'media'))

# URL that handles the media served from MEDIA_ROOT.
MEDIA_URL = '/media/'
########## END MEDIA CONFIGURATION


########## STATIC FILE CONFIGURATION

# See https://docs.djangoproject.com/en/1.4/howto/static-files/
#
# Absolute path to the directory static files should be collected to. Don't put
# anything in this directory yourself; store your static files in apps' static/
# subdirectories and in STATICFILES_DIRS.

STATIC_ROOT = normpath(join(DJANGO_ROOT, 'static'))

# URL prefix for static files.
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
ADMIN_MEDIA_PREFIX = '/static/admin/'

########## END STATIC FILE CONFIGURATION



# IPs allowed to see django-debug-toolbar output.
INTERNAL_IPS = ('127.0.0.1',)

DEBUG_TOOLBAR_CONFIG = {
# If set to True (default), the debug toolbar will show an intermediate
# page upon redirect so you can view any debug information prior to
# redirecting. This page will provide a link to the redirect destination
# you can follow when ready. If set to False, redirects will proceed as
# normal.
    'INTERCEPT_REDIRECTS': False,

# If not set or set to None, the debug_toolbar middleware will use its
# built-in show_toolbar method for determining whether the toolbar should
# show or not. The default checks are that DEBUG must be set to True and
# the IP of the request must be in INTERNAL_IPS. You can provide your own
# method for displaying the toolbar which contains your custom logic. This
# method should return True or False.
'SHOW_TOOLBAR_CALLBACK': None,

# An array of custom signals that might be in your project, defined as the
# python path to the signal.
'EXTRA_SIGNALS': [],

# If set to True (the default) then code in Django itself won't be shown in
# SQL stacktraces.
'HIDE_DJANGO_SQL': True,

# If set to True (the default) then a template's context will be included
# with it in the Template debug panel. Turning this off is useful when you
# have large template contexts, or you have template contexts with lazy
# datastructures that you don't want to be evaluated.
'SHOW_TEMPLATE_CONTEXT': True,

# If set, this will be the tag to which debug_toolbar will attach the debug
# toolbar. Defaults to 'body'.
'TAG': 'html',
}
########## END DJANGO-DEBUG-TOOLBAR CONFIGURATION


########## CELERY CONFIGURATION

CELERY_ALWAYS_EAGER = True

########## END CELERY CONFIGURATION
