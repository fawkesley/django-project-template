from common import *
from prod import *

# This file should mirror prod.py as closely as possible, only
# altering minor things such as disabling email delivery.

########## INSTALLED APPS CONFIGURATION
INSTALLED_APPS += (
    'database_email_backend',
)
########## END INSTALLED APPS CONFIGURATION


########## EMAIL CONFIGURATION

# See: https://docs.djangoproject.com/en/1.4/ref/settings/#email-backend
EMAIL_BACKEND = 'database_email_backend.backend.DatabaseEmailBackend'

########## END EMAIL CONFIGURATION
