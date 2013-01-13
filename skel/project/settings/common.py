"""Common settings and globals."""

import sys
from os import environ
from os.path import abspath, basename, dirname, join, normpath

from helpers import gen_secret_key
env = lambda e, d: environ[e] if environ.has_key(e) else d


########## PATH CONFIGURATION
# Absolute filesystem path to this Django project directory.
DJANGO_ROOT = dirname(dirname(abspath(__file__)))

# Site name.
SITE_NAME = basename(DJANGO_ROOT)

# Absolute filesystem path to the top-level project folder.
SITE_ROOT = dirname(DJANGO_ROOT)

# Absolute filesystem path to the secret file which holds this project's
# SECRET_KEY. Will be auto-generated the first time this file is interpreted.
SECRET_FILE = normpath(join(SITE_ROOT, 'deploy', 'SECRET')) # TODO

# Add all necessary filesystem paths to our system path so that we can use
# python import statements.
sys.path.append(SITE_ROOT)
sys.path.append(normpath(join(DJANGO_ROOT, 'apps')))
sys.path.append(normpath(join(DJANGO_ROOT, 'libs')))
########## END PATH CONFIGURATION


########## DEBUG CONFIGURATION
# Disable debugging by default.
DEBUG = bool(int(env('DEBUG', '0')))
TEMPLATE_DEBUG = DEBUG
########## END DEBUG CONFIGURATION


########## MANAGER CONFIGURATION
# Admin and managers for this project. These people receive private site
# alerts.
ADMINS = (
	('Admin Name', 'admin@example.com'),
)

MANAGERS = ADMINS
########## END MANAGER CONFIGURATION



########## GENERAL CONFIGURATION
# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name although not all
# choices may be available on all operating systems. On Unix systems, a value
# of None will cause Django to use the same timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/London'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html.
LANGUAGE_CODE = 'en-gb'

# The ID, as an integer, of the current site in the django_site database table.
# This is used so that application data can hook into specific site(s) and a
# single database can manage content for multiple sites.
SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True
########## END GENERAL CONFIGURATION


# Additional locations of static files.
STATICFILES_DIRS = (
	normpath(join(DJANGO_ROOT, 'assets')),
)

# List of finder classes that know how to find static files in various
# locations.
STATICFILES_FINDERS = (
	'django.contrib.staticfiles.finders.FileSystemFinder',
	'django.contrib.staticfiles.finders.AppDirectoriesFinder',
	'django.contrib.staticfiles.finders.DefaultStorageFinder',
)
########## END STATIC FILE CONFIGURATION


########## TEMPLATE CONFIGURATION
# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
	'django.template.loaders.filesystem.Loader',
	'django.template.loaders.app_directories.Loader',
)

# Directories to search when loading templates.
TEMPLATE_DIRS = (
	normpath(join(DJANGO_ROOT, 'templates')),
)

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS

TEMPLATE_CONTEXT_PROCESSORS += (
    'django.core.context_processors.static',
    'django.core.context_processors.media',
    #'django.core.context_processors.request',
)
########## END TEMPLATE CONFIGURATION


########## MIDDLEWARE CONFIGURATION
MIDDLEWARE_CLASSES = (
	'django.middleware.common.CommonMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
)
########## END MIDDLEWARE CONFIGURATION


########## APP CONFIGURATION
INSTALLED_APPS = (
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.sites',
	'django.contrib.messages',
	'django.contrib.staticfiles',

    # MYPROJECT apps
    'MYPROJECT.apps.MYAPP',
    
    # Admin panel and documentation.
	'django.contrib.admin',
	'django.contrib.admindocs',

    # South database migration tool.
	'south',

    # Django registration for traditional username/email signups
    #'registration',

	# Celery task queue. djcelery modifies manage.py
    #'celery',
	#'djcelery',

    # Django Facebook integration
    #'django_facebook',

    # PayPal integration
    #'paypal.standard.ipn',
    #'paypal.standard.pdt',

	# django-sentry log viewer.
	#'indexer',
	#'paging',
	#'sentry',
	#'sentry.client',
)
########## END APP CONFIGURATION


########## CELERY CONFIGURATION

#import djcelery
#djcelery.setup_loader()

#CELERY_ALWAYS_EAGER = bool(int(env('CELERY_ALWAYS_EAGER', '0')))

########## END CELERY CONFIGURATION


########## URL CONFIGURATION
ROOT_URLCONF = '%s.urls' % SITE_NAME
########## END URL CONFIGURATION

########## KEY CONFIGURATION
# Try to load the SECRET_KEY from our SECRET_FILE. If that fails, then generate
# a random SECRET_KEY and save it into our SECRET_FILE for future loading. If
# everything fails, then just raise an exception.

try:
    SECRET_KEY = open(SECRET_FILE).read().strip()
except IOError:
    try:
        with open(SECRET_FILE, 'w') as f:
            f.write(gen_secret_key(50))
    except IOError:
        raise Exception('Cannot open file `%s` for writing.' % SECRET_FILE)
########## END KEY CONFIGURATION


# See http://django-facebook.readthedocs.org/en/latest/index.html


AUTHENTICATION_BACKENDS = (
    'django_facebook.auth_backends.FacebookBackend',
    'django.contrib.auth.backends.ModelBackend',
)

# Uncomment once you've created an app with user profiles
# AUTH_PROFILE_MODULE = 'MYUSERAPP.UserProfile'


########## SESSION CONFIGURATION
SESSION_COOKIE_AGE = 60 * 60 * 12 # 12 hours
########## END SESSION CONFIGURATION

