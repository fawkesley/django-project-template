"""Production settings and globals."""

from common import *
from os import environ
from urlparse import urlparse

########## DATABASE CONFIGURATION

if environ.has_key('DATABASE_URL'): # provided by heroku
    url = urlparse(environ['DATABASE_URL'])
    
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': url.path[1:],
        'USER': url.username,
        'PASSWORD': url.password,
        'HOST': url.hostname,
        'PORT': url.port,
    }
}
########## END DATABASE CONFIGURATION

########## INSTALLED APPS CONFIGURATION
INSTALLED_APPS += (
    'gunicorn',
    'storages',
)
########## END INSTALLED APPS CONFIGURATION



########## SSL CONFIGURATION
REDIRECT_TO_SSL = bool(int(env('REDIRECT_TO_SSL', '0')))
if REDIRECT_TO_SSL:
    MIDDLEWARE_CLASSES = ('sslify.middleware.SSLifyMiddleware',) + MIDDLEWARE_CLASSES
########## END SSL CONFIGURATION


########## DJANGO AMAZON STORAGE CONFIGURATION

AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME', 'myawsbucketname')
AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID', None)
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY', None)
AWS_PRELOAD_METADATA = True

# This would be nice but SSL won't validate
#AWS_S3_CUSTOM_DOMAIN = 'static.mydomain.com'
#AWS_S3_SECURE_URLS = False

########## DJANGO AMAZON STORAGE CONFIGURATION


########## STATIC FILE / MEDIA CONFIGURATION
DEFAULT_FILE_STORAGE = 'MYPROJECT.libs.s3utils.MediaRootS3BotoStorage'
STATICFILES_STORAGE = 'MYPROJECT.libs.s3utils.StaticRootS3BotoStorage'

# Thanks to CNAME forwarding...
# STATIC_URL = 'http://static.mydomain.com/static/')
# MEDIA_URL =  'http://static.mydomain.com/media/')

STATIC_URL = "https://%s.s3.amazonaws.com/static/" % AWS_STORAGE_BUCKET_NAME
MEDIA_URL = "https://%s.s3.amazonaws.com/media/" % AWS_STORAGE_BUCKET_NAME

ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'
########## END STATIC FILE / MEDIA CONFIGURATION


########## EMAIL CONFIGURATION

# See: https://docs.djangoproject.com/en/1.4/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL', 'noreply@example.com')

# See: https://docs.djangoproject.com/en/1.4/ref/settings/#email-host
EMAIL_HOST = env('EMAIL_HOST', 'smtp.gmail.com')

# See: https://docs.djangoproject.com/en/1.4/ref/settings/#email-host-user
EMAIL_HOST_USER = env('EMAIL_HOST_USER', 'noreply@example.com')

# See: https://docs.djangoproject.com/en/1.4/ref/settings/#email-host-password
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD', '')

# See: https://docs.djangoproject.com/en/1.4/ref/settings/#email-port
EMAIL_PORT = env('EMAIL_PORT', 587)

# See: https://docs.djangoproject.com/en/1.4/ref/settings/#email-subject-prefix
EMAIL_SUBJECT_PREFIX = '[%s] ' % SITE_NAME

# See: https://docs.djangoproject.com/en/1.4/ref/settings/#email-use-tls
EMAIL_USE_TLS = True

# See: https://docs.djangoproject.com/en/1.4/ref/settings/#server-email
SERVER_EMAIL = EMAIL_HOST_USER

########## END EMAIL CONFIGURATION

