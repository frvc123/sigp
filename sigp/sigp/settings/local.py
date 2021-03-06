from base import *

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']

#bdsigp
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'sigp-desarrollo',
        'USER': 'sigp',
        'PASSWORD': 'sigp',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    BASE_DIR.child('static'),
)

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR.child('media')
